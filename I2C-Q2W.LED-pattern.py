#!/usr/bin/python
#################################################
#
# I2C LED-pattern version 0.1
# (c) 2013 Grey Wolf SoftWare, 
#     uffe.norberg(a)gmail(dot)com
#
# With a Quick2Wire i2c-board this software    
# make 14 LED's blink in different patterns and  
# toggle between the patterns  
# 
#
#################################################
import RPi.GPIO as GPIO
import smbus
import curses
from twisted.internet import task
from twisted.internet import reactor

# Configure -----------------------------------
my_screen   = curses.initscr ()
my_txt_win	= curses.newwin (4, 44, 15, 17)
my_win		= [curses.newwin (5, 11, 5, 17)]
my_win.append (curses.newwin (5, 11, 5, 28))
my_win.append (curses.newwin (5, 11, 5, 39))
my_win.append (curses.newwin (5, 11, 5, 50))
my_win.append (curses.newwin (5, 11, 10, 17))
my_win.append (curses.newwin (5, 11, 10, 28))
my_win.append (curses.newwin (5, 11, 10, 39))
my_win.append (curses.newwin (5, 11, 10, 50))

my_bus		= smbus.SMBus(0)
DEVICE = 0x20 # Device address (A0-A2)
IODIRA = 0x00 # Pin direction register Bank A
IODIRB = 0x01 # Pin direction register Bank B
OLATA  = 0x14 # Register for outputs Bank A
OLATB  = 0x15 # Register for outputs Bank B
GPIOA  = 0x12 # Register for inputs Bank A
GPIOB  = 0x13 # Register for inputs Bank B

my_led_array    = [1, 2, 4, 8, 16, 32, 64];
my_button       = 11
my_key		= 0
my_led		= 1

x0=x1=x2=x3	= 0
x4=x5=x6=x7	= 0
y0=y1=y2=y3	= 0
y4=y5=y6=y7	= 0
my_jump		= [0,3,1,4,2,5,3,6]


# Declare funktions ---------------------------
# LED Pattern 1
def runPattern1 ():
    global x0
    global y0
    my_win[0].addstr (2, (2+x0), '-')
    if my_led == 1:
        my_bus.write_byte_data(DEVICE,OLATA,my_led_array[x0])
    
    x0 += 1
    if x0 > 6 :
        x0 = 0

    my_win[0].addstr (2, (2+x0), '*')        
    my_win[0].refresh ()

# LED Pattern 2
def runPattern2 ():
    global x1
    global y1
    my_win[1].addstr(2, (2+y1), '-')    
    if my_led == 2:
        my_bus.write_byte_data(DEVICE,OLATA,my_led_array[y1])
    
    x1 += 1
    if x1 > 6 :
        x1 = 0
        
    y1 = 6 - x1
    my_win[1].addstr (2, (2+y1), '*')    
    my_win[1].refresh ()


# LED Pattern 3
def runPattern3 ():
    global x2
    global y2
    my_win[2].addstr(2, (2+x2), '-')
    if my_led == 3:
        my_bus.write_byte_data(DEVICE,OLATA,my_led_array[x2])
        
    if y2 == 0:
        x2 += 1	
        if x2 >= 6 :
            y2 = 1
            x2 = 6
    elif y2 == 1:
        x2 -= 1
        if x2 <= 0 :
            y2 = 0
            x2 = 0
    
    my_win[2].addstr (2, (2+x2), '*')
    my_win[2].refresh ()

    
# LED pattern 4
def runPattern4 ():
    global x3
    global y3
    my_win[3].addstr (2, (2+x3), '-')
    my_win[3].addstr (2, (2+(6-x3)), '-')
    if my_led == 4:
        my_bus.write_byte_data(DEVICE,OLATA,my_led_array[x3])
        my_bus.write_byte_data(DEVICE,OLATB,my_led_array[6-x3])
        
    if y3 == 0:
        x3 += 1	
        if x3 >= 6 :
            y3 = 1
            x3 = 6
    elif y3 == 1:
        x3 -= 1
        if x3 <= 0 :
            y3 = 0
            x3 = 0

    my_win[3].addstr (2, (2+x3), '*')
    my_win[3].addstr (2, (2+(6-x3)), '*')
    my_win[3].refresh ()


# LED pattern 5
def runPattern5 ():
    global x4
    global y4
    my_win[4].addstr (2, (2+x4), '-')
    my_win[4].addstr (2, (2+x4+1), '-')
    if my_led == 5:
        my_bus.write_byte_data(DEVICE,OLATA,my_led_array[x4])
        my_bus.write_byte_data(DEVICE,OLATB,my_led_array[x4+1])
        
    x4 += 1
    if x4 > 5 :
        x4 = 0
        
    my_win[4].addstr (2, (2+x4), '*')
    my_win[4].addstr (2, (2+x4+1), '*')
    my_win[4].refresh ()


