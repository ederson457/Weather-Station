
'''
Script description:
Get temperature and humidity fron DHT11 since Arduino
Date: 07_10_2024
Developer: Ederson Valencia
'''

#Import libraries 
#Arduino port
import os
from sqlite3 import Timestamp
import serial
import time
from database import con
import serial.tools.list_ports # type: ignore
from detect_arduino_port import p

arduino_port = p
arduino_bau = 9600

service = serial.Serial(
    arduino_port,
    arduino_bau,
    timeout = 1
)

time.sleep(1) #delaty

ports = serial.tools.list_ports.comports()
na=ports.serial

def data_():
    os.system('clear')
    
    ide = (00000)
    temp = (00000)
    hum = (00000)
    created_at = Timestamp
    
    new_user_query = f'''
        INSERT INTO test_data (username, email, password)
            VALUES ('{ide}','{temp}','{hum}','{created_at}')
    '''
    con.execute(new_user_query)
    con.commit()

    #print('User created succesfully.')
    con.close()


while True:
    #data = service.readline.decode('utf-8').strip()
    data = service.readline().decode('utf-8').rstrip() 
    
    if data:
        print(data)
        temperature, humidity =data.split(",")
        print(f"Temperature:{temperature}°C")
        print(f"humidity:{humidity}%")    
        data_()
        cre=Timestamp
        new_user_query = f'''
        UPDATE test_data
        SET temp = '{temperature}', hum = '{humidity}', created_at = '{cre}'
        WHERE ide = '{na}'
        '''

        con.execute(new_user_query)
        con.commit()
        con.close()



    #print('User created succesfully.'

        #1. create a new model data called test_data
        #fields; id, temp, hum, created_at
        # 2. Create a method to insert data when detect changes in temp or hum
        # 3. Update method: insert data detect changes in temp or hum  
    time.sleep(1)

