from unittest import TestCase
from src.ressie.recipe import Recipe
from src.ressie.ingredient import Ingredient
from src.ressie.unit import Unit as U
from src.ressie.meal_type import MealType


class TestRecipe(TestCase):
    blue_apple_nut_oatmeal = Recipe('Blue Apple Nut Oatmeal', [
        Ingredient('water', 1.5, U.CUPS),
        Ingredient('oats', 30, U.GRAMS),
        Ingredient('raisins', 20, U.GRAMS),
        Ingredient('berries', 120, U.GRAMS),
        Ingredient('bananas', 1, U.UNITS),
        Ingredient('apples', 1, U.UNITS),
        Ingredient('nuts', 15, U.GRAMS)
    ], servings=2, type=MealType.BREAKFAST)

    blue_apple_nut_oatmeal_dict = {
        'name': 'Blue Apple Nut Oatmeal',
        'servings': 2,
        'type': 'Breakfast',
        'ingredients': [
            {
                'name': 'water',
                'amount': 1.5,
                'unit': U.CUPS.value
            },
            {
                'name': 'oats',
                'amount': 30,
                'unit': U.GRAMS.value
            },
            {
                'name': 'raisins',
                'amount': 20,
                'unit': U.GRAMS.value
            },
            {
                'name': 'berries',
                'amount': 120,
                'unit': U.GRAMS.value
            },
            {
                'name': 'bananas',
                'amount': 1,
                'unit': U.UNITS.value
            },
            {
                'name': 'apples',
                'amount': 1,
                'unit': U.UNITS.value
            },
            {
                'name': 'nuts',
                'amount': 15,
                'unit': U.GRAMS.value
            }
        ]
    }

    def test_recipe_serialization(self):
        actual = TestRecipe.blue_apple_nut_oatmeal.to_dict()
        self.assertDictEqual(self.blue_apple_nut_oatmeal_dict, actual)

    def test_recipe_deserialization(self):
        actual = Recipe.from_dict(TestRecipe.blue_apple_nut_oatmeal_dict)
        self.assertEqual(self.blue_apple_nut_oatmeal, actual)
