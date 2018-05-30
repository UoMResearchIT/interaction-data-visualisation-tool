import pandas as pd
import numpy as np
import datetime as dt
import sys, os

bbc_data = pd.read_csv(sys.argv[1])

bbc_data = bbc_data.replace([np.inf, -np.inf], np.nan).dropna(how="all")

if not {'time_diff', 'participant_id', 'action_item'}.issubset(bbc_data.columns):

    bbc_data = bbc_data.sort_values(['participant_id', 'timestamp'], ascending=True)

    bbc_data['action_item'] = bbc_data[['action', 'item']].apply(lambda x: ' '.join(x), axis=1)

    participant_unique = np.unique(bbc_data['participant_id'])

    time_min = []
    time_diff = []

    for i in participant_unique:

        x = bbc_data.loc[bbc_data.participant_id == i, :]

        x = x.sort_values(['timestamp'], ascending=True)

        min_time = x['timestamp'].iloc[0]

        for row in x['timestamp']:
            time_min.append(min_time)

    bbc_data['min_time'] = time_min

    for row in bbc_data['participant_id']:
        df = bbc_data[['timestamp', 'min_time']].astype('datetime64[ns]')

        bbc_data['time_diff'] = df['timestamp'].subtract(df['min_time']).dt.total_seconds()

    bbc_data['time_diff'] = bbc_data['time_diff'].astype(int)

    bbc_data.to_csv(sys.argv[1])

else:
    print('Congrats! You already have these columns. No lets do some Data Viz!')
