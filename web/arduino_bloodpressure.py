import pymysql
import serial

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='YUke1030',
                             db='bank',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# This will have to be changed to the serial port
device = serial.Serial('/dev/cu.usbmodem143201', 19200)
cursor = connection.cursor()

try:
    print("Trying to connect...")
    # Establish the connection on a specific port

    while True:
        print("Reading data ...")
        # read the data from the arduino
        data = device.readline()

        # decode the byte type data to string
        data = data.decode("utf-8", "ignore")

        # split the data by the tab
        pieces = data.split()

        if len(pieces) == 2:
            if pieces[0] == "Diastolic:":
                cursor.execute("INSERT INTO bloodpressure_signal (diastolic) VALUES (%s)", (pieces[1]))
                connection.commit()
            if pieces[0] == "Systolic:":
                cursor.execute("INSERT INTO bloodpressure_signal (systolic) VALUES (%s)", (pieces[1]))
                connection.commit()
            # if pieces[0] == "Pulse/min:":
            #     print("3")

        # if pieces != []:
        #     data = pieces
        #     systolic = data[0][7:len(data[0]) - 3]
        #     print(systolic)
        #     diastolic = data[2][5:len(data[2]) - 1]
        #     print(diastolic)
        #
        #     # Here we are going to insert the data into the Database
        #     cursor.execute("INSERT INTO bloodpressure_signal (diastolic,systolic) VALUES (%s,%s)", (diastolic, systolic))
        #
        #     # commit the insert
        #     connection.commit()
        #     counter += 1

except:
    print("Fail to get data from Arduino")

finally:
    cursor.close()
    print("Done uploading to database")
