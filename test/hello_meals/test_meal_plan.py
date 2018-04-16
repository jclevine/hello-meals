from unittest import TestCase
from src.ressie.cookbook import Cookbook
from unittest.mock import Mock
from src.ressie.meal_type import MealType
from src.ressie.recipe import Recipe
from src.hello_meals.meal_plan import MealPlan


class TestMealPlan(TestCase):

    def test_build_meal_plan_from_cookbook_recipes(self):
        cookbook = Mock(spec=Cookbook)
        expected = Recipe(name='Yummy Dish!', ingredients=[], type=MealType.BREAKFAST, servings=10)
        cookbook.get_recipe = Mock(return_value=expected)

        meal_plan = MealPlan(name='Aweomse Plan, Brah', cookbook=cookbook, recipes=['Yummy Dish!'])
        self.assertEqual([expected], meal_plan.meals)




