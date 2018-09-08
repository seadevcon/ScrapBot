import csv
import time
import datetime
import timestring

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import requests
import pandas as pd


alang_scrap_yard =[72.21433639526367, 21.440925741272014]
imo = []
latitude = []
longitude = []
speed = []
timestamp_string = []
timestamp = []
#Distanz, ab der eine Warnung abgegeben wird
warnung_distance = 0.1

#Distanz, ab der eine Abwracken angenommen wird
scrapping_distance = 0.05

#Gibt an, wieviele rueckblickende Werte innerhalb der Warnungsdistanz sein muessen, damit angenommen wird, dass das Schiff sich auf dem Weg zum abwracken befindet.
look_back_value = 10

def send_to_server(imo, lat, lon, timestamp):
	url = 'http://localhost:8888/scrapping/notify'
	url = url + '?imo='+str(imo)+'&lat='+str(lat)+'&lon='+str(lon)+'&time='+str(timestamp)
	#print imo
	#print lat
	#print lon
	#print timestamp
        #requests.get(url=url)




skip = True
with open('ais_9131137.csv', 'rb') as csvfile:
	file_content = csv.reader(csvfile, delimiter=',')
	for row in file_content:
		imo.append(row[0])
		latitude.append(row[1])
		longitude.append(row[2])
		speed.append(row[3])
		timestamp_string.append(row[4])
		if skip == False:
			timestamp.append(timestring.Date(str(row[4])))
			#print timestring.Date(str(row[4]))
		skip = False

for i in range(1,len(imo)):
	#time.sleep(1)
	if abs(float(latitude[i]) - alang_scrap_yard[1]) < warnung_distance:
		if abs(float(longitude[i]) - alang_scrap_yard[0]) < warnung_distance:
			print "warnung"
	
	if abs(float(latitude[i]) - alang_scrap_yard[1]) < scrapping_distance:
		if abs(float(longitude[i]) - alang_scrap_yard[0]) < scrapping_distance:
			print "scrapping"

	if i > look_back_value:
		calc_su_of_warning_in_the_look_back_time = 0
		for j in range(0,look_back_value):
			if abs(float(latitude[i-j]) - alang_scrap_yard[1]) < warnung_distance:
				if abs(float(longitude[i-j]) - alang_scrap_yard[0]) < warnung_distance:
					calc_su_of_warning_in_the_look_back_time = calc_su_of_warning_in_the_look_back_time + 1
					if calc_su_of_warning_in_the_look_back_time == look_back_value:
						print "calc_su_of_warning_in_the_look_back_time!"
						send_to_server(imo[i], latitude[i], longitude[i], timestamp_string[i])

	


		
	
#print imo
#print latitude
#print longitude
#print speed
#print timestamp




