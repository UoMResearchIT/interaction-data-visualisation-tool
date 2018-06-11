library("tidyverse")
library("forcats")
rm(list=ls())


# read the data
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

# Collapse the actions we're not particularly interested in to a single level
# and make new variable
bbc_data <- bbc_data %>% mutate(action_simplified = 
                                  fct_other(action, keep=c("pause", "play", "rewind"),
                                                           other_level="other"))

## For the plots, try filtering and piping, e.g.

bbc_data %>%
  filter(condition == 1, action_simplified %in% c("pause","play", "other"))  %>% 
  ggplot(aes( x = time_diff, y = factor(participant_id), colour = action)) + 
  geom_point(size=1) +
  coord_cartesian(xlim = c(0, 30)) + 
  labs( x = "Time Difference between clicks (in mins)" , y = "Partipant ID")

# Colours are a pain to deal with; we always want play to be the same colour, etc.
bbc_data %>%
  filter(condition == 1, action_simplified %in% c("pause","play", "rewind", "other"))  %>% 
  ggplot(aes( x = time_diff, y = factor(participant_id), colour = action_simplified)) + 
  geom_point(size=1) +
  coord_cartesian(xlim = c(0, 30)) + 
  labs( x = "Time Difference between clicks (in mins)" , y = "Partipant ID") + 
  scale_colour_manual(values =c("pause" = "red",
                                "play" = "green",
                                "rewind" = "orange",
                                "other" = "grey"))

# We can put this in a function so we can plot for any set of conditions and actions:
# "filter()" uses non-standard evaluation, which is what all the .data and UQ() stuff is about
# see https://uomresearchit.github.io/r-tidyverse-intro/99-function/
plotBBCdata <- function(indata, condition, actions, start_time, end_time){
  

  myplot <- indata %>% mutate(action_simplified = 
                                fct_other(action, keep=actions,
                                          other_level="other")) %>% 
    
  filter(.data$condition == UQ(condition), 
         .data$action_simplified %in% UQ(actions))  %>% 
    ggplot(aes( x = time_diff, y = factor(participant_id), colour = action_simplified)) + 
    geom_point(size=1) +
    coord_cartesian(xlim = c(start_time, end_time)) + 
    labs( x = "Time Difference between clicks (in mins)" , y = "Partipant ID",
          title = paste("Condition -", (if (condition == 1) {
            ("CAKE Multiple")
          } else if (condition == 2) {
            ("CAKE Single")
          } else if (condition == 3) {
            ("Linear Multiple")
          } else  
            ("Linear Single")
          )),
          colour = "Action") + 
    scale_colour_manual(values =c("pause" = "red",
                                  "play" = "green",
                                  "rewind" = "orange",
                                  "other" = "grey"))
  return(myplot)
  
}

 


plotBBCdata(bbc_data, 2, c("play","pause"), 0, 60)

plotBBCdata(bbc_data, 1, c("play","pause", "click", "other"), 0, 30)

plotBBCdata(bbc_data, 3, c("play","pause", "rewind", "other"), 0, 30)

example <- plotBBCdata(bbc_data, 4, c("play", "other"), 10, 30)

example_two <- plotBBCdata(bbc_data, 4, c("play", "other"), 10, 30)

example_two

#### End



# Filter by different experiment conditions 
condition_one <- filter(bbc_data, condition == 1) # CAKE MULTIPLE

condition_two <- filter(bbc_data, condition == 2) # CAKE SINGLE

condition_three <- filter(bbc_data, condition == 3) # LINEAR MULTIPLE

condition_four <- filter(bbc_data, condition == 4) # LINEAR SINGLE


# CONDITION ONE - filter by differnet tyypes of actions
pause_filter <- filter(condition_one, action == "pause")

play_filter <- filter(condition_one, action == "play")

rewind_filter <- filter(condition_one, action == "rewind")




# CONDITION ONE - plots of all incidents of PAUSES, PLAY and REWIND participants in 30 mins.  
pause <- ggplot(pause_filter, aes( x = time_diff, y = factor(participant_id) )) + 
  geom_point(size=1) + coord_cartesian(xlim = c(0, 30)) + labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                                title = "Cake Multiple - Pauses" )

