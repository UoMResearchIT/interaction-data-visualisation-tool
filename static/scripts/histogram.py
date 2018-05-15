import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import pandas as pd
import numpy as np

import os.path

dash_app = dash.Dash()

# Load external CSS
dash_app.css.append_css({"external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"})

# read CAKE and NON CAKE dataData
df = pd.read_csv('static/output/stats/bbc_data_stats.csv')

# Get column names to use in dropdown
available_indicators = list(df.columns.values)

# Layout of Dash App
dash_app.layout = html.Div([

    html.Div([

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

])


# CAKE
@dash_app.callback(
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
    return {
        'data': [trace_all],
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


if __name__ == '__main__':
    dash_app.run_server(host='0.0.0.0/histogram_dash_app', debug=True)