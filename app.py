import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from extract_data import *

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

dash_app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson'

df = extract_coordinates(url)

fig = go.Figure(data=go.Scattergeo(
    lon=df['longitude'],
    lat=df['latitude'],
    mode = 'markers',
    marker = dict(
        size = 10,
        opacity = 0.8,
        line = dict(
            width=1,
            color='rgba(102, 102, 102)'
        )
    ),
))

fig.update_layout(height=400, 
    margin={"r":0,"t":20,"l":0,"b":0},
    geo = dict(
        showland = True,
        landcolor = "rgb(212, 212, 212)",
    )
)
fig.update_geos(projection_type="natural earth")


dash_app.layout = html.Div(children=[
    html.H2(children='All identified earthquakes in the past day',
        style = {
            'textAlign' : 'center'
        }
    ),
    
    html.Div(children='The United States Geological Survey provided this data.', 
        style = {
            'textAlign' : 'center'
        }
    ),
    
    html.Div(children = dcc.Graph(
        id='earthquake-map',
        figure=fig,
    ))
])

if __name__ == '__main__':
    dash_app.run_server(debug=True)

app = dash_app.server