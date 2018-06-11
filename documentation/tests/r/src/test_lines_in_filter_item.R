library(tidyverse)

rm(list=ls())


bbc_data <- read_csv(file = "data/bbc_data_session_id_condition.csv",
                     col_types = cols(
                       X1 = col_integer(),
                       id = col_integer(),
                       participant_id = col_integer(),
                       timestamp = col_datetime(format = ""),
                       pagetime = col_integer(),
                       item = col_character(),
                       action = col_factor(levels=NULL),
                       message = col_character(),
                       condition = col_integer(),
                       action_item = col_character(),
                       min_time = col_datetime(format = ""),
                       time_diff = col_integer(),
                       lag_time = col_datetime(format = ""),
                       interaction_gap = col_integer(),
                       newsession = col_integer(),
                       session_id = col_integer(),
                       participant_session_id = col_character()
                     ))

#  variable to show difference in time between clicks/actions    
bbc_data <- bbc_data %>% group_by(participant_id) %>% 
  mutate(min_time = min(timestamp)) %>% mutate(time_diff = ((timestamp - min_time) / 60))

source("src/functions/plotBBCdata_items.R")

plotBBCdata_items(bbc_data, 3, c("tab-r1", "tab-r2", "tab-r3", "tab-r4"), 0, 10)
