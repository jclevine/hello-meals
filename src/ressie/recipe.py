from functools import reduce
from src.ressie.ingredient import Ingredient
from src.ressie.meal_type import MealType


class Recipe(object):
    def __init__(self, name, ingredients, servings=1, meal_type=MealType.ENTREE):
        self._name = name
        self._ingredients = ingredients
        self._servings = servings
        self._meal_type = meal_type

    @property
    def name(self):
        return self._name

    @property
    def servings(self):
        return self._servings

    @property
    def meal_type(self):
        return self._meal_type

    @property
    def ingredients(self):
        return self._ingredients

    @staticmethod
    def from_dict(recipe_dict):
        return Recipe(recipe_dict['name'],
                      [Ingredient.from_dict(ingredient)
                       for ingredient
                       in recipe_dict['ingredients']],
                      servings=recipe_dict['servings'],
                      meal_type=MealType(recipe_dict['type'])
                      )

    def to_dict(self):
        return {
            'name': self._name,
            'servings': self._servings,
            'type': self._meal_type.value,
            'ingredients': [ingredient.to_dict() for ingredient in self._ingredients]
        }

    def __repr__(self):
        return str(self.to_dict())

    def __str__(self):
        return '{} servings of {}: {} ingredients'.format(self._servings, self._name, len(self._ingredients))

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()
