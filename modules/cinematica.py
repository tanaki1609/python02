import json
import psycopg2
from modules.main import *


class Cinematica(Parser):
    def __init__(self, url):
        r = requests.get(url)
        self.js = json.loads(r.text)
        self.connect = psycopg2.connect(dbname='postgres',
                                        user='postgres',
                                        host='localhost',
                                        password='password')

        self.cursor = self.connect.cursor()

    def create_table(self):
        self.cursor.execute("create table if not exists cinema("
                            "id serial primary key, "
                            "name varchar(255));")
        self.connect.commit()
        self.cursor.execute("create table if not exists films("
                            "id serial primary key, "
                            "name varchar(255),"
                            "price float ,"
                            "hall varchar(255),"
                            "time varchar(255),"
                            "cinema_id int,"
                            "constraint fk_cinema foreign key(cinema_id)"
                            "references cinema(id));")

        self.connect.commit()

    def save_cinema(self):
        self.cursor.execute("insert into cinema(name) "
                            "values('%s');" % 'Cosmopark')
        self.connect.commit()

    def save_movies(self):
        for i in self.js['list'][0]['repertories']:
            self.cursor.execute("insert into films(name, time, price, hall, cinema_id) "
                                "values('%s','%s','%s','%s', '%s');"
                                % (i['movie'],
                                   i['time'],
                                   i['price'],
                                   i['hall'],
                                   1))
            self.connect.commit()

    def get_movies(self):
        self.cursor.execute("select * from films;")
        self.connect.commit()
        for i in (self.cursor.fetchall()):
            print(i)


cinematica = Cinematica('https://cinematica.kg/api/v1/cinema/1/dates')
# cinematica.create_table()
# cinematica.save_cinema()
# cinematica.save_movies()
cinematica.get_movies()

