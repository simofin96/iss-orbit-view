"""
This module provides functions to fetch and validate data from the APIs in use.
"""
import requests
import datetime
from pydantic import ValidationError
from data_validation import OpenNotifyPeopleOnSpaceModel, WhereTheISSAtLocationModel

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
    # print(f"Number of people currently in space: {number_of_people_in_space}")

    list_people_in_space = response_json["people"]
    list_people_on_iss = {astronaut["name"] for astronaut in list_people_in_space if astronaut["craft"] == "ISS"}
    # number_people_on_iss = len(list_people_on_iss)

    # print(f"Number of people currently on the ISS: {number_people_on_iss}")
    # print("\nNames:")
    # for astronaut in list_people_on_iss:
    #     print(astronaut)

    return list_people_on_iss


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

    # print(f"\nTimestamp: {timestamp}")
    # print(f"Current ISS latitude: {iss_latitude}")
    # print(f"Current ISS longitude: {iss_longitude}")

    return timestamp, iss_latitude, iss_longitude