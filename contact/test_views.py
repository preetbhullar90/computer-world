from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail


class TestContactViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.contact_url = reverse('send_email')

    def test_contact_GET(self):
        response = self.client.get(self.contact_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_contact_POST_sends_email(self):
        response = self.client.post(self.contact_url)
        mail.send_mail('Subject here', 'Here is the message.',
                       'from@example.com', ['to@example.com'],
                       )

        self.assertEquals(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')
