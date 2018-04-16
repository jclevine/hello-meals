from enum import Enum


class MealType(Enum):
    BREAKFAST = 'Breakfast'
    ENTREE = 'Entree'
    FRUIT = 'Fruit'
    VEGGIES = 'Veggies'
    SIDES = 'Sides'
    SALAD = 'Salad'


meal_plan = {
    'meal_plan_name': 'Test Meal Plan - 1',
    'meals': [
        {
            'name': 'No-Cook Strawberry Oatmeal To-Go',
            'type': MealType.BREAKFAST,
            'servings': 1
        },
        {
            'name': 'Creamy Buckwheat Porridge',
            'type': MealType.BREAKFAST,
            'servings': 3
        },
        {
            'name': 'Berry "Yogurt"',
            'type': MealType.BREAKFAST,
            'servings': 2
        },
        {
            'name': 'Chia Seed Breakfast Pudding',
            'type': MealType.BREAKFAST,
            'servings': 1
        },



        {
            'name': 'Easy Balsamic Almond Dressing',
            'type': MealType.SALAD,
            'servings': 1
        },
        {
            'name': 'Banana Walnut Dressing',
            'type': MealType.SALAD,
            'servings': 2
        },
        {
            'name': 'Black Bean and Avocado Salad',
            'type': MealType.SALAD,
            'servings': 4
        },




        {
            'name': 'Perfect Pesto',
            'type': MealType.SIDES,
            'servings': 6
        },
        {
            'name': 'Hummus',
            'type': MealType.SIDES,
            'servings': 1
        },



        {
            'name': '"Cream" of Broccoli Soup',
            'type': MealType.ENTREE,
            'servings': 6
        },
        {
            'name': 'Quick and Easy Artichoke and Tomato Sauce Dinner',
            'type': MealType.ENTREE,
            'servings': 2
        },
        {
            'name': 'Creamy Barley Risotto with Tomatoes and Peas',
            'type': MealType.ENTREE,
            'servings': 4
        },
        {
            'name': 'Tofu Pizza Bites',
            'type': MealType.ENTREE,
            'servings': 2
        },


        {
            'name': 'Peppers',
            'type': MealType.VEGGIES,
            'servings': 2
        },
        {
            'name': 'Carrots',
            'type': MealType.VEGGIES,
            'servings': 5
        },

        {
            'name': 'Oranges',
            'type': MealType.FRUIT,
            'servings': 2
        },
        {
            'name': 'Some Fruit',
            'type': MealType.FRUIT,
            'servings': 12
        }
    ]
}
