import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def update_iss_trajectory(fig, map, trajectory_plot, trajectory_lat, trajectory_lon):
    """This function updates the ISS trajectory on the map."""
    trajectory_x, trajectory_y = map(trajectory_lon, trajectory_lat)
    trajectory_plot.set_data(trajectory_x, trajectory_y)
    fig.canvas.draw()
    plt.pause(0.1)


def update_iss_location(fig, map, iss_plot, iss_location_text, new_timestamp, new_iss_latitude, new_iss_longitude):
    """This function updates the position of the ISS on the map."""
    new_iss_x, new_iss_y = map(new_iss_longitude, new_iss_latitude)
    iss_plot.set_data(new_iss_x, new_iss_y)
    iss_location_text.set_text(f"ISS Coordinates\n\nLatitude: {new_iss_latitude}°\nLongitude: {new_iss_longitude}°\n{new_timestamp}")
    fig.canvas.draw()
    plt.pause(0.1)


def draw_earth(timestamp, iss_latitude, iss_longitude, people_on_iss_list):
    """This function draws the Earth and a dot that indicates the current position of the ISS. 
    llcrnrlat, llcrnrlon, urcrnrlat, urcrnrlon are the lat/lon values of the lower left 
    and upper right corners of the map. lat_ts is the latitude of true scale.
    resolution = 'c' means use crude resolution coastlines."""
    fig = plt.figure(figsize=(12, 8)) 
    map = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80,
                llcrnrlon=-180, urcrnrlon=180, lat_ts=20, resolution='c')

    iss_x, iss_y = map(iss_longitude, iss_latitude)
    
    trajectory_plot, = map.plot([iss_x], [iss_y], linestyle="-", color="darkblue", linewidth=4, label="ISS Trajectory")
    iss_plot, = map.plot(iss_x, iss_y, color="red", marker="o", markersize=12, label='ISS Position')
    
    map.drawcoastlines(linewidth=1, color='gray')
    map.drawmapboundary(fill_color='lightblue')
    map.fillcontinents(color='lightgreen', lake_color='lightblue')
    map.drawparallels(np.arange(-90.,91.,30.), labels=[1,0,0,0], fontsize=10, color='gray')  # draw parallels
    map.drawmeridians(np.arange(-180.,181.,60.), labels=[0,0,0,1], fontsize=10, color='gray') # draw meridians
    plt.title("ISS location - Mercator Projection", fontweight="bold", fontsize=16)

    plt.subplots_adjust(bottom=0.2, top=0.95, left=0.05, right=0.8)

    # Crew info in the figure
    fig.text(0.88, 0.72, f"Number of crew members\n\n{len(people_on_iss_list)}", 
             fontweight="bold", 
             fontsize=12,
             ha="center",
             bbox=dict(facecolor='beige', alpha=0.5))
    people_on_iss_list_string = "\n".join(people_on_iss_list) # a single string is created containing each name, separated by \n.
    fig.text(0.88, 0.27, f"Crew members\n\n{people_on_iss_list_string}", 
             fontweight="bold", 
             fontsize=12,
             ha="center",
             bbox=dict(facecolor='beige', alpha=0.5))

    # ISS location in the figure
    iss_location_text = fig.text(0.42, 0.03, f"ISS Coordinates\n\nLatitude: {iss_latitude}°\nLongitude: {iss_longitude}°\n{timestamp}", 
                                 fontweight="bold",
                                 fontsize=12, 
                                 ha="center", 
                                 bbox=dict(facecolor='beige', alpha=0.5))

    # Show the figure
    fig.canvas.draw()
    plt.pause(0.1)

    return fig, map, iss_plot, trajectory_plot, iss_location_text
