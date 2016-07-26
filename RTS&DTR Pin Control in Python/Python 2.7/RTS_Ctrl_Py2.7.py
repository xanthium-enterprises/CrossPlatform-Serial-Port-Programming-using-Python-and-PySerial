#----------------------------------------------------------------------------------------------------#
#Controlling the RTS pin of Serial Port (Runs on Python 2.7)                                         #
#----------------------------------------------------------------------------------------------------#
#Program uses the setRTS() function to set and clear the RTS pin                                     #
#Program uses PySerial module to communicate with Serial Port                                        #
#----------------------------------------------------------------------------------------------------# 

#====================================================================================================#
# www.xanthium.in										                                             #
# Copyright (C) 2015 Rahul.S                                                                         #
#====================================================================================================#

#====================================================================================================#
# Interpreter/IDE  :  Python (2.7) /IDLE     	                                                     #
# Module           :  PySerial                                                                       #
# Commands         :  python RTS_Ctrl_Win32.py                                                       #
# OS               :  NA                                                             #
# Programmer       :  Rahul.S                                                                        #
# Date	           :  22-January-2015                                                                #
#====================================================================================================#



import serial                    # import pySerial module

print '  +-----------------------------------------------------+' 
print '  | Controlling the RTS pin of Serial Port using Python |'
print '  | Python 2.7                                          |'
print '  +-----------------------------------------------------+'

PortName = raw_input('    Enter the name of the Serial port -')#enter the COM port number

ComPort = serial.Serial(PortName)                          # open the COM Port
raw_input('\n    Press any key to CLEAR RTS = 0.~RTS = 1') # wait for input,Press any key
ComPort.setRTS(0)                                          # Make RTS pin low ,~RTS = 1(inverted)
raw_input('\n    Press any key to CLEAR RTS = 1.~RTS = 0') # wait for input,Press any key
ComPort.setRTS(1)				                           # Make RTS pin high ~RTS = 0(inverted)
raw_input('\n    Press any key to exit')				   # wait for input,Press any key
ComPort.close()                                            # Close the COM Port