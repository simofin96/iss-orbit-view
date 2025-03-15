"""
http://open-notify.org/
https://matplotlib.org/basemap/stable/users/index.html
https://www.astroviewer.net/iss/en/
"""
import time
import draw_map
import iss_api_calls
from pydantic import ValidationError

try:
    ### APIs first data extraction ###
    people_on_iss_list = iss_api_calls.get_people_in_iss() # people aboard the ISS
    timestamp, iss_latitude, iss_longitude = iss_api_calls.get_iss_location() # ISS location and timestamp

    ### Draw Earth and auto-update plot ###
    fig, m, iss, iss_location_text = draw_map.draw_earth(timestamp, iss_latitude, iss_longitude, people_on_iss_list)

    while(True):
        timestamp, iss_latitude, iss_longitude = iss_api_calls.get_iss_location()
        draw_map.update_iss_location(fig, m, iss, timestamp, iss_latitude, iss_longitude, iss_location_text)
        time.sleep(5) # recommended delay between consecutive calls in the documentation.

except ValidationError as e:
        print("Validation failed:")
        for error in e.errors():
            print(f" - Field: {error['loc']}, Error: {error['msg']}")
            
except Exception as e:
    print(f"Unexpected exception: {e}")