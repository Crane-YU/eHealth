import pymysql.cursors
import pymysql
import serial

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='YUke1030',
                             db='bank',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# This will have to be changed to the serial port you are using
device = serial.Serial('/dev/cu.usbmodem143201', 115200)
cursor = connection.cursor()
counter = 0

try:
    # print("Trying...", device)
    # Establish the connection on a specific port

    while counter < 10:

        # read the data from the arduino
        data = device.readline()

        # decode the byte type data to string
        data = data.decode("utf-8", "ignore")

        # split the data by the tab
        pieces = data.split()

        if pieces != []:
            data = pieces
            pulse = int(data[0][7:len(data[0]) - 3])
            print(pulse)
            spo2 = int(data[2][5:len(data[2]) - 1])
            print(spo2)

            # Here we are going to insert the data into the Database
            cursor.execute("INSERT INTO bpm_spo2Data (spo2,bpm) VALUES (%s,%s)", (str(spo2), str(pulse)))
            # commit the insert
            connection.commit()
            counter += 1

except:
    print("Fail to get data from Arduino")

finally:
    cursor.close()
    print("Done uploading to database")

# try:
#     # read the data from the arduino
#     data = arduino.readline()
#     # split the data by the tab
#     pieces = data.split("\t")
#     print(pieces)
#
#     # Here we are going to insert the data into the Database
#     try:
#         cursor.execute("INSERT INTO 'bpm_spo2Data' (spo2,bpm) VALUES (%d,%d)", (spo2, pulse))
#         # commit the insert
#         connection.commit()
#

# except:
#     # alter the failure
#     print("Failed to get data from Arduino!")

# try:
# #     with connection.cursor() as cursor:
# #         # Create a new record
# #         sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
# #         cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
# #
# #     # connection is not autocommit by default. So you must commit to save
# #     # your changes.
# #     connection.commit()
# #
# #     with connection.cursor() as cursor:
# #         # Read a single record
# #         sql = "SELECT id, name FROM user"
# #         cursor.execute(sql)
# #         result = cursor.fetchone()
# #         print(result)
# # finally:
# #     connection.close()
