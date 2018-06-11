import plotly.offline as offline
import plotly.graph_objs as go
import pandas as pd

bbc_data = pd.read_csv('../../data/bbc_data_click_stats.csv')

bbc_data = bbc_data.sort_values(by='condition', axis=0, ascending=True)

time = bbc_data['time_taken_mins']
clicks_per_min = bbc_data['clicks_per_minute']
session_id = bbc_data['participant_session_id']
condition = bbc_data['condition']

# Clicks per min x Time

data = [dict(
    type='scatter',
    x=time,
    y=clicks_per_min,
    mode='markers',
    text=session_id,
    transforms=[dict(
      type='groupby',
      groups=condition
    )]
)]

layout = go.Layout(
    title='Clicks per minute plotted against total time',
    hovermode='closest',
    xaxis=dict(
        title='Time Taken in Minutes',
    ),
    yaxis=dict(
        title='Clicks Per Min',
    )
)

offline.plot({'data': data, 'layout': layout}, validate=False)


