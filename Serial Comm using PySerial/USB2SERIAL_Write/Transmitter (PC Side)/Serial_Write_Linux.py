# -*- coding: iso-8859-15 -*-
#----------------------------------------------------------------------------------------------------#
#Serial Communication using Python (Write) (Runs on Python 2.7 and 3.x) (Linux)                      #
#----------------------------------------------------------------------------------------------------#
#Program runs on the PC side and transmits a character to the Serial Port @9600bps .Program uses     #
#PySerial module to communicate with Serial Port                                                     #
#----------------------------------------------------------------------------------------------------# 
# BaudRate     -> 9600                                                                               #
# Data formt   -> 8 databits,No parity,1 Stop bit (8N1)                                              #
# Flow Control -> None                                                                               #
#----------------------------------------------------------------------------------------------------#

#====================================================================================================#
# www.xanthium.in										                                             #
# Copyright (C) 2015 Rahul.S                                                                         #
#====================================================================================================#

#====================================================================================================#
# Interpreter/IDE  :  Python (2.7/3.4.x) /IDLE     	                                                 #
# Module           :  PySerial                                                                       #
# Commands         :  sudo python Serial_Write_Linux.py                                              #
# OS               :  Linux                                                                          #
# Programmer       :  Rahul.S                                                                        #
# Date	           :  20-January-2015                                                                #
#====================================================================================================#

#====================================================================================================#
# Sellecting the COM port Number                                                                     #
#====================================================================================================#
# Find out the serial port number corresponding to your Computer                                     #
#                                                                                                    #
# You can use "dmesg | grep ttyS" to list the serial ports available in your PC.                     #
#    Hardware Serial ports are listed as ttyS* (eg ttyS1,ttyS2 etc)                                  #
#    USB to Serial Converters will be listed as ttyUSB*(eg ttyUSB0),or ttyACM*(ttyACM0) based on Chip#
#                                                                                                    #
# You can also connect your USB to Serial Converter to PC USB port and use "dmesg |tail" to find-    #
# -out the name of the USB to Serial Converter.                                                      #
#                                                                                                    #
# Use the name in the program like this                                                              #
#	ComPort = serial.Serial('/dev/ttyUSB0')                                                          #
#      or                                                                                            #
#   ComPort = serial.Serial('/dev/ttyACM0')                                                          #
#====================================================================================================#

import serial                           # import the module 

ComPort = serial.Serial('/dev/ttyUSB0') # open ttyUSB0 

ComPort.baudrate = 9600                 # set Baud rate 
ComPort.bytesize = 8                    # Number of data bits = 8
ComPort.parity = 'N'                    # No parity
ComPort.stopbits = 1                    # Number of Stop bits = 1

#Write character 'A' to serial port                            
data = bytearray(b'A')                  # Convert Character to byte array
No = ComPort.write(data)                # Write data to serial port

ComPort.close()                  #Close the Serial port
