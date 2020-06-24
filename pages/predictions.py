# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
# Imports from this application
from app import app
df = pd.read_csv(r'C:\Users\alfar\cricket-match-results\Dataframes\appData1.csv')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions
            Your instructions: How to use your app to get new predictions.
            """
        ),
        html.Div([
            dcc.Dropdown(
        id='country-dropdown',
        options=[
            {'label': i, 'value': i} for i in df.iloc[:]['Country']],
        value=df.iloc[1]['Country']
            )
            ])
        
    ],
    md=4,
)



@app.callback(
    Output('bar-plot', 'figure'),
    [Input('country-dropdown','value')]
)
def predict_and_plot(country):
    nyw = df[df['Country'] == country].iloc[0]['Won']/(df[df['Country'] == country].iloc[0]['Won'] + df[df['Country'] == country].iloc[0]['Lost'])
    nywp = df[df['Country'] == country].iloc[0]['Pred_Won']/(df[df['Country'] == country].iloc[0]['Pred_Won'] + df[df['Country'] == country].iloc[0]['Pred_Lost'])
    nyl = df[df['Country'] == country].iloc[0]['Lost']
    nylp = df[df['Country'] == country].iloc[0]['Pred_Lost']
    bar_plot = {
        'data': [
                {'x': [1], 'y': [nyw], 'type': 'bar', 'name': 'Actual'},
                {'x': [1], 'y': [nywp], 'type': 'bar', 'name': u'Predicted'}]
        ,
            'layout': {'title': 'Dash Data Visualization'}
                        
    }
    return bar_plot


column2 = dbc.Col(
    [
        html.Div(dcc.Graph(id='bar-plot'))

    ]
)

layout = dbc.Row([column1, column2])