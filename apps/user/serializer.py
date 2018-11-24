"""
Declare responses of the User class.
"""
from rest_framework import serializers as srs
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.validators import UniqueValidator

from food.serializer import CategorySerializer
from .models import *

"""
Declare fields required for sign-up.
"""
class UserIntroSerializer(srs.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'first_name', 'last_name']

"""
Declare password storage and update rules.
"""
class PasswordSerializer(srs.ModelSerializer):
    old_password = srs.CharField(allow_blank=False, max_length=16, min_length=6, write_only=True,
                                 style={'input_type': 'password'})
    new_password = srs.CharField(allow_blank=False, max_length=16, min_length=6, write_only=True,
                                 style={'input_type': 'password'})

    def update(self, instance, validated_data):
        if instance.check_password(validated_data['old_password']):
            instance.set_password(validated_data['new_password'])
            instance.save()
        else:
            raise srs.ValidationError("old password is not true")

    class Meta:
        model = UserProfile
        fields = ['old_password', 'new_password']

"""
Fields requried for user login.
"""
class UserLoginSerializer(srs.ModelSerializer, AuthTokenSerializer):
    username = srs.CharField(required=True, help_text="username")
    password = srs.CharField(allow_blank=False, max_length=16, min_length=6, write_only=True,
                             style={'input_type': 'password'}, help_text="password")

    class Meta:
        model = UserProfile
        fields = ['username', 'password']

"""
Declare fields of user information.
"""
class UserDetailSerializer(srs.ModelSerializer):
    username = srs.CharField(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name', 'birthday', 'gender', 'email']

"""
User registration rules.
Providing user update and storage mechanism.
"""
class UserRegSerializer(srs.ModelSerializer):
    username = srs.CharField(required=True, allow_blank=False, validators=[UniqueValidator(
        queryset=UserProfile.objects.all(), message="User exists!")])
    password = srs.CharField(allow_blank=False, max_length=16, min_length=6, write_only=True,
                             style={'input_type': 'password'})
    first_name = srs.CharField(required=True, max_length=20)
    last_name = srs.CharField(required=True, max_length=20)

    def create(self, validated_data):
        user = super(UserRegSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = UserProfile
        fields = ['username', 'password', 'first_name', 'last_name']

"""
Display for items in the bag.
Specify fields to display for each item in the bag.
Item list view in bag.
"""
class BagListSerializer(srs.ModelSerializer):
    user = srs.HiddenField(
        default=srs.CurrentUserDefault(), write_only=True
    )
    inputted_time = srs.DateField(read_only=True, format='%Y-%m-%d')
    expire_time = srs.DateField(required=True, format='%Y-%m-%d', input_formats=['%Y-%m-%d', 'iso-8601'])
    ingredients = CategorySerializer()

    class Meta:
        model = BagItemModel
        fields = ['id', 'user', 'weight', 'inputted_time', 'expire_time', 'ingredients']

"""
Data fields for each item.
Stores item inputted time and expiration date
"""
class BagSerializer(srs.ModelSerializer):
    user = srs.HiddenField(
        default=srs.CurrentUserDefault(), write_only=True
    )
    inputted_time = srs.DateField(read_only=True, format='%Y-%m-%d')
    expire_time = srs.DateField(required=True, format='%Y-%m-%d', input_formats=['%Y-%m-%d', 'iso-8601'])

    class Meta:
        model = BagItemModel
        fields = ['id', 'user', 'weight', 'inputted_time', 'expire_time', 'ingredients']
