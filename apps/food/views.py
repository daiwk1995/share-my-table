import coreapi
import coreschema
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, mixins, status
from rest_framework.decorators import api_view, schema
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema

from food.serializer import *
from util.pagination import MyPageNumberPagination
from .filters import *
from .models import CategoryModel, RecipeModel


class CategoryListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
        A ViewSet for listing categories
    """
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    pagination_class = MyPageNumberPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', )
    ordering_fields = ('id', 'name')
    ordering = ('id', )


class CategoryViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
        A ViewSet for listing categories
    """
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class IngredientListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
        A ViewSet for listing ingredient list
    """
    queryset = IngredientModel.objects.all()
    serializer_class = IngredientSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('detail',)
    ordering_fields = ('id', 'detail')
    ordering = ('id',)


class IngredientViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
        A ViewSet for listing ingredients
    """
    queryset = IngredientModel.objects.all()
    serializer_class = IngredientSerializer


class RecipeListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
        A ViewSet for listing recipes list
    """
    queryset = RecipeModel.objects.all()
    serializer_class = RecipeListSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('title', 'categories__name', 'ingredients__detail')
    ordering_fields = ('r_id', 'date')
    ordering = ('r_id', )
    filter_class = RecipeFilter


class RecipeViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
        A ViewSet for listing recipes
    """
    queryset = RecipeModel.objects.all()
    serializer_class = RecipeDetailSerializer


@api_view(('POST',))
@schema(AutoSchema(
    manual_fields=[
        coreapi.Field('ids', location='body', schema=coreschema.Array(description="Ingredient Id (List)"), required=True),
        coreapi.Field(
            'option', location='body',
            schema=coreschema.String(
                description="Query option，default is \"aot\"，must be one of the following:"
                            "\"aot\": \"All Of Them\" abbreviation,meaning query answer satisfies all of ids;"
                            "\"oot\": \"One Of Them\" abbreviation,meaning query answer satisfies any of ids;"),
            required=False)
    ]
))
def list_recipe_through_category_ids(request):
    """
    according to ingredient id (category's id list) to list recipes
    """
    recipe_queryset = RecipeModel.objects.all()
    category_queryset = CategoryModel.objects.all()
    ids = request.data.get("ids", [])
    opt = request.data.get("option", 'aot')
    if opt == 'aot':
        for id_ in ids:
            recipe_queryset = recipe_queryset.filter(categories=category_queryset.get(id=id_))
    elif opt == 'oot':
        recipe_queryset = recipe_queryset.filter(categories__in=ids)
    else:
        return Response("Chose one of the options: aot(All Of Them) and oot(One Of Them).",
                        status=status.HTTP_400_BAD_REQUEST)
    recipe_queryset = recipe_queryset.order_by("r_id")
    if len(recipe_queryset):
        paginator = MyPageNumberPagination()
        result_page = paginator.paginate_queryset(recipe_queryset, request)
        serializer = RecipeListSerializer(result_page, many=True)
        paginate_result = {
            "count": paginator.page_size,
            "next": paginator.get_next_link(),
            "previous": paginator.get_previous_link(),
            "results": serializer.data
        }
        return Response(paginate_result)
