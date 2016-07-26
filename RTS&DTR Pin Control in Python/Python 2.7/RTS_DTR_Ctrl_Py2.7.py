# -*- coding: iso-8859-15 -*-
#----------------------------------------------------------------------------------------------------#
#Controlling the RTS & DTRpin of Serial Port (Runs on Python 2.7)                                    #
#----------------------------------------------------------------------------------------------------#
#Program uses the setRTS() function to set and clear the RTS pin                                     #
#Program uses PySerial module to communicate with Serial Port                                        #
#----------------------------------------------------------------------------------------------------# 

#====================================================================================================#
# www.xanthium.in										                                             #
# Copyright (C) 2015 Rahul.S                                                                         #
#====================================================================================================#

#====================================================================================================#
# Interpreter/IDE  :  Python 2.7 /IDLE     	                                                         #
# Module           :  PySerial                                                                       #
# Commands         :  python RTS_DTR_Ctrl_Win32.py                                                   #
# OS               :  NA                                                                             #
# Programmer       :  Rahul.S                                                                        #
# Date	           :  22-January-2015                                                                #
#====================================================================================================#



import serial                            # import pySerial module

print '  +--------------------------------------------------------------+'
print '  | Controlling the RTS and DTR pins of Serial Port using Python |'
print '  | Python 2.7                                                   |'
print '  +--------------------------------------------------------------+'

PortName = raw_input('    Enter the name of the Serial port -')#enter the COM port number
ComPort = serial.Serial(PortName)         # Open the COM Port

#========== RTS Pin Control =============#
raw_input('\n    Press Any Key to SET RTS ....')   # Wait for input,Press any key
ComPort.setRTS(1)                                  # Make RTS pin high 
raw_input('    Press Any Key to CLEAR RTS ....')   # Wait for input,Press any key
ComPort.setRTS(0)				                   # Make RTS pin low 

#========== DTR Pin Control =============#
raw_input('\n    Press Any Key to SET DTR....')    # Wait for input,Press any key
ComPort.setDTR(1)						           # Make DTR pin high
raw_input('    Press Any Key to CLEAR DTR....')    # Wait for input,Press any key
ComPort.setDTR(0)						           # Make DTR pin low

#======== DTR &RTS Pin Control ==========#
raw_input('\n    DTR = 1,RTS = 0,Press Any key')   # Wait for input,Press any key
ComPort.setDTR(1)                                  # DTR = 1
ComPort.setRTS(0)                                  # RTS = 0

raw_input('\n    DTR = 0,RTS = 1,Press Any key')   # Wait for input,Press any key
ComPort.setDTR(0)						           # DTR = 0
ComPort.setRTS(1)                                  # RTS = 1 

raw_input('\n    Press Any key to exit') 		     # Wait for input,Press any key
ComPort.close()                          # Close the COM Port