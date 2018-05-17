import plotly.offline as offline
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import math

import sys

# reads csv
bbc_data = pd.read_csv(sys.argv[1])

# replace all null values
bbc_data = bbc_data.replace([np.inf, -np.inf], np.nan).dropna(how="all")

pd.to_numeric(bbc_data['time_diff'])

# Find number of unique sessions, and the number of clicks in each session
session_unique, session_count = np.unique(bbc_data['participant_session_id'], return_counts=True)

all_interval_list = []
all_number_of_events_list = []
participant_id_list = []


traces = []

for f in session_unique:

    interval = 300

    df = bbc_data.loc[bbc_data.participant_session_id == f, :]

    # find the time taken
    time_taken = df['time_diff'].iloc[-1]

    # find out how many intervals there needs to be
    number_of_intervals = (math.ceil(time_taken / interval)) + 1

    interval_list = []

    # work out what the intervals will be
    for number in range(number_of_intervals):
        x = number * interval
        interval_list.append(x)

    number_events_list = []

    # work out number of events
    for i in interval_list:
        lower_number = i - interval
        # for the first two values 0 and whatever the interval value is
        if i == 0:
            # filter the df
            x = df.loc[df['time_diff'] <= i]
            # add the number of events to the list
            number_events_list.append(len(x.index))
        else:
            # filter the df to range of i and the previous value in list
            z = df.loc[(df['time_diff'] > lower_number) & (df['time_diff'] <= i)]
            number_events_list.append(len(z.index))

    trace = go.Scatter(
        x=interval_list,
        y=number_events_list,
        text=df['participant_session_id'],
        mode='lines',
        name=str(f),
        marker=dict(
            opacity=0.75
                    ),
        line=dict(
            color='grey',
            width=0.5
        ),
    )

    traces.append(trace)

data = traces

layout = go.Layout(
            title='Number of events in Intervals (seconds)',
            xaxis=dict(
                title='Time in Intervals (Seconds)',
                type="category"
            ),
            yaxis=dict(
                title='Number of Events',
            ),
            hovermode='closest'
        )

fig = go.Figure(data=data, layout=layout)

offline.plot({'data': data, 'layout': layout}, validate=False, filename='templates\\bbc_data_click_density.html',
             auto_open=False)
