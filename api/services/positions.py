import requests

def test_vessel_tracker():
    
    request_data = {'last_known_or_predicted_position_within':{
        "type": "Polygon",
        "coordinates": [
          [
              [8.26171875,-66.51326044311185],[10.546875,-66.51326044311185],[10.546875,-65.58572002329471],[8.26171875,-65.58572002329471],[8.26171875,-66.51326044311185]
          ]
        ]
      },
}
    endpoint = "https://ais.spire.com/vessels/?last_known_or_predicted_position_within:'{\"typ\": \"Polygon\",\"coordinates\": [[[8.26171875,-66.51326044311185],[10.546875,-66.51326044311185],[10.546875,-65.58572002329471],[8.26171875,-65.58572002329471],[8.26171875,-66.51326044311185]]]}'"

    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6eyJpZCI6IjQ0NCIsIm5hbWUiOiJTZWFkZXZjb24gLSBIYWNrYXRob24gVGVtcG9yYXJ5IiwidXVpZCI6IjQ0NCJ9LCJpc3MiOiJzcGlyZS5jb20iLCJpYXQiOjE1MzU1NDcxMTN9.E72ji2Kt4bfREE_0LoyaWL2aPMwVvbIIKd3xPkx4FtI',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.get(url=endpoint,
                             headers=headers)
    jsonText = response.text
    print(jsonText)