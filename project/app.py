#!/usr/bin/env python3
import numpy as np

import datetime

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

temperature = np.array([

])

time = np.array([

])

while count < 10:
    temperature = np.append(temperature, bme280.get_temperature())
    time = np.append(time, datetime.datetime.now())
    count += 1


print(temperature)
print(time)