import dotenv
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from llm_templates import ANALYSIS_TEMPLATE, SURVEY_TEMPLATE

dotenv.load_dotenv()

DEFAULT_MODEL = "gpt-3.5-turbo-instruct"


def get_gpt(
    model: str = DEFAULT_MODEL,
    temperature: float = 0.5,
    top_p: float = 0.9,
    max_tokens: int = 1024,
) -> str:
    llm = OpenAI(
        model=model,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
    )
    return llm


def completion(
    llm: OpenAI,
    prompt: dict[str, str],
    template: str,
) -> str:
    chain = LLMChain(llm=llm, prompt=template)
    return chain.invoke(prompt)


def generate_questions(
    llm: OpenAI, category: str, subcategories: str, number_of_questions: int
) -> str:
    prompt = {
        "category": category,
        "subcategories": subcategories,
        "number_of_questions": number_of_questions,
    }
    template = PromptTemplate(
        template=SURVEY_TEMPLATE,
        input_variables=["category", "subcategories", "number_of_questions"],
    )
    return completion(llm, prompt, template)["text"]


def process_questions(text: str, number_of_questions: int) -> list[str]:
    questions = [
        question
        for i, question in enumerate(text.split("\n"))
        if question.startswith(f"{i+1}.")
    ]
    assert len(questions) >= number_of_questions

    questions = [question[question.index(".") + 1 :] for question in questions]
    questions = questions[:number_of_questions]
    return questions


def multiple_process_questions(
    text: str, number_of_questions: int, retries: int = 3
) -> list[str]:
    for _ in range(retries):
        try:
            return process_questions(text, number_of_questions)
        except AssertionError or IndexError:
            pass
    return None


def generate_analysis(llm: OpenAI, questions: list[str], answers: list[str]) -> str:
    survey = ""
    for i in range(len(questions)):
        survey += f"{questions[i]}: {answers[i]}\n"

    prompt = {
        "survey": survey,
    }
    template = PromptTemplate(
        template=ANALYSIS_TEMPLATE,
        input_variables=["survey"],
    )
    return completion(llm, prompt, template)["text"]
