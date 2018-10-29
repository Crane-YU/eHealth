import serial

ser = serial.Serial('/dev/cu.usbmodem143201', 19200)  # Establish the connection on a specific port

while True:
    # read the data from the arduino
    data = ser.readline()

    # decode the byte type data to string
    data = data.decode("utf-8", "ignore")
    # print(data)

    # split the data by the tab
    pieces = data.split()
    # print(pieces)
    if len(pieces) == 2:
        if pieces[0] == "Diastolic:":
            print("1")
        if pieces[0] == "Systolic:":
            print("2")
        if pieces[0] == "Pulse/min:":
            print("3")
    # if pieces != []:
    #     data = pieces
    #     pulse = int(data[0][7:len(data[0])-3])
    #     print(pulse)
    #     spo2 = int(data[2][5:len(data[2])-1])
    #     print(spo2)

