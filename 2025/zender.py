from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, ForceSensor
from pybricks.parameters import Port, Button
from pybricks.tools import wait

# Initialize the hub.
hub = PrimeHub(broadcast_channel=1)

pressed = []
button3vinger = ForceSensor(Port.C)
button2vinger = ForceSensor(Port.A) or ForceSensor(Port.E)



while True:
    if button3vinger.pressed() == True:
        hub.ble.broadcast("3vingers")
        print("3vingers verzonden")
    elif button3vinger.pressed() == False:
        hub.ble.broadcast("0")
    elif button2vinger.pressed() == True:
        hub.ble.broadcast("2vingers")
        print("2vingers verzonden")
    elif button2vinger.pressed() == False:
        hub.ble.broadcast("0")
    