#!/usr/bin/python
import RPi.GPIO as GPIO
import curses
from time import sleep

# Configure --------------------
my_button	= 11
my_led_array	= [12, 13, 15, 16, 18, 22, 7];
my_counter	= 0
my_screen	= curses.initscr ()
my_yx		= my_screen.getmaxyx ()

# Initiate ---------------------
GPIO.setmode (GPIO.BOARD)

GPIO.setup (my_button, GPIO.IN)
for n in my_led_array:
	GPIO.setup (n, GPIO.OUT)

curses.curs_set (0)
my_screen.nodelay (1)
my_screen.clear ()

# Run loop ------------------
while True:
	for x in range (0,6):
		y = 6 - x
		GPIO.output (my_led_array[x], GPIO.HIGH)
                GPIO.output (my_led_array[y], GPIO.HIGH)
		my_screen.addstr ((my_yx[0]/2-1), (my_yx[1]/2-4+x), '*')
		my_screen.addstr ((my_yx[0]/2-1), (my_yx[1]/2-4+y), '*')
		my_screen.refresh()
		sleep (0.1)
		GPIO.output (my_led_array[x], GPIO.LOW)
                GPIO.output (my_led_array[y], GPIO.LOW)
                my_screen.addstr ((my_yx[0]/2-1), (my_yx[1]/2-4+x), '-')
                my_screen.addstr ((my_yx[0]/2-1), (my_yx[1]/2-4+y), '-')
		my_screen.refresh()

	
	if my_screen.getch() <> -1:
		break
        if GPIO.input(my_button) == True:
               	break

# Clean up ------------------
GPIO.cleanup()
curses.endwin()
del my_screen

print "Raspberry Pi version: ", GPIO.RPI_REVISION
print "GPIO library version: ", GPIO.VERSION

