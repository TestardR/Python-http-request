import requests
from pprint import pprint

url = 'https://api.kanye.rest/'


def fetchData(url):
    try:
        r = requests.get(url)
        json_data = r.json()
        pprint(json_data['quote'])
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

fetchData(url)


