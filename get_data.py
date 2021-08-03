import pandas as pd
import requests

def extract_coordinates(url):
  """Extracts coordinates of earthquakes."""
  resp = requests.get(url)
  data = resp.json()
  earthquakes_number = len(data['features'])
  coordinates = [data['features'][i]['geometry']['coordinates'] for i in range(earthquakes_number)]
  longitude = [cord[0] for cord in coordinates]
  latitude = [cord[1] for cord in coordinates]
  d = {'longitude': longitude, 'latitude': latitude}
  df = pd.DataFrame(data=d)
  return df