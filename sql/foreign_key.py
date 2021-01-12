import psycopg2
class DataBaseClub:
    def __init__(self):
        self.connect = psycopg2.connect(dbname='postgres',
                                        user='postgres',
                                        host='localhost',
                                        password='password')

        self.cursor = self.connect.cursor()

    def create_table(self):
        self.cursor.execute("create table if not exists clubs("
                            "id serial primary key, "
                            "name varchar(255));")
        self.connect.commit()
        self.cursor.execute("create table if not exists players("
                            "id serial primary key, "
                            "name varchar(255),"
                            "club_id int,"
                            "constraint fk_clubs foreign key(club_id)"
                            "references clubs(id));")
        self.connect.commit()

    def set_club_name(self, name):
        self.cursor.execute("insert into clubs(name) "
                            "values('%s');" % name)
        self.connect.commit()

    def get_all_clubs(self):
        self.cursor.execute("select * from clubs;")
        self.connect.commit()
        for i in (self.cursor.fetchall()):
            print(i)
    def set_player_name(self, name, club_id):
        self.cursor.execute("insert into players(name, club_id) "
                            "values('%s', %s);" % (name, club_id))
        self.connect.commit()

    def get_players(self):
        self.cursor.execute("select * from players;")
        self.connect.commit()
        for i in (self.cursor.fetchall()):
            print(i)


data = DataBaseClub()
data.create_table()
name = input('Enter a club name: ')
data.set_club_name(name)
data.get_all_clubs()
player = input('Enter a player name: ')
club_id = int(input('Enter a club id: '))
data.set_player_name(player, club_id)
data.get_players()
