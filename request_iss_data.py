import requests
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeopyError


def iss_tracker() -> dict:
    """ fetches data from the ISS website and return a dictionary with current location data """
    url = "http://api.open-notify.org/iss-now.json"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        position = data["iss_position"]
        latitude = float(position['latitude'])
        longitude = float(position['longitude'])
    except (requests.exceptions.RequestException, KeyError):
        return {
            "error": f"Failed to fetch ISS data - don't panic! - please try again later"
        }

    geolocator = Nominatim(user_agent="alien-abduction-guide")
    try:
        location = geolocator.reverse((latitude, longitude), exactly_one=True, timeout=5)
        location_name = location.address if location else "an unspecified area"
    except (GeocoderTimedOut, GeopyError) as e:
        location_name = f"an unknown region (Geocoding Error: {e}) - don't panic!"

    return {
        "location_name": location_name,
        "latitude": latitude,
        "longitude": longitude
    }


def main():
    print("Convince your alien abductors to drop you off at the nearest space station: \n")
    iss_data = iss_tracker()
    if "error" in iss_data:
        print(iss_data["error"])
    else:
        print(
            f"The ISS is currently over {iss_data['location_name']} at Latitude: {iss_data['latitude']}, "
            f"Longitude: {iss_data['longitude']}"
        )

if __name__ == "__main__":
    main()


