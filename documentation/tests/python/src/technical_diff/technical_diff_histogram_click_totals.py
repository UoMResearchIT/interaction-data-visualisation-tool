import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as offline

import pandas as pd

df = pd.read_csv('../../data/bbc_data_cake_stats_session_id.csv')

tech_diff_participants = tech_diff_participants = [109.1, 109.2, 112.1, 113.1, 121.1, 205.1, 215.1, 217.1, 220.1, 401.1,
                                                   407.1, 407.2, 425.1, ]

dff = df.loc[(df['participant_id'].isin(tech_diff_participants))]

df = df.loc[(~df['participant_id'].isin(tech_diff_participants))]

trace_all = go.Histogram(x=df['click_count'],
                         opacity=0.75,
                         name='CAKE Participants')

trace_tech_diff = go.Histogram(x=dff['click_count'],
                               opacity=0.75,
                               name='Technical Difficulties')

data = [trace_all, trace_tech_diff]
layout = go.Layout(
    title='Histogram of Total Click Count',
    xaxis=dict(
        title='Click Count'
    ),
    yaxis=dict(
        title='Count'
    ),
    bargap=0.2,
    bargroupgap=0.1
)
fig = go.Figure(data=data, layout=layout)

offline.plot(fig, filename='technical_diff_histogram_click_stats.html', image='png')

