#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep 

my_button = 11
my_led    = 12
my_counter= 0

my_led_state    = 0
my_button_state = 1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(my_led, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(my_button, GPIO.IN)

while my_counter < 6:
	if GPIO.input(my_button) == True and my_button_state == False:
		my_counter = my_counter + 1
		my_button_state = True

		if my_led_state == GPIO.LOW:
			GPIO.output(my_led, GPIO.HIGH)
			my_led_state = GPIO.HIGH
	
		elif my_led_state == GPIO.HIGH:
			GPIO.output(my_led, GPIO.LOW)
			my_led_state = GPIO.LOW

	elif GPIO.input(my_button) == False and my_button_state == True:
		my_button_state = False

GPIO.cleanup()

print(GPIO.RPI_REVISION)
print(GPIO.VERSION)

