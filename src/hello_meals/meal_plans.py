from enum import Enum


class MealType(Enum):
    BREAKFAST = 'Breakfast'
    ENTREE = 'Entree'
    FRUIT = 'Fruit'
    VEGGIES = 'Veggies'
    SIDES = 'Sides'
    SALAD = 'Salad'


meal_plan = {
    'meal_plan_name': 'Justin - BLE - Week 2',
    'meals': [
        # Breakfasts
        {
            'name': 'Burrito Breakfast Bake',
            'type': MealType.BREAKFAST,
            'servings': 2
        },


        {
            'name': 'Cereal',
            'type': MealType.BREAKFAST,
            'servings': 2
        },
        {
            'name': 'Milk - 4oz',
            'type': MealType.SIDES,
            'servings': 2
        },
        {
            'name': 'Nuts/Seeds - 1oz',
            'type': MealType.SIDES,
            'servings': 2,
        },
        {
            'name': 'Fruit - 6oz',
            'type': MealType.FRUIT,
            'servings': 2
        },



        # Entrees
        {
            'name': 'Black Bean Burger',
            'type': MealType.ENTREE,
            'servings': 3
        },
        {
            'name': 'Greens - 1oz',
            'type': MealType.VEGGIES,
            'servings': 3
        },
        {
            'name': 'Fruit - 6oz',
            'type': MealType.FRUIT,
            'servings': 3
        },
        {
            'name': 'Peppers|Cauli - 4oz',
            'type': MealType.VEGGIES,
            'servings': 3
        },


        {
            'name': 'Fresh',
            'type': MealType.ENTREE,
            'servings': 1
        },



        {
            'name': 'Chickpea & Vegetable Tagine',
            'type': MealType.ENTREE,
            'servings': 2
        },
        {
            'name': 'Fruit - 5oz/7oz',
            'type': MealType.FRUIT,
            'servings': 1
        },
        {
            'name': 'Nut Butter - 1oz',
            'type': MealType.SIDES,
            'servings': 1
        },
        {
            'name': 'Nuts/Seeds - 1.5oz',
            'type': MealType.SIDES,
            'servings': 1
        },


        {
            'name': 'Taco Salad',
            'type': MealType.ENTREE,
            'servings': 1
        },
        {
            'name': 'Hummus - 3oz',
            'type': MealType.SIDES,
            'servings': 2
        },
        {
            'name': 'Nuts/Seeds - 0.25oz',
            'type': MealType.SIDES,
            'servings': 2
        },
        {
            'name': 'Carrots/Peppers - 4.5oz',
            'type': MealType.VEGGIES,
            'servings': 1
        }
    ]
}
