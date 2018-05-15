import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as offline

import pandas as pd

df = pd.read_csv('static/output/stats/bbc_data_stats.csv')

trace_all = go.Histogram(x=df['click_count'],
                         opacity=0.75,
                         name='Participants')

data = [trace_all]
layout = go.Layout(
    title='Histogram of Total Click Count',
    xaxis=dict(
        title='Click Count'
    ),
    yaxis=dict(
        title='Participant Count'
    ),
    bargap=0.2,
    bargroupgap=0.1
)

offline.plot({'data': data, 'layout': layout}, validate=False, filename='templates\\bbc_data_histogram_click_count.html'
             , auto_open=False)
