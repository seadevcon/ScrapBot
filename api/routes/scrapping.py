from apistar import App, Route, http
from typing import Dict

from services.vessel_service import get_details
from services.fire_not import send_notification

def get_info(app: App, query_params: http.QueryParams) -> Dict:
    return {
        "desc": "Welcome, this is the scrapbot API"
    }

def test(query_params: http.QueryParams):
    params = dict(query_params)
    imo = params.get("imo")
    lat = params.get("lat")
    lon = params.get("lon")
    time = params.get("time")
    vtype, owner, name = get_details(imo)
    send_notification(imo, owner, lat, lon, time, vtype, name)
    


routes = [
    Route("/info", method="POST", handler=get_info),
    Route("/notify", method="GET", handler=test),
    ]