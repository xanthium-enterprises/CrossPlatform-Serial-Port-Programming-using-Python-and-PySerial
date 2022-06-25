# Serial Port exceptions
# (c) www.xanthium.in

import serial

try:
    SerialObj = serial.Serial('COM4',9600) # open the Serial Port
                                            # /dev/ttyUSBx format on Linux
                                            #
                                            # Eg /dev/ttyUSB0
                                            # SerialObj = serial.Serial('/dev/ttyUSB0')
    print('Port Details ->',SerialObj)      # display the properties of Serial Port
    SerialObj.close()
    
except serial.SerialException as var :
    print('An Exception Occured')
    print('Exception Details-> ', var)
    
else:
    print('Serial Port Opened')
    


