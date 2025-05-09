from mailchimp3 import MailChimp
from django.conf import settings


def add_subscriber_to_mailchimp(
    email,
    first_name,
    last_name,
):
    client = MailChimp(mc_api=settings.MAILCHIMP_API_KEY)

    try:
        client.lists.members.create(
            settings.MAILCHIMP_LIST_ID,
            {
                "email_address": email,
                "status": "subscribed",
                "merge_fields": {
                    "FNAME": first_name,
                    "LNAME": last_name,
                },
            },
        )
        print("Successfully added subscriber!")  # Debug statement
        return True
    except Exception as e:
        print(f"Error adding subscriber: {e}")
        return False
