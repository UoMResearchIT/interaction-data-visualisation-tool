# INCOMPLETE

# An attempt to have a hover over feature that would create new graphs and reveal stats of the user.

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

# Read Action Item Data
action_item_data = pd.read_csv('../../data/bbc_data_session_id_condition.csv')

action_item_data = action_item_data.drop('participant_session_id', 1)

action_item_data['participant_session_id'] = action_item_data[['participant_id', 'session_id']]\
    .apply(lambda x: '.'.join(str(value) for value in x), axis=1)

time_diff = action_item_data['time_diff'] / 60
action_item = action_item_data['action_item']

# Read Click Stats

click_stats = pd.read_csv('../../data/bbc_data_click_stats.csv')

available_indicators = list(click_stats.columns.values)

# App layout
app.layout = html.Div([

    # Dropdowns
    html.Div([

        # X Axis dropdown
        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='time_taken_mins'
            ),
        ], style={'width': '48%', 'display': 'inline-block'}),

        # Y Axis dropdown
        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='click_count'
            ),

        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    # Click Stats Graph

    dcc.Graph(id='indicator-graphic',
              hoverData={'points': [{'customdata': '206.1'}]}
              ),

    # Individual Participant ID Graph
    dcc.Graph(
        id='action-item',
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


# Click Stats Graph
@app.callback(
    # Output
    dash.dependencies.Output('indicator-graphic', 'figure'),
    # Input
    [dash.dependencies.Input('xaxis-column', 'value'),
     dash.dependencies.Input('yaxis-column', 'value')])
def update_graph(xaxis_column_name, yaxis_column_name,):

    return {
        # changes the x and y axis based on input
        'data': [go.Scatter(
            # LML: The column name has to be provided to the data frame, which is in xaxis_column_name
            #      but the code below is looking for a column with the literal name 'xaxis_column_name' so fails.
            #      The required name is correctly passed I think, so this now works.
            x=click_stats[xaxis_column_name],
            y=click_stats[yaxis_column_name],

            text=click_stats['participant_session_id'],

            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': go.Layout(
            xaxis={
                'title': xaxis_column_name
            },
            yaxis={
                'title': yaxis_column_name
            },
            # is the margin needed?
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }


@app.callback(
    dash.dependencies.Output('action-item', 'figure'),
    [dash.dependencies.Input('indicator-graphic', 'hoverData'),
     ])
def update_action_item(hoverData):
    psd = hoverData['points'][0]['customdata']

    return {
        'data': [go.Scatter(
            x=time_diff,
            y=action_item_data[psd],
            mode='markers',
            text=action_item,
            customdata=hoverData['points'][0]['customdata'],
            transforms=[dict(
                type='groupby',
                groups=action_item)
            ]
        )],
        # Layout of graph
        'layout': go.Layout(
            title='Participant Session ID and Time Difference Between Clicks',
            hovermode='closest',
            xaxis=dict(
                title='Time in minutes',
            ),
            yaxis=dict(
                title='Participant Session ID',
            )
        ),
    }


# Run server
if __name__ == '__main__':
    app.run_server()
