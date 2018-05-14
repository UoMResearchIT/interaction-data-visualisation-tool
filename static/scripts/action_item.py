import plotly.offline as offline
import pandas as pd
import plotly.graph_objs as go

from flask import render_template

upload_folder = 'static/output/'

bbc_data = pd.read_csv('static/input/bbc_data_session_id_condition.csv')

time_diff = bbc_data['time_diff'] / 60
participant_id = bbc_data['participant_id']
action_item = bbc_data['action_item']

data = [dict(
    type='scatter',
    x=time_diff,
    y=participant_id,
    mode='markers',
    text=action_item,
    transforms=[dict(
      type='groupby',
      groups=action_item
    )]
)]

layout = go.Layout(
    title='Participant ID and Time Difference Between Clicks',
    hovermode='closest',
    xaxis=dict(
        title='Time in minutes',
    ),
    yaxis=dict(
        title='Participant ID',
    ),
)

path = 'static\output\plots'

offline.plot({'data': data, 'layout': layout}, validate=False, filename='templates\plots\\action_item.html',
             auto_open=False)

# action_item_plot = offline.plot({'data': data, 'layout': layout},  show_link=False, output_type="div",
#                                 include_plotlyjs=False)
