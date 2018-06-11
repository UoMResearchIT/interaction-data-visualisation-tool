# Function for user to plot graphs based on the CAKE Trials data. User inputs data, condition, item 
# and start and end time in minutes.

# Plots Items instead of actions

plotBBCdata_items <- function(indata, condition, items, start_time, end_time){
  
  # Get the data and add a column that matches the "actions" specified by user.
  # Those not specified are assigned "Other"
  myplot <- indata %>% mutate(item_simplified = 
                                fct_other(item, keep=items,
                                          other_level="other")) %>% 
    
    # Filter Data with the condition specified, and match that with the "item_simplified"
    filter(.data$condition == UQ(condition), 
           .data$item_simplified %in% UQ(items))  %>% 
    # Plot graph 
    ggplot(aes( x = time_diff, y = factor(participant_id), colour = item_simplified)) +
    # Add a line between points
    geom_line() +
    # Plot points
    geom_point(size=3) +
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
          colour = "Items") + 
    # Assign colours to the actions. Keeps things consistent
    scale_colour_manual(values =c("tab-r1" = "green",
                                  "tab-r2" = "blue",
                                  "tab-r3" = "red",
                                  "tab-r4" = "pink"))
  return(myplot)
  
}