from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class UserProfile(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(null=True, blank=True, max_length=1,
                              choices=(("m", "male"), ("f", "female")), default="m")

    class Meta:
        verbose_name = "User"

    def __str__(self):
        return self.username


class BagItemModel(models.Model):
    """
    Bag Item Model
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    ingredients = models.ForeignKey('food.CategoryModel', on_delete=models.CASCADE)
    weight = models.FloatField()
    inputted_time = models.DateField(auto_now=True)
    expire_time = models.DateField(null=True, blank=True)
