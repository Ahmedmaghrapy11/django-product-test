from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product
class ProductViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_products_list_view(self):
        Product.objects.create(user=self.user, code='P1', name='Product 1')
        Product.objects.create(user=self.user, code='P2', name='Product 2')
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('products_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Product 1')
        self.assertContains(response, 'Product 2')

    def test_create_product_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('create_product'), {'code': 'P1', 'name': 'Product 1'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Product.objects.count(), 1)

    def test_update_product_view(self):
        product = Product.objects.create(user=self.user, code='P1', name='Product 1')
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('update_product', kwargs={'pk': product.pk}), {'code': 'P1 Updated', 'name': 'Product 1 Updated'})
        self.assertEqual(response.status_code, 302)
        product.refresh_from_db()
        self.assertEqual(product.code, 'P1 Updated')

    def test_delete_product_view(self):
        product = Product.objects.create(user=self.user, code='P1', name='Product 1')
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('delete_product', kwargs={'pk': product.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Product.objects.count(), 0)