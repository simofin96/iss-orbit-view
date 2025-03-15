"""
https://matplotlib.org/basemap/stable/users/index.html
https://www.astroviewer.net/iss/en/
"""
import time
import draw_map
import iss_api_calls
from pydantic import ValidationError
from logger_config import configure_logger

logger = configure_logger()

try:
    ### APIs first data extraction
    people_on_iss_list = iss_api_calls.get_people_in_iss() # people aboard the ISS
    timestamp, iss_latitude, iss_longitude = iss_api_calls.get_iss_location() # ISS location and timestamp

    ### Draw Earth and auto-update plot
    fig, m, iss, trajectory, iss_location_text = draw_map.draw_earth(timestamp, iss_latitude, iss_longitude, people_on_iss_list)

    # Initialize lists to store the ISS trajectory
    initial_iss_longitude, initial_iss_latitude = m(iss_longitude, iss_latitude)
    trajectory_lon = [initial_iss_longitude]
    trajectory_lat = [initial_iss_latitude]

    while(True):
        time.sleep(5) # delay between consecutive API calls
        timestamp, iss_latitude, iss_longitude = iss_api_calls.get_iss_location()
        
        new_iss_longitude, new_iss_latitude = m(iss_longitude, iss_latitude)
        trajectory_lon.append(new_iss_longitude)
        trajectory_lat.append(new_iss_latitude)

        draw_map.update_iss_location(fig, iss, timestamp, new_iss_latitude, new_iss_longitude, iss_location_text)
        draw_map.update_iss_trajectory(fig, trajectory, trajectory_lat, trajectory_lon)

except ValidationError as e:
    error_messages = " | ".join([f"Field: {error['loc']}, Error: {error['msg']}" for error in e.errors()])
    logger.error(f"Validation failed: {error_messages}")

except Exception as e:
    logger.error(f"Unexpected exception: {e}")