play <-  ggplot(play_filter, aes( x = time_diff, y = factor(participant_id), group = participant_id )) + 
  geom_point(size=1) + coord_cartesian(xlim = c(0, 30)) + labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                                title = "Cake Multiple - Play" )

rewind <-  ggplot(rewind_filter, aes( x = time_diff, y = factor(participant_id), group = action )) + 
  geom_point(size=1) + coord_cartesian(xlim = c(0, 30)) + labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                                title = "Cake Multiple - Rewind" )

# CONFITION ONE - Manually assign the colour to the action

colour_scheme <- c("pause" = "red", "play" = "green", "rewind" = "orange", " " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black"," " = "black" )
                   
combined_colour <- ggplot(condition_one, aes( x = time_diff, y = factor(participant_id), group = action, colour = action )) + 
  geom_point(size=1) + coord_cartesian(xlim = c(0, 30)) + labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                                title = "Cake Multiple - Pause, Play, Rewind - 30 mins" ) + scale_colour_manual(values = colour_scheme)

colour_scheme_black <- c("pause" = "red", "play" = "green", "rewind" = "orange", "1" = "black","2" = "black","3" = "black",
                         "back" = "black","click" = "black","collapsed" = "black","deselect" = "black","dinner" = "black",
                         "ended" = "black","fullscreen" = "black","learn" = "black","lots" = "black","mullet" = "black",
                         "not_ready" = "black","toggle" = "black")

combined_colour_black <- ggplot(condition_one, aes( x = time_diff, y = factor(participant_id), group = action, colour = action )) + 
  geom_point(size=1) + coord_cartesian(xlim = c(0, 30)) + labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                                title = "Cake Multiple - Pause, Play, Rewind - 30 mins" ) + scale_colour_manual(values = colour_scheme_black)

colour_scheme_grey <- c("pause" = "red", "play" = "green", "rewind" = "orange", "1" = "grey","2" = "grey",
                                               "3" = "grey","back" = "grey","click" = "grey","collapsed" = "grey","deselect" = "grey",
                                               "dinner" = "grey","ended" = "grey","fullscreen" = "grey","learn" = "grey",
                                               "lots" = "grey","mullet" = "grey","not_ready" = "grey","toggle" = "grey", 
                                                "6" = "grey", "not_really" = "grey", "4" = "grey", "choc_pots" = "grey",
                                                    "blur" = "grey", "focus" = "grey","finish" = "grey", "seeked" = "grey",
                                                          "webkitfullscreenchange" = "grey")

combined_colour_grey <- ggplot(condition_one, aes( x = time_diff, y = factor(participant_id), group = action, colour = action )) + 
  geom_point(size=1) + coord_cartesian(xlim = c(0, 30)) + labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                                title = "Cake Multiple - Pause, Play, Rewind - 30 mins" ) + scale_colour_manual(values = colour_scheme_grey)

# CONDITION Two 

combined_colour_grey_two <- ggplot(condition_two, aes( x = time_diff, y = factor(participant_id), group = action, colour = action )) + 
  geom_point(size=1) + coord_cartesian(xlim = c(0, 30)) + labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                                title = "Cake Single - Pause, Play, Rewind - 30 mins" ) + scale_colour_manual(values = colour_scheme_grey)


# CONDITION THREE

combined_colour_grey_three <- ggplot(condition_three, aes( x = time_diff, y = factor(participant_id), group = action, colour = action )) + 
  geom_point(size=1) + coord_cartesian(xlim = c(0, 30)) + labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                                title = "Linear Multiple - Pause, Play, Rewind - 30 mins" ) + scale_colour_manual(values = colour_scheme_grey)


# CONDITION FOUR

combined_colour_grey_four <- ggplot(condition_four, aes( x = time_diff, y = factor(participant_id), group = action, colour = action )) + 
  geom_point(size=1) + coord_cartesian(xlim = c(0, 30)) + labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                                title = "Linear Single - Pause, Play, Rewind - 30 mins" ) + scale_colour_manual(values = colour_scheme_grey)









