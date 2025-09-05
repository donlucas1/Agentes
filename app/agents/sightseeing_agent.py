from typing import List, Dict
import os
import requests

class SightseeingAgent:
    """Agent that suggests tourist attractions using OpenTripMap API."""

    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.getenv("OPENTRIPMAP_API_KEY")

    def attractions(self, city: str) -> List[Dict]:
        """Fetch tourist attractions for a given city."""
        if not self.api_key:
            return []
        base_url = "https://api.opentripmap.com/0.1/en/places/geoname"
        try:
            resp = requests.get(base_url, params={"name": city, "apikey": self.api_key}, timeout=10)
            resp.raise_for_status()
            geodata = resp.json()
            lon, lat = geodata.get("lon"), geodata.get("lat")
            if lon is None or lat is None:
                return []
            resp = requests.get(
                "https://api.opentripmap.com/0.1/en/places/radius",
                params={"lon": lon, "lat": lat, "radius": 1000, "limit": 5, "apikey": self.api_key},
                timeout=10,
            )
            resp.raise_for_status()
            data = resp.json().get("features", [])
        except requests.RequestException:
            data = []
        return [feat["properties"] for feat in data]
