# subscriptions/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from .models import Subscriber


class SubscriptionTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.subscribe_url = reverse("subscribe")

    def test_valid_submission(self):
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "agree_to_policy": True,
        }
        response = self.client.post(self.subscribe_url, data)

        # Debug: Print form errors if the response is not a redirect
        if response.status_code != 302:
            print("Form errors:", response.context["form"].errors)

        # Check for redirect
        self.assertEqual(response.status_code, 302)

        # Check if the subscriber was saved
        self.assertTrue(
            Subscriber.objects.filter(email="john.doe@example.com").exists()
        )

    def test_invalid_submission(self):
        data = {
            "first_name": "",  # Missing required field
            "last_name": "Doe",
            "email": "invalid-email",  # Invalid email
            "agree_to_policy": False,  # Must be True
        }
        response = self.client.post(self.subscribe_url, data)
        self.assertEqual(response.status_code, 200)  # Form should re-render
        self.assertFormError(response, "form", "first_name", "This field is required.")
        self.assertFormError(response, "form", "email", "Enter a valid email address.")
        self.assertFormError(
            response, "form", "agree_to_policy", "This field is required."
        )
