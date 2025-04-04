"""
This module provides functions to fetch and validate data from the APIs in use.
"""
import requests
import datetime
from pydantic import ValidationError
from data_validation import OpenNotifyPeopleOnSpaceModel, WhereTheISSAtLocationModel
import logging

logger = logging.getLogger()

def get_people_in_iss():
    """This function uses the Open Notify API to return the list of crew members currently aboard the ISS."""
    response = requests.get("http://api.open-notify.org/astros.json")
    response_json = response.json()

    # Data validation
    try:
        OpenNotifyPeopleOnSpaceModel(**response_json)
    except ValidationError as val_err:
        raise val_err
    
    # Data extraction
    # number_of_people_in_space = response_json["number"]
    # logger.info(f"Number of people currently in space: {number_of_people_in_space}")

    people_in_space_list = response_json["people"]
    people_on_iss_list = {astronaut["name"] for astronaut in people_in_space_list if astronaut["craft"] == "ISS"}
    # number_people_on_iss = len(people_on_iss_list)

    # logger.info(f"Number of people currently on the ISS: {number_people_on_iss}")
    # astronaut_names = ", ".join(people_on_iss_list)
    # logger.info(f"Names of astronauts currently on the ISS: {astronaut_names}")

    return people_on_iss_list


def get_iss_location():
    """This function uses the 'Where the ISS at?' API to return the latitude and longitude of the ISS along with the corresponding timestamp."""    
    response = requests.get("https://api.wheretheiss.at/v1/satellites/25544")
    response_json = response.json()

    # Data validation
    try:
        WhereTheISSAtLocationModel(**response_json)
    except ValidationError as val_err:
        raise(val_err)
    
    # Data extraction
    timestamp_unix_format = response_json["timestamp"]
    timestamp = datetime.datetime.fromtimestamp(timestamp_unix_format) 
    iss_latitude = response_json["latitude"]
    iss_longitude = response_json["longitude"]

    # logger.info(f"Timestamp: {timestamp}")
    # logger.info(f"Current ISS latitude: {iss_latitude}")
    # logger.info(f"Current ISS longitude: {iss_longitude}")

    return timestamp, iss_latitude, iss_longitude