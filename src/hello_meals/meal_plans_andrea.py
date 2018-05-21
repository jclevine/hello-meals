from enum import Enum


class MealType(Enum):
    BREAKFAST = 'Breakfast'
    ENTREE = 'Entree'
    FRUIT = 'Fruit'
    VEGGIES = 'Veggies'
    SIDES = 'Sides'
    SALAD = 'Salad'


meal_plan = {
    'meal_plan_name': 'Andrea - BLE - Week 2',
    'meals': [
        # Breakfasts
        {
            'name': 'Cereal',
            'type': MealType.BREAKFAST,
            'servings': 4
        },
        {
            'name': 'Milk - 4oz',
            'type': MealType.SIDES,
            'servings': 4
        },
        {
            'name': 'Nuts/Seeds - 1oz',
            'type': MealType.SIDES,
            'servings': 4,
        },
        {
            'name': 'Fruit - 6oz',
            'type': MealType.FRUIT,
            'servings': 4
        },



        # Entrees
        {
            'name': 'Black Bean Burger',
            'type': MealType.ENTREE,
            'servings': 2
        },
        {
            'name': 'Greens - 1oz',
            'type': MealType.VEGGIES,
            'servings': 2
        },
        {
            'name': 'Fruit - 6oz',
            'type': MealType.FRUIT,
            'servings': 2
        },
        {
            'name': 'Peppers|Cauli - 4oz',
            'type': MealType.VEGGIES,
            'servings': 2
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
            'servings': 2
        },
        {
            'name': 'Nut Butter - 0.5oz',
            'type': MealType.SIDES,
            'servings': 2
        },
        {
            'name': 'Olives - 2oz',
            'type': MealType.SIDES,
            'servings': 2
        },


        {
            'name': 'Taco Salad',
            'type': MealType.ENTREE,
            'servings': 2
        },
        {
            'name': 'Hummus - 3oz',
            'type': MealType.SIDES,
            'servings': 2
        },
        {
            'name': 'Olives - 1oz',
            'type': MealType.SIDES,
            'servings': 2
        },
        {
            'name': 'Carrots/Peppers - 4.5oz',
            'type': MealType.VEGGIES,
            'servings': 2
        }
    ]
}
