from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### Evaluate

The distribution of predictions closely matches the true distribution of incomes, with slight overpredictions around the median and underpredictions of the few high income outliers.

Unsurprisingly, median income of an area is highly correlated with unemployment and poverty rates. High levels of Professional and Services employment greatly boost incomes. 

The model predicts highest incomes for areas with an average commute time of 36 minutes, presumably reflecting the prosperity of suburbs compared to urban and rural communities.

"""),

html.Img(src='/assets/randomforest.png', style={'width': '80%'})]       
