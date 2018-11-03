from datetime import datetime

from django.db import models


class RecipeModel(models.Model):
    """
    Recipe model
    """
    r_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256, unique=True)
    rating = models.FloatField()
    calories = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    sodium = models.FloatField()
    date = models.DateTimeField(default=datetime.now)
    desc = models.CharField(max_length=512, null=True, blank=True)
    ingredients = models.ManyToManyField('IngredientModel')
    categories = models.ManyToManyField('CategoryModel')

    class Meta:
        verbose_name = "Recipe"

    def __str__(self):
        return self.title


class DirectionModel(models.Model):
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE, related_name="directions")
    sequence = models.IntegerField()
    detail = models.CharField(max_length=512)


class IngredientModel(models.Model):
    detail = models.CharField(max_length=256)

    def __str__(self):
        return self.detail


class CategoryModel(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name
