from typing import List, Dict
import os
import requests

class AccommodationAgent:
    """Agent that searches accommodation options using external providers."""

    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.getenv("AIRBNB_API_KEY")

    def search(self, location: str, check_in: str, check_out: str) -> List[Dict]:
        """Search for accommodations at a destination.

        In a production environment this method would call an API such as Airbnb
        or Booking.com. Here we perform a simple HTTP request to a public
        endpoint that returns sample data to illustrate the flow.
        """
        params = {
            "location": location,
            "check_in": check_in,
            "check_out": check_out,
        }
        try:
            # Placeholder API call - replace with real provider
            resp = requests.get("https://jsonplaceholder.typicode.com/posts", params=params, timeout=10)
            resp.raise_for_status()
            data = resp.json()
        except requests.RequestException:
            data = []
        return data[:5]
