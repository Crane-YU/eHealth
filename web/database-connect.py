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
device = '/dev/tty.usbmodem1411'
cursor = connection.cursor()

try:
    print("Trying...", device)
    arduino = serial.Serial(device, 9600)

except:
    print("Failed to connect on", device)

try:
    # read the data from the arduino
    data = arduino.readline()
    # split the data by the tab
    pieces = data.split("\t")

    # Here we are going to insert the data into the Database
    try:
        cursor.execute("INSERT INTO weatherData (humidity,tempC) VALUES (%s,%s)", (pieces[0], pieces[1]))
        # commit the insert
        connection.commit()

    finally:
        # close just in case it failed
        connection.close()
except:
    # alter the failure
    print("Failed to get data from Arduino!")

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
