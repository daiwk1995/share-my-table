from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'recipes', RecipeListViewSet, base_name="recipes")
router.register(r'recipes', RecipeViewSet, base_name='recipes')
router.register(r'ingredients', IngredientListViewSet, base_name="ingredients")
router.register(r'ingredients', IngredientViewSet, base_name='ingredients')
router.register(r'categories', CategoryViewSet, base_name="categories")
router.register(r'categories', CategoryListViewSet, base_name="categories")

urlpatterns = [
    *router.urls,
    path(r'recipesByCategoriesIds/', list_recipe_through_category_ids),
]
