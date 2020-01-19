
import zmq
import datetime
import time
import random
import multisensor
import tempreader1

context = zmq.Context()
socket = context.socket(zmq.DEALER)
socket.connect("tcp://localhost:5556")

while True:
    ID = 1
    currentdatetime = datetime.datetime.now().strftime("%m-%d-%Y- %H:%M:%S")

    
    temp1 = tempreader1.read_temp()
    temp2 = multisensor.temp()
    
    
    humidity = multisensor.humidity()
    #socket.send_string("%i %s %i %i" % (ID, Time, temp, humidity))
    #time.sleep(1)
    print ("%i %s %i %i %i" % (ID, currentdatetime, temp1, temp2, humidity) + "%")
    print('sent')

