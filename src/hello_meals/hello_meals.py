from src.hello_meals.meal_plans import meal_plan, MealType
from src.pyllo.pyllo import Pyllo, LabelColor
from calendar import day_name as weekday_names
import calendar
import json
import logging
from src.TqdmToLogger import TqdmToLogger
from tqdm import tqdm


class HelloMeals(object):
    bar_format = '{l_bar}{bar}| {n}/{total} {unit}'

    def __init__(self, a_pyllo, a_meal_plan, tqdm_out):
        self.pyllo = a_pyllo
        response = self.pyllo.create_board(a_meal_plan['meal_plan_name'])
        logging.debug('Create Board response: %s', response.text)
        self.meal_plan_id = json.loads(response.text)['id']
        logging.info('Meal Plan "%s:" Id = %s', a_meal_plan['meal_plan_name'], self.meal_plan_id)

        self.meal_labels = self.create_meal_type_labels(self.meal_plan_id)
        logging.info('Meal Labels Created')

        self.create_weekday_lists()
        logging.info('Weekday Lists Created')

        meal_response = self.pyllo.create_list(self.meal_plan_id, 'Meals', 'top')
        logging.debug('Create Meals List Response: %s', meal_response.text)
        meal_list_id = json.loads(meal_response.text)['id']
        logging.info('Meals List Id = %s', meal_list_id)

        for meal in tqdm(a_meal_plan['meals'], file=tqdm_out, unit='meal'):
            for _ in tqdm(range(meal['servings']), file=tqdm_out, unit='serving'):
                self.pyllo.create_card(
                    meal_list_id,
                    '{}'.format(meal['name']), self.meal_labels[meal['type']]
                )

    def create_weekday_lists(self, meals_in_day=None):
        if meals_in_day is None:
            meals_in_day = [
                MealType.BREAKFAST,
                MealType.ENTREE,
                MealType.VEGGIES,
                MealType.FRUIT,
                MealType.SIDES,
                MealType.ENTREE,
                MealType.SALAD,
                MealType.FRUIT
            ]
        for i, day in tqdm(enumerate(range(calendar.firstweekday(), calendar.firstweekday() + len(weekday_names))),
                           file=tqdm_log, unit='day', total=7):
            response = self.pyllo.create_list(self.meal_plan_id, weekday_names[day % 7], i + 1)
            logging.debug('Create Weekday List response: %s', response.text)
            day_id = json.loads(response.text)['id']

            for meal_in_day in meals_in_day:
                self.pyllo.create_card(day_id, meal_in_day.value, self.meal_labels[meal_in_day])

    def create_meal_type_labels(self, meal_plan_id, color_map=None):
        if color_map is None:
            color_map = {
                MealType.BREAKFAST: LabelColor.SKY,
                MealType.FRUIT: LabelColor.RED,
                MealType.VEGGIES: LabelColor.YELLOW,
                MealType.ENTREE: LabelColor.BLACK,
                MealType.SIDES: LabelColor.PINK,
                MealType.SALAD: LabelColor.GREEN
            }

        meal_type_to_color_id = {}
        for meal_type in list(MealType):
            response = self.pyllo.create_label(meal_type.value, meal_plan_id, color_map[meal_type])
            logging.debug('Create Meal Type Label response', response.text)
            meal_type_to_color_id[meal_type] = json.loads(response.text)['id']
            logging.info('Meal Type Label %s = %s', meal_type, meal_type_to_color_id[meal_type])
        return meal_type_to_color_id


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s [%(levelname)-8s] %(message)s')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    tqdm_log = TqdmToLogger(logger, level=logging.INFO)

    calendar.setfirstweekday(calendar.SUNDAY)
    pyllo = Pyllo(key='',
                  token='')
    hello_meals = HelloMeals(pyllo, meal_plan, tqdm_log)
