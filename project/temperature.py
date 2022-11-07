import time
from bme280 import BME280

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

import logging

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

logging.info("""weather.py - Print readings from the BME280 weather sensor.

Press Ctrl+C to exit!

""")

bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

count = 0
values = {

}


def add_value(temp, pres, hum):
    value = {
        "temperature": temp,
        "pressure": pres,
        "humidity": hum
    }
    values.append(value)


while True:
    temperature = bme280.get_temperature()
    pressure = bme280.get_pressure()
    humidity = bme280.get_humidity()
    add_value(temperature, pressure, humidity)
    print(values)
    time.sleep(1)