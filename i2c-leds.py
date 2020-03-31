#!/usr/bin/python
import smbus
import time

bus = smbus.SMBus(0)

DEVICE = 0x20 # Device address (A0-A2)
IODIRA = 0x00 # Pin direction register Bank A
IODIRB = 0x01 # Pin direction register Bank B
OLATA  = 0x14 # Register for outputs Bank A
OLATB  = 0x15 # Register for outputs Bank B
GPIOA  = 0x12 # Register for inputs Bank A
GPIOB  = 0x13 # Register for inputs Bank B

# Set all GPA pins as outputs
bus.write_byte_data(DEVICE,IODIRA,0x00)

# Set all GPB pins as outputs
bus.write_byte_data(DEVICE,IODIRB,0x00)

# Set output all 16 output bits to 0
bus.write_byte_data(DEVICE,OLATA,0)
bus.write_byte_data(DEVICE,OLATB,0)

while (1):
  for MyData in range (1,128):
    bus.write_byte_data(DEVICE,OLATA,MyData)
  #  print MyData 
    time.sleep (0.1)

  bus.write_byte_data(DEVICE,OLATA,0)

  for MyData in range (1,128):
    bus.write_byte_data(DEVICE,OLATB,MyData)
  #  print MyData
    time.sleep (0.1)

  bus.write_byte_data(DEVICE,OLATB,0)

  for MyData in range (1,128):
    bus.write_byte_data(DEVICE,OLATA,MyData)
    bus.write_byte_data(DEVICE,OLATB,MyData)
  #  print MyData
    time.sleep (0.1)

  for MyData in range (1,10):
    bus.write_byte_data(DEVICE,OLATA,0)
    bus.write_byte_data(DEVICE,OLATB,127)
    time.sleep(0.2)
    bus.write_byte_data(DEVICE,OLATA,127)
    bus.write_byte_data(DEVICE,OLATB,127)
    time.sleep(0.2)
    bus.write_byte_data(DEVICE,OLATA,127)
    bus.write_byte_data(DEVICE,OLATB,0)
    time.sleep(0.2)
  
  bus.write_byte_data(DEVICE,OLATA,0)
  bus.write_byte_data(DEVICE,OLATB,0)

