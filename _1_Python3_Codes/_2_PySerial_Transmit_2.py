# Python code transmits a byte to Arduino /Microcontroller


import serial
import time

SerialObj = serial.Serial('COM11') # COMxx   format on Windows
                                   # ttyUSBx format on Linux
                                   
#SerialObj = serial.Serial('COM11',9600)

print(SerialObj) #display default parameters

time.sleep(3)   # Only needed for Arduino,For AVR/PIC/MSP430 & other Micros not needed
                # opening the serial port from Python will reset the Arduino.
                # Both Arduino and Python code are sharing Com11 here.
                # 3 second delay allows the Arduino to settle down.

SerialObj.baudrate = 9600  # set Baud rate to 9600
SerialObj.bytesize = 8     # Number of data bits = 8
SerialObj.parity   ='N'    # No parity
SerialObj.stopbits = 1     # Number of Stop bits = 1

print(SerialObj)

BytesWritten = SerialObj.write(b'A')

text = 'H'
text = bytearray(text,'utf8')

SerialObj.write(text)

SerialObj.close()

