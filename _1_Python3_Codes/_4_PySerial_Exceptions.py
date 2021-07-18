# Serial Port exceptions
# (c) www.xanthium.in

import serial

try:
    SerialObj = serial.Serial('COM17',9600) # open the Serial Port
    print('Port Details ->',SerialObj)      # display the properties of Serial Port
    
except serial.SerialException as var :
    print('An Exception Occured')
    print('Exception Details-> ', var)
    
else:
    print('Serial Port Opened')
    

