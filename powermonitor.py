"""
Created: 2016.02.18

Last modified: 2016.08.23

@author: manu

This code is intended to communicate with an Arduino that has the .ino file named
'Power_Meter.ino'

This program listens for information being sent to it, by the Arduino via serial
and stores that information in 'file', which is a text file

"""

import serial
import time
import datetime
import os
import RPi.GPIO as GPIO

time.sleep(5)

## Use the GPIO board to turn LED on/off to show system status
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led = 47
GPIO.setup(led,GPIO.OUT)
GPIO.output(led, 1)


## Open serial port, ser = Arduino
ser = serial.Serial("/dev/ttyACM0", baudrate = 9600)
time.sleep(.5)

## open serial ports if closed
if(ser.isOpen() == False):
    ser.open()

## filefolder is the directory where the power usage data will be stored
filefolder = '/home/pi/Desktop/PowerData'

global file
## Specify Event Log output file
file = open('%s/EventLog.txt' % (filefolder), "a")

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H.%M.%S')

global fileP
## Specify Power Log output file
fileP = open('%s/%s - PowerLog.txt' % (filefolder, st), "a")

def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)
    return

def arduino_connect():
    connected = False;        ##(this is a logical statement to make connection
    while not connected:
        serin = ser.read()
        connected = True
        ts = time.time()
    	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        print >>file, st, " - Arduino Connected"
    return

## Connect to Arduino
arduino_connect()

## Give the connection 5 seconds to 'settle'
time.sleep(5)

GPIO.output(led,0)
time.sleep(1)
GPIO.output(led,1)
time.sleep(1)
GPIO.output(led,0)
time.sleep(1)
GPIO.output(led,1)
time.sleep(1)
GPIO.output(led,0)
time.sleep(1)
GPIO.output(led,1)
time.sleep
GPIO.output(led,0)
time.sleep(2)
ser.flushOutput()
ser.flushInput()

while 1:
    data = ser.read()
    #time.sleep(0.00001)
    if data:
        #GPIO.output(led,1)
        ts = time.time()
        dataRemain = ser.inWaiting()
        data += ser.read(dataRemain)
    	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        print >>fileP, st, data
        #GPIO.output(led,0)

