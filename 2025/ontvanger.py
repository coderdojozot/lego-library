from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Color, Port
from pybricks.tools import wait

# Initialize the hub.
hub = PrimeHub(observe_channels=[1])

drievingers = Motor(Port.D)
tweevingers = Motor(Port.B)

data = "wachten"


while True:

    data = hub.ble.observe(1)
    
    if data == "3vingers":
        start_positie3 = drievingers.angle()
        
        drievingers.run_until_stalled(500, duty_limit=70)
        print("Drie vingers gesloten")
        eind_positie3 = drievingers.angle()
        data = hub.ble.observe(1)
        if data == "0":
            print("start openen drie vingers")
            naar_start_positie3 = start_positie3 - eind_positie3
            drievingers.run_angle(500, naar_start_positie3)
            print("Drie vinges open")

    elif data == "2vingers":
        start_positie2 = tweevingers.angle()
        
        tweevingers.run_until_stalled(500, duty_limit=70)
        print("Twee vingers gesloten")
        eind_positie2 = tweevingers.angle()
        naar_start_positie2 = start_positie2 - eind_positie2
        tweevingers.run_angle(500, naar_start_positie2)
        data = hub.ble.observe(1)
        if data == "0":
            naar_start_positie2 = start_positie2 - eind_positie2
            tweevingers.run_angle(500, naar_start_positie2)
            print("Twee vingers open")
    wait(100)
