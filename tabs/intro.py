from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### Intro

With the 2020 Census on the horizon, I want to dive into the predictive powers of past data gathering efforts. While the Census is an enormous effort employing hundreds of thousands of people and projected to cost $15.6 billion next year, the American Community Survey collects yearly information on a smaller scale.

The 2017 ACS survey provides 36 high-level data points on the 3,142 counties and county-equivalents in the United States as well as 74,000 census tracts, with an average population of 4,400. With this information I trained regression models to predict Median Income for a given area, primarily using Random Forest and XGBoost Regressor.

To make your own predictions, there are 6 sliders in the 'Predict' tab to control for a few of the most predictive features: Unemployment Rate, Poverty Rate, Professional Employment (% in management, business, science or arts jobs), Services Employment (% in service jobs), Production Employment (% in production or transportation jobs), and Average Commute Time.

"""),
          
html.Img(src='/assets/1950censusform.jpg', style={'width': '100%'})]
