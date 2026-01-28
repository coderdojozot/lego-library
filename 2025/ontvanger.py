from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Color, Port
from pybricks.tools import wait

# Initialize the hub.
hub = PrimeHub(observe_channels=[1])

drievingers = Motor(Port.D)
tweevingers = Motor(Port.B)

data = "wachten"
angle_drie = 1100
angle_twee = 1000

while True:

    data = hub.ble.observe(1)
    
    if data == "3vingers":
        print("Drie vingers")
        drievingers.run_angle(500, angle_drie)
        print("Drie vingers open")
        wait(2000)
        drievingers.run_angle(500, -angle_drie)
        print("Drie vingers klaar")

    elif data == "2vingers":
        print("Twee vingers")
        
    else:
        drievingers.stop()
        tweevingers.stop()
        print("Wachten op input")
    wait(100)
