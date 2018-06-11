# INCOMPLETE

# This is an attempt at simple version of app.py. Only the x and y axis parameters can be changed/

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

# load data
df = pd.read_csv('../../data/bbc_data_click_stats.csv')

# get x and y parameters
available_indicators = list(df.columns.values)

# App layout
app.layout = html.Div([
    html.Div([

        # X axis dropdown
        html.Div([
            dcc.Dropdown(
                id='x-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='time_taken_mins'
            ),
        ], style={'width': '48%', 'display': 'inline-block'}),

        # y axis dropdown
        html.Div([
            dcc.Dropdown(
                id='y-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='click_count'
            ),

        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    # Graph
    dcc.Graph(id='indicator-graphic'),

])


@app.callback(
    # Output
    dash.dependencies.Output('indicator-graphic', 'figure'),
    # Input
    [dash.dependencies.Input('x-column', 'value'),
     dash.dependencies.Input('y-column', 'value')])
def update_graph(x_column_name, y_column_name):

    # Return a graph based on input and output. This is based on example in Multiple Inputs
    # in Dash (docs https://dash.plot.ly/getting-started-part-2)
    return {
        'data': [go.Scatter(
            x=df[x_column_name],
            y=df[y_column_name],
            text=df['participant_session_id'],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'},
            },
        )],
        # Change the label on graph (Doesn't work)
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


if __name__ == '__main__':
    app.run_server()