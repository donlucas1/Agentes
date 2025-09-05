from fastapi import FastAPI
from .agents.accommodation_agent import AccommodationAgent
from .agents.sightseeing_agent import SightseeingAgent
from .agents.visa_agent import VisaAgent

app = FastAPI(title="Tourism Multi-Agent API")

accommodation_agent = AccommodationAgent()
sightseeing_agent = SightseeingAgent()
visa_agent = VisaAgent()


@app.get("/accommodation")
def accommodation(city: str, check_in: str, check_out: str):
    """Get accommodation options for a city and date range."""
    return {"results": accommodation_agent.search(city, check_in, check_out)}


@app.get("/sightseeing")
def sightseeing(city: str):
    """Get tourist attractions for a city."""
    return {"results": sightseeing_agent.attractions(city)}


@app.get("/requirements")
def requirements(country_from: str, country_to: str):
    """Get visa requirements for travel from one country to another."""
    return visa_agent.requirements(country_from, country_to)
