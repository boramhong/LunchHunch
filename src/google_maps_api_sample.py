import googlemaps
from config import GOOGLE_MAP_API_KEY


# Python Client for Google Maps Services (https://github.com/googlemaps/google-maps-services-python) is employed.
# Documentation: https://googlemaps.github.io/google-maps-services-python/docs/

gmaps = googlemaps.Client(key=GOOGLE_MAP_API_KEY)

# Geocoding an address


# Places Search Example
gmaps.places("Myeong-dong restaurants")

# Nearby Search Example
gmaps.places_nearby(location=(37.56, 126.98), radius=600)
