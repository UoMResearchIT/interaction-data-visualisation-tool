library("tidyverse")

rm(list=ls())

bbc_data <- read_csv(file = "data/bbc_data_session_id_condition.csv",
                     col_types = 
                       cols(
                         id = col_integer(),
                         participant_id = col_integer(),
                         timestamp = col_datetime(format = ""),
                         pagetime = col_integer(),
                         item = col_character(),
                         action = col_character(),
                         message = col_character()
                       ))

bbc_data <- bbc_data %>% mutate(action_item=paste(action,item))

uniqueparticipants <- unique(bbc_data$participant_id)

uniqueparticipants

participantlist <- list()
for(participant in uniqueparticipants){
  
  participantlist[[as.character(participant)]] <- filter(bbc_data, participant_id == participant)
  
}

select(bbc_data, participant_id)


participantlist[["310"]]

participantlist[["401"]]

time_lapsed <- bbc_data %>% group_by(participant_id) %>% 
  mutate(min_time = min(timestamp)) %>% mutate(time_diff = timestamp - min_time)


# creates the bbc_data_session_id.csv
time_lapsed <- bbc_data  %>% arrange(participant_id, timestamp) %>% 
  group_by(participant_id) %>% 
  mutate(lag_time = lag(timestamp)) %>%  mutate(interaction_gap =  timestamp - lag_time) %>% 
  mutate(newsession = ifelse(is.na(lag_time) | interaction_gap > 2400, 1, 0)) %>% # if there is a 40min gap a new session is made or if first time seeing new particpant
  mutate(session_id = cumsum(newsession)) %>% # identify the seperate sessions for each participant
  mutate(participant_session_id = paste(participant_id, session_id, sep = "-")) %>% ## creates participant session identifier
  ungroup() %>% # new group
  group_by(participant_session_id) %>% # group by participant_id
  mutate(min_time = min(timestamp)) %>% # first timestamp of eaxh session
  mutate(time_diff = timestamp - min_time) # gets diff between event time since session started



multiple_sessions <- time_lapsed %>% filter(session_id %in% c("2", "3", "4", "5")) # find participants who have up to 5 sessions

uniquesessions <- unique(multiple_sessions$participant_id) # put the uniqueparticpants in a list

uniquesessions # test

multiple_session_particpants <- time_lapsed %>% filter(participant_id %in% uniquesessions) # tibble with all data of particpants with multiple sessions

                                            