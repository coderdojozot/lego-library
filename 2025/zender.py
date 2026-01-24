from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Initialize the hub.
hub = PrimeHub(broadcast_channel=1)
sensor1 = ColorSensor(Port.D)

while True:
    if sensor1.color() == Color.BLUE:
        hub.light.on(Color.BLUE)
        hub.ble.broadcast("run")
    else:
        hub.light.off()
        hub.ble.broadcast("stop")

