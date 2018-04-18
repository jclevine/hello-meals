from src.ressie.recipe import Recipe


class Cookbook(object):
    def __init__(self, db):
        self._db = db

    def add_recipes(self, recipes):
        [self._db.upsert(recipe.to_dict()) for recipe in recipes]

    def get_recipe(self, recipe_name):
        return Recipe.from_dict(self._db.retrieve(recipe_name))
