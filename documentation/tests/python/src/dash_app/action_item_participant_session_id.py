# COMPLETE

# A more comprehensive version of read_bbc_data_groupby_action_itemn,html
# Includes a brief README that gives overview of plot and what it means.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as np

app = dash.Dash()

# Load external CSS
app.css.append_css({"external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"})

# Markdown Text that gives brief explanation of plot
markdown_text = '''
### CAKE Trials Action Item Plot

Participant Session ID's are plotted against the time taken.

A Participant Session ID is formatted like so, '425.1' means the Participant ID is 425, and it's session 1.

Each point represents a click. Hovering over each one gives more information e.g. (84.5, 119.1, finish-window), 
this is (Time of click, Participant Session ID, Type of Click)

Participants were split into 4 conditions, with roughly matching Participant ID's

* CAKE Multiple - 100's
* CAKE Single - 200's
* Linear Multiple - 400's
* Linear Single - 300's

Outliers 
108, 119 - Linear Single
407, 414 - CAKE Single


'''

# Read BBC Data
bbc_data = pd.read_csv('../../data/bbc_data_session_id_condition.csv')

bbc_data = bbc_data.drop('participant_session_id', 1)

bbc_data['participant_session_id'] = bbc_data[['participant_id', 'session_id']]\
    .apply(lambda x: '.'.join(str(value) for value in x), axis=1)

time_diff = bbc_data['time_diff'] / 60
action_item = bbc_data['action_item']

# print(participant_id)

# App layout
app.layout = html.Div([

    # Graph
    dcc.Graph(
        id='action-item',
        figure={
            'data': [dict(
                    type='scatter',
                    x=time_diff,
                    y=bbc_data['participant_session_id'],
                    mode='markers',
                    text=action_item,
                    transforms=[dict(
                      type='groupby',
                      groups=action_item)
                    ]
                )],
            # Layout of graph
            'layout': go.Layout(
                title='Participant ID and Time Difference Between Clicks',
                hovermode='closest',
                xaxis=dict(
                    title='Time in minutes',
                ),
                yaxis=dict(
                    title='Participant Session ID',
                )
            ),
        }
    ),

    # Markdown text
    html.Div(
        dcc.Markdown(id='graph-description',
                     children=markdown_text,),
        style={
            'margin-left': '50px'
        }
    )

])

# Run server
if __name__ == '__main__':
    app.run_server()
