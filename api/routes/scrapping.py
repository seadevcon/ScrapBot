from apistar import App, Route, http
from typing import Dict


def get_info(app: App, query_params: http.QueryParams) -> Dict:
    return {
        "desc": "Welcome, this is the scrapbot API"
    }


routes = [
    Route("/info", method="POST", handler=get_info),
    ]