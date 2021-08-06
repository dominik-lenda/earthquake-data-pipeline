import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from extract_data import *

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