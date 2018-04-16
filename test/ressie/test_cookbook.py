from unittest import TestCase
from src.ressie.recipe import Recipe
from src.ressie.ingredient import Ingredient
from src.ressie.unit import Unit as U
from src.ressie.cookbook import Cookbook
from unittest.mock import Mock, MagicMock


class TestCookbook(TestCase):
    blue_apple_nut_oatmeal = Recipe('Blue Apple Nut Oatmeal', [
        Ingredient('water', 1.5, U.CUPS),
        Ingredient('oats', 30, U.GRAMS),
        Ingredient('raisins', 20, U.GRAMS),
        Ingredient('berries', 120, U.GRAMS),
        Ingredient('bananas', 1, U.UNITS),
        Ingredient('apples', 1, U.UNITS),
        Ingredient('nuts', 15, U.GRAMS)
    ])

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
    ])

    def test_create_cookbook_with_2_recipes(self):
        mock_db = MagicMock()
        cookbook = Cookbook(mock_db)
        cookbook.add_recipes([TestCookbook.blue_apple_nut_oatmeal, TestCookbook.cinnamon_spied_baked_oatmeal])
        self.assertDictEqual(TestCookbook.blue_apple_nut_oatmeal.to_dict(), mock_db.insert.call_args_list[0][0][0])
        self.assertDictEqual(TestCookbook.cinnamon_spied_baked_oatmeal.to_dict(), mock_db.insert.call_args_list[1][0][0])

    def test_retrieve_recipe(self):
        mock_db = MagicMock()
        mock_db.retrieve = Mock(return_value=TestCookbook.blue_apple_nut_oatmeal.to_dict())
        cookbook = Cookbook(mock_db)
        cookbook.get_recipe('Blue Apple Nut Oatmeal')
        self.assertEqual('Blue Apple Nut Oatmeal', mock_db.retrieve.call_args[0][0])
