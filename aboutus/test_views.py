from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail


class TestAboutusViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.aboutus_url = reverse('aboutus')
        self.sitemap_url = reverse('sitemap')
        self.newsletter_signup_url = reverse('newsletter_signup')
        self.newsletter_unsubscribe_url = reverse('newsletter_unsubscribe')
        self.privacy_policy_url = reverse('privacy_policy')

    def test_aboutus_GET(self):
        response = self.client.get(self.aboutus_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'aboutus/aboutus.html')

    def test_sitemap_GET(self):
        response = self.client.get(self.sitemap_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'aboutus/sitemap.html')

    def test_newsletter_signup_page_GET(self):
        response = self.client.get(self.newsletter_signup_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'aboutus/sign_up.html')

    def test_unsubscribe_GET(self):
        response = self.client.get(self.newsletter_unsubscribe_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'aboutus/unsubscribe.html')

    def test_signup_page_POST_sends_email(self):
        response = self.client.post(self.newsletter_signup_url)
        mail.send_mail('Subject here', 'Here is the message.',
                       'from@example.com', ['to@example.com'],
                       )

        self.assertEquals(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')

    def test_unsubscribe_page_POST_sends_email(self):
        response = self.client.post(self.newsletter_unsubscribe_url)
        mail.send_mail('Subject here', 'Here is the message.',
                       'from@example.com', ['to@example.com'],
                       )

        self.assertEquals(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')

    def test_privacy_policy_GET(self):
        response = self.client.get(self.privacy_policy_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'aboutus/privacy_policy.html')
