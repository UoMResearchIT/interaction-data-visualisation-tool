# COMPLETE

# A more comprehensive version of read_bbc_data_groupby_action_itemn,html
# Includes a brief README that gives overview of plot and what it means.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

# Load external CSS
app.css.append_css({"external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"})

# Markdown Text that gives brief explanation of plot
markdown_text = '''
### CAKE Trials Action Item Plot

Participant ID's are plotted against the time taken.

Each point represents a click. Hovering over each one gives more information e.g. (84.5, 119, finish-window), 
this is (Time of click, Participant ID, Type of Click)

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

# Set variables
time_diff = bbc_data['time_diff'] / 60
participant_id = bbc_data['participant_id']
action_item = bbc_data['action_item']

# App layout
app.layout = html.Div([

    # Graph
    dcc.Graph(
        id='action-item',
        figure={
            'data': [dict(
                    type='scatter',
                    x=time_diff,
                    y=participant_id,
                    mode='markers',
                    text=action_item,
                    transforms=[dict(
                      type='groupby',
                      groups=action_item
                    )]
                )],
            # Layout of graph
            'layout': go.Layout(
                title='Participant ID and Time Difference Between Clicks',
                hovermode='closest',
                xaxis=dict(
                    title='Time in minutes',
                ),
                yaxis=dict(
                    title='Participant ID',
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
