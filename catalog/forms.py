from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

from .models import Comment, Cook, Dish


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'text_comment']


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'image', 'price', 'dish_type', 'cooks']
