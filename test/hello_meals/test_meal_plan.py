from unittest import TestCase
from src.ressie.cookbook import Cookbook
from unittest.mock import Mock


class TestMealPlan(TestCase):

    def test_build_meal_plan_from_cookbook_recipes(self):
        cookbook = Mock(spec=Cookbook)
        cookbook.add_recipes([{name}])



