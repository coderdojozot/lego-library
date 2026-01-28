from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Button
from pybricks.tools import wait

# Initialize the hub.
hub = PrimeHub(broadcast_channel=1)

pressed = []

while True:

    while not any(pressed):
        hub.ble.broadcast("stop")
        pressed = hub.buttons.pressed()
        wait(10)

    while any(hub.buttons.pressed()):
        wait(10)
    

    if Button.LEFT in pressed:
        hub.ble.broadcast("3vingers")
    