# INCOMPLETE

# This is an attempt at simple version of app.py. Only the x and y axis parameters can be changed/

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

# load data
df = pd.read_csv('../../data/bbc_data_click_stats_technical.csv')

# get x and y parameters
available_indicators = list(df.columns.values)

# Load external CSS
app.css.append_css({"external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"})

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

    dcc.Input(id='participant_input', type='text', value=''),

    # Graph
    dcc.Graph(id='indicator-graphic'),

])


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

        for participant_id in participant_id_list:

            dff = df.loc[df.participant_id == participant_id, :]

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


if __name__ == '__main__':
    app.run_server()
