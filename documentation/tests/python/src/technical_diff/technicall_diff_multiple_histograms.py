import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.offline as offline

import pandas as pd
import numpy as np
import math

# Markdown Text that gives brief explanation of plot
markdown_text = '''
### CAKE Trials Histograms

Creates Histograms of number of clicks in each 300 second (5min interval). 

Participant sessions are split by those who had Technical Difficulties, and those hwo didn't. 

Choose which 5 min interval you'd like to see along with the bin size.

'''


app = dash.Dash()

# Load external CSS
app.css.append_css({"external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"})

# reads csv
bbc_data = pd.read_csv('../../data/bbc_data_cake.csv')

# replaces the dash '-' with a '.' makes things simpler with floats, ints etc
bbc_data['participant_session_id'] = bbc_data[['participant_id', 'session_id']]\
    .apply(lambda x: '.'.join(str(value) for value in x), axis=1)

# replace all null values
bbc_data = bbc_data.replace([np.inf, -np.inf], np.nan).dropna(how="all")

# make sure all items in 'time_diff' column are integers
pd.to_numeric(bbc_data['time_diff'])

# Find number of unique sessions, and the number of clicks in each session
session_unique, session_count = np.unique(bbc_data['participant_session_id'], return_counts=True)

# a list with all the dictionaries
dict_list = []
interval_list_all = []

# for each participant, create a dictionary with number of clicks after each interval
for f in session_unique:

    # set interval number (in seconds)
    interval = 300

    # filter df by participant
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
        interval_list_all.append(x)

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

    # create the dictionary with participant_id, interval time and number of clicks
    interval_events = dict(zip(interval_list, number_events_list))
    interval_events["participant_id"] = f

    dict_list.append(interval_events)


# create df with the list of dictionaries
df = pd.DataFrame(dict_list)

max_value = max(interval_list_all)

cols = list(df.columns.values)

# reorganise for readability
df = df[['participant_id', 0, 300, 600, 900, 1200, 1500, 1800, 2100, 2400, 2700, 3000, 3300, 3600, 3900, 4200, 4500, 4800]]

# define participants with tech difficulties
tech_diff_participants = ['109.1', '109.2', '112.1', '113.1', '121.1', '205.1', '215.1', '217.1', '220.1', '401.1',
                          '407.1', '407.2', '425.1']

# create two separate df's, one with tech diffs, one without
dff = df.loc[(df['participant_id'].isin(tech_diff_participants))]
df = df.loc[(~df['participant_id'].isin(tech_diff_participants))]


# Layout of Dash App
app.layout = html.Div([

    html.Div([

        # Markdown text
        html.Div(
            dcc.Markdown(id='graph-description',
                         children=markdown_text, ),
            style={
            }
        ),

        # Interval Number Input
        html.Div([
            dcc.Markdown(
                """ Choose an Interval """
            ),
            dcc.Dropdown(
                id='interval_dropdown',
                options=[{'label': i, 'value': i} for i in cols],
                value=300,
            ),
            ], style={'display': 'inline-block', 'font-weight': 'bold'}
        ),


        html.Div([
            dcc.Markdown(
                """ Choose a Bin Size """
            ),
            dcc.Input(
                id='bin_size',
                type='number',
                value='10',
            ),
        ], style={'margin-top': '30',  'font-weight': 'bold'})


    ], style={'margin': '30'}),

    html.Div([
        # CAKE Graph
        dcc.Graph(id='graph'),
    ], style={'margin-bottom': '50'}
    ),

])


# Graph
@app.callback(
    # Output
    dash.dependencies.Output('graph', 'figure'),
    # Input
    [dash.dependencies.Input('interval_dropdown', 'value'),
     dash.dependencies.Input('bin_size', 'value')
     ])
def update_graph(interval_dropdown, bin_size):

    max_bin_value = df[interval_dropdown].max()

    bins = dict(start=0, end=max_bin_value, size=bin_size)

    trace_all = go.Histogram(x=df[interval_dropdown],
                             opacity=0.75,
                             name='CAKE Participants',
                             autobinx=False,
                             xbins=bins,
                             )

    trace_tech_diff = go.Histogram(x=dff[interval_dropdown],
                                   opacity=0.75,
                                   name='Technical Difficulties',
                                   autobinx=False,
                                   xbins=bins
                                   )

    return {
        'data': [trace_all, trace_tech_diff],
        'layout': go.Layout(
            title='Histogram of interval ' + str(interval_dropdown - interval) + '-' + str(interval_dropdown),
            xaxis=dict(
                title='Number of clicks in this interval',
            ),
            yaxis=dict(
                title='Participant Count'
            ),
            bargap=0.2,
            bargroupgap=0.1
        )

    }


if __name__ == '__main__':
    app.run_server()