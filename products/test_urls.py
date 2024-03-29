from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import (all_products, product_detail, add_product,
                            edit_product, delete_product, submit_review,
                            edit_review, delete_review)


class TestProductUrls(SimpleTestCase):
    def test_all_products_url_is_resolved(self):
        url = reverse('products')
        self.assertEquals(resolve(url).func, all_products)

    def test_product_detail_url_is_resolved(self):
        url = reverse('product_detail', args=['1'])
        self.assertEquals(resolve(url).func, product_detail)

    def test_add_product_url_is_resolved(self):
        url = reverse('add_product')
        self.assertEquals(resolve(url).func, add_product)

    def test_edit_product_url_is_resolved(self):
        url = reverse('edit_product', args=[1])
        self.assertEquals(resolve(url).func, edit_product)

    def test_delete_product_url_is_resolved(self):
        url = reverse('delete_product', args=[3])
        self.assertEquals(resolve(url).func, delete_product)

    def test_submit_review_url_is_resolved(self):
        url = reverse('submit_review', args=[3])
        self.assertEquals(resolve(url).func, submit_review)

    def test_edit_review_url_is_resolved(self):
        url = reverse('edit_review', args=[4])
        self.assertEquals(resolve(url).func, edit_review)

    def test_delete_review_url_is_resolved(self):
        url = reverse('delete_review', args=[5])
        self.assertEquals(resolve(url).func, delete_review)
