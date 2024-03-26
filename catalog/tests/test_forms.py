from django.test import TestCase

from catalog.forms import CommentForm, DishForm


class CommentFormTest(TestCase):
    def test_comment_form_valid(self):
        form_data = {'name': 'John Doe', 'email': 'john@example.com', 'text_comment': 'This is a test comment.'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid(self):
        form_data = {'name': 'John Doe', 'email': 'invalidemail', 'text_comment': 'This is a test comment.'}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())


class DishFormTest(TestCase):
    def test_dish_form_valid(self):
        form_data = {'name': 'Pizza', 'description': 'Delicious pizza', 'price': 10.99, 'dish_type': 'Main Dish', 'cooks': [1]}
        form = DishForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_dish_form_invalid(self):
        form_data = {'name': '', 'description': 'Delicious pizza', 'price': 10.99, 'dish_type': 'Main Dish', 'cooks': [1]}
        form = DishForm(data=form_data)
        self.assertFalse(form.is_valid())
