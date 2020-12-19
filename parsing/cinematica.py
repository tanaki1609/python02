import json
from pprint import pprint

import requests

r = requests.get('https://cinematica.kg/api/v1/movies/today')
js = json.loads(r.text)
pprint(js['list'][0]['name'])