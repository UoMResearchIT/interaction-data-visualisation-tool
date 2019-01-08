# PLOTS TYPES OF CLICKS

import plotly.offline as offline
import pandas as pd
import plotly.graph_objs as go
import sys

# Gets the first sys arg from app.py. Tells script where the input file is.
bbc_data = pd.read_csv(sys.argv[1])

# Place columns in variables
time_diff = bbc_data['time_diff'] / 60 # Divide by 60 for mins as its more readable than seconds.
participant_id = bbc_data['participant_id']
action_item = bbc_data['action_item']

# DATA to be plotted

data = [dict(
    type='scattergl',   # uses WebGL to load/render graph. Speeds up large datasets
    x=time_diff,        # X axis to time_diff
    y=participant_id,   # Y Axis to be participants
    mode='markers',     # marker mode in Plotly
    text=action_item,   # show action_item when viewing marker
    transforms=[dict(   # groups the data by action_item so can see different types of button click
      type='groupby',
      groups=action_item
    )]
)]

# LAYOUT to be used

layout = go.Layout(
    title=sys.argv[2] + ' - Participant ID and Time Difference Between Clicks',     # Title of PLot
    hovermode='closest',                                                            # What to display on hover
    xaxis=dict(                                                                     # Label x + Y Axis
        title='Time in minutes',
    ),
    yaxis=dict(
        title='Participant ID',
    ),
)

# Rename plot
filename = sys.argv[2] + '_action_item.html'

# Sets filepath for plot to be saved to
file_path = 'static/output//' + sys.argv[2] + '/click_plots//' + filename

# TEMPLATE - Plot saved in template folder to be displayed on web
offline.plot({'data': data, 'layout': layout}, validate=False, filename='templates//idvt_data_action_item.html',
             auto_open=False)

# STATIC - Plot saved in static to be retrieved later
offline.plot({'data': data, 'layout': layout}, validate=False, filename=file_path,
             auto_open=False)


