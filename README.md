# ISS Orbit View
A project to track and visualize the International Space Station (ISS) in real-time. It fetches the ISS's position via an API, validates the data, and displays the station’s current location and trajectory on a map. Future enhancements may include predictive algorithms for trajectory forecasting.

## Table of Contents
- [APIs Data Extraction](#apis-data-extraction)

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
