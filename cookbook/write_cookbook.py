from src.ressie.cookbook import Cookbook
from src.ressie.ingredient import Ingredient
from src.ressie.meal_type import MealType
from src.ressie.recipe import Recipe
from src.ressie.tinydb_cookbook import TinyDBCookbook
from src.ressie.unit import Unit as U
from src.ressie.ingredients import Ingredients as I
import os

recipes = [
    Recipe('Blue Apple Nut Oatmeal', [
        Ingredient(I.WATER, 1.5, U.CUPS),
        Ingredient(I.OATS, 30, U.GRAMS),
        Ingredient(I.RAISINS, 20, U.GRAMS),
        Ingredient(I.BERRIES, 120, U.GRAMS),
        Ingredient(I.BANANAS, 1, U.UNITS),
        Ingredient(I.APPLES, 1, U.UNITS),
        Ingredient(I.NUTS, 15, U.GRAMS)
    ],
           servings=2,
           type=MealType.BREAKFAST
           ),
    Recipe('Cinnamon-Spiced Baked Oatmeal', [
        Ingredient(I.OATS, 100, U.GRAMS),
        Ingredient(I.RAISINS, 50, U.GRAMS),
        Ingredient(I.DATES, 2, U.UNITS),
        Ingredient(I.FLAXSEEDS, 10, U.GRAMS),
        Ingredient(I.MILK, 237, U.MILLILITRES),
        Ingredient(I.WATER, 158, U.MILLILITRES),
        Ingredient(I.VANILLA_EXTRACT, 1, U.TEASPOONS),
        Ingredient(I.CINNAMON, 1, U.TEASPOONS),
        Ingredient(I.BERRIES, 0.5, U.CUPS)
    ],
           servings=3,
           type=MealType.BREAKFAST
           ),
    Recipe('No-Cook strawberry Oatmeal To-Go', [
        Ingredient(I.OATS, 33, U.GRAMS),
        Ingredient(I.CHIA_SEEDS, 10, U.GRAMS),
        Ingredient(I.MILK, 158, U.MILLILITRES),
        Ingredient(I.BERRIES, 1, U.CUPS),
        Ingredient(I.NUTS, 6, U.UNITS)
    ],
           servings=1,
           type=MealType.BREAKFAST
           ),
    Recipe('Creamy Buckwheat Porridge', [
        Ingredient(I.BUCKWHEAT, 1, U.CUPS),
        Ingredient(I.DATES, 2, U.UNITS),
        Ingredient(I.MILK, 3, U.TABLESPOONS),
        Ingredient(I.VANILLA_EXTRACT, 1, U.TEASPOONS),
        Ingredient(I.CINNAMON, 0.5, U.TEASPOONS),
        Ingredient(I.CHIA_SEEDS, 10, U.GRAMS),
        Ingredient(I.NUTS, 2, U.TABLESPOONS),
        Ingredient(I.FRUIT, 0.5, U.CUPS)
    ],
           servings=3,
           type=MealType.BREAKFAST
           ),
    Recipe('Quick Breakfast Quinoa', [
        Ingredient(I.QUINOA, 1, U.CUPS),
        Ingredient(I.WATER, 474, U.MILLILITRES),
        Ingredient(I.APPLES, 1, U.UNITS),
        Ingredient(I.NUTS, 67, U.GRAMS),
        Ingredient(I.BERRIES, 115, U.GRAMS),
        Ingredient(I.DATES, 62, U.GRAMS),
        Ingredient(I.CINNAMON, 1, U.TEASPOONS),
        Ingredient(I.MILK, 119, U.MILLILITRES)
    ],
           servings=4,
           type=MealType.BREAKFAST
           ),
    Recipe('Chia Seed Breakfast Pudding', [
        Ingredient(I.MILK, 119, U.MILLILITRES),
        Ingredient(I.CHIA_SEEDS, 2, U.TABLESPOONS),
        Ingredient(I.OATS, 2, U.TABLESPOONS),
        Ingredient(I.BANANAS, 0.5, U.UNITS),
        Ingredient(I.BERRIES, 0.5, U.CUPS)
    ],
           servings=1,
           type=MealType.BREAKFAST
           ),
    Recipe('Quick Banana Walnut Breakfast', [
        Ingredient(I.BANANAS, 1, U.UNITS),
        Ingredient(I.MILK, 119, U.MILLILITRES),
        Ingredient(I.BERRIES, 0.5, U.CUPS),
        Ingredient(I.NUTS, 0.25, U.CUPS),
        Ingredient(I.FLAXSEEDS, 0.5, U.TABLESPOONS)
    ],
           servings=1,
           type=MealType.BREAKFAST
           ),
    Recipe('Fruity Chickpea Cereal', [
        Ingredient(I.CHICKPEAS, 1.5, U.CUPS),
        Ingredient(I.BANANAS, 2, U.UNITS)
    ],
           servings=2,
           type=MealType.BREAKFAST
           ),
    Recipe('Tofu Scramble with Tomatoes and Peppers', [
        Ingredient(I.PEPPERS, 1, U.CUPS),
        Ingredient(I.ONIONS, 0.5, U.CUPS),
        Ingredient(I.GARLIC, 1, U.UNITS),
        Ingredient(I.TOMATOES_DICED, 1.5, U.CUPS),
        Ingredient(I.TOFU_FIRM, 14, U.OUNCES),
        Ingredient(I.SPINACH, 1, U.CUPS),
        Ingredient(I.GARLIC_POWDER, 1, U.TEASPOONS),
        Ingredient(I.TURMERIC, 0.5, U.TEASPOONS),
        Ingredient(I.RED_PEPPER_FLAKES, 0.25, U.TEASPOONS),
    ],
           servings=2,
           type=MealType.BREAKFAST
           ),
    Recipe('Creamy Breakfast Broccoli', [
        Ingredient(I.BROCCOLI, 1, U.UNITS),
        Ingredient(I.LEEKS, 1, U.UNITS),
        Ingredient(I.AVOCADOS, 1, U.UNITS),
        Ingredient(I.BLACK_PEPPER, 0.25, U.TEASPOONS)
    ],
           servings=2,
           type=MealType.BREAKFAST
           ),

    Recipe('Ginger Almond Dressing', [
        Ingredient(I.ALMONDS, 70, U.GRAMS),
        Ingredient(I.SEEDS_SESAME, 14, U.GRAMS),
        Ingredient(I.MILK, 119, U.MILLILITRES),
        Ingredient(I.VINEGAR_RICE, 30, U.MILLILITRES),
        Ingredient(I.DATES, 50, U.GRAMS),
        Ingredient(I.GARLIC, 1, U.UNITS),
        Ingredient(I.GINGER, 0.5, U.INCHES)
    ],
           servings=3,
           type=MealType.SALAD_DRESSING
           ),
    Recipe('Easy Balsamic Almond Dressing', [
        Ingredient(I.WATER, 2, U.TABLESPOONS),
        Ingredient(I.VINEGAR_BALSAMIC, 25, U.MILLILITRES),
        Ingredient(I.BUTTER_ALMOND, 17, U.GRAMS),
        Ingredient(I.ONION_POWDER, 0.25, U.TEASPOONS),
        Ingredient(I.GARLIC_POWDER, 0.25, U.TEASPOONS),
        Ingredient(I.OREGANO, 0.125, U.TEASPOONS),
        Ingredient(I.BASIL_DRIED, 0.125, U.TEASPOONS)
    ],
           servings=1,
           type=MealType.SALAD_DRESSING
           ),
    Recipe('Banana Walnut Dressing', [
        Ingredient(I.BANANAS, 2, U.UNITS),
        Ingredient(I.NUTS, 2, U.TABLESPOONS),
        Ingredient(I.RAISINS, 2, U.TABLESPOONS),
        Ingredient(I.VINEGAR_FRUITY, 59, U.MILLILITRES),
        Ingredient(I.GARLIC_POWDER, 0.25, U.TEASPOONS),
        Ingredient(I.OREGANO, 0.125, U.TEASPOONS),
        Ingredient(I.BASIL_DRIED, 0.125, U.TEASPOONS)
    ],
           servings=2,
           type=MealType.SALAD_DRESSING
           ),
    Recipe('Balsamic Tomato and Asparagus Salad', [
        Ingredient(I.ASPARAGUS, 454, U.GRAMS),
        Ingredient(I.TOMATOES, 1, U.CUPS),
        Ingredient(I.VINEGAR_BALSAMIC, 30, U.MILLILITRES),
        Ingredient(I.JUICE_ORANGE, 15, U.MILLILITRES),
        Ingredient(I.BLACK_PEPPER, 0.5, U.TEASPOONS),
        Ingredient(I.ONIONS_RED, 15, U.GRAMS),
        Ingredient(I.GREENS, 5, U.OUNCES),
        Ingredient(I.NUTS_PINE, 3, U.TABLESPOONS)
    ],
           servings=4,
           type=MealType.SALAD
           ),
    Recipe('Black Bean and Avocado Salad', [
        Ingredient(I.BEANS_BLACK, 15, U.OUNCES),
        Ingredient(I.TOMATOES_PLUM, 3, U.UNITS),
        Ingredient(I.CORN, 0.75, U.CUPS),
        Ingredient(I.PEPPERS, 0.25, U.CUPS),
        Ingredient(I.ONIONS_RED, 0.25, U.CUPS),
        Ingredient(I.CILANTRO, 2, U.TABLESPOONS),
        Ingredient(I.PEPPERS_JALEPENO, 1, U.UNITS),
        Ingredient(I.VINEGAR_RED_WINE, 30, U.MILLILITRES),
        Ingredient(I.LIMES, 0.5, U.UNITS),
        Ingredient(I.CUMIN, 0.25, U.TEASPOONS),
        Ingredient(I.AVOCADOS, 2, U.UNITS)
    ],
           servings=4,
           type=MealType.SALAD
           ),

    Recipe('Back-to-Basics Guacamole', [
        Ingredient(I.AVOCADOS, 2, U.UNITS),
        Ingredient(I.ONIONS, 65, U.GRAMS),
        Ingredient(I.TOMATOES, 80, U.GRAMS),
        Ingredient(I.GARLIC, 1, U.UNITS),
        Ingredient(I.CILANTRO, 12, U.GRAMS),
        Ingredient(I.JUICE_LIME, 30, U.MILLILITRES),
        Ingredient(I.CUMIN, 0.25, U.TEASPOONS),
        Ingredient(I.BLACK_PEPPER, 0.25, U.TEASPOONS)
    ],
           servings=4,
           type=MealType.SIDES
           ),
    Recipe('Perfect Pesto', [
        Ingredient(I.NUTS, 110, U.GRAMS),
        Ingredient(I.NUTS_PINE, 90, U.GRAMS),
        Ingredient(I.BASIL, 1, U.CUPS),
        Ingredient(I.CILANTRO, 26, U.GRAMS),
        Ingredient(I.GARLIC, 3, U.UNITS),
        Ingredient(I.BRAGGS_LIQUID_AMINOS, 10, U.MILLILITRES),
        Ingredient(I.JUICE_LEMON, 30, U.MILLILITRES),
        Ingredient(I.TOMATOES, 80, U.GRAMS)
    ],
           servings=6,
           type=MealType.SIDES
           ),

    Recipe('Buenas Noches Black Bean Soup', [
        Ingredient(I.ONIONS, 1, U.UNITS),
        Ingredient(I.CELERY, 2, U.CUPS),
        Ingredient(I.CARROTS, 2, U.CUPS),
        Ingredient(I.GARLIC, 4, U.UNITS),
        Ingredient(I.CUMIN, 1, U.TABLESPOONS),
        Ingredient(I.CHILI_POWDER, 2, U.TEASPOONS),
        Ingredient(I.BLACK_PEPPER, 0.25, U.TEASPOONS),
        Ingredient(I.WATER, 6, U.CUPS),
        Ingredient(I.MRS_DASH, 1, U.TABLESPOONS),
        Ingredient(I.BEANS_BLACK, 60, U.OUNCES),
        Ingredient(I.SALSA, 16, U.OUNCES),
        Ingredient(I.CORN, 2, U.CUPS),
        Ingredient(I.TOMATOES_DICED, 1.5, U.CUPS)
    ],
           servings=6,
           type=MealType.ENTREE
           ),
    Recipe('Easy Split Pea Stew', [
        Ingredient(I.SPLIT_PEAS, 453, U.GRAMS),
        Ingredient(I.BROTH, 8, U.CUPS),
        Ingredient(I.BAY_LEAVES, 1, U.UNITS),
        Ingredient(I.THYME_DRIED, 0.5, U.TEASPOONS),
        Ingredient(I.CUMIN, 1, U.TEASPOONS),
        Ingredient(I.ONIONS, 260, U.GRAMS),
        Ingredient(I.CELERY, 190, U.GRAMS),
        Ingredient(I.CARROTS, 180, U.GRAMS),
        Ingredient(I.MUSHROOMS, 65, U.GRAMS),
        Ingredient(I.GARLIC, 2, U.UNITS),
        Ingredient(I.SPINACH, 200, U.GRAMS),
        Ingredient(I.VINEGAR_SHERRY, 30, U.MILLILITRES)
    ],
           servings=6,
           type=MealType.ENTREE
           ),

    Recipe('Easy Ratatouille', [
        Ingredient(I.TOMATOES_CRUSHED, 26, U.OUNCES),
        Ingredient(I.ZUCCHINIS, 6, U.UNITS),
        Ingredient(I.EGGPLANTS, 1, U.UNITS),
        Ingredient(I.ONIONS, 1, U.UNITS),
        Ingredient(I.GARLIC, 6, U.UNITS),
        Ingredient(I.MRS_DASH, 2, U.TABLESPOONS),
        Ingredient(I.THYME_DRIED, 1, U.TEASPOONS),
        Ingredient(I.ROSEMARY_DRIED, 0.5, U.TEASPOONS)
    ],
           servings=4,
           type=MealType.ENTREE
           ),
    Recipe('Baked Kale and Cabbage Casserole', [
        Ingredient(I.ONIONS, 2, U.UNITS),
        Ingredient(I.BRAGGS_LIQUID_AMINOS, 1, U.TEASPOONS),
        Ingredient(I.CABBAGES, 0.5, U.UNITS),
        Ingredient(I.KALE, 1, U.UNITS),
        Ingredient(I.CARROTS, 2, U.UNITS),
        Ingredient(I.TOFU_SILKEN, 7, U.OUNCES),
        Ingredient(I.MILK, 60, U.MILLILITRES),
        Ingredient(I.NUTRITIONAL_YEAST, 0.25, U.CUPS),
        Ingredient(I.BASIL_DRIED, 2, U.TEASPOONS),
        Ingredient(I.OREGANO, 1, U.TEASPOONS),
        Ingredient(I.PAPRIKA, 1, U.TEASPOONS),
        Ingredient(I.GARLIC, 3, U.UNITS),
        Ingredient(I.ALMONDS, 0.5, U.CUPS)
    ],
           servings=6,
           type=MealType.ENTREE
           ),
    Recipe('Creamy Barley Risotto with Tomatoes and Peas', [
        Ingredient(I.ONIONS, 1, U.UNITS),
        Ingredient(I.GARLIC, 1, U.TEASPOONS),
        Ingredient(I.BARLEY, 1.5, U.CUPS),
        Ingredient(I.BASIL_DRIED, 0.5, U.TEASPOONS),
        Ingredient(I.OREGANO, 0.5, U.TEASPOONS),
        Ingredient(I.TOMATOES, 1.5, U.CUPS),
        Ingredient(I.MILK, 350, U.MILLILITRES),
        Ingredient(I.WATER, 473, U.CUPS),
        Ingredient(I.NUTRITIONAL_YEAST, 0.25, U.CUPS),
        Ingredient(I.MISO, 0.5, U.TABLESPOONS),
        Ingredient(I.PEAS, 1, U.CUPS)
    ],
           servings=4,
           type=MealType.ENTREE
           ),
    Recipe('Farro with Black Beans and Fresh Herbs', [
        Ingredient(I.FARRO, 1, U.CUPS),
        Ingredient(I.PEPPERS, 2, U.UNITS),
        Ingredient(I.ONIONS_RED, 0.5, U.UNITS),
        Ingredient(I.PARSLEY, 2, U.TABLESPOONS),
        Ingredient(I.CILANTRO, 2, U.TABLESPOONS),
        Ingredient(I.LEMONS, 1, U.UNITS),
        Ingredient(I.BEANS_BLACK, 1.5, U.CUPS),
        Ingredient(I.GARLIC_POWDER, 0.5, U.TEASPOONS),
        Ingredient(I.BLACK_PEPPER, 0.25, U.TEASPOONS),
        Ingredient(I.CUMIN, 0.25, U.TEASPOONS)
    ],
           servings=4,
           type=MealType.ENTREE
           ),

    Recipe('Chickpea Burgers', [
        Ingredient(I.CHICKPEAS, 250, U.GRAMS),
        Ingredient(I.ONIONS_RED, 35, U.GRAMS),
        Ingredient(I.ZUCCHINIS, 60, U.GRAMS),
        Ingredient(I.VINEGAR_RED_WINE, 30, U.MILLILITRES),
        Ingredient(I.KETCHUP, 35, U.GRAMS),
        Ingredient(I.BUTTER_PEANUT, 30, U.GRAMS),
        Ingredient(I.CUMIN, 1, U.TEASPOONS),
        Ingredient(I.GARLIC_POWDER, 1, U.TEASPOONS),
        Ingredient(I.BLACK_PEPPER, 0.25, U.TEASPOONS),
        Ingredient(I.OATS, 90, U.GRAMS),
        Ingredient(I.TOMATOES, 2, U.UNITS),
        Ingredient(I.GREENS, 3, U.OUNCES)
    ],
           servings=3,
           type=MealType.ENTREE
           ),
    Recipe('Tofu Pizza Bites', [
        Ingredient(I.TOFU_FIRM, 12, U.OUNCES),
        Ingredient(I.PASTA_SAUCE, 1, U.CUPS),
        Ingredient(I.TOMATO_PASTE, 2, U.TABLESPOONS),
        Ingredient(I.GARLIC_POWDER, 1, U.TEASPOONS),
        Ingredient(I.ONION_POWDER, 1, U.TEASPOONS)
    ],
           servings=2,
           type=MealType.ENTREE
           ),

    Recipe('Peppers', [
        Ingredient(I.PEPPERS, 3, U.UNITS)
    ],
           servings=3,
           type=MealType.VEGGIES
           ),
    Recipe('Carrots', [
        Ingredient(I.CARROTS, 3, U.UNITS)
    ],
           servings=3,
           type=MealType.VEGGIES
           ),
    Recipe('Cucumbers', [
        Ingredient(I.CUCUMBERS, 1, U.UNITS)
    ],
           servings=4,
           type=MealType.VEGGIES
           ),

    Recipe('Strawberries', [
        Ingredient(I.STRAWBERRIES, 900, U.GRAMS)
    ],
           servings=5,
           type=MealType.FRUIT
           ),
    Recipe('Pears', [
        Ingredient(I.PEARS, 3, U.UNITS)
    ],
           servings=3,
           type=MealType.FRUIT
           ),
    Recipe('Grapes', [
        Ingredient(I.GRAPES, 1, U.UNITS)
    ],
           servings=5,
           type=MealType.FRUIT
           ),
    Recipe('Apples', [
        Ingredient(I.APPLES, 3, U.UNITS)
    ],
           servings=3,
           type=MealType.FRUIT
           )
]

if __name__ == '__main__':
    db_path = os.path.join(os.getcwd(), 'cookbook.tinydb')

    with TinyDBCookbook(db_path) as db:
        cookbook = Cookbook(db)
        cookbook.add_recipes(recipes)
