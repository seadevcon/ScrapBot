from apistar import App, Route, http
from typing import Dict

from services.positions import test_vessel_tracker


def get_info(app: App, query_params: http.QueryParams) -> Dict:
    return {
        "desc": "Welcome, this is the scrapbot API"
    }

def test():
    test_vessel_tracker()


routes = [
    Route("/info", method="POST", handler=get_info),
    Route("/test", method="POST", handler=test),
    ]