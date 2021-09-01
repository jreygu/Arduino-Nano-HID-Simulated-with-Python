import serial, os 



with open("vars.txt", "r") as tf:
    lines = tf.read()

var = lines.split(',')

input = '' 
serialPort = serial.Serial(port = var[0] , baudrate=115200) 
while(1):
    input = serialPort.read()
    if(input == b'a'): 
        path = var[1]
        path = os.path.realpath(path)
        os.startfile(path)
    if(input == b'b'): #Button 2
        path = var[2]
        path = os.path.realpath(path)
        os.startfile(path)
    if(input == b'c'): #Button 3
        path = var[3]
        path = os.path.realpath(path)
        os.startfile(path) 
    if(input == b'd'): #Button 4
        path = var[4]
        path = os.path.realpath(path)
        os.startfile(path)
    if(input == b'e'): #Button 5
        path = var[5]
        path = os.path.realpath(path)
        os.startfile(path)
    if(input == b'f'): #Button 6
        path = var[6]
        path = os.path.realpath(path)
        os.startfile(path)
    if(input == b'g'): #Button 7
        path = var[7]
        path = os.path.realpath(path)
        os.startfile(path)
    if(input == b'h'): #Button 8
        path = var[8]
        path = os.path.realpath(path)
        os.startfile(path)
    if(input == b'i'): #Button 9
        break
