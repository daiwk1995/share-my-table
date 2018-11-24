from rest_framework import serializers as srs

from food.models import CategoryModel, IngredientModel, DirectionModel, RecipeModel

"""
    convert complex data to native Python data types
"""
class CategorySerializer(srs.ModelSerializer):
    """
        convert category data to native Python data types
    """
    class Meta:
        model = CategoryModel
        fields = "__all__"


class IngredientSerializer(srs.ModelSerializer):
    """
        convert ingredient data to native Python data types
    """
    class Meta:
        model = IngredientModel
        fields = "__all__"


class DirectionSerializer(srs.ModelSerializer):
    """
        convert direction data to native Python data types
    """
    class Meta:
        model = DirectionModel
        fields = ["sequence", "detail"]


class RecipeListSerializer(srs.ModelSerializer):
    """
        convert recipe list data to native Python data types
    """
    date = srs.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    ingredients = IngredientSerializer(many=True)
    categories = CategorySerializer(many=True)

    class Meta:
        model = RecipeModel
        fields = ['r_id', 'title', 'rating', 'calories', 'protein', 'fat', 'sodium', 'date', 'ingredients',
                  'categories']


class RecipeDetailSerializer(srs.ModelSerializer):
    """
        convert Recipe detail data to native Python data types
    """
    date = srs.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    ingredients = srs.StringRelatedField(many=True)
    categories = CategorySerializer(many=True)
    directions = DirectionSerializer(many=True)

    class Meta:
        model = RecipeModel
        fields = "__all__"
