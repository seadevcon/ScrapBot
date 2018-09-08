library("rjson")
library(leaflet)

m <- leaflet() %>%
  addTiles() #%>%  # Add default OpenStreetMap map tiles

scrapyard_places <- list(c(72.21433, 21.4409))

file_and_path <- rstudioapi::getSourceEditorContext()$path
tmp <- strsplit(file_and_path,"/")
tmp <- paste(tmp[[1]][-length(tmp[[1]])], collapse="/")
tmp <- paste(tmp,"/raw_api_data/",sep="")

distance = 5.0
setwd(tmp)
tmp1 <- list.files()

for (filename_index in 1:length(tmp1)){
  json_file <- paste(tmp,tmp1[filename_index],sep="")
  json_data <- fromJSON(paste(readLines(json_file), collapse=""))
  
  for (i in seq_along(json_data)){
  
    #json_file <- "/home/anon/Desktop/hackathon/ScrapBot/backend/raw_api_data/"+tmp[i]+.txt"
    if(is.numeric(json_data[[i]]$last_known_position$geometry$coordinates[1]) && is.numeric(json_data[[i]]$last_known_position$geometry$coordinates[2])){
        
        for( z in 1:length(scrapyard_places)){
          
          if((json_data[[i]]$last_known_position$geometry$coordinates[1] > (scrapyard_places[[z]][1]-distance)) && (json_data[[i]]$last_known_position$geometry$coordinates[1] < (scrapyard_places[[z]][1]+distance))){
            if((json_data[[i]]$last_known_position$geometry$coordinates[2] > (scrapyard_places[[z]][2]-distance)) && (json_data[[i]]$last_known_position$geometry$coordinates[2] < (scrapyard_places[[z]][2]+distance))){
              if(!is.null(json_data[[i]]$last_known_position)){
                m <- m %>% addMarkers(lng=json_data[[i]]$last_known_position$geometry$coordinates[1], lat=json_data[[i]]$last_known_position$geometry$coordinates[2], popup=json_data[[i]]$name)
            }
          }
        }
      }
    }
  }
}

m







