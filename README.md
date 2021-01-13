# WiFi Reconnection-based Covert Channel Implementation

This repository contains the proof-of-concept code provided for the review process of the following paper:

S. Zillien, S. Wendzel: *Reconnection-based Covert Channels in Wireless Networks* (submitted to IFIP SEC 2021 in January 2021).

The full documentation will be made public in parallel to the camera-ready paper version in case of acceptance (for now, the details of the covert channels are only described in the submitted paper). The code was implemented by S. Zillien.

## Quick Start Guide

### Usage

#### Sender Method 1

Example call
``` 
./sender.py --msg HelloWorld --delay 0 --count 64 --wait 0.5 
```

All options can be shown with 
``` 
./sender.py -h
```

The wireless adaptor needs to be manually set into monitor mode and configured for the target channel.
The tool [airmon-ng](https://www.aircrack-ng.org/doku.php?id=airmon-ng) can be used to set these parameters.
The script expects the wireless adaptor to be called `wlan0mon`. An interface can be renamed with
```
ip link set <interface> name wlan0mon
```

#### Sender Method 2
Example call
``` 
./sender.py --msg HelloWorld --port /dev/ttyACM0 
```

The script expects an Arduino or similar microcontroller with our firmware, that is connected via a serial connection.

#### Receiver
The receiver does not have configuration parameters and can be started with the call.
``` 
./receiver.py
```

### Requirements
- Python 3
    - Scapy
    - more_itertools
    - pyserial

SenderMethod2 requires additional hardware to communicate between sender and clients. We used ESP32 boards as clients and an Arduino Leonardo to communicate with them.
