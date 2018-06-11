import plotly.offline as offline
import pandas as pd
import plotly.graph_objs as go


bbc_data = pd.read_csv('../../data/bbc_data_session_id_condition.csv')

time_diff = bbc_data['time_diff'] / 60
participant_id = bbc_data['participant_id']

data = [dict(
    type='scatter',
    x=time_diff,
    y=participant_id,
    mode='markers',
    transforms=[dict(
      type='groupby',
      groups=participant_id,
    )]
)]

layout = go.Layout(
    title='Participant ID and Time Difference Between Clicks',
    xaxis=dict(
        title='Time in Minutes',
    ),
    yaxis=dict(
        title='Participant ID',
    )
)

offline.plot({'data': data, 'layout': layout}, validate=False)
