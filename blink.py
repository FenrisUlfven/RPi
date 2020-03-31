#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

my_button 	= 11
my_green_led	= 12
my_red_led	= 13


GPIO.setmode(GPIO.BOARD)

GPIO.setup(my_green_led, GPIO.OUT)
GPIO.setup(my_red_led, GPIO.OUT)
GPIO.setup(my_button, GPIO.IN)

while True:
	GPIO.output(my_green_led, GPIO.LOW)
	sleep(0.5)
	GPIO.output(my_green_led, GPIO.HIGH)
	sleep(0.5)
	if GPIO.input(my_button) == True:
		break
        GPIO.output(my_red_led, GPIO.LOW)
        sleep(0.5)
        GPIO.output(my_red_led, GPIO.HIGH)
        sleep(0.5)
        if GPIO.input(my_button) == True:
                break


GPIO.cleanup()

GPIO.RPI_REVISION
GPIO.VERSION

