from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Color, Port
from pybricks.tools import wait

# Initialize the hub.
hub = PrimeHub(observe_channels=[1])
Motor = Motor(Port.D)
hub.light.on(Color.RED)
data = "0"
while True:
    data = hub.ble.observe(1)
    if data == "run":
        hub.light.on(Color.GREEN)

        Motor.run(1000)
    elif data == "stop":
        hub.light.on(Color.RED)

        Motor.stop()
