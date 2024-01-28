import json

from flask import Flask, redirect, render_template, request, url_for, session

from llm import generate_questions, process_questions, get_gpt
            
class Category:
    def __init__(self, id, name, subcategories):
        self.name = name
        self.subcategories = subcategories
        self.id = id
        
class CategoryManager:
    def __init__(self):
        self.categories = []
        
    def load_categories(self, json_file):
        with open(json_file) as f:
            categories = json.load(f)
        for i, category in enumerate(categories):
            self.categories.append(Category(i, category['name'], category['subcategories']))
            

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'
categories = CategoryManager()
categories.load_categories('categories.json')


@app.route('/', methods=['GET', 'POST'])
def category():
    if request.method == 'POST':
        data = request.form
        category_id = int(data['category'])
        return redirect(url_for('subcategories', cat_id=category_id))
    elif request.method == 'GET':
        categories_list = categories.categories
        return render_template('index.html', categories=categories_list)


@app.route('/subcategories/<cat_id>', methods=['GET', 'POST'])
def subcategories(cat_id):
    if request.method == 'POST':
        data = request.form
        subcategories = list(data.values())
        subcategories_str = ', '.join(subcategories)
        questions = generate_questions(get_gpt(), categories.categories[int(cat_id)].name, subcategories_str, 5)
        questions = process_questions(questions)
        session['questions'] = questions
        return redirect(url_for('survey'))
    elif request.method == 'GET':
        category = categories.categories[int(cat_id)]
        subcategories = category.subcategories
        return render_template('subcategories.html', subcategories=subcategories)
    
    
@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        data = request.form
        return redirect(url_for('analysis', survey=data))
    elif request.method == 'GET':
        questions = session['questions']
        return render_template('survey.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)
    