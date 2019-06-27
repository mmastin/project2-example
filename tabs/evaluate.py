from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### Evaluate

The distribution of predictions closely matches the true distribution of incomes, with slight overpredictions around the median and underpredictions of the few high income outliers.

"""),

html.Img(src='/assets/randomforest.png', style={'width': '100%'})]       
