import numpy as np

def update_trajectory(lat_list, lon_list, new_lat, new_lon, max_length=1000, lat_threshold=90, lon_threshold=180):
    """
    Updates the ISS trajectory lists, managing map jumps and maximum length.

    Parameters:
        lat_list (list): List of recorded latitudes.
        lon_list (list): List of recorded longitudes.
        new_lat (float): New latitude to add.
        new_lon (float): New longitude to add.
        max_length (int): Maximum number of elements in the lists.
        lat_threshold (float): Latitude jump threshold.
        lon_threshold (float): Longitude jump threshold.

    Returns:
        list, list: Updated lists of latitudes and longitudes.
    """
    ### Check for sudden jumps in coordinates
    if lat_list and lon_list: # check if the lists are not empty
        last_lat = lat_list[-1]
        last_lon = lon_list[-1]

        # If the jump is greater than the thresholds, insert a NaN before adding the new points
        if abs(new_lat - last_lat) > lat_threshold or abs(new_lon - last_lon) > lon_threshold:
            lat_list.append(np.nan)
            lon_list.append(np.nan)

    # Add the new values to the lists
    lat_list.append(new_lat)
    lon_list.append(new_lon)

    ### Ensure the trajectory lists do not exceed the maximum length
    # If the lists exceed the maximum length, remove the oldest elements
    if len(lat_list) > max_length or len(lon_list) > max_length:
        removed_lat = lat_list.pop(0)
        removed_lon = lon_list.pop(0)

        # If the removed element is NaN, remove the next element as well
        if (np.isnan(removed_lat) or np.isnan(removed_lon)) and lat_list and lon_list:
            lat_list.pop(0)
            lon_list.pop(0)

    return lat_list, lon_list
