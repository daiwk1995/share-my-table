"""
Define callable requests and responses of the User class actions.
"""
import coreapi
import coreschema
from django.contrib.auth import login, user_logged_in
from django_filters.rest_framework import DjangoFilterBackend
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework import viewsets, mixins, status, generics, filters
from rest_framework.decorators import schema, api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema

from .serializer import *


class LoginView(KnoxLoginView, generics.CreateAPIView):
    """
    Login procedure.
    """
    authentication_classes = []
    permission_classes = [AllowAny, ]
    serializer_class = UserLoginSerializer

    def post(self, request, format_=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)

class UserRegViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """
    Logic for creating an instance of a new user.
    """
    queryset = UserProfile.objects.all()
    authentication_classes = tuple()
    permission_classes = (AllowAny,)
    serializer_class = UserRegSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data

        re_dict['token'] = AuthToken.objects.create(user)
        user_logged_in.send(sender=user.__class__, request=request, user=user)
        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

    def get_object(self):
        return self.request.user


class UserViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    """
    Get the specified user instance from user objects.
    """
    serializer_class = UserDetailSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return UserProfile.objects.get(self.request.user)

    def get_object(self):
        return self.request.user


class UserPasswordViewSet(viewsets.GenericViewSet, mixins.UpdateModelMixin):
    """
    Logic for matching the password of a user.
    """
    serializer_class = PasswordSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return UserProfile.objects.get(self.request.user)

    def get_object(self):
        return self.request.user


class BagListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """
    Define page view of the Bag.
    Specify fields to be display on page.
    Items will be displayed in descending expiration date.
    """
    serializer_class = BagListSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('ingredients__name',)
    ordering_fields = ('id', 'expire_time')
    ordering = ('expire_time',)

    def get_queryset(self):
        return BagItemModel.objects.filter(user=self.request.user)


class BagViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """
    Find and display the bag related to the designated user.
    """
    serializer_class = BagSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return BagItemModel.objects.filter(user=self.request.user)


@api_view(('POST',))
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
@schema(AutoSchema(
    manual_fields=[
        coreapi.Field('category_names', location='body',
                      schema=coreschema.Array(description="Item name (List)"), required=True),
    ]
))
def is_items_exit(request):
    """
    search for the quantity avalaible in the user's bag of a specified item.
    """
    queryset = BagItemModel.objects.filter(user=request.user)
    category_names = request.data.get("category_names", [])
    result = []
    for category_name in category_names:
        category_set = queryset.filter(ingredients__name__icontains=category_name)
        if category_set.count() == 0:
            return Response(0)
        for i in category_set:
            result.append(i)
    count = len(result)
    return Response(count)
