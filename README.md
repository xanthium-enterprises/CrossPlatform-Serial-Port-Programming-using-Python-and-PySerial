# Cross Platform Serial programming using Python and PySerial

<img src ="http://xanthium.in/sites/default/files/site-images/serial-prog-python/cross-platform-serial-programming-python-tutorial.jpg"/>
-----------------------------------------------------------------------------------------------------------------------------------------

A short introduction into serial port programming using Python and PySerial Library on Windows and Linux Systems.
The Python code running on the x86 PC communicates with an microcontroller through serial link (TX,RX and Ground). 

<a href ="http://www.xanthium.in/Cross-Platform-serial-communication-using-Python-and-PySerial">Original tutorial can be found here </a>

- Runs on Both Linux and Windows
- supports both Python 2.7.x and Python 3.x.x Versions
- Microcontroller used is MSP430G2553 on Launchpad
- MSP430 Codes written in C and Compiled using IAR Embedded WorkBench

---------------------------------------------------------------------------------------------------------------------------------------

## Source Code Explanation

- **RTS&DTR Pin Control in Python** - Contains Code for Controlling RTS and DTR pins of SerialPort or that of a USB to Serial Converter

- **Serial Comm using PySerial** - Contains code for communicating (Transmission and Reception)with MSP430 from an x86 Linux or Windows PC.

   - **USB2SERIAL_Read** - PC reads a string send by MSP430 and displays it on the console Window.
   - **USB2SERIAL_Write** - PC transmits a character to MSP430 and MSP430 lights up an LED on receiving the character from PC.
  
-------------------------------------------------------------------------------------------------------------------------------------
## Circuit 

- <a href ="http://www.xanthium.in/Cross-Platform-serial-communication-using-Python-and-PySerial">Available  in the original Tutorial</a>

<img src ="http://xanthium.in/sites/default/files/site-images/serial-prog-linux/MSP430-Connected-to-USB2SERIAL_Marked.jpg"/>

-------------------------------------------------------------------------------------------------------------------------------------
## Hardware used 

- <img src="http://www.xanthium.in/sites/default/files/site-images/product-page/usb_to_rs485_converter_250px.jpg"/>
   - **USB to RS485/RS232/Serial Converter**
   - <a href = "http://xanthium.in/USB-to-Serial-RS232-RS485-Converter">Details can be found here </a>
   
- <img src="http://www.xanthium.in/sites/default/files/site-images/msp430-launchpad-tutorial-brief-intro/msp430-launchpad-tutorial-for-beginners.jpg"/>
 - **MSP430 Launchpad Development Board**
 - <a href = "http://www.xanthium.in/brief-introduction-msp430g2xxx-using-ti-launchpad-development-board">A short tutorial can be found here</a>
  
