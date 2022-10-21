import bluetooth
import subprocess

print("looking for bluetooth devices .......... ")
nearby_devices = bluetooth.discover_devices(duration=10, lookup_names=True)

print("Znaleziono {} urzadzen".format(len(nearby_devices)))
for addr, name in nearby_devices:
    print("----------------------------------------")
    print("Adres : ", addr)
    print("Nazwa : ", name)
print("----------------------------------------")
