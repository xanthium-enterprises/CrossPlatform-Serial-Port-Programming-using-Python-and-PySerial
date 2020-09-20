# Cross Platform Serial programming using Python and PySerial

<img src ="http://xanthium.in/sites/default/files/site-images/serial-prog-python/cross-platform-serial-programming-python-tutorial.jpg"/>

-----------------------------------------------------------------------------------------------------------------------------------------

A short introduction into serial port programming using Python and PySerial Library on **Windows** and **Linux** Systems.

The Python code running on the **x86/x64** PC communicates with an microcontroller through serial link (TX,RX and Ground). 

- Runs on Both Linux and Windows
- supports both Python 2.7.x and Python 3.x.x Versions
- Microcontroller used is MSP430G2553 on Launchpad
- MSP430 Codes written in C and Compiled using IAR Embedded WorkBench

---------------------------------------------------------------------------------------------------------------------------------------

## Online Tutorial

- [Python Serial Communication program for embedded development using PySerial library](https://www.xanthium.in/Cross-Platform-serial-communication-using-Python-and-PySerial)

---------------------------------------------------------------------------------------------------------------------------------------

## Source Code Explanation

- **RTS&DTR Pin Control in Python** - Contains Code for Controlling RTS and DTR pins of SerialPort or that of a USB to Serial Converter

- **Serial Comm using PySerial** - Contains code for communicating (Transmission and Reception)with MSP430 from an x86/x64 Linux or Windows PC.

   - **USB2SERIAL_Read** - PC reads a string send by MSP430 and displays it on the console Window.
   - **USB2SERIAL_Write** - PC transmits a character to MSP430 and MSP430 lights up an LED on receiving the character from PC.
  
-------------------------------------------------------------------------------------------------------------------------------------

## Circuit 

- <a href ="http://www.xanthium.in/Cross-Platform-serial-communication-using-Python-and-PySerial">Available  in the original Tutorial</a>

-------------------------------------------------------------------------------------------------------------------------------------

## Hardware used 


- [USB to Serial/RS485 Converter](https://www.xanthium.in/ft232-based-usb-to-serial-rs485-converter-industrial-scientific-applications)
  
