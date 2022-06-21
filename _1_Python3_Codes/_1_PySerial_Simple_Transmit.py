# Python code transmits a byte 'A' to Arduino /Microcontroller to Blink LED
# Requires PySerial

# (c) www.xanthium.in 2022
# Rahul.S

# https://www.xanthium.in/Cross-Platform-serial-communication-using-Python-and-PySerial


import serial
import time

SerialObj = serial.Serial('COM4') # COMxx   format on Windows

                                   
                                   #/dev/ttyUSBx format on Linux
                                   #
                                   #Eg /dev/ttyUSB0
                                   #SerialObj = serial.Serial('/dev/ttyUSB0')

SerialObj.baudrate = 9600  # set Baud rate to 9600
SerialObj.bytesize = 8     # Number of data bits = 8
SerialObj.parity   ='N'    # No parity
SerialObj.stopbits = 1     # Number of Stop bits = 1

#Another way to configure the Ports
#SerialObj.bytesize = serial.EIGHTBITS     # Number of data bits = 8
#SerialObj.bytesize = serial.SEVENBITS     # Number of data bits = 7

#SerialObj.parity   = serial.PARITY_NONE   # No parity
#SerialObj.parity   = serial.PARITY_EVEN   # Parity Even

#SerialObj.stopbits = serial.STOPBITS_ONE  # Number of Stop bits = 1


time.sleep(3)   # Only needed for Arduino,For AVR/PIC/MSP430 & other Micros not needed
                # opening the serial port from Python will reset the Arduino.
                # Both Arduino and Python code are sharing Com11 here.
                # 3 second delay allows the Arduino to settle down.

BytesWritten = SerialObj.write(b'A')      # transmit 'A' (8bit) to micro/Arduino
                                          # Declare A as a Byte (b'A')

print('BytesWritten = ', BytesWritten)

SerialObj.close()          # Close the port



