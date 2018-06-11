library("tidyverse")

rm(list=ls())

# read the data
bbc_data <- read_csv(file = "data/bbc_data_session_id.csv")

               
#  variable to show difference in time between clicks/actions    
bbc_data <- bbc_data %>% group_by(participant_id) %>% 
  mutate(min_time = min(timestamp)) %>% mutate(time_diff = ((timestamp - min_time) / 60))


# 1_participant_id_timediff_mins
all <- ggplot(bbc_data, aes( x = time_diff, y = factor(participant_id), group = participant_id)) + 
  geom_point() + labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
title = "Clicks over entire time of CAKE Trial" ) + guides(colour="none")


# 1a_participant_id_timediff_mins_colour
all_colour <- ggplot(bbc_data, aes( x = time_diff, y = factor(participant_id), group = participant_id, colour = participant_session_id)) + 
  geom_point() + labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                       title = "Participant ID and Time Difference between clicks" ) + guides(colour="none")


# 2_different slices of time

one <- ggplot(bbc_data, aes( x = time_diff, y = factor(participant_id), group = participant_id)) + 
  geom_point(size=1) + coord_cartesian(xlim = c(0, 1)) + labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                      title = "Density of clicks in 1 Minute" )
five <- ggplot(bbc_data, aes( x = time_diff, y = factor(participant_id), group = participant_id)) + 
  geom_point(size=1) + coord_cartesian(xlim = c(0, 5))+ labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                        title = "Density of clicks in 5 Minutes" )

ten <- ggplot(bbc_data, aes( x = time_diff, y = factor(participant_id), group = participant_id)) + 
  geom_point(size=1) + coord_cartesian(xlim = c(0, 10))+ labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                         title = "Density of clicks in 10 Minutes" )
thirty <- ggplot(bbc_data, aes( x = time_diff, y = factor(participant_id), group = participant_id)) + 
  geom_point(size=1) + coord_cartesian(xlim = c(0, 30))+ labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                         title = "Density of clicks in 30 Minutes" )
sixty <- ggplot(bbc_data, aes( x = time_diff, y = factor(participant_id), group = participant_id)) + 
  geom_point(size=1) + coord_cartesian(xlim = c(0, 60))+ labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                         title = "Density of clicks in 60 Minutes" )
one_twenty <- ggplot(bbc_data, aes( x = time_diff, y = factor(participant_id), group = participant_id)) + 
  geom_point(size=1) + coord_cartesian(xlim = c(0, 120))+ labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                          title = "Density of clicks in 2 hours" )


# 3_differenct slices of time with action_item in colour

one_colour <- ggplot(bbc_data, aes( x = time_diff, y = factor(participant_id), group = participant_id, colour = action_item)) + 
  geom_point() + coord_cartesian(xlim = c(0, 1)) + guides(colour="none") + labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                                                 title = "Types of clicks in 1 Minute" ) + guides(colour="none")

five_colour <- ggplot(bbc_data, aes( x = time_diff, y = factor(participant_id), group = participant_id, colour = action_item)) + 
  geom_point() + coord_cartesian(xlim = c(0, 5))+ guides(colour="none") + labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                                             title = "Types of clicks in 5 Minutes (by action_item)" ) + guides(colour="none")

ten_colour <- ggplot(bbc_data, aes( x = time_diff, y = factor(participant_id), group = participant_id, colour = action_item)) + 
  geom_point(size=1) + coord_cartesian(xlim = c(0, 10))+ labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                               title = "Types of clicks in 10 Minutes (by action_item)" ) + guides(colour="none")
thirty_colour <- ggplot(bbc_data, aes( x = time_diff, y = factor(participant_id), group = participant_id, colour = action_item)) + 
  geom_point(size=1) + coord_cartesian(xlim = c(0, 30))+ labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                               title = "Types of clicks in 30 Minutes (by action_item)" ) + guides(colour="none")
sixty_colour <- ggplot(bbc_data, aes( x = time_diff, y = factor(participant_id), group = participant_id, colour = action_item)) + 
  geom_point() + coord_cartesian(xlim = c(0, 60))+ labs( x = "Time Difference between clicks (in mins) " , y = "Particapant ID", 
                                                         title = "Types of clicks in 60 Minutes (by action_item)" ) + guides(colour="none")
one_twenty_colour <- ggplot(bbc_data, aes( x = time_diff, y = factor(participant_id), group = participant_id, colour = action_item)) + 
  geom_point() + coord_cartesian(xlim = c(0, 120))+ labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                          title = "Types of clicks in 2 hours (by action_item)" ) + guides(colour="none")

