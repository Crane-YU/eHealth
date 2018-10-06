from time import sleep
import serial

ser = serial.Serial('/dev/cu.usbmodem14611', 115200)  # Establish the connection on a specific port

while True:
    # read the data from the arduino
    data = ser.readline()
    # split the data by the tab
    # pieces = data.split("\t")
    # check the data type
    print(type(data))
    # check the raw data value
    print(data)
