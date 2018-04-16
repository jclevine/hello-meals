from unittest import TestCase
from src.ressie.tinydb_cookbook import TinyDBCookbook
from src.ressie.recipe import Recipe
from src.ressie.ingredient import Ingredient
from src.ressie.unit import Unit as U
from src.ressie.cookbook import Cookbook
import os


class TestTinyDBCookbook(TestCase):
    blue_apple_nut_oatmeal = Recipe('Blue Apple Nut Oatmeal', [
        Ingredient('water', 1.5, U.CUPS),
        Ingredient('oats', 30, U.GRAMS),
        Ingredient('raisins', 20, U.GRAMS),
        Ingredient('berries', 120, U.GRAMS),
        Ingredient('bananas', 1, U.UNITS),
        Ingredient('apples', 1, U.UNITS),
        Ingredient('nuts', 15, U.GRAMS)
    ], servings=2)

    cinnamon_spied_baked_oatmeal = Recipe('Cinnamon-Spiced Baked Oatmeal', [
        Ingredient('oats', 100, U.GRAMS),
        Ingredient('raisins', 50, U.GRAMS),
        Ingredient('dates', 2, U.UNITS),
        Ingredient('flaxseeds', 10, U.GRAMS),
        Ingredient('milk', 250, U.MILLILITRES),
        Ingredient('water', 166.67, U.MILLILITRES),
        Ingredient('vanilla extract', 1, U.TEASPOONS),
        Ingredient('cinnamon', 1, U.TEASPOONS),
        Ingredient('berries', 0.5, U.CUPS)
    ], servings=3)

    def test_insert_and_retrieve_recipe(self):
        db_path = os.path.join(os.getcwd(), 'db.json')

        with TinyDBCookbook.open(db_path) as db:
            cookbook = Cookbook(db)
            cookbook.add_recipes([self.blue_apple_nut_oatmeal, self.cinnamon_spied_baked_oatmeal])
            actual = cookbook.get_recipe('Blue Apple Nut Oatmeal')
            self.assertEqual(self.blue_apple_nut_oatmeal, actual)
