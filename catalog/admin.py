from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Dish, Cook, DishType, Comment, Beverages

admin.site.register(Dish)
admin.site.register(Cook,UserAdmin)
admin.site.register(DishType)
admin.site.register(Comment)
admin.site.register(Beverages)
