#!/usr/bin/env python3

from __future__ import print_function
import time
import convert
import argparse
import serial

parser = argparse.ArgumentParser(description='Send a secret Message via reconnect Covert Channel - arudino puppeteer')
parser.add_argument('--msg', help='String to send')
parser.add_argument('--port', help='Serial Port to use')
parser.add_argument('--raw', action='store', default=3, type=int, help='Raw input to only disconnect one client')


args = parser.parse_args()

if args.msg:
    message = convert.string2ternary(args.msg)
elif args.raw is not None:
    message = [args.raw]
else:
    message = [0]

ser = serial.Serial(args.port, baudrate=115200)  
print("Using: " + ser.name)         
print("Baudrate: " + str(ser.baudrate))

packet = []
for i in message:
    if i == 0:
        packet.append(0x01)
    if i == 1:
        packet.append(0x02)
    if i == 2:
        packet.append(0x03)
ser.write(packet)
ser.close()
