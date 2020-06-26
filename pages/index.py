# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## T20I Cricket Winrates
            This application predicts the win rates of International Cricket teams in T20 Cricket and matches in with the Actual.
            """
        ),
        dcc.Link(dbc.Button('Predictions', color='primary'), href='/predictions')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        html.Img(src='https://miro.medium.com/max/1000/1*pBBwH936X-elTgE-7b2sfw.jpeg', 
				 className='img-fluid'),
    ]
)

layout = dbc.Row([column1, column2])