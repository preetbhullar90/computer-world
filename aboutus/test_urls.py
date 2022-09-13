from django.test import SimpleTestCase
from django.urls import reverse, resolve
from aboutus.views import aboutus, newsletter_signup
from aboutus.views import newsletter_unsubscribe, privacy_policy, sitemap


class TestAboutusUrls(SimpleTestCase):
    def test_aboutus_url_is_resolved(self):
        url = reverse('aboutus')
        self.assertEquals(resolve(url).func, aboutus)

    def test_newsletter_signup_url_is_resolved(self):
        url = reverse('newsletter_signup')
        self.assertEquals(resolve(url).func, newsletter_signup)

    def test_newsletter_unsubscribe_url_is_resolved(self):
        url = reverse('newsletter_unsubscribe')
        self.assertEquals(resolve(url).func, newsletter_unsubscribe)

    def test_privacy_policy_url_is_resolved(self):
        url = reverse('privacy_policy')
        self.assertEquals(resolve(url).func, privacy_policy)

    def test_sitemap_url_is_resolved(self):
        url = reverse('sitemap')
        self.assertEquals(resolve(url).func, sitemap)
