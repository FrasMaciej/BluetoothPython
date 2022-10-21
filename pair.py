import bluetooth
import subprocess
nearby_devices = bluetooth.discover_devices(duration=4, lookup_names=True,
                                            flush_cache=True, lookup_class=False)

name = 'POCO'
addr = '58:20:59:1E:A1:A5'
port = 1
passkey = "1111"

try:
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.connect((addr, port))
except bluetooth.btcommon.BluetoothError as err:
    pass

print("Connected. Type something...")
while True:
    data = input()
    if not data:
        break
    s.send(data)
