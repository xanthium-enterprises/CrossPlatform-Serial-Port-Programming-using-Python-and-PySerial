#!/bin/python3

# Simple script o open a serial port on Linux and display status
# www.xanthium.in
# Rahul.S

# Make script executable  using chmod +x command 

import serial

SerialPortName = input('\nEnter Port Name ->') # Enter Portname ttyUSBx /ttyACMx
SerialPortName = '/dev/' + SerialPortName       # create Full name by adding /dev/

SerialPortObj = serial.Serial(SerialPortName)   # open the port with default settings

print ('\nStatus -> ',SerialPortObj)            #display the status of the port

SerialPortObj.close()                           #close the port

print (f'\nSerial Port {SerialPortName} closed\n')