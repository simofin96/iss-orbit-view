"""
http://open-notify.org/
https://matplotlib.org/basemap/stable/users/index.html
https://www.astroviewer.net/iss/en/
"""
import time
import draw_map
import iss_api_calls

### People in ISS ###
number_people_on_iss, list_people_on_iss = iss_api_calls.get_people_in_iss()

### ISS location ###
timestamp, iss_latitude, iss_longitude = iss_api_calls.get_iss_location()

### Draw Earth and auto-update plot ###
fig, m, iss = draw_map.draw_earth(iss_latitude, iss_longitude)

while(True):
    timestamp, iss_latitude, iss_longitude = iss_api_calls.get_iss_location()
    draw_map.update_iss_location(fig, m, iss, iss_latitude, iss_longitude)
    time.sleep(5) # recommended delay between consecutive calls in the documentation.