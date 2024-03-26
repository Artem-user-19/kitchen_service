from django.test import TestCase

from catalog.models import DishType, Dish, Comment, Beverages

from django.contrib.auth.models import User


class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.dish_type = DishType.objects.create(name='Test Type')
        self.dish = Dish.objects.create(name='Test Dish', description='Test Description', price=10.99, dish_type='Appetizer')
        self.comment = Comment.objects.create(post=self.dish, name='Test Commenter', email='test@example.com', text_comment='Test Comment')
        self.beverage = Beverages.objects.create(name='Test Beverage', price=5.99)

    def test_dish_type_str(self):
        self.assertEqual(str(self.dish_type), 'Test Type')

    def test_cook_str(self):
        self.assertEqual(str(self.user), 'testuser')

    def test_dish_str(self):
        self.assertEqual(str(self.dish), 'Test Dish')

    def test_comment_str(self):
        self.assertEqual(str(self.comment), 'Test Commenter - Test Dish')

    def test_beverage_str(self):
        self.assertEqual(str(self.beverage), 'Test Beverage - 5.99')
