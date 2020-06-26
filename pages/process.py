# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Data
            The data used for this process includes the individual batting statistics for international players and the statistics for
            Team match results. I took the two datasets and merged them together so that I can use both player stats and team stats to
            fit into my model. The data was sourced from https://data.world/cclayford/cricinfo-statsguru-data.

            I used Logistic Regression, XGBoost, Decision Tree and Random Forests to see which model can give me the most accurate predictions.
            I ended up with the following scores:



            """
        ),
        html.Img(src='assets/permutation.PNG', width="20%", height="20%", 
				 className='img-fluid'),
        html.Img(src='assets/permutation.PNG', width="20%", height="20%", 
				 className='img-fluid')

    ],
)

layout = dbc.Row([column1])