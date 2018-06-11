import plotly.offline as offline
import plotly.graph_objs as go
import pandas as pd


bbc_data = pd.read_csv('../../data/bbc_data_click_stats.csv')

bbc_data = bbc_data.sort_values(by='condition', axis=0, ascending=True)

# Time Taken (Seconds)

# Create a trace

data = [dict(
    type='bar',
    x=bbc_data['participant_session_id'],
    y=bbc_data['time_taken_secs'],
    mode='lines',
    transforms=[dict(
      type='groupby',
      groups=bbc_data['condition']
    )]
)]


layout = go.Layout(
    title='Time Taken based on condition',
    hovermode='closest',
    xaxis=dict(
        title='Participant Session ID',
    ),
    yaxis=dict(
        title='Total Time Taken in seconds',
    )
)

# Time taken in (Minutes)

data = [dict(
    type='bar',
    x=bbc_data['participant_session_id'],
    y=bbc_data['time_taken_mins'],
    mode='lines',
    transforms=[dict(
      type='groupby',
      groups=bbc_data['condition']
    )]
)]


layout = go.Layout(
    title='Time Taken based on condition',
    hovermode='closest',
    xaxis=dict(
        title='Participant Session ID',
    ),
    yaxis=dict(
        title='Total Time Taken in minutes',
    )
)

offline.plot({'data': data, 'layout': layout}, validate=False)

# Number of clicks

data = [dict(
    type='bar',
    x=bbc_data['participant_session_id'],
    y=bbc_data['click_count'],
    mode='lines',
    transforms=[dict(
      type='groupby',
      groups=bbc_data['condition']
    )]
)]


layout = go.Layout(
    title='Total number of clicks based on condition',
    hovermode='closest',
    xaxis=dict(
        title='Participant Session ID',
    ),
    yaxis=dict(
        title='Total Number of Clicks',
    )
)

offline.plot({'data': data, 'layout': layout}, validate=False)

# Clicks per second

data = [dict(
    type='bar',
    x=bbc_data['participant_session_id'],
    y=bbc_data['clicks_per_second'],
    mode='lines',
    transforms=[dict(
      type='groupby',
      groups=bbc_data['condition']
    )]
)]


layout = go.Layout(
    title='Clicks per second based on condition',
    hovermode='closest',
    xaxis=dict(
        title='Participant Session ID',
    ),
    yaxis=dict(
        title='Clicks per Second',
    )
)

offline.plot({'data': data, 'layout': layout}, validate=False)


# Clicks per minute

data = [dict(
    type='bar',
    x=bbc_data['participant_session_id'],
    y=bbc_data['clicks_per_minute'],
    mode='lines',
    transforms=[dict(
      type='groupby',
      groups=bbc_data['condition']
    )]
)]


layout = go.Layout(
    title='Clicks per minute based on condition',
    hovermode='closest',
    xaxis=dict(
        title='Participant Session ID',
    ),
    yaxis=dict(
        title='Clicks per Minute',
    )
)

offline.plot({'data': data, 'layout': layout}, validate=False)
