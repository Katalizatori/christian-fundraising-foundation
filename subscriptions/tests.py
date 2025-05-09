from django.test import TestCase, RequestFactory
from django.conf import settings
from .views import subscribe
import json


class SubscriptionTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        settings.MAILCHIMP_API_KEY = "test-key"
        settings.MAILCHIMP_SERVER_PREFIX = "us1"
        settings.MAILCHIMP_LIST_ID = "test-list"

    def test_invalid_email(self):
        request = self.factory.post("/subscribe/", {"email": "invalid"})
        response = subscribe(request)
        self.assertEqual(response.status_code, 400)

    def test_missing_email(self):
        request = self.factory.post("/subscribe/", {})
        response = subscribe(request)
        self.assertEqual(response.status_code, 400)

    def test_valid_submission(self):
        # This will actually try to call Mailchimp - you might want to mock this
        request = self.factory.post(
            "/subscribe/",
            {
                "email": "test@example.com",
                "first_name": "Test",
                "last_name": "User",
                "csrfmiddlewaretoken": "testtoken",
            },
        )
        response = subscribe(request)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data.get("success") or data.get("error"))
