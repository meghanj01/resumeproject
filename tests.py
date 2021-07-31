from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def test_first_run(self):
        print("Successful test")
        self.assertEqual(200 ,200)


AdminSiteTests().test_first_run()