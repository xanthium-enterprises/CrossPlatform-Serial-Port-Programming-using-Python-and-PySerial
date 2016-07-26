#----------------------------------------------------------------------------------------------------#
#Controlling the RTS pin of Serial Port (Runs on Python 3.0) (Windows)                               #
#----------------------------------------------------------------------------------------------------#
#Program uses the setRTS() function to set and clear the RTS pin                                     #
#Program uses PySerial module to communicate with Serial Port                                        #
#----------------------------------------------------------------------------------------------------# 

#====================================================================================================#
# www.xanthium.in										                                             #
# Copyright (C) 2015 Rahul.S                                                                         #
#====================================================================================================#

#====================================================================================================#
# Interpreter/IDE  :  Python (3.4.x) /IDLE     	                                                     #
# Module           :  PySerial                                                                       #
# Commands         :  python RTS_Ctrl_Win32.py                                                       #
# OS               :  Windows(Windows 7)                                                             #
# Programmer       :  Rahul.S                                                                        #
# Date	           :  22-January-2015                                                                #
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

import serial                    # import pySerial module

print('  +-----------------------------------------------------+')
print('  | Controlling the RTS pin of Serial Port using Python |')
print('  | Python 3.0                                          |')
print('  +-----------------------------------------------------+')

PortName = input('    Enter the name of the Serial port -')#enter the COM port number

ComPort = serial.Serial(PortName)                      # open the COM Port
input('\n    Press any key to CLEAR RTS = 0.~RTS = 1') # wait for input,Press any key
ComPort.setRTS(0)                                      # Make RTS pin low ,~RTS = 1(inverted)
input('\n    Press any key to CLEAR RTS = 1.~RTS = 0') # wait for input,Press any key
ComPort.setRTS(1)				                       # Make RTS pin high 
input('\n    Press any key to exit')				   # wait for input,Press any key
ComPort.close()                                        # Close the COM Port