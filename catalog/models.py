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
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.CharField(max_length=20, choices=DISH_TYPE_CHOICES)
    cooks = models.ManyToManyField(Cook, related_name='dishes')

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='comments', null=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    text_comment = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.post}"


class Beverages(models.Model):
    name = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.price}"
