'''
Dev: Joan C.
Script description: wather-station DataBase
Engine: SQLite3
Data: 09-09-2024
'''

#Import engine database package
import sqlite3

#Create weather-station database connection
con = sqlite3.connect('weather_station.db')

#create.cursor()
cur = con.cursor()

#Users model
user_model = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY ,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        email TEXT NOT NULL,
        role TEXT NOT NULL,
        status boolean default True,
        created_at TIMESTAMP DEFAULT(datetime('now','localtime')),
        updated_at TIMESTAMP DEFAULT(datetime('now','localtime')),
        deleted_at null 
    );
    
    '''

#execute query
cur.execute(user_model)

#close database connection
con.close()




