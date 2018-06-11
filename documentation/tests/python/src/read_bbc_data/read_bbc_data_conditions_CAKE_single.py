import plotly.offline as offline
import pandas as pd
import plotly.graph_objs as go


bbc_data = pd.read_csv('../../data/bbc_data_session_id_condition.csv')

condition = bbc_data.loc[bbc_data['condition'] == 2]

time_diff = condition['time_diff'] / 60
participant_id = condition['participant_id']

data = [dict(
    type='scatter',
    x=time_diff,
    y=participant_id,
    mode='markers',
    transforms=[dict(
      type='groupby',
      groups=condition['action_item'],
  )]
)]

layout = go.Layout(
    title='CAKE Single - Clicks by participant',
    xaxis=dict(
        title='Time in minutes',
    ),
    yaxis=dict(
        title='Participant ID',
    )
)

offline.plot({'data': data, 'layout': layout}, validate=False)
