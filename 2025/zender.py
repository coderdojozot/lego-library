from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize the hub.
hub = PrimeHub(broadcast_channel=1)


bricht = "hallo"

hub.ble.broadcast(bricht)
print("hallo")