# LED pattern 6
def runPattern6 ():
    global x5
    global y5
    my_win[5].addstr (2, (2+y5), '-')
    my_win[5].addstr (2, (2+y5+1), '-')
    if my_led == 6:
        my_bus.write_byte_data(DEVICE,OLATA,my_led_array[y5])
        my_bus.write_byte_data(DEVICE,OLATB,my_led_array[y5+1])
        
    x5 += 1
    if x5 > 5 :
        x5 = 0
        
    y5 = 5 - x5
    my_win[5].addstr (2, (2+y5), '*')
    my_win[5].addstr (2, (2+y5+1), '*')        
    my_win[5].refresh ()
    
    
# LED pattern 7
def runPattern7 ():
    global x6
    global y6
    my_win[6].addstr (2, (2+x6), '-')
    my_win[6].addstr (2, (2+x6+1), '-')
    if my_led == 7:
        my_bus.write_byte_data(DEVICE,OLATA,my_led_array[x6])
        my_bus.write_byte_data(DEVICE,OLATB,my_led_array[x6+1])
        
    if y6 == 0:
        x6 += 1	
        if x6 >= 5 :
            y6 = 1
            x6 = 5
    elif y6 == 1:
        x6 -= 1
        if x6 <= 0 :
            y6 = 0
            x6 = 0
            
    my_win[6].addstr (2, (2+x6), '*')
    my_win[6].addstr (2, (2+x6+1), '*')
    my_win[6].refresh ()


# LED pattern 8
def runPattern8 ():
    global x7
    global y7
    global my_jump
    my_win[7].addstr (2, (2+my_jump[x7]), '-')
    if my_led == 8:
        my_bus.write_byte_data(DEVICE,OLATA,my_led_array[my_jump[x7]])
        
    if y7 == 0:
        x7 += 1
        if x7 > 6 :
            y7 = 1
            x7 = 7
    elif y7 == 1:
        x7 -= 1
        if x7 < 1 :
            y7 = 0
            x7 = 0

    my_win[7].addstr (2, (2+my_jump[x7]), '*')
    my_win[7].refresh ()

    
# Key input funktion.
def	runKeyPress ():
    global my_key
    global my_led
    my_key = my_screen.getch()
    if (my_key <> -1) or (GPIO.input(my_button) == True):
        my_win[my_led-1].addstr (1, 1, str(my_led), curses.A_NORMAL)
        if GPIO.input(my_button) == True:
            my_led += 1
            if my_led > 8:
                my_led = 1
        elif my_key == 113:
            reactor.stop()
        elif my_key == 81:
            reactor.stop()
        elif my_key == 49:
            my_led = 1
        elif my_key == 50:
            my_led = 2
        elif my_key == 51:
            my_led = 3
        elif my_key == 52:
            my_led = 4
        elif my_key == 53:
            my_led = 5
        elif my_key == 54:
            my_led = 6
        elif my_key == 55:
            my_led = 7
        elif my_key == 56:
            my_led = 8
        
        my_bus.write_byte_data(DEVICE,OLATA,0)
        my_bus.write_byte_data(DEVICE,OLATB,0)
        
        my_win[my_led-1].addstr (1, 1, str(my_led), curses.A_REVERSE)



# Initiate interfaces -----------------

# Set all GPA and GPB pins as outputs
my_bus.write_byte_data(DEVICE,IODIRA,0x00)
my_bus.write_byte_data(DEVICE,IODIRB,0x00)

# Initiate GPIO for button input
GPIO.setmode (GPIO.BOARD)
GPIO.setup (my_button, GPIO.IN)

# Initiating UI
curses.curs_set (0)
curses.noecho ()
my_screen.nodelay (1)
my_screen.clear ()
my_screen.addstr (0, 0, 'I2C LED-pattern version 0.1')
my_screen.addstr (1, 0, '(c) 2013 Gray Wolf SoftWare')
my_screen.refresh ()
my_txt_win.border ()
my_txt_win.addstr (1, 2, 'Press number key to choose LED-pattern.')
my_txt_win.addstr (2, 14, 'Press Q to quit.')
my_txt_win.refresh ()
for n in range (0,8):	
	my_win[n].border ()
	my_win[n].addstr (1, 1, str(n+1))
	my_win[n].addstr (2, 2, '-------')
	my_win[n].refresh()

my_win[my_led-1].addstr (1, 1, str(my_led), curses.A_REVERSE)

# Initiate task loops -----------------
my_task1	= task.LoopingCall(runPattern1)
my_task1.start (0.1)

my_task2        = task.LoopingCall(runPattern2)
my_task2.start (0.1)

my_task3        = task.LoopingCall(runPattern3)
my_task3.start (0.1)

my_task4	= task.LoopingCall(runPattern4)
my_task4.start (0.1)

my_task5	= task.LoopingCall(runPattern5)
my_task5.start (0.11)

my_task6	= task.LoopingCall(runPattern6)
my_task6.start (0.11)

my_task7	= task.LoopingCall(runPattern7)
my_task7.start (0.11)

my_task8	= task.LoopingCall(runPattern8)
my_task8.start (0.15)

my_Key		= task.LoopingCall(runKeyPress)
my_Key.start (0.5)


# Start program loop
reactor.run()


# Clean up ------------------
GPIO.cleanup()
curses.endwin()
del my_win
del my_screen

