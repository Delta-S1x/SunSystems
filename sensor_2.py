#!/root/PycharmProjects/Suntest/venv/bin/python
import zmq
import datetime
import time
import random
#!/root/PycharmProjects/Suntest/venv/bin/
context = zmq.Context()
socket = context.socket(zmq.DEALER)
socket.connect("tcp://localhost:5556")
while True:
    ID = 2
    currentdatetime = datetime.datetime.now()
    hour = currentdatetime.hour
    minute = currentdatetime.minute
    second = currentdatetime.second
    Time = str(second)
    temp = random.randrange(1,100)
    humidity = random.randrange(30,100)
    socket.send_string("%i %s %i %i" % (ID, Time, temp, humidity))
    time.sleep(.5)
    print('sent')

