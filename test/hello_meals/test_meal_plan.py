from unittest import TestCase
from src.ressie.cookbook import Cookbook
from unittest.mock import Mock, patch
from src.ressie.meal_type import MealType
from src.ressie.recipe import Recipe
from src.hello_meals.meal_plan import MealPlan
from src.ressie.ingredients import Ingredients as I
from src.hello_meals.hello_meals import HelloMeals
from src.pyllo.pyllo import Pyllo


class TestMealPlan(TestCase):

    def test_build_meal_plan_from_cookbook_recipes(self):
        cookbook = Mock(spec=Cookbook)
        expected_recipe = Recipe(name='Yummy Dish!', ingredients=[], meal_type=MealType.BREAKFAST, servings=10)
        cookbook.get_recipe = Mock(return_value=expected_recipe)

        meal_plan = MealPlan(name='Aweomse Plan, Brah', cookbook=cookbook, recipes=['Yummy Dish!'])
        self.assertEqual([expected_recipe], meal_plan.meals)

    @patch.object(Pyllo, 'get_labels')
    def test_build_plan_returns_meal_tally(self, pyllo):
        pyllo.return_value = {'Breakfast': '123456789'}
        cookbook = Mock(spec=Cookbook)
        breakfast_1_recipe = Recipe(name='Yummy Breakfast!', ingredients=[I.STRAWBERRIES, I.ONION_POWDER],
                                    meal_type=MealType.BREAKFAST, servings=10)
        breakfast_2_recipe = Recipe(name='Delish Breakfast Dish!', ingredients=[I.APPLES, I.MILK],
                                    meal_type=MealType.BREAKFAST, servings=3)
        entree_1_recipe = Recipe(name='Yummy Lunch!', ingredients=[I.ONIONS, I.ONION_POWDER],
                                 meal_type=MealType.BREAKFAST, servings=4)
        entree_2_recipe = Recipe(name='Delish Dinner Dish!', ingredients=[I.MILK, I.ONION_POWDER],
                                 meal_type=MealType.BREAKFAST, servings=1)

        def mock_get_recipe_func():
            for recipe in [breakfast_1_recipe, breakfast_2_recipe, entree_1_recipe, entree_2_recipe]:
                yield recipe

        cookbook.get_recipe = Mock(side_effect=mock_get_recipe_func())

        meal_plan = MealPlan(name='Cool Plan, fsure', cookbook=cookbook, recipes=[
            'Yummy Lunch!', 'Delish Dinner Dish!', 'Delish Breakfast Dish!', 'Yummy Breakfast'])

        hello_meals = HelloMeals(pyllo)
        actual = hello_meals.create_meal_plan(meal_plan, Mock())





