from modules.main import Parser
from modules.main import pprint


class Russia(Parser):

    def get_movies(self):
        trs = self.html.find('body').find('div', id="afishaContents").find_all('tbody')
        movies = trs[1].find_all('tr', class_="tRow tooltips")
        l = []
        for movie in movies:
            l.append(
                {'time': movie.find_all('td')[0].text,
                 'name': movie.find_all('td')[1].text,
                 'price': movie.find_all('td')[4].text,
                 'hall': movie.find_all('td')[3].text,
                 }
            )
        pprint(l)


russia = Russia('http://cinema.kg')
russia.get_movies()
