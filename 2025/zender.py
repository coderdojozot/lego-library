from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, ForceSensor
from pybricks.parameters import Port, Button
from pybricks.tools import wait

hub = PrimeHub(broadcast_channel=1)

button3vinger = ForceSensor(Port.C)
button2vingerA = ForceSensor(Port.A)
button2vingerE = ForceSensor(Port.E)

while True:

    if button3vinger.pressed() == True:
        hub.ble.broadcast("3vingers")
        print("3vingers verzonden")
        pass

    elif button3vinger.pressed() == False:
        hub.ble.broadcast("0")
        print("0 verzonden")
        pass

    elif button2vingerA.pressed() == True:
        hub.ble.broadcast("2vingers")
        print("2vingers verzonden")
        pass

    elif button2vingerA.pressed() == False:
        hub.ble.broadcast("0")
        print("0 verzonden")
        pass