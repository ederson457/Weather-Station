
# importmlibraries
import Serial
import time


#Arduino port
arduino_port = "COM11"
arduino_bau=9600

service=serial.Serial(
    
    arduino_port,
    arduino_bau,
    timeout=1
    
)

time.sleep(1) #Delay

while True:
    #data = service.readline.decode('utf-8').strip()
    data = service.readline.decode('utf-8').rstrip()
    
    
    if data:
        hum,temp = data.split(",")
        
        print(f"Temperature: {temperature}C")
        print(f"Humidity: {humidity}%")