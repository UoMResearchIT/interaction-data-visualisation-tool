# COMPLETE

# Overview of CAKE with Visualisations

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

# Load external CSS
app.css.append_css({"external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"})

# Markdown Texts

general_overview = '''
### CAKE (Cook Along Kitchen Experience) Data Visualisation

The `Cook-Along Kitchen Experience' (CAKE) is an audience-facing experience designed to support learning.  
It enables people to select and cook recipes, presenting the information at a pace that matches the cooking speed of 
the viewer. CAKE was the first experience created by R&D for which the whole process, from conception to delivery,
was performed in an Object-Based way.

The main experimental study was based around four conditions:  two recipes and two presentations.  
Two recipes were used to study the effectiveness of CAKE for more complex recipes where users have to cook multiple dishes: 

1. **Single**: A dessert comprising a single dish,Chocolate and Orange Pots, "Sumptuous and not-too-naughty chocolate 
desserts served with curls of fresh orange and cacao nibs". 
2. **Multiple**: A main course comprising three dishes,Mullet with Kale & Cannellini Beans - "A delicious and hearty fissh dish, 
parcelled and steamed in the oven, accompanied by two knock-out veggie sides". 

The two presentation conditions compared CAKE with a more traditional video: 

1. **CAKE**:The object-based experience.
2. **Linear**: A web page with a linear edit of the videos and written instructions.  
Each dish was presented in its own video; the multiple recipes were presented within individual tabs on the page. 

Participants were split among the 4 conditions, with roughly matching Participant ID's

* CAKE Multiple - 100's
* CAKE Single - 200's
* Linear Multiple - 400's
* Linear Single - 300's

Outliers 
* 108, 119 - Linear Single
* 407, 414 - CAKE Single

'''

action_item_text = '''
### CAKE Action Item Plot

In this plot Participant Session ID's are plotted against the time taken.

Each point represents a click. Hovering over each one gives more information e.g. (84.5, 119.1, finish-window), 
this is (Time of click, Participant Session ID, Type of Click)

**NOTE**: A Participant Session ID is formatted like so, '425.1' means the Participant ID is 425, and it's session 1.

Along the right are all the various types of clicks. Double clicking on one will isolate that type of button click. It's
possible to isolate more than one type of button click. 

'''

click_stats_text = '''
### CAKE Click Stats Plot

This plot take stats from each Participant Session such as time taken in minutes, click count, clicks per minute etc. 

You can choose what to plot using the dropdowns. The one on the left controls the X axis, the one on the right the Y axis.

The Radio buttons below the plot allow filtering by condition.


'''

# Read Action Item Data
action_item_data = pd.read_csv('../../data/bbc_data_session_id_condition.csv')

action_item_data = action_item_data.drop('participant_session_id', 1)

action_item_data['participant_session_id'] = action_item_data[['participant_id', 'session_id']]\
    .apply(lambda x: '.'.join(str(value) for value in x), axis=1)

time_diff = action_item_data['time_diff'] / 60
action_item = action_item_data['action_item']
participant_id = action_item_data['participant_session_id']

# Read Click Stats

click_stats = pd.read_csv('../../data/bbc_data_click_stats.csv')

available_indicators = list(click_stats.columns.values)

# App layout
app.layout = html.Div([

    # Overview Text
    html.Div(
        dcc.Markdown(id='graph-description',
                     children=general_overview, ),
        style={
            'margin-left': '50px',
            'margin-top': '50px',
            'width': '50%'
        }
    ),

    # Action Item Text
    html.Div(
        dcc.Markdown(id='graph-description',
                     children=action_item_text, ),
        style={
            'margin-left': '50px',
            'margin-top': '50px'
        }
    ),
    # Action Item Graph
    dcc.Graph(
        id='action-item',
        figure={
            'data': [dict(
                type='scatter',
                x=time_diff,
                y=participant_id,
                mode='markers',
                text=action_item,
                transforms=[dict(
                    type='groupby',
                    groups=action_item
                )]
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
                )
            ),
        },
    ),

    # Click Stats Text
    html.Div(
        dcc.Markdown(id='graph-description',
                     children=click_stats_text, ),
        style={
            'margin-left': '50px',
            'margin-bottom': '50px'
        }
    ),


    # Dropdowns
    html.Div([

        # X Axis dropdown
        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='time_taken_mins'
            ),
        ], style={'width': '20%',
                  'display': 'inline-block',
                  'margin-left': '50px',
                  'margin-right': '50px',
                  'margin-bottom': '30px'
                  }),

        # Y Axis dropdown
        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='click_count'
            ),

        ], style={'width': '20%',
                  'display': 'inline-block',
                  'margin-bottom': '30px'})
    ]),

    # Click Stats Graph

    dcc.Graph(id='indicator-graphic',
              hoverData={'points': [{'customdata': '206.1'}]},
              style={'margin-left': '40px',
                     'margin-bottom': '20px',
                     'width': '60%'}
              ),

    # Choose condition. Conditions are labelled properly
    dcc.RadioItems(
        id='condition-type',
        options=[{'label': i, 'value': i} for i in ['ALL', 'CAKE Multiple', 'CAKE Single', 'Linear Multiple',
                                                    'Linear Single']],
        value='ALL',
        labelStyle={'display': 'inline-block',
                    'padding': '20px'},
    style={'margin-left': '150px',
               'display': 'inline-block',
               'margin-bottom':'200px'}
    ),

])


# Click Stats Graph
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
        dff = click_stats
    else:
        dff = click_stats[click_stats['condition'] == condition_value]

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


# Run server
if __name__ == '__main__':
    app.run_server()
