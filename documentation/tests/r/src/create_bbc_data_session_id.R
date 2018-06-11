library("tidyverse")

rm(list=ls())

bbc_data <- read_csv(file = "data/interaction_live.csv",
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

ggplot(time_lapsed, aes( x = time_diff, y = factor(participant_id), group = participant_id)) + 
  geom_point() + coord_cartesian(xlim = c(0, 1800))


# creates the bbc_data_session_id.csv
time_lapsed <- bbc_data  %>% arrange(participant_id, timestamp) %>% 
                              group_by(participant_id) %>% 
 mutate(lag_time = lag(timestamp)) %>%  mutate(interaction_gap =  timestamp - lag_time) %>% 
 mutate(newsession = ifelse(is.na(lag_time) | interaction_gap > 1800, 1, 0)) %>% # if there is a 30min gap a new session is made or if first time seeing new particpant
  mutate(session_id = cumsum(newsession)) %>% # identify the seperate sessions for each participant
  mutate(participant_session_id = paste(participant_id, session_id, sep = "-")) %>% ## creates participant session identifier
  ungroup() %>% # new group
  group_by(participant_session_id) %>% # group by participant_id
  mutate(min_time = min(timestamp)) %>% # first timestamp of eaxh session
  mutate(time_diff = timestamp - min_time) # gets diff between event time since session started


# Test plot
ggplot(time_lapsed, aes( x = time_diff, y = factor(participant_id), group = participant_session_id, 
                         colour = action_item)) + 
  geom_point() + coord_cartesian(xlim = c(0, 1800)) + guides(colour="none")



dput(sort(unique(time_lapsed$action)))

