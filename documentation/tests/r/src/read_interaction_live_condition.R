library("tidyverse")

rm(list=ls())

# read the data
bbc_data <- read_csv(file = "data/interaction_live_condition.csv")

bbc_data <- bbc_data %>% mutate(action_item=paste(action,item))

#  variable to show difference in time between clicks/actions    
bbc_data <- bbc_data %>% group_by(participant_id) %>% 
  mutate(min_time = min(timestamp)) %>% mutate(time_diff = ((timestamp - min_time) / 60))

bbc_data <- bbc_data  %>% arrange(participant_id, timestamp) %>% 
  group_by(participant_id) %>% 
  mutate(lag_time = lag(timestamp)) %>%  mutate(interaction_gap =  timestamp - lag_time) %>% 
  mutate(newsession = ifelse(is.na(lag_time) | interaction_gap > 1800, 1, 0)) %>% # if there is a 30min gap a new session is made or if first time seeing new particpant
  mutate(session_id = cumsum(newsession)) %>% # identify the seperate sessions for each participant
  mutate(participant_session_id = paste(participant_id, session_id, sep = "-")) %>% ## creates participant session identifier
  ungroup() %>% # new group
  group_by(participant_session_id) %>% # group by participant_id
  mutate(min_time = min(timestamp)) %>% # first timestamp of eaxh session
  mutate(time_diff = timestamp - min_time) # gets diff between event time since session started


