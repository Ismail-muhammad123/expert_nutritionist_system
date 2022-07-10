from unicodedata import category
from django.db import models

# Create your models here.


class FoodItem(models.Model):
    name = models.CharField(max_length=200, unique=True)
    calories = models.PositiveIntegerField()
    unit = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
