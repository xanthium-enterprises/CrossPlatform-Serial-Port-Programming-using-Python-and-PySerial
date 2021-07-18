# Receives a string from Arduino using readline()
# Requires PySerial

# (c) www.xanthium.in 2021
# Rahul.S

import serial
import time

SerialObj = serial.Serial('COM11',9600) # COMxx   format on Windows
                                        # ttyUSBx format on Linux

time.sleep(3)   # Only needed for Arduino,For AVR/PIC/MSP430 & other Micros not needed
                # opening the serial port from Python will reset the Arduino.
                # Both Arduino and Python code are sharing Com11 here.
                # 3 second delay allows the Arduino to settle down.



ReceivedString = SerialObj.readline() #readline reads a string terminated by \n

print(ReceivedString)

SerialObj.close()          # Close the port