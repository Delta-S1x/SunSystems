import Adafruit_DHT
sensor = Adafruit_DHT.AM2302
pin = 24

def temp():
    humidity, temp = Adafruit_DHT.read_retry(sensor, pin)
    temp = round(temp,2)
    temp = (temp * 9/5) + 32
    return temp


def humidity():
    h, temp = Adafruit_DHT.read_retry(sensor, pin)
    h = round(h,2)
    return h
