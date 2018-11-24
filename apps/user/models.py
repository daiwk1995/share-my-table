from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class UserProfile(AbstractUser):
    """
    Model for each individual user.
    Store information about the user.
    Contains birthday and gender of an user.
    """
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(null=True, blank=True, max_length=1,
                              choices=(("m", "male"), ("f", "female")), default="m")

    class Meta:
        verbose_name = "User"

    def __str__(self):
        return self.username


class BagItemModel(models.Model):
    """
    Model for items in the bag.
    Stores informaion about each item in the bag.
    Contains name of item, quantity of item, item entry date and item expiration date.
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, help_text="user")
    ingredients = models.ForeignKey('food.CategoryModel', on_delete=models.CASCADE, help_text="individual item")
    weight = models.FloatField(help_text="item quantity")
    inputted_time = models.DateField(auto_now=True, help_text="item entry date")
    expire_time = models.DateField(null=True, blank=True, help_text="item expiration date")
