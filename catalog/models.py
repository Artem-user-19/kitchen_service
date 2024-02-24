from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    year_of_experience = models.IntegerField(null=True, default=0)


class Dish(models.Model):
    DISH_TYPE_CHOICES = (
        ('Appetizer', 'Appetizer'),
        ('Main Course', 'Main Course'),
        ('Dessert', 'Dessert'),
        ('Beverage', 'Beverage'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.CharField(max_length=20, choices=DISH_TYPE_CHOICES)
    cooks = models.ManyToManyField(Cook, related_name='dishes')

    def __str__(self):
        return self.name
