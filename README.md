Pebble heart rate monitor
==

![](example.png)

The `index.py` server starts a basic websocket server that uses bleak to report the heart rate. It should work with anything that supports `00002a37-0000-1000-8000-00805f9b34fb` BLE heart rate char single byte type however it hasn't been tested.

`index.html` provides a basic webpage that will connect to the websocket and display the heart rate as number + graph suitable for OBS usage.

## Usage
1. Pair your device to your PC
1. Install Python 3, and do `pip3 install bleak websockets`
1. Update `index.py` to be the correct MAC address
1. Run `python3 index.py`
1. Also run `python3 -m http.server` in this folder to host the index.html
1. In OBS add a browser component for http://127.0.0.1:8000