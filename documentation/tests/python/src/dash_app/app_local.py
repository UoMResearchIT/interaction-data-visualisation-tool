# INCOMPLETE

# The final app. Would allow users to change the value of x and y axis,
# as well as condition they want to view

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

# load stats from BBC Data
df = pd.read_csv('../../data/bbc_data_click_stats.csv')

# the values that I want on x and y axis, his is click count, time taken etc,
# all columns names in example in Dash docs the indicators are VALUES taken form acolumn
available_indicators = list(df.columns.values)

# App layout
app.layout = html.Div([
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

    # Graph
    dcc.Graph(id='indicator-graphic'),

    # Choose condition. Conditions are labelled properly
    dcc.RadioItems(
        id='condition-type',
        options=[{'label': i, 'value': i} for i in ['ALL', 'CAKE Multiple', 'CAKE Single', 'Linear Multiple',
                                                    'Linear Single']],
        value='ALL',
        labelStyle={'display': 'inline-block'}
    )
])


@app.callback(
    # Output
    dash.dependencies.Output('indicator-graphic', 'figure'),
    # Input
    [dash.dependencies.Input('xaxis-column', 'value'),
     dash.dependencies.Input('yaxis-column', 'value'),
     dash.dependencies.Input('condition-type', 'value')])
def update_graph(xaxis_column_name, yaxis_column_name,
                 condition_value):
    # this is where it startes toi go wrong. I don't quite understand what is going on
    # Based it on Multiple Inputs example in Dash docs (https://dash.plot.ly/getting-started-part-2)

    if condition_value == 'ALL':
        dff = df
    else:
        dff = df[df['condition'] == condition_value]

    return {
        # changes the x and y axis based on input
        'data': [go.Scatter(
            # LML: The column name has to be provided to the data frame, which is in xaxis_column_name
            #      but the code below is looking for a column with the literal name 'xaxis_column_name' so fails.
            #      The required name is correctly passed I think, so this now works.
            x=dff[xaxis_column_name],
            y=dff[yaxis_column_name],

            # don't quite understand what the text part is doing here

            # LML: This is adding some text to each data point, selected by a column name from the data frame
            #      In this insance the column is literally called 'participant_session_id'
            text=dff['participant_session_id'],

            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': go.Layout(
            # x and y labels currently don't appear automatically like they should
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


if __name__ == '__main__':
    app.run_server()
