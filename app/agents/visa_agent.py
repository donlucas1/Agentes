from typing import Dict, Any
import requests

class VisaAgent:
    """Agent that checks visa and entry requirements using TravelBriefing API."""

    def requirements(self, country_from: str, country_to: str) -> Dict[str, Any]:
        """Get visa requirements from TravelBriefing API."""
        url = f"https://travelbriefing.org/{country_to}?format=json"
        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            data = resp.json()
        except requests.RequestException:
            return {}

        passports = data.get("passports", {})
        return passports.get(country_from.upper(), {})
