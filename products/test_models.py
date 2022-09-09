from django.test import TestCase
from products.models import Category, Product, Review
import tempfile


class TestProdutsModels(TestCase):

    def setUp(self):
        self.category = Category(
            name='preet',
            friendly_name='monitor'
            )
        self.product = Product(
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

        self.reviews = Review(
            product=self.product,
            rating=3.4,
            review='this is review',
            status=True,
        )

    def test_create_category(self):
        self.assertEquals(self.category.name, 'preet')
        self.assertEquals(self.category.friendly_name, 'monitor')

    def test_create_product(self):
        self.assertEquals(self.product.sku, '45353er')
        self.assertEquals(self.product.name, 'preet')
        self.assertEquals(self.product.description, 'this is description')
        self.assertEquals(self.product.has_sizes, True)
        self.assertEquals(self.product.price, 34.5)
        self.assertEquals(self.product.weight, 34.5)
        self.assertEquals(self.product.dimension, '34')

    def test_create_reviews(self):
        self.assertEquals(self.reviews.rating, 3.4)
        self.assertEquals(self.reviews.review, 'this is review')
        self.assertEquals(self.reviews.status, True)

    def test_category_cascade_works(self):
        category = self.category
        category.save()

        product = len(Product.objects.all())
        reviews = len(Review.objects.all())

        self.assertEquals(product, 0)
        self.assertEquals(reviews, 0)
