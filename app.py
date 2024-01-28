import json

from flask import Flask, redirect, render_template, request, url_for
            
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
categories = CategoryManager()
categories.load_categories('categories.json')


@app.route('/', methods=['GET', 'POST'])
def category():
    if request.method == 'POST':
        data = request.form
        print(data)
        category_id = int(data['category'])
        category = categories.categories[category_id]
        return redirect(url_for('subcategories', cat_id=category_id))
    elif request.method == 'GET':
        categories_list = categories.categories
        return render_template('index.html', categories=categories_list)


@app.route('/subcategories/<cat_id>', methods=['GET', 'POST'])
def subcategories(cat_id):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        category = categories.categories[int(cat_id)]
        subcategories = category.subcategories
        return render_template('subcategories.html', subcategories=subcategories)

if __name__ == '__main__':
    app.run(debug=True)
    