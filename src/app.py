import argparse
import os
from configparser import ConfigParser

import dotenv
from flask import Flask, redirect, render_template, request, url_for, session

from llm import (
    generate_questions,
    get_gpt,
    generate_analysis,
    multiple_process_questions,
)
from categories import CategoryManager

dotenv.load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")

config = ConfigParser()
config.read("config.ini")

categories = CategoryManager()
categories.load_categories("categories.json")

survey_llm = get_gpt(
    model=config["gpt_survey"]["model_name"],
    temperature=float(config["gpt_survey"]["temperature"]),
    top_p=float(config["gpt_survey"]["top_p"]),
    max_tokens=int(config["gpt_survey"]["max_new_tokens"]),
)
analysis_llm = get_gpt(
    model=config["gpt_analysis"]["model_name"],
    temperature=float(config["gpt_analysis"]["temperature"]),
    top_p=float(config["gpt_analysis"]["top_p"]),
    max_tokens=int(config["gpt_analysis"]["max_new_tokens"]),
)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true")
    return parser.parse_args()


@app.route("/", methods=["GET", "POST"])
def category():
    if request.method == "POST":
        data = request.form
        category_id = int(data["category"])
        return redirect(url_for("subcategories", cat_id=category_id))
    elif request.method == "GET":
        categories_list = categories.categories
        return render_template("categories.html", categories=categories_list)


@app.route("/category/<cat_id>", methods=["GET", "POST"])
def subcategories(cat_id: int):
    if request.method == "POST":
        NUM_QUESTION_FIELD_NAME = "number_of_questions"
        data = request.form

        subcategories = [val for val in data.values() if val != NUM_QUESTION_FIELD_NAME]
        subcategories_str = ", ".join(subcategories)
        num_questions = int(data[NUM_QUESTION_FIELD_NAME])
        category_name = categories.categories[int(cat_id)].name

        text = generate_questions(
            survey_llm, category_name, subcategories_str, num_questions
        )
        questions = multiple_process_questions(text, num_questions)
        session["questions"] = questions
        return redirect(url_for("survey"))
    elif request.method == "GET":
        category = categories.categories[int(cat_id)]
        subcategories = category.subcategories
        return render_template("subcategories.html", subcategories=subcategories)


@app.route("/survey", methods=["GET", "POST"])
def survey():
    if request.method == "POST":
        data = request.form
        questions = session["questions"]
        answers = list(data.values())
        session["analysis"] = generate_analysis(analysis_llm, questions, answers)
        return redirect(url_for("analysis"))
    elif request.method == "GET":
        questions = session["questions"]
        return render_template("survey.html", questions=enumerate(questions))


@app.route("/analysis", methods=["GET"])
def analysis():
    analysis = session["analysis"]
    return render_template("analysis.html", analysis=analysis)


if __name__ == "__main__":
    args = parse_args()
    app.run(debug=args.debug)
