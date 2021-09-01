# Arduino Nano/Uno HID (Simulated) with Python 
 Use your Arduino Nano or Uno like HID without HoodLoader2

## Connection in Arduino:
![Schematic](/Schematic.png "Schematic")
Used ports: 2,3,4,5,6,7,8,9,10


## Screenshot Running Interface:
![Screenshot](/Screenshot.PNG "Screenshot")

## Requirements
1. The interface was made with [***EasyGui*** ](http://easygui.sourceforge.net/) for [***Python***](https://www.python.org/).
2. Serial Communication between ***Arduino*** and ***Python*** by [PySerial](https://github.com/pyserial/pyserial)

## Installation
Not Required.

## How to use
You can find the Executables in [***Executables Folder***](https://github.com/jreygu/Arduino-Nano-HID-Simulated-with-Python/tree/main/Executables).

### Steps
1. Open ```interface.exe``` then you can set the serial port and define the folders or files you want open.
2. Press ```Cambiar``` to make the changes in the varibles.
3. Next, press in ```CrearArchivo``` to save variables file (In the folder you will see a txt called ```vars.txt```).
4. Then press ```Ejecutar``` to run ```run.exe```.
5. The ```Run.exe``` Process starts in the *task manager*, this communicates the arduino with your pc.
6. In ```interface.exe``` you can press ```Exit```, you dont need it to keep the ```Run.exe``` Running.
7. You have now a keyboard extension for custom hotkeys

## Notes
1. The first 8 buttons (Pins 2, 3, 4, 5, 6, 7, 8, 9) can be a hotkey.
2. The last button (Pin 10) **Stops the run.exe Process**.
3. You can open the ```run.exe``` file anytime, you dont need to reconfigurate your hotkeys.


# Enjoy 😄
