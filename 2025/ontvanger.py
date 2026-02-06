from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Color, Port
from pybricks.tools import wait, multitask, run_task

# Initialize the hub.
hub = PrimeHub(observe_channels=[1])

drievingers = Motor(Port.D)
tweevingers = Motor(Port.B)

data = "wachten"

start_positie2 = 0
start_positie3 = 0
eindpositie2 = 0
eindpositie3 = 0
naar_start_positie2 = 0
naar_start_positie3 = 0
async def close3():
    global start_positie2, start_positie3, eindpositie2, eindpositie3, naar_start_positie2, naar_start_positie3
    start_positie3 = drievingers.angle()
    eindpositie3 = await drievingers.run_until_stalled(1000, duty_limit=70)
    drievingers.stop()

async def close2():
    global start_positie2, start_positie3, eindpositie2, eindpositie3, naar_start_positie2, naar_start_positie3
    start_positie2 = tweevingers.angle()
    eindpositie2 = await tweevingers.run_until_stalled(1000, duty_limit=35)
    tweevingers.stop()

async def open3():
    global start_positie2, start_positie3, eindpositie2, eindpositie3, naar_start_positie2, naar_start_positie3
    naar_start_positie3 = start_positie3 - eindpositie3
    await drievingers.run_angle(1000, naar_start_positie3)
    drievingers.stop()

async def open2():
    global start_positie2, start_positie3, eindpositie2, eindpositie3, naar_start_positie2, naar_start_positie3
    naar_start_positie2 = start_positie2 - eindpositie2
    await tweevingers.run_angle(1000, naar_start_positie2)
    tweevingers.stop()

async def main():
    global start_positie2, start_positie3, eindpositie2, eindpositie3, naar_start_positie2, naar_start_positie3
    while True:

        data = hub.ble.observe(1)
        if data == "3vingers":
            
            start_positie3 = drievingers.angle()
            eindpositie3 = await drievingers.run_until_stalled(500, duty_limit=70)
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
                    await drievingers.run_angle(500, naar_start_positie3)
                    drievingers.brake()
                    print("Drie vingers open")
                    break
            
        data = hub.ble.observe(1)

        if data == "2vingers":
            start_positie2 = tweevingers.angle()
            eindpositie2 = await tweevingers.run_until_stalled(1000, duty_limit=35)
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
                    await tweevingers.run_angle(500, naar_start_positie2)
                    tweevingers.brake()
                    print("Twee vingers open")
                    break
        data = hub.ble.observe(1)
        
        if data == "2 en 3":
            print("start 2 en 3")
            start_positie3 = drievingers.angle()
            start_positie2 = tweevingers.angle()

            await multitask(close3(), close2())
            eindpositie3 = drievingers.angle()
            eindpositie2 = tweevingers.angle()
            print("Drie en twee vingers gesloten")
            data = hub.ble.observe(1)
            print('data ontvangen')
            print(data)
            while data != 0:
                data = hub.ble.observe(1)
                print("data: " + data)
                if data == "0":
                    print("onvangen 0")
                    data = hub.ble.observe(1)
                    drievingers.stop()
                    tweevingers.stop()
                    print("start openen drie en twee vingers")
                    await multitask(open3(),open2())
                    drievingers.brake()
                    tweevingers.brake()
                    print("Drie en twee vingers open")
                    break
run_task(main())