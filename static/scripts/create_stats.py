import pandas as pd
import numpy as np

import os.path
import sys

# Gets the first sys arg from app.py. Tells script where the input file is.
idvt_data = pd.read_csv(sys.argv[1])

# Replace null values (as precaution)
idvt_data = idvt_data.replace([np.inf, -np.inf], np.nan).dropna(how="all")

# Find number of unique sessions, and the number of clicks in each session
session_unique, session_count = np.unique(idvt_data['participant_id'], return_counts=True)

# for loop filters the data by unique participant, counts the number of clicks in that session
# then finds the total amount of time in each session.
# from this we are able to work out clicks per second, and seconds per click

participant_id_list = []
click_count_list = []
time_taken_secs_list = []
time_taken_mins_list = []
clicks_per_minute_list = []
minutes_per_click_list = []
clicks_per_second_list = []
seconds_per_click_list = []

for i in session_unique:
    # Sort data
    x = idvt_data.loc[idvt_data.participant_id == i, :]

    # Calculate data
    click_count = np.count_nonzero(x == i)
    time_taken = x['time_diff'].iloc[-1]

    clicks_per_second = click_count / time_taken
    seconds_per_click = time_taken / click_count

    minutes = time_taken / 60
    clicks_per_minute = click_count / minutes
    minutes_per_click = minutes / click_count

    # Append data to lists
    participant_id_list.append(i)
    click_count_list.append(click_count)
    time_taken_secs_list.append(time_taken)
    time_taken_mins_list.append(minutes)
    clicks_per_second_list.append(clicks_per_second)
    seconds_per_click_list.append(seconds_per_click)
    clicks_per_minute_list.append(clicks_per_minute)
    minutes_per_click_list.append(minutes_per_click)

# Create dataframe
idvt_data_sorted = pd.DataFrame(
    {'participant_id': participant_id_list,
     'click_count': click_count_list,
     'time_taken_secs': time_taken_secs_list,
     'time_taken_mins':time_taken_mins_list,
     'clicks_per_second': clicks_per_second_list,
     'seconds_per_click': seconds_per_click_list,
     'clicks_per_minute': clicks_per_minute_list,
     'minutes_per_click': minutes_per_click_list,
     }
)

# Sort datatframe so be more readable
idvt_data_sorted = idvt_data_sorted[['participant_id', 'click_count', 'time_taken_secs',
                                   'time_taken_mins', 'clicks_per_second', 'seconds_per_click', 'clicks_per_minute',
                                   'minutes_per_click' ]]

# Set file path for the CSV to be saved to
csv_path = sys.argv[3]

# Set name of CSV
csv_name = sys.argv[2] + '_stats.csv'

# Set file path for HTML version to be saved to
html_path = 'templates'

# STATIC - Plot saved in static to be retrieved later
idvt_data_sorted.to_csv(os.path.join(csv_path, csv_name))

# TEMPLATE - Plot saved in template folder to be displayed on web
idvt_data_sorted.to_html(os.path.join(html_path, r'idvt_data_stats.html'))
idvt_data_sorted.to_csv(os.path.join(html_path, r'idvt_data_stats.csv'))


