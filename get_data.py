import requests

url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson'

def get_magnitudes(url):
  url = url
  resp = requests.get(url)
  data = resp.json()
  earthquakes_number = len(data['features'])
  magnitudes = [data['features'][i]['properties']['mag'] for i in range(earthquakes_number-1)]
  return magnitudes

def averageOfList(numOfList):
  avg = sum(numOfList) / len(numOfList)
  return avg

magnitudes = get_magnitudes(url)
print(averageOfList(magnitudes))