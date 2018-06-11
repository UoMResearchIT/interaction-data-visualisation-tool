library(jsonlite)
library(tibble)
library(data.table)

rm(list=ls())

participants <- fromJSON(file="data/participants.json")

participants

participants_flat <- flatten(participants)

participants_flat

participants_tbl <- as_data_frame(participants_flat)

participants_tbl

write.csv(participants_tbl, "participants.csv")
