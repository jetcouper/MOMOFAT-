import sqlite3

def create_db():

	
	cnt = sqlite3.connect('sql.db')
	cursor = cnt.cursor()
	print('DB Init')
	
	query = 'select sqlite_version();'
	cursor.execute(query)
	
	result = cursor.fetchall()
	print('SQLite Version is {}'.format(result))
	
	cursor.close()


def create_table():
    cnt = sqlite3.connect('sql.db')
    cnt.execute('''CREATE TABLE Profils
             (NAME TEXT NOT NULL,
             PASSWORD INT NOT NULL,
             GAME_DATA_ID INT PRIMARY KEY NOT NULL);''')
    cnt.close()







def get_all_IDs():
    id_list = []
    cnt = sqlite3.connect('sql.db')
    cursor = cnt.execute('''SELECT GAME_DATA_ID FROM Profils''')
    for i in cursor:
        id_list.append(i[0])
    cnt.close()
    return id_list

def create_profil(name,password,id):
    cnt = sqlite3.connect('sql.db')
    cnt.execute('''INSERT INTO Profils VALUES (?, ?, ?)''', (name, password, id))
    cnt.commit()
    cnt.close()

def delete_profil(name):
    cnt = sqlite3.connect('sql.db')
    cnt.execute('''DELETE FROM Profils WHERE NAME = ?''', (name,))
    cnt.commit()
    cnt.close()

def delete_profil(id):
    cnt = sqlite3.connect('sql.db')
    cnt.execute('''DELETE FROM Profils WHERE GAME_DATA_ID = ?''', (id,))
    cnt.commit()
    cnt.close()

def get_profil(id):
    profil = []
    cnt = sqlite3.connect('sql.db')
    cursor = cnt.execute('''SELECT * FROM Profils WHERE GAME_DATA_ID = ?''', (id,))
    for i in cursor:
        profil.append(i)
    cnt.close()
    return profil

def get_all_profils():
    profils = []
    cnt = sqlite3.connect('sql.db')
    cursor = cnt.execute('''SELECT NAME FROM Profils''')
    for i in cursor:
        profils.append(i)
    cnt.close()
    return profils
    

def get_game_id_by_name(name):
    profil = []
    cnt = sqlite3.connect('sql.db')
    cursor = cnt.execute('''SELECT * FROM Profils WHERE NAME = ?''', (name,))
    for i in cursor:
        profil.append(i[2])
    cnt.close()
    return profil

#create_profil("Jacques",368168,45)
# for i in get_all_IDs():
#     if i == 45:
#         delete_profil(i)
# player = get_all_IDs()
# print(player)

