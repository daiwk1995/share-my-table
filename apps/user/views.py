from django.contrib.auth import login, user_logged_in
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework import viewsets, mixins, status, generics, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .serializer import *


class LoginView(KnoxLoginView, generics.CreateAPIView):
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
    queryset = UserProfile.objects.all()
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
    serializer_class = UserDetailSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return UserProfile.objects.get(self.request.user)

    def get_object(self):
        return self.request.user


class UserPasswordViewSet(viewsets.GenericViewSet, mixins.UpdateModelMixin):
    serializer_class = PasswordSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return UserProfile.objects.get(self.request.user)

    def get_object(self):
        return self.request.user


class BagListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = BagListSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('ingredients__name',)
    ordering_fields = ('id', 'expire_time')
    ordering = ('expire_time',)

    def get_queryset(self):
        return BagItemModel.objects.filter(user=self.request.user)


class BagViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = BagSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return BagItemModel.objects.filter(user=self.request.user)
