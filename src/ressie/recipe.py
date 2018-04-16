from functools import reduce
from src.ressie.ingredient import Ingredient


class Recipe(object):
    def __init__(self, name, ingredients, servings=1):
        self._name = name
        self._ingredients = ingredients
        self._servings = servings

    @property
    def name(self):
        return self._name

    @staticmethod
    def from_dict(recipe_dict):
        return Recipe(recipe_dict['name'],
                      [Ingredient.from_dict(ingredient)
                       for ingredient
                       in recipe_dict['ingredients']],
                      servings=recipe_dict['servings']
                      )

    def to_dict(self):
        return {
            'name': self._name,
            'servings': self._servings,
            'ingredients': [ingredient.to_dict() for ingredient in self._ingredients]
        }

    def __repr__(self):
        return str(self.to_dict())

    def __str__(self):
        return '{} servings of {}: {} ingredients'.format(self._servings, self._name, len(self._ingredients))

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()
