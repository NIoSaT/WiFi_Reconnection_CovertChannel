#!/usr/bin/env python3

from scapy.all import Dot11, sniff, Dot11Auth, wireshark, Dot11AssoReq

from functools import partial

import convert

esp_1 = 'AB:CD:EF:AB:CD:EF'
esp_2 = 'AB:CD:EF:AB:CD:EF'
esp_3 = 'AB:CD:EF:AB:CD:EF'


class recvList:
    pktlist = []
    watchers = []

    def append(self,x):
        self.pktlist.append(x)
        print(x)
        if len(self.pktlist) % 3 ==0:
            print("len: "+str(len(self.pktlist)))
            self.notify()

    def addWatcher(self,x):
        self.watchers.append(x)

    def delWatcher(self,x):
        self.watchers.remove(x)

    def notify(self):
        for i in self.watchers:
            i(self.pktlist)


def PacketHandler(myList: recvList, packet) :
    if packet.haslayer(Dot11) :
        if packet.haslayer(Dot11AssoReq) :
            if packet.addr2.upper() == esp_1:
                myList.append(0)
            if packet.addr2.upper() == esp_2:
                mylist.append(1)
            if packet.addr2.upper() == esp_3:
                mylist.append(2)

def printer(x):
    pass
    print(convert.ternary2string(x))

mylist = recvList()
mylist.addWatcher(printer)

sniff(iface="wlan0mon", prn = partial(PacketHandler, mylist))

