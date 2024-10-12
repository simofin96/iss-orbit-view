"""
http://open-notify.org/
"""
import requests

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
