

import serial

def get_arduino_port():
    ports = serial.tools.list_ports.comports()
    print (ports)
    for port in ports:
        if "Arduino" in port.description or "USB-SERIAL CH340":
          print(f"Detected port: {port.device}")
          print(f"Name: {port.name}")
          print(f"Description: {port.description}")
          print(f"HWID: {port.hwid}")
          print(f"PID: {port.pid}")
          print(f"Serial Number: {port.serial}")
          print(f"Manufacturer: {port.manufacturer}")
          print(f"Product: {port.product}")
          print(f"Interfaces: {port.interfaces}")
          print(f"Locactions: {port.locactions}")

    return ports.device
print("No arduino port detected")


p=get_arduino_port()
print (p)

