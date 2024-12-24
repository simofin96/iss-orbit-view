import requests
import datetime

def get_people_in_iss():
    """This function returns the number of people aboard the ISS and a list of its crew members."""
    response = requests.get("http://api.open-notify.org/astros.json")

    # number_of_people_in_space = response.json()["number"]
    # print(f"People currently in space: {number_of_people_in_space}")

    list_people_in_space = response.json()["people"]
    list_people_on_iss = {astronaut["name"] for astronaut in list_people_in_space if astronaut["craft"] == "ISS"}
    number_people_on_iss = len(list_people_on_iss)

    # print(f"Number of people currently on the ISS: {number_people_on_iss}")
    # print("\nNames:")
    # for astronaut in list_people_on_iss:
    #     print(astronaut)

    return number_people_on_iss, list_people_on_iss


def get_iss_location():
    """This function returns the coordinates (latitude and longitude) of the ISS and the corresponding timestamp.""" 
    response = requests.get("http://api.open-notify.org/iss-now.json")

    timestamp_unix_format = response.json()["timestamp"]
    timestamp = datetime.datetime.fromtimestamp(timestamp_unix_format) 
    iss_latitude = float(response.json()["iss_position"]["latitude"])
    iss_longitude = float(response.json()["iss_position"]["longitude"])

    # print(f"\nTimestamp: {timestamp}")
    # print(f"Current ISS latitude: {iss_latitude}")
    # print(f"Current ISS longitude: {iss_longitude}")

    return timestamp, iss_latitude, iss_longitude