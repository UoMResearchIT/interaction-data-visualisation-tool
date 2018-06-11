import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import math

app = dash.Dash()

# Load external CSS
app.css.append_css({"external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"})

# reads csv
bbc_data = pd.read_csv('../../data/bbc_data_session_id_condition.csv')

# replace all null values
bbc_data = bbc_data.replace([np.inf, -np.inf], np.nan).dropna(how="all")

# make sure all items in 'time_diff' column are integers
pd.to_numeric(bbc_data['time_diff'])

# Find number of unique sessions, and the number of clicks in each session
session_unique, session_count = np.unique(bbc_data['participant_id'], return_counts=True)

intro = '''

### CAKE Trials ###

This graph shows how many number of events there are after certain intervals during the 
CAKE trials.

For example choosing an interval time of 300 secs (5 Mins) will show how many events occurred in that 5 minute 
interval

          
'''

# Layout of Dash App
app.layout = html.Div([
    html.Div([

        html.Div(
            dcc.Markdown(id='graph-description',
                         children=intro, ),
            style={
                'margin': '30px'
            }
        ),

        # Interval Number Input
        html.Div([
            dcc.Markdown(
                """ Choose Interval (in seconds) """
            ),
            dcc.Input(
                id='interval_input',
                type='number',
                value=''
            ),
        ], style={'display': 'inline-block', 'margin': '30px'}),

        # Participant Number Input
        html.Div([
            dcc.Markdown((
                """ Choose Participant ID """
            )),
            dcc.Input(
                id='participant_input',
                type='number',
                value=''
            ),

        ], style={'display': 'inline-block'})
    ]),

    # Graph
    dcc.Graph(id='indicator-graphic'),

])


@app.callback(
    # Output
    dash.dependencies.Output('indicator-graphic', 'figure'),
    # Input
    [dash.dependencies.Input('interval_input', 'value'),
     dash.dependencies.Input('participant_input', 'value')])
def update_graph(interval_input, participant_input,):

    interval = interval_input

    participant_id = participant_input

    df = bbc_data.loc[bbc_data.participant_id == participant_id, :]

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

    return {
        'data': [go.Scatter(
            x=interval_list,
            y=number_events_list,
            text=df['participant_id'],
            mode='lines',
        )],
        'layout': go.Layout(
            title='Number of events in Intervals (seconds)',
            xaxis=dict(
                title='Time in Intervals (Seconds)',
                categoryorder='array',
                categoryarray=interval_list,
                type="category"
            ),
            yaxis=dict(
                title='Number of Events',
            ),
            hovermode='closest'
        )
    }


if __name__ == '__main__':
        app.run_server()
