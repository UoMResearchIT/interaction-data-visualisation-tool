# PLOTS CLICK DENSITY

import plotly.offline as offline
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import math
import sys

# Gets the first sys arg from app.py. Tells script where the input file is.
idvt_data = pd.read_csv(sys.argv[1])

# Find number of unique sessions, and the number of clicks in each session
session_unique, session_count = np.unique(idvt_data['participant_id'], return_counts=True)

# Lists for the necessary to data to be put into
all_interval_list = []
all_number_of_events_list = []
participant_id_list = []

# List with all the traces
traces = []

for f in session_unique:

    # 300 secs == 5 minutes. Can be changed
    interval = 300

    # Create data frame with just that participant
    df = idvt_data.loc[idvt_data.participant_id == f, :]

    # Find total  time taken
    time_taken = df['time_diff'].iloc[-1]

    # Find out how many intervals there needs to be
    number_of_intervals = (math.ceil(time_taken / interval)) + 1

    # List of all intervals
    interval_list = []

    # Work out when the intervals will be
    for number in range(number_of_intervals):
        x = number * interval
        interval_list.append(x)

    # List of number of events
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

    # Create a Trace based on data worked out above
    trace = go.Scattergl(
        x=interval_list,            # all the intervals
        y=number_events_list,       # number of events at eahc interval
        text=df['participant_id'],  # text to be displayed
        mode='lines',               # use lines
        name=str(f),                # name each line with participant_id
        marker=dict(                # change opacity of marker
            opacity=0.75
                    ),
        line=dict(                  # change opacity of line
            color='grey',
            width=0.5
        ),
    )

    # add the trace to the trace list
    traces.append(trace)

# DATA to be plotted
data = traces

# LAYOUT to be used
layout = go.Layout(
            title=sys.argv[2] + ' - Number of events in Intervals (seconds)',
            xaxis=dict(
                title='Time in Intervals (Seconds)',
                type="category"
            ),
            yaxis=dict(
                title='Number of Events',
            ),
            hovermode='closest'
        )

# create figure
fig = go.Figure(data=data, layout=layout)

# rename plot
filename = sys.argv[2] + '_click_density.html'

# filepath for plot
file_path = 'static/output//' + sys.argv[2] + '/click_plots//' + filename

# TEMPLATE - Plot saved in template folder to be displayed on web
offline.plot({'data': data, 'layout': layout}, validate=False, filename='templates//idvt_data_click_density.html',
             auto_open=False)

# STATIC - PLot saved in static to be retrieved later
offline.plot({'data': data, 'layout': layout}, validate=False, filename=file_path,
             auto_open=False)