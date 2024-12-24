from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

def update_iss_location(fig, m, iss, new_timestamp, new_lat, new_lon, iss_location_text):
    """This function updates the position of the ISS on the map."""
    x, y = m(new_lon, new_lat)
    iss.set_data(x, y)
    iss_location_text.set_text(f"ISS Coordinates\n\nLatitude: {new_lat}°\nLongitude: {new_lon}°\n{new_timestamp}")
    fig.canvas.draw()
    plt.pause(0.1)

def draw_earth(timestamp, iss_latitude, iss_longitude, number_people_on_iss, list_people_on_iss):
    """This function draws the Earth and a dot that indicates the current position of the ISS. 
    llcrnrlat, llcrnrlon, urcrnrlat, urcrnrlon are the lat/lon values of the lower left 
    and upper right corners of the map. lat_ts is the latitude of true scale.
    resolution = 'c' means use crude resolution coastlines."""
    fig = plt.figure(figsize=(12, 8)) 
    m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80,
                llcrnrlon=-180, urcrnrlon=180, lat_ts=20, resolution='c')

    x, y = m(iss_longitude, iss_latitude)
    iss, = m.plot(x, y, color="red", marker="o", markersize=10, label='ISS Position')

    m.drawcoastlines()
    m.fillcontinents(color='lightgreen', lake_color='aqua')
    m.drawmapboundary(fill_color='aqua')
    # m.drawparallels(np.arange(-90.,91.,30.)) # draw parallels
    # m.drawmeridians(np.arange(-180.,181.,60.)) # draw meridians
    plt.title("ISS location - Mercator Projection", fontweight="bold")
    plt.subplots_adjust(bottom=0.2, top=0.95, left=0.05, right=0.8)

    # Crew info in the figure
    fig.text(0.87, 0.75, f"Number of crew members\n\n{number_people_on_iss}", fontweight="bold", ha="center")
    string_list_people_on_iss = "\n".join(list_people_on_iss) # a single string is created containing each name, separated by \n.
    fig.text(0.87, 0.4, f"Crew members\n\n{string_list_people_on_iss}", fontweight="bold", ha="center")

    # ISS location in the figure
    iss_location_text = fig.text(0.4, 0.08, f"ISS Coordinates\n\nLatitude: {iss_latitude}°\nLongitude: {iss_longitude}°\n{timestamp}", fontweight="bold", ha="center")

    return fig, m, iss, iss_location_text
