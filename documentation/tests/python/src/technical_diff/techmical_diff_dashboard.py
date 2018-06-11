# INCOMPLETE

# Attempt to bring all tech diff plots together

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import pandas as pd

import math
import numpy as np

app = dash.Dash()

# LOAD BBC DATA
bbc_data = pd.read_csv('../../data/bbc_data_session_id_condition.csv')

# replace all null values
bbc_data = bbc_data.replace([np.inf, -np.inf], np.nan).dropna(how="all")

pd.to_numeric(bbc_data['time_diff'])

# Find number of unique sessions, and the number of clicks in each session
session_unique, session_count = np.unique(bbc_data['participant_id'], return_counts=True)


# LOAD STATS
df = pd.read_csv('../../data/bbc_data_click_stats_technical.csv')

# get x and y parameters
available_indicators = list(df.columns.values)

unique_sessions = np.unique(df['participant_id'])

# Load external CSS
app.css.append_css({"external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"})

# App layout
app.layout = html.Div([
    html.Div([
        dcc.Input(dcc.Markdown(
                """ Choose Participants  """
            ),
            dcc.Input(
                id='participant_input',
                type='text',
                value='',
                style={'margin-left': '50px',
                         'margin-bottom': '20px',
                         'width': '20%'}
                  ),
            html.Div([
                dcc.Markdown(
                    """ Choose Interval (in seconds) """
                ),
                dcc.Input(
                    id='interval_input',
                    type='number',
                    value='300',
                    style={'display': 'inline-block',
                           'margin': '30px'}
            )
                  ]),
            # Tech diff Graphs
            dcc.Graph(id='tech-diff-events',
                      style={'margin-left': '40px',
                             'margin-bottom': '20px',
                             'width': '80%'}
                      ),
            html.Div([
                # X axis dropdown
                html.Div([
                      dcc.Dropdown(
                          id='x-column',
                          options=[{'label': i, 'value': i} for i in available_indicators],
                          value='time_taken_mins'
                      ),
                ], style={'width': '20%',
                          'display': 'inline-block',
                          'margin-left': '50px',
                          'margin-right': '50px',
                          'margin-bottom': '30px',
                          'margin-top': '50px',
                  }
                ),
                # y axis dropdown
                html.Div([
                    dcc.Dropdown(
                        id='y-column',
                        options=[{'label': i, 'value': i} for i in available_indicators],
                        value='click_count'
                    ),
                ], style={'width': '20%',
                          'display': 'inline-block',
                          'margin-bottom': '30px'})
            ]),
            # Tech Diff Stats
            dcc.Graph(id='indicator-graphic',
                      style={'margin-left': '40px',
                             'margin-bottom': '20px',
                             'width': '80%'}
                      ),
        )]
    )]
)


# Tech Diff Stats
@app.callback(
    # Output
    dash.dependencies.Output('indicator-graphic', 'figure'),
    # Input
    [dash.dependencies.Input('x-column', 'value'),
     dash.dependencies.Input('y-column', 'value'),
     dash.dependencies.Input('participant_input', 'value')])
def update_graph(x_column_name, y_column_name, participant_input):

    if participant_input:

        traces = []
        participant_id_list = []

        for i in participant_input.split(','):
            i = int(i)
            participant_id_list.append(i)

        for participant_id in unique_sessions:

            dff = df.loc[df.participant_id == participant_id, :]

            if participant_id in participant_id_list:
                colour = 'red'
            else:
                colour = 'grey'

            trace = go.Scatter(
                x=dff[x_column_name],
                y=dff[y_column_name],
                text=df['participant_id'],
                mode='markers',
                name=participant_id,
                marker={
                    'size': 15,
                    'opacity': 0.5,
                    'line': {'width': 0.5, 'color': 'white'},
                },
                line=dict(
                    color=colour,
                )
            )

            traces.append(trace)

        return {
            'data': traces,
            'layout': go.Layout(
                xaxis={
                    'title': x_column_name
                },
                yaxis={
                    'title': y_column_name
                },
                hovermode='closest'
            )
        }

    else:
        dff = df
        return {
            'data': [go.Scatter(
                x=dff[x_column_name],
                y=dff[y_column_name],
                text=dff['participant_id'],
                mode='markers',
                marker={
                    'size': 15,
                    'opacity': 0.5,
                    'line': {'width': 0.5, 'color': 'white'},
                },
                )],
            'layout': go.Layout(
                xaxis={
                    'title': x_column_name
                },
                yaxis={
                    'title': y_column_name
                },
                hovermode='closest'
            )

    }


# Tech Diff Number of Events

@app.callback(
    # Output
    dash.dependencies.Output('indicator-graphic', 'figure'),
    # Input
    [dash.dependencies.Input('interval_input'),
     dash.dependencies.Input('participant_input', 'value')])
def update_graph(interval_input, participant_input):

    participant_id_list = []

    for i in participant_input.split(','):
        i = int(i)
        participant_id_list.append(i)

    traces = []

    for f in participant_id_list:

        interval = interval_input

        dff = bbc_data.loc[bbc_data.participant_id == f, :]

        # find the time taken
        time_taken = dff['time_diff'].iloc[-1]

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

        if f in participant_id_list:
            colour = 'red'
            marker = 1.5
        else:
            colour = 'grey'
            marker = 0.5

        trace = go.Scatter(
            x=interval_list,
            y=number_events_list,
            text=df['participant_id'],
            mode='lines',
            name=str(f),
            marker=dict(
                opacity=marker
            ),
            line=dict(
                color=colour,
                width=marker
            ),
        )

        traces.append(trace)

    return {
        'data': traces,
        'layout' : go.Layout(
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
    }

if __name__ == '__main__':
    app.run_server()
