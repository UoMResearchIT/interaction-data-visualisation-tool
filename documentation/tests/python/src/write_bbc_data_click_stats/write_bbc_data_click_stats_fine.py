import plotly.offline as offline
import plotly.graph_objs as go
import pandas as pd
import numpy as np

bbc_data = pd.read_csv('../../data/bbc_data_click_stats.csv')

bbc_data = bbc_data.replace([np.inf, -np.inf], np.nan).dropna(how="all")

print(bbc_data)
# Mean, median, standard deviation of the different conditions in CAKE Trial

conditions = ['CAKE Multiple', 'CAKE Single', 'Linear Multiple', 'Linear Single']

mean_c_l = []
median_c_l = []
std_c_l = []

mean_tm_l = []
median_tm_l = []
std_tm_l = []

mean_cpm_l = []
median_cpm_l = []
std_cpm_l = []

for i in conditions:

    x = bbc_data.loc[bbc_data.condition == i, :]

    mean_clicks = x["click_count"].mean()
    median_clicks = x["click_count"].median()
    std_clicks = x["click_count"].std()

    mean_time_mins = x["time_taken_mins"].mean()
    median_time_mins = x["time_taken_mins"].median()
    std_time_mins = x["time_taken_mins"].std()

    mean_clicks_per_min = x["clicks_per_minute"].mean()
    median_clicks_per_min = x["clicks_per_minute"].median()
    std_clicks_per_min = x["clicks_per_minute"].std()

    mean_c_l.append(mean_clicks)
    median_c_l.append(median_clicks)
    std_c_l.append(std_clicks)

    mean_tm_l.append(mean_time_mins)
    median_tm_l.append(median_time_mins)
    std_tm_l.append(std_time_mins)

    mean_cpm_l.append(mean_clicks_per_min)
    median_cpm_l.append(median_clicks_per_min)
    std_cpm_l.append(std_clicks_per_min)


# Mean, median, standard deviation of entire CAKE Trial

mean_clicks = bbc_data["click_count"].mean()
median_clicks = bbc_data["click_count"].median()
std_clicks = bbc_data["click_count"].std()

mean_time_mins = bbc_data["time_taken_mins"].mean()
median_time_mins = bbc_data["time_taken_mins"].median()
std_time_mins = bbc_data["time_taken_mins"].std()

mean_clicks_per_min = bbc_data["clicks_per_minute"].mean()
median_clicks_per_min = bbc_data["clicks_per_minute"].median()
std_clicks_per_min = bbc_data["clicks_per_minute"].std()

conditions.append('ALL')

mean_c_l.append(mean_clicks)
median_c_l.append(median_clicks)
std_c_l.append(std_clicks)

mean_tm_l.append(mean_time_mins)
median_tm_l.append(median_time_mins)
std_tm_l.append(std_time_mins)

mean_cpm_l.append(mean_clicks_per_min)
median_cpm_l.append(median_clicks_per_min)
std_cpm_l.append(std_clicks_per_min)

bbc_data_stats_sorted = pd.DataFrame(
    {'condition': conditions,
     'mean_click_count': mean_c_l,
     'median_click_count': median_c_l,
     'std_click_count': std_c_l,
     'mean_time_mins': mean_tm_l,
     'median_time_mins': median_tm_l,
     'std_time_mins': std_tm_l,
     'mean_clicks_per_minute': mean_cpm_l,
     'median_clicks_per_minute': median_cpm_l,
     'std_clicks_per_minute': std_cpm_l,
     }
)

print(bbc_data_stats_sorted.head())


bbc_data_stats_sorted.to_csv('bbc_data_click_stats_fine', encoding='utf-8', index=False)
