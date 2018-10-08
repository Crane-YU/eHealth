from time import sleep
import serial

ser = serial.Serial('/dev/cu.usbmodem143201', 115200)  # Establish the connection on a specific port

while True:
    # read the data from the arduino
    data = ser.readline()

    # decode the byte type data to string
    data = data.decode("utf-8", "ignore")

    # split the data by the tab
    pieces = data.split()
    if pieces != []:
        data = pieces
        pulse = int(data[0][7:len(data[0])-3])
        print(pulse)
        spo2 = int(data[2][5:len(data[2])-1])
        print(spo2)

