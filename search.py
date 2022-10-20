import bluetooth, subprocess

print("looking for bluetooth devices .......... ")
nearby_devices = bluetooth.discover_devices(duration=5,lookup_names=True)

print("Found {} devices".format(len(nearby_devices)))
for addr, name in nearby_devices:
    print("----------------------------------------")
    print("address : ", addr)
    print("name : ", name)
print("----------------------------------------")
