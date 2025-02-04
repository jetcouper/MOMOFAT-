import sqlite3






# try:

# 	# Connect to DB and create a cursor
# 	cnt = sqlite3.connect('sql.db')
# 	cursor = cnt.cursor()
# 	print('DB Init')

# 	# Write a query and execute it with cursor
# 	query = 'select sqlite_version();'
# 	cursor.execute(query)

# 	# Fetch and output result
# 	result = cursor.fetchall()
# 	print('SQLite Version is {}'.format(result))



# 	# Close the cursor
# 	cursor.close()
 
 

# # Handle errors
# except sqlite3.Error as error:
# 	print('Error occurred - ', error)

# # Close DB Connection irrespective of success
# # or failure
# finally:

# 	if cnt:
# 		cnt.close()
# 		print('SQLite Connection closed')
  

cnt = sqlite3.connect('sql.db')

cnt.execute('''CREATE TABLE Profils( 
NAME TEXT, 
PIN INTEGER,
GAME_DATA_ID INTEGER);''')

cnt.close()