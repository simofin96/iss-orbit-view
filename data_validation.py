"""
This module defines Pydantic models for validating responses from the APIs in use.
"""
from pydantic import BaseModel, field_validator
from typing import List

# Model for Open Notify API response
class Astronaut(BaseModel):
    craft: str
    name: str

class OpenNotifyPeopleOnSpaceModel(BaseModel):
    """Validates the response containing the list of people currently in space."""
    people: List[Astronaut]
    number: int
    message: str

# Model for "Where the ISS at?" API response
class WhereTheISSAtLocationModel(BaseModel):
    """Validates the real-time position and orbital data of the ISS."""
    name: str
    id: int
    latitude: float
    longitude: float
    altitude: float
    velocity: float
    visibility: str
    footprint: float
    timestamp: int
    daynum: float
    solar_lat: float
    solar_lon: float
    units: str

    @field_validator("latitude")
    def check_lat(cls, value):
        if not (-90 <= value <= 90):
            raise ValueError(f"Latitude {value} is out of range. It must be between -90 and 90.")
        return value
    
    @field_validator("longitude")
    def check_lon(cls, value):
        if not (-180 <= value <= 180):
            raise ValueError(f"Longitude {value} is out of range. It must be between -180 and 180.")
        return value