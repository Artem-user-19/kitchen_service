from django import forms

from .models import Comment, Dish


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "text_comment"]


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ["name", "description", "image", "price", "dish_type", "cooks"]
