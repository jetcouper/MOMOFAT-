import sqlite3

cnt = sqlite3.connect('sql.db')


def get_ID():
    cursor = cnt.execute('''SELECT GAME_DATA_ID FROM Profils''')
    for i in cursor:
        print(str(i[0]))

def create_profil(name,password,id):

    cnt.execute('''INSERT INTO Profils VALUES (?, ?, ?)''', (name, password, id))
    cnt.commit()

#get_ID()  

create_profil("Jacques",368168,45)

cnt.close()