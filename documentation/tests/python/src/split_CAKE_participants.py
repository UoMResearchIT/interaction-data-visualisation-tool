# Splits CAKE Data into Cake and non Cake users

import pandas as pd

# Load Data that needs to be sorted
bbc_data = pd.read_csv('../data/bbc_data_session_id_condition.csv')
df = pd.read_csv('../data/bbc_data_click_stats_technical_session_id.csv')

# Split Data
cake = bbc_data.loc[(bbc_data['condition'].isin([1, 2]))]
non_cake = bbc_data.loc[(bbc_data['condition'].isin([3, 4]))]

# Write Data
cake.to_csv('bbc_data_cake', encoding='utf-8', index=False)
non_cake.to_csv('bbc_data_non_cake', encoding='utf-8', index=False)

# Split Stats Data
cake_stats = df.loc[(df['condition'].isin([1, 2]))]
non_cake_stats = df.loc[(df['condition'].isin([3, 4]))]

# Write Stats Data
cake_stats.to_csv('bbc_data_cake_stats_session_id', encoding='utf-8', index=False)
non_cake_stats.to_csv('bbc_data_non_cake_stats_session_id', encoding='utf-8', index=False)





