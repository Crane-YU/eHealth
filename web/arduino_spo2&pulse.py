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
device = serial.Serial('/dev/cu.usbmodem143201', 115200)
cursor = connection.cursor()
counter = 0

try:
    # Establish the connection on a specific port
    print("Trying to connect...")

    while counter < 10:
        # read the data from the arduino
        data = device.readline()

        # decode the byte type data to string
        data = data.decode("utf-8", "ignore")

        # split the data by the tab
        pieces = data.split()

        if pieces != []:
            data = pieces
            pulse = data[0][7:len(data[0]) - 3]
            print(pulse)
            spo2 = data[2][5:len(data[2]) - 1]
            print(spo2)

            # Here we are going to insert the data into the Database
            cursor.execute("INSERT INTO bpm_spo2Data (spo2,bpm) VALUES (%s,%s)", (spo2, pulse))
            # commit the insert
            connection.commit()
            counter += 1

except:
    print("Fail to get data from Arduino")

finally:
    cursor.close()
    print("Done uploading to database")