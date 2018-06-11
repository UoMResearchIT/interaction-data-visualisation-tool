library("tidyverse")

rm(list=ls())

multiplot <- function(..., plotlist=NULL, file, cols=1, layout=NULL) {
  library(grid)
  
  # Make a list from the ... arguments and plotlist
  plots <- c(list(...), plotlist)
  
  numPlots = length(plots)
  
  # If layout is NULL, then use 'cols' to determine layout
  if (is.null(layout)) {
    # Make the panel
    # ncol: Number of columns of plots
    # nrow: Number of rows needed, calculated from # of cols
    layout <- matrix(seq(1, cols * ceiling(numPlots/cols)),
                     ncol = cols, nrow = ceiling(numPlots/cols))
  }
  
  if (numPlots==1) {
    print(plots[[1]])
    
  } else {
    # Set up the page
    grid.newpage()
    pushViewport(viewport(layout = grid.layout(nrow(layout), ncol(layout))))
    
    # Make each plot, in the correct location
    for (i in 1:numPlots) {
      # Get the i,j matrix positions of the regions that contain this subplot
      matchidx <- as.data.frame(which(layout == i, arr.ind = TRUE))
      
      print(plots[[i]], vp = viewport(layout.pos.row = matchidx$row,
                                      layout.pos.col = matchidx$col))
    }
  }
}


# read the data
bbc_data <- read_csv(file = "data/bbc_data_session_id_condition.csv")

#  variable to show difference in time between clicks/actions    
bbc_data <- bbc_data %>% group_by(participant_id) %>% 
  mutate(min_time = min(timestamp)) %>% mutate(time_diff = ((timestamp - min_time) / 60))



# Filter by different experiment conditions 
condition_one <- filter(bbc_data, condition == 1)

condition_two <- filter(bbc_data, condition == 2) 

condition_three <- filter(bbc_data, condition == 3)

condition_four <- filter(bbc_data, condition == 4)


# plots of all participants in each condition. 30 mins 
c1 <- ggplot(condition_one, aes( x = time_diff, y = factor(participant_id), group = participant_id)) + 
  geom_point(size=1) + coord_cartesian(xlim = c(0, 30)) + labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                               title = "Cake Multiple - Density of Clicks" )

c2 <- ggplot(condition_two, aes( x = time_diff, y = factor(participant_id), group = participant_id)) + 
  geom_point(size=1) + coord_cartesian(xlim = c(0, 30)) + labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                               title = "Cake Single - Density of Clicks" )

c3 <- ggplot(condition_three, aes( x = time_diff, y = factor(participant_id), group = participant_id)) + 
  geom_point(size=1) + coord_cartesian(xlim = c(0, 30)) + labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                               title = "Linear Multiple - Density of Clicks" )

c4 <- ggplot(condition_four, aes( x = time_diff, y = factor(participant_id), group = participant_id)) + 
  geom_point(size=1) + coord_cartesian(xlim = c(0, 30)) + labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                               title = "Linear Single - Density of Clicks" )

condition_multiplot <- multiplot(c1, c2, c3, c4, cols=2) + labs(title = "Density of clicks across the differenct conditions") 


# Individual User Condition One
indiv_user <- filter(condition_one, participant_id == 220)

indiv_user

type_click_indiv_user <- ggplot(indiv_user, aes( x = time_diff, y = factor(participant_id), group = participant_id, colour = action_item)) + 
  geom_point() + coord_cartesian(xlim = c(0, 30)) + labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                                                 title = "Participant ID 220 - Cake Multiple - Types of clicks in 30 Minutes" )

type_click_indiv_user

type_click_indiv_user_sig <- ggplot(indiv_user, aes( x = time_diff, y = factor(participant_id), group = participant_id, colour = action_item)) + 
  geom_point() + coord_cartesian(xlim = c(12, 13)) + labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                          title = "Participant ID 220 - Cake Multiple - Types of clicks between 12th and 13th Minute" )

type_click_indiv_user_sig


# Individual User Condition Two

indiv_user_two <- filter(condition_two, participant_id == 126)

type_click_indiv_user_two <- ggplot(indiv_user_two, aes( x = time_diff, y = factor(participant_id), group = participant_id, colour = action_item)) + 
  geom_point() + coord_cartesian(xlim = c(0, 30)) + labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                          title = "Participant ID 126 - Cake Single - Types of clicks in 30 Minutes" )
type_click_indiv_user_two



# Individual User Condition Three

indiv_user_three <- filter(condition_three, participant_id == 422)

type_click_indiv_user_three <- ggplot(indiv_user_three, aes( x = time_diff, y = factor(participant_id), group = participant_id, colour = action_item)) + 
  geom_point() + coord_cartesian(xlim = c(0, 30)) + labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                          title = "Participant ID 422 - Linear Multiple - Types of clicks in 30 Minutes" )
type_click_indiv_user_three



# Individual User Condition Two

indiv_user_four <- filter(condition_four, participant_id == 314)

type_click_indiv_user_four <- ggplot(indiv_user_four, aes( x = time_diff, y = factor(participant_id), group = participant_id, colour = action_item)) + 
  geom_point() + coord_cartesian(xlim = c(0, 30)) + labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID", 
                                                          title = "Participant ID 314 - Linear Single - Types of clicks in 30 Minutes" )
type_click_indiv_user_four


# All Individual Users on One Graph

group_users <- bbc_data %>% filter(participant_id == 220 | participant_id == 126 | participant_id == 422 | participant_id == 314) %>% 
  mutate (participant_id_condition=paste(participant_id,condition, sep = "-"))

group_users_plot <- ggplot(group_users, aes( x = time_diff, y = factor(condition), group = participant_id, colour = action_item)) + 
  geom_point() + coord_cartesian(xlim = c(0, 30)) + labs( x = "Time Difference between clicks (in mins)" , y = "Particapant ID and Condition Number", 
                                                          title = "All Conditions, Individual Users - Types of clicks in 30 Minutes" )

group_users_plot

