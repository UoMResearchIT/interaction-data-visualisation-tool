#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#
library(shiny)
library(tidyverse)
library(forcats)
library(stats)

bbc_data <- read_csv(file = "../data/bbc_data_session_id_condition.csv",
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

source("../src/functions/plotBBCdata.R")

# Define UI for application that draws a histogram
ui <- fluidPage(
   
   # Application title
   titlePanel("CAKE Trials Data"),
   
   # Sidebar with a slider input for number of bins 
   sidebarLayout(
      sidebarPanel(
        
         radioButtons("condition", label = h3("Conditions"),
                      choices = list("CAKE Mutiple" = 1, "CAKE Single" = 2, "Linear Multiple" = 3, "Linear Single" = 4), 
                      selected = 1),
         checkboxGroupInput("actions", label = h3("Actions"), 
                            choices = list("Play" = "play", "Pause" = "pause", "Rewind" = "rewind", "Other" = "other"),
                            selected = "play"),
         sliderInput("time", label = h3("Time"), min = 0, 
                     max = 120, value = c(0 , 30))
         
         
         ),
      
      # Show a plot of the generated distribution
      mainPanel(
         plotOutput("distPlot")
      )
   )
)

# Define server logic required to draw a histogram
server <- function(input, output) {
   
   output$distPlot <- renderPlot({
      # generate bins based on input$bins from ui.R
      #x    <- faithful[, 2] 
      #bins <- seq(min(x), max(x), length.out = input$bins + 1)
      
      # draw the histogram with the specified number of bins
      #hist(x, breaks = bins, col = 'darkgray', border = 'white')
     
    plotBBCdata(bbc_data, input$condition, c(input$actions), input$time[1],input$time[2])
     
   })
}

# Run the application 
shinyApp(ui = ui, server = server)

