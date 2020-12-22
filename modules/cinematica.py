import json

from modules.main import *


class Cinematica(Parser):
    def __init__(self, url):
        r = requests.get(url)
        self.js = json.loads(r.text)

    def get_movies(self):
        for i in self.js['list']:
            print(i['name'])


cinematica = Cinematica('https://cinematica.kg/api/v1/movies/today')
cinematica.get_movies()
