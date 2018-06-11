import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import pandas as pd
import numpy as np

# Markdown Text that gives brief explanation of plot
markdown_text = '''
### CAKE and LINEAR Stats Histograms

Creates Histograms based on the stats taken from each participant session. 
Choose the stats you want to see, and bin size. 

Participant sessions are split by those who had Technical Difficulties, and those hwo didn't. 
'''

app = dash.Dash()

# Load external CSS
app.css.append_css({"external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"})

# read CAKE and NON CAKE dataData
df = pd.read_csv('../../data/bbc_data_cake_stats_session_id.csv')
df2 = pd.read_csv('../../data/bbc_data_non_cake_stats_session_id.csv')

df = df.replace([np.inf, -np.inf], np.nan).dropna(how="all")
df2 = df2.replace([np.inf, -np.inf], np.nan).dropna(how="all")


# Get column names to use in dropdown
available_indicators = list(df.columns.values)

# Participants with technical difficulties
tech_diff_participants = [109.1, 109.2, 112.1, 113.1, 121.1, 205.1, 215.1, 217.1, 220.1, 401.1,
                          407.1, 407.2, 425.1, ]

# create df with tech diff participants
dff = df.loc[(df['participant_id'].isin(tech_diff_participants))]
dff2 = df2.loc[(df2['participant_id'].isin(tech_diff_participants))]

# df with everyone else
df = df.loc[(~df['participant_id'].isin(tech_diff_participants))]
df2 = df2.loc[(~df2['participant_id'].isin(tech_diff_participants))]


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
                """ Choose a Variable to Count """
            ),
            dcc.Dropdown(
                id='x_axis',
                options = [{'label': i, 'value': i} for i in available_indicators],
                value='click_count',
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
        ], style={'margin-top': '30', 'font-weight': 'bold'})


    ], style={'margin': '30'}),

    html.Div([
        # CAKE Graph
        dcc.Graph(id='cake'),
    ], style={'margin-bottom': '50'}
    ),


    html.Div([
        # NON CAKE Graph
        dcc.Graph(id='non_cake'),
    ], style={'margin-bottom': '50'})

])


# CAKE
@app.callback(
    # Output
    dash.dependencies.Output('cake', 'figure'),
    # Input
    [dash.dependencies.Input('x_axis', 'value'),
     dash.dependencies.Input('bin_size', 'value')
     ])
def update_graph(x_axis, bin_size):

    max_value = df[x_axis].max()

    bins = dict(start=0, end=max_value, size=bin_size)

    trace_all = go.Histogram(x=df[x_axis],
                             opacity=0.75,
                             name='CAKE Participants',
                             autobinx=False,
                             xbins=bins
                             )

    trace_tech_diff = go.Histogram(x=dff[x_axis],
                                   opacity=0.75,
                                   name='Technical Difficulties',
                                   autobinx=False,
                                   xbins=bins
                                   )
    return {
        'data': [trace_all, trace_tech_diff],
        'layout' : go.Layout(
            title='Histogram of' + ' ' + x_axis + ' in CAKE',
            xaxis=dict(
                title=x_axis
            ),
            yaxis=dict(
                title='Count'
            ),
            bargap=0.2,
            bargroupgap=0.1
        )

        }


# NON CAKE
@app.callback(
    # Output
    dash.dependencies.Output('non_cake', 'figure'),
    # Input
    [dash.dependencies.Input('x_axis', 'value'),
     dash.dependencies.Input('bin_size', 'value')])
def update_graph(x_axis, bin_size):

    max_value = df2[x_axis].max()

    bins = dict(start=0, end=max_value, size=bin_size)

    trace_all_non_cake = go.Histogram(x=df2[x_axis],
                                      opacity=0.75,
                                      name='Linear Participants',
                                      autobinx=False,
                                      xbins=bins
                                      )

    trace_tech_diff_non_cake = go.Histogram(x=dff2[x_axis],
                                            opacity=0.75,
                                            name='Technical Difficulties',
                                            autobinx=False,
                                            xbins=bins
                                            )
    return {
        'data': [trace_all_non_cake, trace_tech_diff_non_cake],
        'layout': go.Layout(
            title='Histogram of' + ' ' + x_axis + ' in Linear Conditions',
            xaxis=dict(
                title=x_axis
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
