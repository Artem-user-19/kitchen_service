from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User

# from catalog.admin import Dish, CookAdmin, DishTypeAdmin, CommentAdmin, BeveragesAdmin
from catalog.models import Dish, Cook, DishType, Comment, Beverages


class AdminTestCase(TestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(username='admin', email='admin@example.com', password='admin')
        self.client.login(username='admin', password='admin')

    def test_dish_admin(self):
        site = AdminSite()
        dish_admin = DishAdmin(Dish, site)
        self.assertEqual(dish_admin.list_display, ('name', 'description', 'price', 'dish_type', 'cooks'))
        self.assertTrue(dish_admin.list_filter, ('dish_type', 'cooks'))

    def test_cook_admin(self):
        site = AdminSite()
        cook_admin = CookAdmin(Cook, site)
        self.assertEqual(cook_admin.list_display, ('username', 'email', 'first_name', 'last_name'))
        self.assertTrue(cook_admin.list_filter, ('is_staff', 'is_superuser'))

    def test_dish_type_admin(self):
        site = AdminSite()
        dish_type_admin = DishTypeAdmin(DishType, site)
        self.assertEqual(dish_type_admin.list_display, ('name',))
        self.assertTrue(dish_type_admin.search_fields, ('name',))

    def test_comment_admin(self):
        site = AdminSite()
        comment_admin = CommentAdmin(Comment, site)
        self.assertEqual(comment_admin.list_display, ('dish', 'user', 'comment', 'created_at'))
        self.assertTrue(comment_admin.list_filter, ('created_at',))

    def test_beverages_admin(self):
        site = AdminSite()
        beverages_admin = BeveragesAdmin(Beverages, site)
        self.assertEqual(beverages_admin.list_display, ('name', 'description', 'price', 'cooks'))
        self.assertTrue(beverages_admin.list_filter, ('cooks',))
