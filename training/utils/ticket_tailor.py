import os
import requests
from django.conf import settings
from django.utils.timezone import make_aware
from datetime import datetime


def get_ticket_tailor_events():
    api_key = os.getenv("TICKET_TAILOR_API_KEY")
    url = "https://api.tickettailor.com/v1/events"
    headers = {"Authorization": f"Bearer {api_key}", "Accept": "application/json"}

    response = requests.get(url, headers=headers)
    events = response.json().get("data", [])

    processed_events = []
    for event in events:
        processed_events.append(
            {
                "event_id": event["id"],
                "name": event["name"],
                "description": event.get("description", ""),
                "start_datetime": make_aware(
                    datetime.fromisoformat(event["start"]["date"])
                ),
                "end_datetime": make_aware(
                    datetime.fromisoformat(event["end"]["date"])
                ),
                "url": event["url"],
                "image_url": event.get("image_url"),
                "is_active": event["status"] == "published",
            }
        )

    return processed_events
