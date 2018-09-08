import csv
import time
import datetime
import timestring

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import requests
import pandas as pd

use_file = 'ais_9131137.csv'
# use_file = 'alang_ais.csv'

alang_scrap_yard = [72.21433639526367, 21.440925741272014]
imo2 = []
latitude2 = []
longitude2 = []
speed2 = []
timestamp_string2 = []
timestamp2 = []
# Distanz, ab der eine Warnung abgegeben wird
warnung_distance = 0.1

# Distanz, ab der eine Abwracken angenommen wird
scrapping_distance = 0.05

# Gibt an, wieviele rueckblickende Werte innerhalb der Warnungsdistanz sein muessen, damit angenommen wird, dass das Schiff sich auf dem Weg zum abwracken befindet.
look_back_value = 10


def send_to_server(imo, lat, lon, timestamp):
    url = 'http://localhost:8888/scrapping/notify'
    url = url + '?imo=' + str(imo) + '&lat=' + str(lat) + '&lon=' + str(lon) + '&time=' + str(timestamp)
    requests.get(url=url)


skip = True
mentioned = True
with open(use_file, 'r') as csvfile:
    file_content = csv.reader(csvfile, delimiter=',')
    for row in file_content:
        if skip == False:
            imo2.append(row[0])
            latitude2.append(row[1])
            longitude2.append(row[2])
            speed2.append(row[3])
            timestamp_string2.append(row[4])
            timestamp2.append(timestring.Date(str(row[4])))
        # print timestring.Date(str(row[4]))
        skip = False

output = set()
for x in imo2:
    output.add(x)
print("Found ships:", output)

for ship in output:
    imo = []
    latitude = []
    longitude = []
    speed = []
    timestamp_string = []
    timestamp = []
    for u in range(0, len(imo2)):
        if imo2[u] == ship:
            imo.append(imo2[u])
            latitude.append(latitude2[u])
            longitude.append(longitude2[u])
            speed.append(speed2[u])
            timestamp_string.append(timestamp_string2[u])
            timestamp.append(timestamp2[u])
    
    # print imo
    
    for i in range(1, len(imo)):
        # time.sleep(1)
        if abs(float(latitude[i]) - alang_scrap_yard[1]) < warnung_distance:
            if abs(float(longitude[i]) - alang_scrap_yard[0]) < warnung_distance:
                print("warnung")
        
        if abs(float(latitude[i]) - alang_scrap_yard[1]) < scrapping_distance:
            if abs(float(longitude[i]) - alang_scrap_yard[0]) < scrapping_distance:
                #time.sleep(5)
                if mentioned == True:
                    mentioned = False
                    send_to_server(imo[i], latitude[i], longitude[i], timestamp_string[i])
                    print("scrapping")
    
    if i > look_back_value:
        calc_su_of_warning_in_the_look_back_time = 0
        for j in range(0, look_back_value):
            if abs(float(latitude[i - j]) - alang_scrap_yard[1]) < warnung_distance:
                if abs(float(longitude[i - j]) - alang_scrap_yard[0]) < warnung_distance:
                    calc_su_of_warning_in_the_look_back_time = calc_su_of_warning_in_the_look_back_time + 1
                    if calc_su_of_warning_in_the_look_back_time == look_back_value:
                        print("calc_su_of_warning_in_the_look_back_time!")
                        send_to_server(imo[i], latitude[i], longitude[i], timestamp_string[i])

for i in range(1, len(imo)):
    # time.sleep(1)
    if abs(float(latitude[i]) - alang_scrap_yard[1]) < warnung_distance:
        if abs(float(longitude[i]) - alang_scrap_yard[0]) < warnung_distance:
            print("warnung")
    
    if abs(float(latitude[i]) - alang_scrap_yard[1]) < scrapping_distance:
        if abs(float(longitude[i]) - alang_scrap_yard[0]) < scrapping_distance:
            if mentioned:
                mentioned = False
                send_to_server(imo[i], latitude[i], longitude[i], timestamp_string[i])
                print("scrapping")
    
    if i > look_back_value:
        calc_su_of_warning_in_the_look_back_time = 0
        for j in range(0, look_back_value):
            if abs(float(latitude[i - j]) - alang_scrap_yard[1]) < warnung_distance:
                if abs(float(longitude[i - j]) - alang_scrap_yard[0]) < warnung_distance:
                    calc_su_of_warning_in_the_look_back_time = calc_su_of_warning_in_the_look_back_time + 1
                    if calc_su_of_warning_in_the_look_back_time == look_back_value:
                        print("calc_su_of_warning_in_the_look_back_time!")
                        # send_to_server(imo[i], latitude[i], longitude[i], timestamp_string[i])

# print imo
# print latitude
# print longitude
# print speed
# print timestamp
