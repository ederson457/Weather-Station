
'''
Script description:
Get temperature and humidity fron DHT11 since Arduino
Date: 07_10_2024
Developer: Ederson Valencia
'''

#Import libraries 
#Arduino port
import serial
import time
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

while True:
    #data = service.readline.decode('utf-8').strip()
    data = service.readline().decode('utf-8').rstrip() 
    
    if data:
        print(data)
        temperature, humidity =data.split(",")
        print(f"Temperature:{temperature}°C")
        print(f"humidity:{humidity}%")    
        
        
        #1. create a new model data called test_data
        #fields; id, temp, hum, created_at
        # 2. Create a method to insert data when detect changes in temp or hum
        # 3. Update method: insert data detect changes in temp or hum 
        
time.sleep(1)