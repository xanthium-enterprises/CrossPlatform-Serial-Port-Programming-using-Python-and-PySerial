# RTS Blinking
# Requires PySerial

# (c) www.xanthium.in 2021
# Rahul.S

import serial
import time

HIGH = 1
LOW  = 0

SerialObj = serial.Serial('COM6',9600)  # COMxx   format on Windows
                                        # ttyUSBx format on Linux

while 1 :
    SerialObj.rts = HIGH  #Make RTS High
    time.sleep(1)
    SerialObj.rts = LOW   #Make RTS LOW
    time.sleep(1)
    
    
    
