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
            The data used for this process includes the individual batting statistics for international players per match 
            and the statistics for team match results. I took the two datasets and merged them together so that 
            I can use both player stats and team stats to fit into my model. The data was sourced from 
            https://data.world/cclayford/cricinfo-statsguru-data.

            ## Process

            I split the data into a training set, a validation set and a test set. For the training set I used the year 2014-2017,
            for the validation set I used the year 2018 and for the test set I used 2019. My target in this data is the 'Result' column
            which contains the value 'Won' or 'Lost'. I used my training set to find a baseline.
            Lost    0.548154
            Won     0.451846
            
            The Majority class is the value 'Lost' and gives me a baseline accuracy of 0.548154.

            I used Logistic Regression, XGBoost, Decision Tree and Random Forests with Ordinal encoding and 
            OneHotEncoding to see which model can give me the most accurate predictions. OneHotEncoding gave me
            significantly higher scores so that is what I used to continue.
            I ended up with the following scores:



            """
        ),
        html.Img(src='assets/accScores.PNG', width="35%", height="35%", 
				 className='img-fluid'),
        dcc.Markdown(
            """
        
            Decision tree and Random forests had the best scores and were significantly above the baseline but they 
            were very close to eachother. I decided get the Permutation Importances to see if Isolating to more important features 
            might help me obtain a better score.


            """
        ),
        html.Img(src='assets/permutation.PNG', width="20%", height="20%", 
				 className='img-fluid'),
        dcc.Markdown(
            """
        
            I tried my model a few more times using the the best features from the permutation importances but
            always ended up with a much lower score.
            Since Decision tree and Random Forests had scores that were so close to each other I decided to investigate 
            further to see which one had the more accurate model. I used the test data for each to plot a confusion matrix.
            the Decision tree is on the left and the Random forests is on the right.


            """
        ),
        html.Img(src='https://raw.githubusercontent.com/alfaroqueIslam/cricket-match-results/master/assets/treeMatrix.PNG', width="25%", height="25%", 
				 className='img-fluid'),
        html.Img(src='https://raw.githubusercontent.com/alfaroqueIslam/cricket-match-results/master/assets/forestMatrix.PNG', width="25%", height="25%", 
				 className='img-fluid'),
        dcc.Markdown(
            """
        
            The two models still had very similar figures so I decided to get the ROC AUC score and plot the ROC curve to make
            a more definitive comparison.


            """
        ),
        html.Img(src='https://raw.githubusercontent.com/alfaroqueIslam/cricket-match-results/master/assets/rocScores.PNG', width="35%", height="35%", 
				 className='img-fluid'),
        html.Img(src='https://raw.githubusercontent.com/alfaroqueIslam/cricket-match-results/master/assets/rocCurve.PNG', width="40%", height="40%", 
				 className='img-fluid'),

    ],
)

layout = dbc.Row([column1])