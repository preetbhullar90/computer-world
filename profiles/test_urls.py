from django.test import SimpleTestCase
from django.urls import reverse, resolve
from profiles.views import profile, order_history


class TestProfileUrls(SimpleTestCase):
    def test_profile_url_is_resolved(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

    def test_order_history_url_is_resolved(self):
        url = reverse('order_history', args=['some-slug'])
        self.assertEquals(resolve(url).func, order_history)
