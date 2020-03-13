# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:03:22 2020

@author: Bucky
"""


import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)
import plotly.io as pio
pio.renderers.default = "browser"

#import chart_studio
#chart_studio.tools.set_credentials_file(username='******', api_key='*********')

import pandas as pd
import numpy as np


# Read in data and convert index to a datetime
df = pd.read_csv('coronavirus.csv', 
                 header=0, index_col=0)

country_list = list(df.columns)

#Create cumulative scatters
country_data=[]
for country in country_list:
    country_series = df.loc[:, country]
    country_data.append(go.Scatter(x=country_series.index,
                        y=country_series,
                        line=go.scatter.Line(width = 1.5),
                           opacity=0.8,
                           name=country,
                           text=[f'Cumulative: {x:.0f}' for x in country_series.values]))

#create doubling time data
df2=df.copy()
for i in df.index[:-1]:
    for j, country in enumerate(df.columns):
        try:
            df2.at[i,country] = 1. / (np.log2(df.loc[i+1][j] / df.loc[i][j]))
        except:
            df2.at[i,country] = 0
            
#Create doubling scatters
doubling_data=[]
for country in country_list:
    doubling_series = df2.loc[:, country]
    doubling_data.append(go.Scatter(x=doubling_series.index,
                        y=doubling_series,
                        line=go.scatter.Line(width = 1.5),
                           opacity=0.8,
                           name=country,
                           text=[f'Doubling time: {x:.0f} days' for x in doubling_series.values]))

#Create update menus for 2 graphs
button_layer_1_height = 1.11
updatemenus1 = list([
    dict(
        type = "buttons",
        direction = "left",            
        pad={"r": 10, "t": 10},
        showactive=True,
        x=0.1,
        xanchor="left",
        y=button_layer_1_height,
        yanchor="top",
        active=0,
        buttons=list([
            dict(
                label='Log',
                method='update',
                args=[{}, {
                    'yaxis': {'type': 'log'}
                }]),
            dict(
                label='Linear',
                method='update',
                args=[{}, {
                    'yaxis': {'type': 'linear'}
                }])
        ]),
    ),
    dict(
        type = "buttons",
        direction = "left",            
        pad={"r": 10, "t": 10},
        showactive=True,
        x=0.5,
        xanchor="left",
        y=button_layer_1_height,
        yanchor="top",
        active=0,
        buttons=list([
            dict(
                label='1k',
                method='update',
                args=[{}, {
                    'yaxis': {'range': [0,1000]}
                }]),
            dict(
                label='10k',
                method='update',
                args=[{}, {
                    'yaxis': {'range': [0,10000]}
                }]),
            dict(
                label='100k',
                method='update',
                args=[{}, {
                    'yaxis': {'range': [0,100000]}
                }])
        ]),
    ),
])

updatemenus2 = list([
    dict(
        type = "buttons",
        direction = "left",            
        pad={"r": 10, "t": 10},
        showactive=True,
        x=0.1,
        xanchor="left",
        y=button_layer_1_height,
        yanchor="top",
        active=0,
        buttons=list([
            dict(
                label='Log',
                method='update',
                args=[{}, {
                    'yaxis': {'type': 'log'}
                }]),
            dict(
                label='Linear',
                method='update',
                args=[{}, {
                    'yaxis': {'type': 'linear'}
                }])
        ]),
    ),
    dict(
        type = "buttons",
        direction = "left",            
        pad={"r": 10, "t": 10},
        showactive=True,
        x=0.5,
        xanchor="left",
        y=button_layer_1_height,
        yanchor="top",
        active=0,
        buttons=list([
            dict(
                label='6',
                method='update',
                args=[{}, {
                    'yaxis': {'range': [0,6]}
                }]),
            dict(
                label='10',
                method='update',
                args=[{}, {
                    'yaxis': {'range': [0,10]}
                }]),
            dict(
                label='20',
                method='update',
                args=[{}, {
                    'yaxis': {'range': [0,20]}
                }])
        ]),
    ),
])
                    
# Create a layout with rangesliders on the axes and scale selector
layout1 = go.Layout(height=700, width=1000, font=dict(size=14),
                   updatemenus = updatemenus1,
                   title='Coronavirus outbreaks',
                   xaxis=dict(title='Days since passing 40 cases',
                                         rangeslider=dict(visible=True),
                                         type='linear'),
                   # yaxis
                   yaxis=dict(title = 'Cumulative Cases', type = 'log')
                   )

# Create a layout with rangesliders on the axes and scale selector
layout2 = go.Layout(height=700, width=1000, font=dict(size=14),
                   updatemenus = updatemenus2,
                   title='Coronavirus outbreaks',
                   xaxis=dict(title='Days since passing 40 cases',
                                         rangeslider=dict(visible=True),
                                         type='linear'),
                   # yaxis
                   yaxis=dict(title = 'Doubling time (days)', type = 'log')
                   )

# Create the figure and display
fig = go.Figure(data=country_data[:-3], layout=layout1)
iplot(fig)

# Create the figure and display
fig = go.Figure(data=doubling_data[:-3], layout=layout2)
iplot(fig)

# fig = make_subplots(rows = 2, cols = 1)

# fig.add_trace(country_data[0], row=1, col=1)
# fig.add_trace(doubling_data[0], row=2, col=1)

# fig.update_layout(height=1300, width=1000, font=dict(size=16),
#                    updatemenus = updatemenus,
#                    title='Coronavirus outbreaks',
#                    xaxis=dict(title='Days since passing 40 cases',
#                                          rangeslider=dict(visible=True),
#                                          type='linear'),
#                    # yaxis
#                    yaxis=dict(title = 'Cumulative Cases', type = 'log')
#                    )

# iplot(fig)


