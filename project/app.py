#!/usr/bin/env python3
import numpy as np
import tensorflow as tf
from tensorflow import keras
import datetime

import time
from bme280 import BME280


def get_formatted_time():
    current_hour = int(current_time.strftime("%H"))
    current_minute = int(current_time.strftime("%M"))
    current_second = int(current_time.strftime("%S"))

    formatted_time = current_hour + current_minute / 60 + current_second / 3600

    return formatted_time


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

    time = np.append(time, get_formatted_time)
    count += 1


print(temperature)
print(time)

model = keras.Sequential([
    keras.layers.Dense(units=1, input_shape=[1])
])

model.compile(
    optimizer = 'sgd',
    loss = 'mean_squared_error'
)

model.fit(time, temperature, epochs=500)



prediction = model.predict([get_formatted_time])
actual = bme280.get_temperature()

 