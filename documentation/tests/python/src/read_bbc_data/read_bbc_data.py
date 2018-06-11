import plotly.offline as offline

import plotly.graph_objs as go

import pandas as pd


bbc_data = pd.read_csv('../../data/bbc_data_session_id_condition.csv')

# Create a trace

trace = go.Scatter(
    x=bbc_data['time_diff'] / 60,
    y=bbc_data['participant_id'],
    mode='markers'
)

data = [trace]

layout = go.Layout(
    title='Participant ID and Time Difference Between Clicks',
    xaxis=dict(
        title='Time in minutes',
    ),
    yaxis=dict(
        title='Participant ID',
    )
)

figure = go.Figure(data=data, layout=layout)

offline.plot(figure)
