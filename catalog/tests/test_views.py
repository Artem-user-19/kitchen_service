from django.test import TestCase, Client
from django.urls import reverse
from catalog.models import Dish, Beverages, Cook
from django.contrib.auth.models import User


class ViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.cook = Cook.objects.create(username='cookuser', password='cookpassword')
        self.dish = Dish.objects.create(name='Test Dish', description='Test Description', price=10.99, dish_type='Appetizer')
        self.beverage = Beverages.objects.create(name='Test Beverage', price=5.99)
        self.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse('catalog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.jinja')

    def test_guest_page_view(self):
        response = self.client.get(reverse('catalog:guest_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'guest_page.jinja')

    def test_details_view(self):
        response = self.client.get(reverse('catalog:detail', args=[self.dish.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail.jinja')

    def test_beverage_list_view(self):
        response = self.client.get(reverse('catalog:beverages'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'beverages.jinja')

    def test_user_dishes_view(self):
        response = self.client.get(reverse('catalog:user_dishes', args=[self.cook.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cooker_data.jinja')

    def test_create_dish_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('catalog:create_dish'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_dish.jinja')

    def test_update_dish_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('catalog:update_dish', args=[self.dish.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dish_form.jinja')

    def test_delete_dish_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('catalog:delete_dish', args=[self.dish.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_dish.jinja')

    def test_logout_view(self):
        response = self.client.get(reverse('catalog:logout'))
        self.assertEqual(response.status_code, 302)  # Redirects after logout
