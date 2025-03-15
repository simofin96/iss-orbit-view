# ISS Orbit View
A project to track and visualize the International Space Station (ISS) in real-time. It fetches the ISS's position via an API, validates the data, and displays the station’s current location and trajectory on a map. Future enhancements may include predictive algorithms for trajectory forecasting.


## Table of Contents
- [APIs Data Extraction](#apis-data-extraction)
- [ISS Location Visualization](#iss-location-visualization)


## APIs Data Extraction
This project utilizes two different APIs to extract data related to the International Space Station (ISS):
- [Open Notify API](http://open-notify.org/)  
This API provides real-time information about the astronauts currently in space, specifically those aboard the ISS.
  
- [Where the ISS At? API](https://wheretheiss.at/)  
This API provides the current location of the ISS, including:
  - Latitude and longitude coordinates
  - Timestamp of the location data
  - Velocity
  - Altitude
  
### Data Validation
Both APIs' responses are validated using [Pydantic](https://pydantic-docs.helpmanual.io/), which ensures that the data conforms to the expected structure before it is processed. This validation guarantees the integrity and correctness of the data before it is utilized in the application.

### Error Handling
The code includes robust error handling that ensures the execution stops if the data returned from either API is incorrect. If any validation errors are encountered during the data extraction process, a `ValidationError` is raised, halting the execution to prevent the usage of invalid data.


## ISS Location Visualization
The ISS location is visualized on a world map, dynamically updating its position based on latitude and longitude. The map is displayed using the Mercator projection and includes the following features:

### Features
- **Current ISS Position**: The ISS is represented by a red dot on the map, which updates in real-time based on the latest coordinates.
- **Map Features**: The map includes coastlines, continents, and ocean boundaries, providing a global view.
- **Crew Information**: The number and names of crew members currently aboard the ISS are displayed on the map for context.
- **ISS Coordinates**: The current latitude, longitude, and timestamp of the ISS are shown on the map.

### How It Works
1. **Initialization**: The `draw_earth` function initializes the map using `matplotlib` and the `Basemap` toolkit. It plots the current position of the ISS on the map based on the provided latitude and longitude, displaying the ISS as a red dot.
2. **Dynamic Updates**: The `update_iss_location` function updates the position of the ISS on the map as new coordinates are provided. It also updates the ISS coordinates in the text displayed on the map.
3. **Customizable Map**: The map uses the Mercator projection, with customizable resolution and coastline details. The map is also responsive, adjusting to show the latest position of the ISS.
