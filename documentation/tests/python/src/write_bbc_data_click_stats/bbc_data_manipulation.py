import pandas as pd
import numpy as np

# Read BBC Data
bbc_data = pd.read_csv('../../data/bbc_data_session_id_condition.csv')

# Find number of unique sessions, and the number of clicks in each session
session_unique, session_count = np.unique(bbc_data['participant_session_id'], return_counts=True)

# for loop filters the data by unique session, counts the number of clicks in that session
# then finds the total amount of time in each session.
# from this we are able to work out clicks per second, and seconds per click

for i in session_unique:
    x = bbc_data.loc[bbc_data.participant_session_id == i, :]
    click_count = np.count_nonzero(x == i)
    time_taken = x['time_diff'].iloc[-1]

    clicks_per_second = click_count / time_taken
    seconds_per_click = time_taken / click_count

    print(i, ': clicks per second = ', clicks_per_second)
    print(i, 'took', seconds_per_click, 'seconds per click')
