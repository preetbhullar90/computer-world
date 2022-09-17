from django.test import TestCase, Client
from django.urls import reverse
from products.models import Category, Product, Review
import tempfile


class TestProductsViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.category_url = reverse('product_detail', args=['1'])
        self.product_url = reverse('products')
        self.product_add_url = reverse('add_product')
        self.product_edit_url = reverse('edit_product', args=['1'])
        self.product_delete_url = reverse('delete_product', args=['5'])
        self.submit_review_url = reverse('submit_review', args=['3'])
        self.edit_review_url = reverse('edit_review', args=['1'])
        self.delete_review_url = reverse('delete_review', args=['1'])

        self.category = Category.objects.create(
            name='preet',
            friendly_name='monitor'
        )

        self.product = Product.objects.create(
            category=self.category,
            sku='45353er',
            name='preet',
            description='this is description',
            has_sizes=True,
            price=34.5,
            image_url=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            image1=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            image2=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            weight=34.5,
            dimension='34',
        )

        self.reviews = Review.objects.create(
            product=self.product,
            rating=3.4,
            review='this is review',
            status=True,
        )

    def test_category_GET(self):
        response = self.client.get(self.category_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_product_GET(self):
        response = self.client.get(self.product_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_add_url_GET(self):
        response = self.client.get(self.product_add_url)
        self.assertEquals(response.status_code, 302)

    def test_product_edit_url_GET(self):
        response = self.client.get(self.product_edit_url)
        self.assertEquals(response.status_code, 302)

    def test_product_delete_url_GET(self):
        response = self.client.get(self.product_delete_url)
        self.assertEquals(response.status_code, 302)

    def test_submit_review_GET(self):
        response = self.client.get(self.submit_review_url)
        self.assertEquals(response.status_code, 404)

    def test_edit_review_GET(self):
        response = self.client.get(self.edit_review_url)
        self.assertEquals(response.status_code, 302)

    def test_delete_review_GET(self):
        response = self.client.get(self.delete_review_url)
        self.assertEquals(response.status_code, 302)

        response = self.client.post(self.category_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(Category.objects.all()), 1)

        response = self.client.post(self.product_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(Product.objects.all()), 1)

        response = self.client.post(self.product_add_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(len(Product.objects.all()), 1)

        response = self.client.post(self.product_edit_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(len(Product.objects.all()), 1)

        response = self.client.post(self.product_delete_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(len(Product.objects.all()), 1)

        response = self.client.post(self.submit_review_url)
        self.assertEquals(response.status_code, 404)
        self.assertEquals(len(Review.objects.all()), 1)

        response = self.client.post(self.edit_review_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(len(Review.objects.all()), 1)

        response = self.client.post(self.delete_review_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(len(Review.objects.all()), 1)
