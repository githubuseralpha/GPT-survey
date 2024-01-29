import json


class Category:
    def __init__(self, id: int, name: str, subcategories: list[str]):
        self.name = name
        self.subcategories = subcategories
        self.id = id


class CategoryManager:
    def __init__(self):
        self.categories = []

    def load_categories(self, json_file: str):
        with open(json_file) as f:
            categories = json.load(f)
        for i, category in enumerate(categories):
            self.categories.append(
                Category(i, category["name"], category["subcategories"])
            )
