"""
An example code to run live queries on the SPIRE API.
"""

import requests
import json
import time

# SPIRE AIS ENDPOINT
ENDPOINT = 'https://ais.spire.com/vessels'

# FORMAT
FORMAT = 'json'

# YOUR TOKEN
AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6eyJpZCI6IjQ0NCIsIm5hbWUiOiJTZWFkZXZjb24gLSBIYWNrYXRob24gVGVtcG9yYXJ5IiwidXVpZCI6IjQ0NCJ9LCJpc3MiOiJzcGlyZS5jb20iLCJpYXQiOjE1MzU1NDcxMTN9.E72ji2Kt4bfREE_0LoyaWL2aPMwVvbIIKd3xPkx4FtI"

HEADERS = {"Authorization": "Bearer {}".format(AUTH_TOKEN), 'last_known_or_predicted_position_within': '{"type": "Polygon","coordinates": [[[-5.9765625,51.31688050404585], [12.12890625,51.31688050404585],[12.12890625,61.39671887310411], [-5.9765625,61.39671887310411],[-5.9765625,51.31688050404585]]]}'}


# Message Processing
def process_messages(messages):
    '''Function that will be used to process data fetched from the API'''
    print len(messages), 'messages'


def query_data():
    print 'Start Querying SPIRE Data...'
    request = ENDPOINT
    prev_since = None
    num_of_files = 1
    while True:
        print request
        response = requests.get(request, headers=HEADERS)

        data = response.json()

        try:
            process_messages(data['data'])

	    with open('./raw_api_data/raw_downloaded_json'+str(num_of_files)+'.txt', 'w') as outfile:
                json.dump(data['data'], outfile) 
                outfile.write("\n")
            num_of_files = num_of_files + 1
        except KeyError, e:
            print "Got a KeyError - Reason: %s" % str(e)
            print data
            print "Sleep 10 seconds..."
            time.sleep(1)
            continue

        if 'paging' in data:
            print data['paging']
	    print data
            since = data['paging']['next']
            request = ENDPOINT + "?next=%s" % since
        else:
            print 'The data transfer is over. Thank you.'
            return

        if prev_since == since:
            print 'Waiting for 1 minute.'
            time.sleep(10)
        else:
            prev_since = since

if __name__ == '__main__':
    query_data()
