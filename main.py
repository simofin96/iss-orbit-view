"""
http://open-notify.org/
"""
import requests
import datetime
import draw_map

### People in ISS ###
response = requests.get("http://api.open-notify.org/astros.json")

number_of_people_in_space = response.json()["number"]
print(f"People currently in space: {number_of_people_in_space}")

list_people_in_space = response.json()["people"]
list_people_on_ISS = {astronaut["name"] for astronaut in list_people_in_space if astronaut["craft"] == "ISS"}
print(f"People currently on the ISS: {len(list_people_on_ISS)}")

print("\nNames:")
for astronaut in list_people_on_ISS:
    print(astronaut)

### ISS location ###
response = requests.get("http://api.open-notify.org/iss-now.json")

timestamp_unix_format = response.json()["timestamp"]
readable_date = datetime.datetime.fromtimestamp(timestamp_unix_format) 
current_latitude = response.json()["iss_position"]["latitude"]
current_longitude = response.json()["iss_position"]["longitude"]

print(f"\nTimestamp: {readable_date}")
print(f"Current latitude: {current_latitude}")
print(f"Current longitude: {current_longitude}")

### Draw Earth ###
draw_map.draw_earth()