# Created by: Daria Bernice Calitis
# Created on: Feb 2022
# This program is called Blinky and a Button

""" Example for Pico. Turns on the built-in LED."""

import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True

while True:
    led.value = not led.value
    time.sleep(0.5)
