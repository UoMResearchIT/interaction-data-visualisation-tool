library(tidyverse)

rm(list=ls())

participants <- read.csv(file="data/participants.csv")

participants

bbc_data <- read_csv(file = "data/bbc_data_session_id.csv")

uniqueparticipants <- unique(bbc_data$participant_id)

uniqueparticipants

for(participants in uniqueparticipants){
  
  participantlist[[as.character(participants)]] <- filter(bbc_data, participant_id == participants)
  
}

select(bbc_data, participant_id)