from django.conf import settings
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
import json

class MailchimpService:
    def __init__(self):
        # print(f"Using API Key: {settings.MAILCHIMP_API_KEY}")  # Debug
        # print(f"Server Prefix: {settings.MAILCHIMP_SERVER_PREFIX}")  # Debug
        # print(f"List ID: {settings.MAILCHIMP_LIST_ID}")  # Debug
        
        self.client = Client()
        self.client.set_config({
            "api_key": settings.MAILCHIMP_API_KEY,
            "server": settings.MAILCHIMP_SERVER_PREFIX  # Must match key suffix
        })
        self.list_id = settings.MAILCHIMP_LIST_ID

    def add_subscriber(self, email, first_name, last_name):
        member_info = {
            "email_address": email,
            "status": "subscribed",
            "merge_fields": {
                "FNAME": first_name,
                "LNAME": last_name
            }
        }
        
        try:
            response = self.client.lists.add_list_member(
                self.list_id,
                member_info
            )
            return True, response
        except ApiClientError as error:
            # Enhanced error parsing
            try:
                error_dict = json.loads(error.text)
                error_msg = error_dict.get('detail', error_dict.get('title', str(error)))
            except:
                error_msg = str(error)
            return False, error_msg
        except Exception as e:
            return False, f"Unexpected error: {str(e)}"