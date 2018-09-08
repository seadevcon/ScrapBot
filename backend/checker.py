from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import requests
import pandas as pd


alang = [(
    72.21433639526367,
    21.440925741272014
),
    (
        72.15030670166016,
        21.384991490613558
    ),
    (
        72.18669891357422,
        21.34902245935883
    ),
    (
        72.24472045898436,
        21.42270950855108
    ),
    (
        72.21433639526367,
        21.440925741272014
    )]

def check_ais():
    url = 'http://localhost:8888/scrapping/notify'
    
    ais_df = pd.read_csv("ais_9131137.csv")
    ais_list = ais_df.values.tolist()
    for m in ais_list:
        imo = m[0]
        lat = m[1]
        lon = m[2]
        timestamp = m[4]
        point = Point(lon, lat)
        polygon = Polygon(alang)
        if polygon.contains(point):
            url = url + '?imo='+str(imo)+'&lat='+str(lat)+'&lon='+str(lon)+'&time='+str(timestamp)
            requests.get(url=url)
        


check_ais()
