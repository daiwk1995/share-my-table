import os
import sys
import json

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_demo.settings')
sys.path.append(os.path.dirname(__file__))
django.setup()

from food.models import RecipeModel, IngredientModel, DirectionModel, CategoryModel


def set_null_value(value):
    return value if value else 0


def input_data(recipe_dict_list):
    for recipe in recipe_dict_list:
        try:
            if RecipeModel.objects.filter(title=recipe["title"]):
                print("[%s] existed. current: %d/%d" %
                      (recipe["title"], len(RecipeModel.objects.all()), len(recipe_dict_list)))
                continue
            ing_list = [IngredientModel.objects.get_or_create(detail=ing)[0] for ing in recipe["ingredients"]]
            cat_list = [CategoryModel.objects.get_or_create(name=cat)[0] for cat in recipe["categories"]]

            rec_model = RecipeModel.objects.create(
                fat=set_null_value(recipe["fat"]),
                date=recipe["date"],
                calories=set_null_value(recipe["calories"]),
                desc=recipe["desc"],
                protein=set_null_value(recipe["protein"]),
                rating=set_null_value(recipe["rating"]),
                title=recipe["title"],
                sodium=set_null_value(recipe["sodium"]),
            )

            [DirectionModel.objects.create(sequence=i + 1, detail=dire, recipe_id=rec_model.r_id)
             for i, dire in enumerate(recipe["directions"])]

            for i in ing_list:
                rec_model.ingredients.add(i)
            for j in cat_list:
                rec_model.categories.add(j)
            rec_model.save()
            print("current: %d/%d" % (len(RecipeModel.objects.all()), len(recipe_dict_list)))
        except KeyError:
            print("record error. current: %d/%d" %
                  (len(RecipeModel.objects.all()), len(recipe_dict_list)))


with open("full_format_recipes.json", encoding='utf-8') as data_file:
    line = data_file.readline()
    d = json.loads(line)
    input_data(d)
