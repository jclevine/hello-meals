class MealPlan(object):
    def __init__(self, name, cookbook, recipes):
        self._name = name
        self._meals = [cookbook.get_recipe(recipe) for recipe in recipes]

    @property
    def name(self):
        return self._name

    @property
    def meals(self):
        return self._meals
