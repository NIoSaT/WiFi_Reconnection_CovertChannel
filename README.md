# WiFi Reconnection-based Covert Channel Implementation

We present two covert channels that communicate by triggering artificial reconnections of WiFi nodes. The code was implemented by S. Zillien.

This repository contains the proof-of-concept code for the following paper:

S. Zillien, S. Wendzel: *[Reconnection-based Covert Channels in Wireless Networks](https://link.springer.com/chapter/10.1007/978-3-030-78120-0_8)*, in Proc. 36th IFIP TC-11 International Information Security and Privacy Conference (*IFIP SEC 2021*), Springer, 2021.

You can send us a request via [ResearchGate](https://www.researchgate.net/publication/350877087_Reconnection-based_Covert_Channels_in_Wireless_Networks) or e-mail if you do not have access to the paper.


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
