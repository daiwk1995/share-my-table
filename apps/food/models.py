from datetime import datetime

from django.db import models


class RecipeModel(models.Model):
    """
    Recipe model for storing recipe information
    """
    r_id = models.AutoField(primary_key=True, help_text="recipe id")
    title = models.CharField(max_length=256, unique=True, help_text="recipe name")
    rating = models.FloatField()
    calories = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    sodium = models.FloatField()
    date = models.DateTimeField(default=datetime.now, help_text="added time")
    desc = models.CharField(max_length=512, null=True, blank=True, help_text="description")
    ingredients = models.ManyToManyField('IngredientModel', help_text="ingredient details")
    categories = models.ManyToManyField('CategoryModel', help_text="ingredients")

    class Meta:
        verbose_name = "Recipe"

    def __str__(self):
        return self.title


class DirectionModel(models.Model):
    """
    Direction model for storing steps information
    """
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE, related_name="directions", help_text="recipe")
    sequence = models.IntegerField(help_text="sequence of steps")
    detail = models.CharField(max_length=512, help_text="detail of this step")


class IngredientModel(models.Model):
    """
    Ingredient model for storing ingredient information
    """
    detail = models.CharField(max_length=256, help_text="Ingredient details")

    def __str__(self):
        return self.detail


class CategoryModel(models.Model):
    """
    Category model for storing category information
    """
    name = models.CharField(max_length=256, unique=True, help_text="Ingredient name")

    def __str__(self):
        return self.name
