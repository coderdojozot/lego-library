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
        eindpositie3 = drievingers.run_until_stalled(500, duty_limit=70)
        drievingers.stop()
        print("Drie vingers gesloten")
        data = hub.ble.observe(1)
        print('data ontvangen')
        print(data)
        while data != 0:
            data = hub.ble.observe(1)
            print("wachten op 0")
            print(data)
            if data == "0":
                print("onvangen 0")
                data = hub.ble.observe(1)
                drievingers.stop()
                print("start openen drie vingers")
                naar_start_positie3 = start_positie3 - eindpositie3
                print(naar_start_positie3)
                drievingers.run_angle(500, naar_start_positie3)
                drievingers.brake()
                print("Drie vingers open")
                break
        

    elif data == "2vingers":
        start_positie2 = tweevingers.angle()
        eindpositie2 = tweevingers.run_until_stalled(1000, duty_limit=28)
        tweevingers.stop()
        print("Twee vingers gesloten")
        data = hub.ble.observe(1)
        print('data ontvangen')
        print(data)
        while data != 0:
            data = hub.ble.observe(1)
            print("wachten op 0")
            print(data)
            if data == "0":
                print("onvangen 0")
                data = hub.ble.observe(1)
                tweevingers.stop()
                print("start openen twee vingers")
                naar_start_positie2 = start_positie2 - eindpositie2
                print(naar_start_positie2)
                tweevingers.run_angle(500, naar_start_positie2)
                tweevingers.brake()
                print("Twee vingers open")
                break
    elif data == "2 en 3":
        start_positie3 = drievingers.angle()
        start_positie2 = tweevingers.angle()
        eindpositie3 = drievingers.run_until_stalled(500, duty_limit=70)
        eindpositie2 = tweevingers.run_until_stalled(1000, duty_limit=28)
        drievingers.stop()
        tweevingers.stop()
        print("Drie en twee vingers gesloten")
        data = hub.ble.observe(1)
        print('data ontvangen')
        print(data)
        while data != 0:
            data = hub.ble.observe(1)
            print("wachten op 0")
            print(data)
            if data == "0":
                print("onvangen 0")
                data = hub.ble.observe(1)
                drievingers.stop()
                tweevingers.stop()
                print("start openen drie en twee vingers")
                naar_start_positie3 = start_positie3 - eindpositie3
                naar_start_positie2 = start_positie2 - eindpositie2
                print(naar_start_positie3)
                print(naar_start_positie2)
                drievingers.run_angle(500, naar_start_positie3)
                tweevingers.run_angle(500, naar_start_positie2)
                drievingers.brake()
                tweevingers.brake()
                print("Drie en twee vingers open")
                break
