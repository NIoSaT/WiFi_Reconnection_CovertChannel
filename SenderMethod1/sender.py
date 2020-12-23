#!/usr/bin/env python3

from __future__ import print_function
from scapy.all import ( Dot11,
                        Dot11Beacon,
                        Dot11Elt,
                        RadioTap,
                        sendp,
                        hexdump, RandMAC, randstring, Dot11Deauth, Dot11Disas)
import time
import convert
import argparse

parser = argparse.ArgumentParser(description='Send a secret Message via reconnect Covert Channel')
parser.add_argument('--disass', action='store_true', help='Use Disassosiation frames instead of Deauthentication frames(default: deauth)')
parser.add_argument('--count', action='store', type=int, default=64, help='Number of frames to send for a single reconnect attempt')
parser.add_argument('--wait', action='store', type=float, default=1.0, help='Number of seconds(float) to wait after a reconnect attempt')
parser.add_argument('--delay', action='store', type=float, default=0.0, help='Number of seconds(float) to wait after a complete letter has been sent')
parser.add_argument('--msg', help='String to send')
parser.add_argument('--raw', action='store', default=3, type=int, help='Raw input to only disconnect one client')
parser.add_argument('--silent', action='store_true', default=False, help='Turn off all output')


args = parser.parse_args()

iface = 'wlan0mon'   

AP = 'AB:CD:EF:AB:CD:EF'
AP_small = 'AB:CD:EF:AB:CD:EF'


esp_1 = 'AB:CD:EF:AB:CD:EF'
esp_2 = 'AB:CD:EF:AB:CD:EF'
esp_3 = 'AB:CD:EF:AB:CD:EF'

phone = 'AB:CD:EF:AB:CD:EF'
phone_2 = 'AB:CD:EF:AB:CD:EF'

broadcast = 'FF:FF:FF:FF:FF:FF'


if args.msg:
    message = convert.string2ternary(args.msg)
elif args.raw is not None:
    message = [args.raw]
else:
    message = [3]

oldnum = -1

for idx, i in enumerate(message):
    if oldnum == i:
        time.sleep((args.wait)*2)
    elif oldnum == -1:
        time.sleep(0)
    else:
        time.sleep(args.wait)

    if i == 0 :
        dot11 = Dot11(addr1=esp_1, addr2=AP_small, addr3=AP_small)
    if i == 1 :
        dot11 = Dot11(addr1=esp_2, addr2=AP_small, addr3=AP_small)
    if i == 2 :
        dot11 = Dot11(addr1=esp_3, addr2=AP_small, addr3=AP_small)
    if i == 3:
        dot11 = Dot11(addr1=phone_2, addr2=AP_small, addr3=AP_small)
    
    if args.disass:
        frame = RadioTap()/dot11/Dot11Disas(reason=7)
    else:
        frame = RadioTap()/dot11/Dot11Deauth(reason=7)

    if not args.silent:
        print(frame.summary())
    sendp(frame, iface=iface, count=args.count, realtime=True, verbose=(not args.silent))
    oldnum=i

    if idx % 3 == 0:
        time.sleep(args.delay)
