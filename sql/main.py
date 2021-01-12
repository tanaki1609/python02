import psycopg2


class DataBaseClub:
    def __init__(self):
        self.connect = psycopg2.connect(dbname='postgres',
                                        user='postgres',
                                        host='localhost',
                                        password='password')

        self.cursor = self.connect.cursor()

    def create_table(self):
        self.cursor.execute("create table if not exists club("
                            "id serial primary key, "
                            "name varchar(255));")
        self.connect.commit()

    def set_club_name(self, name):
        self.cursor.execute("insert into club(name) "
                            "values('%s');" % name)
        self.connect.commit()

    def get_all_clubs(self):
        self.cursor.execute("select * from club;")
        self.connect.commit()
        for i in (self.cursor.fetchall()):
            print(i)


data = DataBaseClub()
data.create_table()
name = input('Enter a club name: ')
data.set_club_name(name)
data.get_all_clubs()
