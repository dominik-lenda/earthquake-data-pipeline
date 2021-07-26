# https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php

import requests

resp = requests.get('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_hour.geojson')
print(resp.json())
