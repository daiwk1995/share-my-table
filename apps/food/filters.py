import django_filters

from food.models import *


class RecipeFilter(django_filters.FilterSet):
    min_rating = django_filters.NumberFilter('rating', lookup_expr='gte')
    max_rating = django_filters.NumberFilter('rating', lookup_expr='lte')
    min_calories = django_filters.NumberFilter('calories', lookup_expr='gte')
    max_calories = django_filters.NumberFilter('calories', lookup_expr='lte')
    min_protein = django_filters.NumberFilter('protein', lookup_expr='gte')
    max_protein = django_filters.NumberFilter('protein', lookup_expr='lte')
    min_fat = django_filters.NumberFilter('fat', lookup_expr='gte')
    max_fat = django_filters.NumberFilter('fat', lookup_expr='lte')
    min_sodium = django_filters.NumberFilter('sodium', lookup_expr='gte')
    max_sodium = django_filters.NumberFilter('sodium', lookup_expr='lte')
    category_id = django_filters.NumberFilter('categories__id', lookup_expr='exact')
    ingredient_id = django_filters.NumberFilter('ingredients__id', lookup_expr='exact')

    class Meta:
        model = RecipeModel
        fields = ('min_rating', 'max_rating', 'min_calories', 'max_calories', 'min_protein', 'max_protein', 'min_fat',
                  'max_fat', 'min_sodium', 'max_sodium', 'category_id', 'ingredient_id')
