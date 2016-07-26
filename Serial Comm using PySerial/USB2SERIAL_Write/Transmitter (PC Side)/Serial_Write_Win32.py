#----------------------------------------------------------------------------------------------------#
#Serial Communication using Python (Write) (Runs on Python 2.7 and 3.x) (Windows)                    #
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
# Commands         :  python Serial_Write_Win32.py                                                   #
# OS               :  Windows(Windows 7)                                                             #
# Programmer       :  Rahul.S                                                                        #
# Date	           :  20-January-2015                                                                #
#====================================================================================================#

#====================================================================================================#
# Sellecting the COM port Number                                                                     #
#----------------------------------------------------------------------------------------------------#
# Use "Device Manager" in Windows to find out the COM Port number allotted to USB2SERIAL converter-  # 
# -in your Computer                                                                                  #
#                                                                                                    #
# for eg:-                                                                                           #
# If your COM port number is COM32 in device manager(will change according to system)                #
# then                                                                                               #
#	ComPort = serial.Serial('COM32')                                                                 #
#====================================================================================================#
import serial                    # import the module 

ComPort = serial.Serial('COM24') # open COM24 

ComPort.baudrate = 9600          # set Baud rate 
ComPort.bytesize = 8             # Number of data bits = 8
ComPort.parity = 'N'             # No parity
ComPort.stopbits = 1             # Number of Stop bits = 1

#Write character 'A' to serial port                            
data = bytearray(b'A')           # Convert Character to byte array 
No = ComPort.write(data)         # Write data to serial port

ComPort.close()                  #Close the Serial port