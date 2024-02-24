from django.shortcuts import render
from .models import Dish


def index(request):
    dishes = Dish.objects.all()
    return render(request, 'index.html', {'dishes': dishes})
