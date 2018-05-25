import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as offline

import pandas as pd
import sys

df = pd.read_csv(sys.argv[1])

trace_all = go.Histogram(x=df['clicks_per_minute'],
                         opacity=0.75,
                         name='Participants')

data = [trace_all]
layout = go.Layout(
    title=sys.argv[2] + ' - Histogram of Total Clicks Per Minute',
    xaxis=dict(
        title='Clicks Per Minute'
    ),
    yaxis=dict(
        title='Participant Count'
    ),
    bargap=0.2,
    bargroupgap=0.1
)


filename = sys.argv[2] + 'histogram_clicks_per_minute.html'

file_path = 'static\output\\' + sys.argv[2] + '\stats\\' + filename

offline.plot({'data': data, 'layout': layout}, validate=False,
             filename='templates\\bbc_data_histogram_clicks_per_minute.html', auto_open=False)

offline.plot({'data': data, 'layout': layout}, validate=False, filename=file_path,
             auto_open=False)
