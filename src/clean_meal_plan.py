import logging
import calendar
from src.pyllo.pyllo import Pyllo
from src.meal_plans import MealType


def is_meal_slot(meal):
    return meal['name'] in [meal_type.value for meal_type in list(MealType)]


def slot_has_been_filled(meals, i, meal):
    not_last_meal = i + 1 != len(meals)
    if is_meal_slot(meal) and not_last_meal and not is_meal_slot(meals[i + 1]):
        logging.debug('Slot has been filled: {} | {}'.format(meal['name'], meals[i+1]['name']))
        return True


def clean_meal_plan(a_pyllo, meal_plan_name):
    days = a_pyllo.get_lists(meal_plan_name)
    logging.debug('Days in %s: %s', meal_plan_name, days)

    for day in days:
        logging.debug('Day: %s', day)
        meals = a_pyllo.get_cards(day['id'])
        logging.debug('Meals: %s', meals)

        [
            a_pyllo.delete_card(meal['id']) and
            a_pyllo.remove_labels(meals[i + 1]['id']) and
            logging.info('Deleting Meal Slot {} on {}'.format(meal['name'], day['name']))
            for i, meal in enumerate(meals)
            if slot_has_been_filled(meals, i, meal)
        ]


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s [%(levelname)-8s] %(message)s')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    calendar.setfirstweekday(calendar.SUNDAY)
    pyllo = Pyllo(key='',
                  token='')
    clean_meal_plan(pyllo, 'Test Meal Plan - 1')
