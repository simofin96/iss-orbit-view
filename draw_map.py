from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

def update_iss_location(fig, m, iss, new_lat, new_lon):
    """This function updates the position of the ISS on the map."""
    x, y = m(new_lon, new_lat)
    iss.set_data(x, y)
    fig.canvas.draw()
    plt.pause(0.1)

def draw_earth(iss_latitude, iss_longitude):
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
    plt.title("Mercator Projection")
    
    return fig, m, iss
