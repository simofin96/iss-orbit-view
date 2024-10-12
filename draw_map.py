from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

def draw_earth(current_iss_latitude, current_iss_longitude):
    # llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
    # are the lat/lon values of the lower left and upper right corners
    # of the map.
    # lat_ts is the latitude of true scale.
    # resolution = 'c' means use crude resolution coastlines.

    plt.figure(figsize=(12, 8)) 
    m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,\
                llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')

    x, y = m(current_iss_longitude, current_iss_latitude)
    m.plot(x, y, color="red", marker="o", markersize=10, label='ISS Position')

    m.drawcoastlines()
    m.fillcontinents(color='lightgreen',lake_color='aqua')

    # draw parallels and meridians.
    m.drawparallels(np.arange(-90.,91.,30.))
    m.drawmeridians(np.arange(-180.,181.,60.))
    
    m.drawmapboundary(fill_color='aqua')

    plt.title("Mercator Projection")
    plt.show()