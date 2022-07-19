from django.test import TestCase, Client
from django.urls import reverse
from profiles.models import UserProfile


class TestProfileViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.profile_url = reverse('order_history', args=['1'])

        self.profile = UserProfile(
            default_phone_number='0123456789',
            default_street_address1='anywhere',
            default_street_address2='anywhere',
            default_town_or_city='south',
            default_county='london',
            default_postcode='12345',
            default_country='london',
            )

    def test_profile_GET(self):
        response = self.client.get(self.profile_url)

        self.assertEquals(response.status_code, 404)

        response = self.client.post(self.profile_url)
        self.assertEquals(response.status_code, 404)
        self.assertEquals(len(UserProfile.objects.all()), 0)
