'''
Dev: Ederson V.
Script description : Weather - Station DataBase
Engine: SQLite3
Data: 09-09-2024
'''

#Import database engine package
import sqlite3

#Create Weather-station database connection
con = sqlite3.connect('weather_station.db')

#Create cursor
#permite ejecutar las  operaciones cur
cur = con.cursor() 

#User model
users_model = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        role INTEGER NOT NULL DEFAULT 1,
        status BOOLEAN DEFAULT true,
        created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        update_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        deleted_at null
    )
'''

#test data model
test_data = '''
    CREATE TABLE IF NOT EXISTS test_data (
        id INTEGER PRIMARY KEY,
        temp INTEGER NOT NULL,
        hum INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )

'''

#Execute query
cur.execute(users_model)
cur.execute(test_data)

#Close connection
#con.close()
    



