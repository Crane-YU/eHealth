import pymysql
import serial

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='YUke1030',
                             db='bank',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# This will set the serial port number
device = serial.Serial('/dev/cu.usbmodem143201', 19200)
cursor = connection.cursor()

try:
    # Establish the connection on a specific port
    print("Trying to connect...")

    while True:
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

except:
    print("Fail to get data from Arduino")

finally:
    cursor.close()
    print("Done uploading to database")
