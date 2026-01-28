from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Color, Port
from pybricks.tools import wait

# Initialize the hub.
hub = PrimeHub(observe_channels=[1])
drievingers = Motor(Port.D)
tweevingers = Motor(Port.B)
hub.light.on(Color.RED)
data = "0"
angle_drie = 100
angle_twee = 100
while True:
    data = hub.ble.observe(1)
    if data == "3vingers":
        drievingers.angle(angle_drie)
        drievingers.angle(-angel_drie)
    elif data == "2vingers":
        pass
    else:
        drievingers.stop()
        tweevingers.stop()
