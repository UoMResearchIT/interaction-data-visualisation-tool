# COMPLETE

# A more comprehensive version of read_bbc_data_groupby_action_itemn,html
# Includes a brief README that gives overview of plot and what it means.

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
### CAKE Trial Technical Difficulties Action Item Plot

Action item data for participants with technical differences.

'''

# Read BBC Data
bbc_data = pd.read_csv('../../data/bbc_data_session_id_condition.csv')

time_diff = bbc_data['time_diff'] / 60
action_item = bbc_data['action_item']

tech_diff_participants = [109, 112, 113, 121, 205, 215, 217, 220, 401, 407, 425]

df = bbc_data[bbc_data['participant_id'].isin([109, 112, 113, 121, 205, 215, 217, 220, 401, 407, 425])]

# App layout
app.layout = html.Div([

    # Markdown text
    html.Div(
        dcc.Markdown(id='graph-description',
                     children=markdown_text,),
        style={
            'margin': '50px'
        }
    ),

    # Graph
    dcc.Graph(
        id='action-item',
        figure={
            'data': [dict(
                    type='scatter',
                    x=time_diff,
                    y=df['participant_id'],
                    mode='markers',
                    text=action_item,
                    transforms=[dict(
                      type='groupby',
                      groups=action_item)
                    ]
                )],
            # Layout of graph
            'layout': go.Layout(
                title='Participant ID and Time Difference Between Clicks',
                hovermode='closest',
                xaxis=dict(
                    title='Time in minutes',
                ),
                yaxis=dict(
                    title='Participant Session ID',
                    categoryorder='array',
                    categoryarray=tech_diff_participants,
                    type="category"
                )
            ),
        }
    ),

])

# Run server
if __name__ == '__main__':
    app.run_server()
