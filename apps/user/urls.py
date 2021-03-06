"""
Redirect to pages according to user action.
Specifies URL for user actions.
"""
from django.urls import path
from knox import views as knox_views
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'register', UserRegViewSet, base_name='users')
router.register(r'password', UserPasswordViewSet, base_name='users')
router.register(r'users', UserViewSet, base_name='users')
router.register(r'bag_items', BagListViewSet, base_name='bag')
router.register(r'bag_item', BagViewSet, base_name='bag')

urlpatterns = [
    path(r'itemsExit/', is_items_exit),
    path(r'login/', LoginView.as_view(), name='login'),
    path(r'logout/', knox_views.LogoutView.as_view(), name='logout'),
    *router.urls,
]
