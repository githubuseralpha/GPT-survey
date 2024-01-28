import json

from flask import Flask, render_template
            
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
def index():
    categories_list = categories.categories
    return render_template('index.html', categories=categories_list)


if __name__ == '__main__':
    app.run(debug=True)
    