from enum import Enum
from src.ressie.meal_type import MealType
from itertools import product
from src.common.gender import Gender


meals = [MealType.BREAKFAST, MealType.LUNCH, MealType.DINNER]


def create_meal_plan_types_enum_map(meals, maintenance_levels_count):
    combos = list(product(*[meals, list(Gender), list(range(1, maintenance_levels_count))]))
    for combo in combos:
        name = '{}_{}_{}'.format(combo[0].value, combo[1].value, combo[2]).upper()
        print("{0} = MealPlanType('{0}', MealType.{1}, Gender.{2}, {3})"
              .format(name, combo[0].value.upper(), combo[1].value.upper(), combo[2]))


create_meal_plan_types_enum_map(meals, 17)
