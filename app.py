import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
# from extract_data import *

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

dash_app = dash.Dash(__name__)
url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson'

df = extract_coordinates(url)

fig = go.Figure(data=go.Scattergeo(
    lon=df['longitude'],
    lat=df['latitude']
))

dash_app.layout = html.Div(children=[
    html.H1(children='All identified earthquakes in the past day.'),
    html.Div(children='''
        This data was provided by the USGS.
    '''),

    dcc.Graph(
        id='example-map',
        figure=fig
    )
])

if __name__ == '__main__':
    dash_app.run_server(debug=True)

app = dash_app.server
