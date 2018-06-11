# Function for user to plot graphs based on the CAKE Trials data. User inputs data, actions and start and end time in minutes.
# It will display all 4 conditions at once, as opposed to allowing auser to choose which condition to show


plotBBCdata_facet_wrap <- function(indata, actions, start_time, end_time){
  
  # Get the data and add a column that matches the "actions" specified by user.
  # Those not specified are assigned "Other"
  myplot <- indata %>% mutate(action_simplified = 
                                fct_other(action, keep=actions,
                                          other_level="other")) %>% 
    
    # Filter Data with the condition specified, and match that with the "action_simplified"
    filter(.data$action_simplified %in% UQ(actions))  %>% 
    # Plot graph 
    ggplot(aes( x = time_diff, y = factor(participant_id), colour = action_simplified)) + 
    # Change size of plots
    geom_point(size=1) +
    # specify what criteria to split the plots by, in this case condition
    facet_wrap( ~ condition) +
    coord_cartesian(xlim = c(start_time, end_time)) + 
    labs( x = "Time Difference between clicks (in mins)" , y = "Partipant ID",
          colour = "Action") + 
    # Assign colours to the actions. Keeps things consistent
    scale_colour_manual(values =c("pause" = "red",
                                  "play" = "green",
                                  "rewind" = "orange",
                                  "other" = "grey"))

  
  
  return(myplot)
  
}