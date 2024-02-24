from django.contrib import admin

from .models import Dish, Cook, DishType

admin.site.register(Dish)
admin.site.register(Cook)
admin.site.register(DishType)
