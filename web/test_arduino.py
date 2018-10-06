from time import sleep
import serial

ser = serial.Serial('/dev/cu.usbmodem14611', 115200)  # Establish the connection on a specific port

while True:
    # read the data from the arduino
    data = ser.readline()

    # check the data type
    print(type(data))

    # check the raw data value
    print(data)

    # decode the byte type data to string
    # data = data.decode("utf-8", "ignore")

    # split the data by the tab
    # pieces = data.split("\t")
    # print(pieces)

