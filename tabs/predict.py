from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from joblib import load
import numpy as np
import pandas as pd

from app import app

style = {'padding': '1.5em'}

layout = html.Div([
    dcc.Markdown("""
        ### Predict

        Median Income of an Area with Six Factors. 
    
    """), 
    
    html.Div(id='prediction-content', style={'fontWeight':'bold'}), 

    html.Div([
        dcc.Markdown('###### Unemployment Rate'), 
        dcc.Slider(
            id='Unemployment', 
            min=0,
            max=60,
            step=5,
            value=5, 
            marks={n: str(n) for n in range(0,60,5)}
        ), 
    ], style=style), 
    
    html.Div([
        dcc.Markdown('###### Poverty Rate'), 
        dcc.Slider(
            id='Poverty', 
            min=0,
            max=25, 
            step=5, 
            value=5, 
            marks={n: str(n) for n in range(0,25,5)}
        ),
    ], style=style), 
    
    html.Div([
        dcc.Markdown('###### Professional Employment Rate'), 
        dcc.Slider(
            id='Professional', 
            min=0, 
            max=90, 
            step=10, 
            value=30, 
            marks={n: str(n) for n in range(0,90,10)}
        )
    ], style=style),    
    
    
    html.Div([
        dcc.Markdown('###### Services Employment Rate'), 
        dcc.Slider(
            id='Service', 
            min=0, 
            max=70, 
            step=10, 
            value=20, 
            marks={n: str(n) for n in range(0,70,10)}
        )
    ], style=style),
    
    html.Div([
        dcc.Markdown('###### Production Employment Rate'), 
        dcc.Slider(
            id='Production', 
            min=0, 
            max=60, 
            step=10, 
            value=10, 
            marks={n: str(n) for n in range(0,60,10)}
        )
    ], style=style),    
    


    html.Div([
        dcc.Markdown('###### Mean Commute in Minutes'), 
        dcc.Slider(
            id='MeanCommute', 
            min=4, 
            max=72, 
            step=8, 
            value=20, 
            marks={n: str(n) for n in range(4,72,8)}
        ),  
    ], style=style), 

])

@app.callback(
    Output('prediction-content', 'children'),
    [Input('Service', 'value'),
     Input('Production', 'value'),
     Input('Unemployment', 'value'),
     Input('MeanCommute', 'value'),
     Input('Poverty', 'value'),
     Input('Professional', 'value')])
def predict(Service, Production, Unemployment, MeanCommute, Poverty, Professional):

    df = pd.DataFrame(
        columns=['Service', 'Production', 'Unemployment', 'MeanCommute', 'Poverty', 'Professional'], 
        data=[[Service, Production, Unemployment, MeanCommute, Poverty, Professional]]
    )

    pipeline = load('model/pipeline.joblib')
    y_pred = pipeline.predict(df)[0]


    return f'Median Income for Census Tract: ${y_pred:,.2f}'
