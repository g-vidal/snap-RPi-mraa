snap-RPi-mraa
=============

Project under development not functional!!!!!
Any help will be greatly appreciated!

Project forked from [pbrown66/snap-RPi](https://github.com/pbrown66/snap-RPi) project

## What is this

A set of blocks (currently only 2) and code which enables us to use the GPIOs on a Raspberry Pi from [Snap!BYOB](http://snap.berkeley.edu/) with [mraa INTEL IoT DevKit](https://github.com/intel-iot-devkit/mraa). RpiGPIO originally used has been exchanged with mraa to enable the use of all our [notebooks](https://github.com/g-vidal/CahierDeProgrammes) under snap!

## Bits

- The blocks (currently 2 'blocks') in RPiGPIO.xml. Blocks are located in Looks and Operators.

- The server the blocks connect to: RPiGPIO.py 

## How to install

Copy the server RPiGPIOmraa.py onto your Pi. Copy RPiGPIOmraa.xml onto your main computer.

## How to run

Run the python script from your Pi (from a user having GPIO acces rights see [comments on IFÉ-ENS de Lyon RaspberryPi image](http://blog.climatetmeteo.fr/GerardVidal/Pi3W_Stretch_install.html)). Access Snap! from the browser on your main computer. Import RPiGPIOmraa.xml file into Snap!.

You will have to change the IP address of the "RaspberryPi GPIO server" in the snap! blocks (right click + _Edit_) so it points to your Raspberry Pi on your network.

**Pin numbers are the position on the device nuombered from top -> bottom and left -> right (1 -> top left = 3.3V 40 -> bottim right =  GPIO 21). There are NOT THE GPIO numbers.**

## Caveat

You can run Snap! from a server on the Pi (nginx is installed by default ion the IFÉ-ENS image) or access the "RaspberryPi GPIO server" from a more powerful computer on your network. Or just from the snap! installed on your computer.

## Why does this exist?

Because Snap! is easy and intuitive to extend, which makes it ideal for educational purposes, i.e., you can use this to teach students how to meta-program, developing the language that they can then use to program the Rpi. This leads to many interesting possibilities.
