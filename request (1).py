import base64
import requests


def send_request():
    # Request

    try:
        response = requests.get(
            url="https://www.mysportsfeeds.com/api/feed/pull/mlb/2016-regular/game_boxscore.json?gameid=20160404-CHC-LAA&teamstats=W,L,RF,RA&playerstats=AB,H,R,HR,ER",
            headers={
                "Authorization": "Basic " + base64.b64encode("ckauss:419901")
            }
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

send_request()