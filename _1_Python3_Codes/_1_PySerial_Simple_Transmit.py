# Python code transmits a byte 'A' to Arduino /Microcontroller to Blink LED
# Requires PySerial

# (c) www.xanthium.in 2021
# Rahul.S


import serial
import time

SerialObj = serial.Serial('COM11') # COMxx   format on Windows

                                   
                                   #/dev/ttyUSBx format on Linux
                                   #
                                   #Eg /dev/ttyUSB0
                                   #SerialObj = serial.Serial('/dev/ttyUSB0')

SerialObj.baudrate = 9600  # set Baud rate to 9600
SerialObj.bytesize = 8     # Number of data bits = 8
SerialObj.parity   ='N'    # No parity
SerialObj.stopbits = 1     # Number of Stop bits = 1

time.sleep(3)   # Only needed for Arduino,For AVR/PIC/MSP430 & other Micros not needed
                # opening the serial port from Python will reset the Arduino.
                # Both Arduino and Python code are sharing Com11 here.
                # 3 second delay allows the Arduino to settle down.

BytesWritten = SerialObj.write(b'A')      #transmit 'A' (8bit) to micro/Arduino

print('BytesWritten = ', BytesWritten)

SerialObj.close()          # Close the port