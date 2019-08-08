#!/root/PycharmProjects/Suntest/venv/bin/python
import time
import zmq
import mysql.connector

context = zmq.Context()
socket = context.socket(zmq.ROUTER)
socket.bind("tcp://*:5556")

while True:
    #  Wait for next request from client
    message = socket.recv()
    try:
        message = message.decode('ascii')

        print("Received request: %s" % message)
        id, Time, Temp, Humidity = message.split()

        mydb = mysql.connector.connect(
            host="localhost",
            user="Delta",
            passwd="PASSWORD",
            database="mysql"
        )

        mycursor = mydb.cursor()

        mycursor.execute("UPDATE SunTest SET Time = %s, Humidity = %s, Temp = %s where ID = %s" % (Time, Humidity, Temp, id))
        mycursor.execute("Select* from SunTest")
        for tb in mycursor:
            print(tb)
        mydb.commit()
        mycursor.close()
        mydb.close()
    except:
        pass
