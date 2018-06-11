# Function for user to plot graphs based on the CAKE Trials data. User inputs data, condition, actions 
# and start and end time in minutes.

plotBBCdata <- function(indata, condition, actions, start_time, end_time){
  
  # Get the data and add a column that matches the "actions" specified by user.
  # Those not specified are assigned "Other"
  myplot <- indata %>% mutate(action_simplified = 
                                fct_other(action, keep=actions,
                                          other_level="other")) %>% 
    
    # Filter Data with the condition specified, and match that with the "action_simplified"
    filter(.data$condition == UQ(condition), 
           .data$action_simplified %in% UQ(actions))  %>% 
    # Plot graph 
    ggplot(aes( x = time_diff, y = factor(participant_id), colour = action_simplified)) + 
    # Change size of plots
    geom_point(size=3) +
    # Set the time on the y axis
    coord_cartesian(xlim = c(start_time, end_time)) + 
    # Label the graph based on the condition user specifies.
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
    # Assign colours to the actions. Keeps things consistent
    scale_colour_manual(values =c("pause" = "red",
                                  "play" = "green",
                                  "rewind" = "orange",
                                  "other" = "grey"))
  
  
  return(myplot)
  
}
