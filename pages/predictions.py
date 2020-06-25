# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
# Imports from this application
from app import app

url = 'https://raw.githubusercontent.com/alfaroqueIslam/cricket-match-results/master/Dataframes/batData1.csv'
url1 = 'https://raw.githubusercontent.com/alfaroqueIslam/cricket-match-results/master/Dataframes/batData2.csv'
url2 = 'https://raw.githubusercontent.com/alfaroqueIslam/cricket-match-results/master/Dataframes/batval.csv'
url3 = 'https://raw.githubusercontent.com/alfaroqueIslam/cricket-match-results/master/Dataframes/battest.csv'

df = pd.read_csv(url)
df1 = pd.read_csv(url1)
df2 = pd.read_csv(url2)
df3 = pd.read_csv(url3)
df = df.sort_values(by=['Country'])
df1 = df1.sort_values(by=['Country'])
df2 = df2.sort_values(by=['Country'])
df3 = df3.sort_values(by=['Country'])

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions
            Predicting the win rate
            """
        ),
        html.Div([
            dcc.Markdown("###### Select Year"),
            dcc.Dropdown(
        id='year-dropdown',
        options=[
            {'label': '2018', 'value': 2018},
            {'label': '2019', 'value': 2019}
            ],
        value=2018
            )
            ]),
        html.Div([
            dcc.Markdown("###### Select Country"),
            dcc.Dropdown(
        id='country-dropdown',
        options=[
            {'label': i, 'value': i} for i in df.iloc[:]['Country']],
        value=df.iloc[0]['Country']
            )
            ]),
        html.Div([
            dcc.Markdown("###### Home or Away"),
            dcc.Dropdown(
        id='home_away-dropdown',
        options=[
            {'label': 'All', 'value': 'All'},
            {'label': 'Home', 'value': 'Home'},
            {'label': 'Away', 'value': 'Away'}],
        value='All'
            )
            ]),
        html.Div([
            dcc.Markdown("###### Batting First or Second"),
            dcc.Dropdown(
        id='batting_order-dropdown',
        options=[
            {'label': 'All', 'value': 'All'},
            {'label': 'First', 'value': 1},
            {'label': 'Second', 'value': 2}],
        value='All'
            )
            ])
        
    ],
    md=4,
)

def makeDF(df,arr):
    arrw = []
    arrl = []
    arrwp = []
    arrlp = []
    
    for s in arr:
        tempdf = df[df['Country'] == s]
        dateList = tempdf['Match_Date'].unique()
        
        nw = 0
        nwp = 0
        nl = 0
        nlp = 0
        n = 0
        for i in dateList:
            
            dateListdf = tempdf[tempdf['Match_Date'] == i]
            dateListdf1 = dateListdf[['Result','Match_Date']]
            dateListdf = dateListdf[['Pred_Result','Match_Date']]
            dateListdf = dateListdf.drop_duplicates()
            dateListdf1 = dateListdf1.drop_duplicates()
            nw = nw + len(dateListdf1[dateListdf1['Result'] == 'Won'])
            nl = nl + len(dateListdf1[dateListdf1['Result'] == 'Lost'])
            if dateListdf['Pred_Result'].iloc[0] == 'Won':
                nwp = nwp + 1
            else:
                nlp = nlp + 1
            #nwp = nwp + len(dateListdf[dateListdf['Pred_Result'] == 'Won'])
            #nlp = nlp + len(dateListdf[dateListdf['Pred_Result'] == 'Lost'])
            n = n + 1
            
        arrw.append(nw)
        arrl.append(nl)
        arrwp.append(nwp)
        arrlp.append(nlp)
        
    tempdf1 = {"Country" : arr, "Won" : arrw, "Pred_Won" : arrwp, "Lost" : arrl, "Pred_Lost" : arrlp}
    tempdf1 = pd.DataFrame(tempdf1)
    return tempdf1

@app.callback(
    Output('bar-plot', 'figure'),
    [Input('year-dropdown','value'),
    Input('country-dropdown','value'),
    Input('home_away-dropdown','value'),
    Input('batting_order-dropdown','value')]
)
def predict_and_plot(year,country,home_away,batting_order):
    
    if year == 2018:
        arlist = df2['Country'].unique()
        
        dft = df2
        if batting_order == 1:
            
            dft = dft[dft['Home/Away'] == 'Home']
            dft = dft[dft['Country'] == country]
            
            
           
        elif batting_order == 2:
            
            dft = dft[dft['Home/Away'] == 'Away']
            dft = dft[dft['Country'] == country]
            
            
        if batting_order == 1:
            
            dft = dft[dft['Innings_Number'] == 1]
            dft = dft[dft['Country'] == country]
            
            
            
        elif batting_order == 2:
            
            dft = dft[dft['Innings_Number'] == 2]
            dft = dft[dft['Country'] == country]

        
        dft = dft[dft['Country'] == country]
        dft = makeDF(dft,arlist)
        try:
            nyw = dft[dft['Country'] == country].iloc[0]['Won']/(dft[dft['Country'] == country].iloc[0]['Won'] + dft[dft['Country'] == country].iloc[0]['Lost'])
        except ZeroDivisionError:
            nyw = 0
        try:
            nywp = dft[dft['Country'] == country].iloc[0]['Pred_Won']/(dft[dft['Country'] == country].iloc[0]['Pred_Won'] + dft[dft['Country'] == country].iloc[0]['Pred_Lost'])
        except ZeroDivisionError:
            nywp = 0
    else:
        arlist = df3['Country'].unique()
        dft = df3
        if batting_order == 1:
            
            dft = dft[dft['Innings_Number'] == 1]
            dft = dft[dft['Country'] == country]
           
            
        elif batting_order == 2:
            
            dft = dft[dft['Innings_Number'] == 2]
            dft = dft[dft['Country'] == country]
            
            
        dft = dft[dft['Country'] == country]
        dft = makeDF(dft,arlist)
        try:
            nyw = dft[dft['Country'] == country].iloc[0]['Won']/(dft[dft['Country'] == country].iloc[0]['Won'] + dft[dft['Country'] == country].iloc[0]['Lost'])
        except ZeroDivisionError:
            nyw = 0
        try:
            nywp = dft[dft['Country'] == country].iloc[0]['Pred_Won']/(dft[dft['Country'] == country].iloc[0]['Pred_Won'] + dft[dft['Country'] == country].iloc[0]['Pred_Lost'])
        except ZeroDivisionError:
            nywp = 0
        nyl = dft[dft['Country'] == country].iloc[0]['Lost']
        nylp = dft[dft['Country'] == country].iloc[0]['Pred_Lost']
    bar_plot = {
        'data': [
                {'x': [1], 'y': [nyw], 'type': 'bar', 'name': 'Actual'},
                {'x': [1], 'y': [nywp], 'type': 'bar', 'name': u'Predicted'}]
        ,
        'layout': {'title': 'Team Win Rate'}
                        
    }
    return bar_plot


column2 = dbc.Col(
    [
        html.Div(dcc.Graph(id='bar-plot'))

    ]
)

layout = dbc.Row([column1, column2])