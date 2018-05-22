from unittest.mock import Mock
from src.ressie.cookbook import Cookbook
from mock_cookbook.write_cookbook import recipes
from src.pyllo.pyllo import Pyllo

mock_cookbook = Mock(spec=Cookbook)
mock_cookbook.get_recipe = lambda name: [recipe for recipe in recipes if recipe.name == name][0]

mock_pyllo = Mock(spec=Pyllo)
mock_pyllo.get_labels = lambda: {'Breakfast': '1', 'Entree': '2'}
