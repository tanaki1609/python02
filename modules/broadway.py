from modules.main import *


class BroadWay(Parser):

    def get_movies(self):
        section = self.html.find('body').find_all('section')
        uls = section[1].find('div', class_='nano-content').find_all('ul')
        list = []
        for i in uls:
            list.append(
                {'time': i.find_all('li')[0].text,
                 'name': i.find_all('li')[1].text,
                 'price': i.find_all('li')[2].text,
                 'hall': i.find_all('li')[3].text,
                 }
            )

        pprint(list)


broadway = BroadWay('https://broadway.kg/reserve/')
broadway.get_movies()
