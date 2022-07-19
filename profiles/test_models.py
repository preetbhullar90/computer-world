from django.test import TestCase
from profiles.models import UserProfile


class TestProfilesModels(TestCase):

    def setUp(self):
        self.profile = UserProfile(
            default_phone_number='0123456789',
            default_street_address1='anywhere',
            default_street_address2='anywhere',
            default_town_or_city='south',
            default_county='london',
            default_postcode='12345',
            default_country='london',
            )

    def test_create_profile(self):
        self.assertEquals(self.profile.default_phone_number, '0123456789')
        self.assertEquals(self.profile.default_street_address1, 'anywhere')
        self.assertEquals(self.profile.default_street_address2, 'anywhere')
        self.assertEquals(self.profile.default_town_or_city, 'south')
        self.assertEquals(self.profile.default_county, 'london')
        self.assertEquals(self.profile.default_postcode, '12345')
        self.assertEquals(self.profile.default_country, 'london')

    def test_profile_cascade_works(self):
        profile = len(UserProfile.objects.all())

        self.assertEquals(profile, 0)

