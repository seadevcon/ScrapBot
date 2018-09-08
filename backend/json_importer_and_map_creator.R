library("rjson")
library(leaflet)

# Make a list of icons. We'll index into it based on name.
oceanIcons <- iconList(
  ship = makeIcon("../ferry-18.png", "ferry-18@2x.png", 18, 18),
  pirate = makeIcon("../danger-24.png", "danger-24@2x.png", 24, 24)
)

# Some fake data
df <- sp::SpatialPointsDataFrame(
  cbind(
    (runif(20) - .5) * 10 - 90.620130,  # lng
    (runif(20) - .5) * 3.8 + 25.638077  # lat
  ),
  data.frame(type = factor(
    ifelse(runif(20) > 0.75, "pirate", "ship"),
    c("ship", "pirate")
  ))
)

m <- leaflet() %>%
  addTiles() #%>%  # Add default OpenStreetMap map tiles

scrapyard_places <- list(c(72.21433, 21.4409))

file_and_path <- rstudioapi::getSourceEditorContext()$path
tmp <- strsplit(file_and_path,"/")
tmp <- paste(tmp[[1]][-length(tmp[[1]])], collapse="/")
tmp <- paste(tmp,"/raw_api_data/",sep="")

distance = 5.0
distance_ok = 25.0
setwd(tmp)
tmp1 <- list.files()

for (filename_index in 1:10){#length(tmp1)){
  json_file <- paste(tmp,tmp1[filename_index],sep="")
  json_data <- fromJSON(paste(readLines(json_file), collapse=""))
  
  for (i in seq_along(json_data)){
  
    #json_file <- "/home/anon/Desktop/hackathon/ScrapBot/backend/raw_api_data/"+tmp[i]+.txt"
    if(is.numeric(json_data[[i]]$last_known_position$geometry$coordinates[1]) && is.numeric(json_data[[i]]$last_known_position$geometry$coordinates[2])){
        
        for( z in 1:length(scrapyard_places)){
          
          if((json_data[[i]]$last_known_position$geometry$coordinates[1] > (scrapyard_places[[z]][1]-distance_ok)) && (json_data[[i]]$last_known_position$geometry$coordinates[1] < (scrapyard_places[[z]][1]+distance_ok))){
            if((json_data[[i]]$last_known_position$geometry$coordinates[2] > (scrapyard_places[[z]][2]-distance_ok)) && (json_data[[i]]$last_known_position$geometry$coordinates[2] < (scrapyard_places[[z]][2]+distance_ok))){

                if((json_data[[i]]$last_known_position$geometry$coordinates[1] > (scrapyard_places[[z]][1]-distance)) && (json_data[[i]]$last_known_position$geometry$coordinates[1] < (scrapyard_places[[z]][1]+distance))){
                  if((json_data[[i]]$last_known_position$geometry$coordinates[2] > (scrapyard_places[[z]][2]-distance)) && (json_data[[i]]$last_known_position$geometry$coordinates[2] < (scrapyard_places[[z]][2]+distance))){
                    if(!is.null(json_data[[i]]$last_known_position)){
                      m <- m %>% addMarkers(lng=json_data[[i]]$last_known_position$geometry$coordinates[1], lat=json_data[[i]]$last_known_position$geometry$coordinates[2], popup=json_data[[i]]$name, icon=oceanIcons["pirate"])
                    }else{
                      m <- m %>% addMarkers(lng=json_data[[i]]$last_known_position$geometry$coordinates[1], lat=json_data[[i]]$last_known_position$geometry$coordinates[2], popup=json_data[[i]]$name, icon=oceanIcons["ship"])
                    }
                  }else{
                    
                    m <- m %>% addMarkers(lng=json_data[[i]]$last_known_position$geometry$coordinates[1], lat=json_data[[i]]$last_known_position$geometry$coordinates[2], popup=json_data[[i]]$name, icon=oceanIcons["ship"])
                  }
                }else{
                  
                  m <- m %>% addMarkers(lng=json_data[[i]]$last_known_position$geometry$coordinates[1], lat=json_data[[i]]$last_known_position$geometry$coordinates[2], popup=json_data[[i]]$name, icon=oceanIcons["ship"])
            }
            }
        }
      }
    }
  }
}

m







