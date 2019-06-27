from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### Explain

An XGBoost Regressor model with 32 features and Ordinal Encoding most accurately predicted the Median Income of census tracts, with a Root Mean Squared Logarithmic Error of 0.167. I utilized a train dataframe of 58,174 tracts and a test dataframe of 14,544 tracts.

The interactive prediction model is a simplified version based on some of the most important features.

"""),
          
html.Img(src='/assets/model.png', style ={'width':'100%'}),
          
html.Img(src='/assets/feature_importance.png', style={'width':'100%'})]
