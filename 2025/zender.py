from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, ForceSensor
from pybricks.parameters import Port, Button, Color
from pybricks.tools import wait

hub = PrimeHub(broadcast_channel=1)

button3vinger = ForceSensor(Port.C)
button2vingerA = ForceSensor(Port.A)
button2vingerE = ForceSensor(Port.E)

while True:

    if button3vinger.pressed() == True:
        wait(500)
        if button2vingerA.pressed() == True:
            hub.light.on(Color.GREEN)
            hub.ble.broadcast("2 en 3")
            print("2 en 3 verzonden")
            pass
        elif button2vingerE.pressed() == True:
            hub.light.on(Color.GREEN)
            hub.ble.broadcast("2 en 3")
            print("2 en 3 verzonden")
            pass
        else:
            hub.light.on(Color.GREEN)
            hub.ble.broadcast("3vingers")
            print("3vingers verzonden")
            pass

    if button2vingerA.pressed() == True:
        wait(500)
        if button3vinger.pressed() == True:
            hub.light.on(Color.GREEN)
            hub.ble.broadcast("2 en 3")
            print("2 en 3 verzonden")
            pass
        else:
            hub.light.on(Color.GREEN)
            hub.ble.broadcast("2vingers")
            print("2vingers verzonden")
            pass
    if button2vingerE.pressed() == True:
        wait(500)
        if button3vinger.pressed() == True:
            hub.light.on(Color.GREEN)
            hub.ble.broadcast("2 en 3")
            print("2 en 3 verzonden")
            pass
        else:
            hub.light.on(Color.GREEN)
            hub.ble.broadcast("2vingers")
            print("2vingers verzonden")
            pass

    if button2vingerE.pressed() == False or button3vinger.pressed() == False or button2vingerA.pressed() == False:
        hub.light.on(Color.RED)
        hub.ble.broadcast("0")
        print("0 verzonden")
        pass