import pandas as pd
import numpy as np

# Read BBC Data
bbc_data = pd.read_csv('../../data/bbc_data_session_id_condition.csv')

bbc_data = bbc_data.replace([np.inf, -np.inf], np.nan).dropna(how="all")

bbc_data = bbc_data.drop('participant_session_id', 1)

bbc_data['participant_session_id'] = bbc_data[['participant_id', 'session_id']]\
    .apply(lambda x: '.'.join(str(value) for value in x), axis=1)

# Find number of unique sessions, and the number of clicks in each session
session_unique, session_count = np.unique(bbc_data['participant_session_id'], return_counts=True)

# for loop filters the data by unique session, counts the number of clicks in that session
# then finds the total amount of time in each session.
# from this we are able to work out clicks per second, and seconds per click

participant_id_list = []
condition_list = []
click_count_list = []
time_taken_secs_list = []
time_taken_mins_list = []
clicks_per_minute_list = []
minutes_per_click_list = []
clicks_per_second_list = []
seconds_per_click_list = []

for i in session_unique:
    # Sort data
    x = bbc_data.loc[bbc_data.participant_session_id == i, :]

    condition = x['condition'].iloc[-1]

    # Condition
    if condition == 1:
        condition = "CAKE Multiple"
    elif condition == 2:
        condition = "CAKE Single"
    elif condition == 3:
        condition = "Linear Multiple"
    else:
        condition = "Linear Single"

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
    condition_list.append(condition)

bbc_data_sorted = pd.DataFrame(
    {'participant_session_id': participant_id_list,
     'click_count': click_count_list,
     'time_taken_secs': time_taken_secs_list,
     'time_taken_mins':time_taken_mins_list,
     'clicks_per_second': clicks_per_second_list,
     'seconds_per_click': seconds_per_click_list,
     'clicks_per_minute': clicks_per_minute_list,
     'minutes_per_click': minutes_per_click_list,
     'condition': condition_list,
     }
)

bbc_data_sorted = bbc_data_sorted[['participant_session_id', 'condition', 'click_count', 'time_taken_secs',
                                   'time_taken_mins', 'clicks_per_second', 'seconds_per_click', 'clicks_per_minute', 'minutes_per_click', ]]

bbc_data_sorted.to_csv('bbc_data_click_stats', encoding='utf-8', index=False)