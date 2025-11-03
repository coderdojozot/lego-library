from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from code_vuilbak.Xprobeersels.rijden_met_gyro_versie_lukas import draai_met_yaw, gyro_rechtdoor
hub = InventorHub()

motor_sensor = Motor(Port.B)
eyes = UltrasonicSensor(Port.C)
rijden = DriveBase(motor_links, motor_rechts, 55, 127)  
rijden.use_gyro(True)

sensor_kijken = 0
motor_sensor.reset_angle(0)
wachten = "nee"
welke_richting = "midden"
def kijken():
    if eyes.distance <= 60:
        wachten = "ja"
        rijden.stop()
        if welke_richting == "rechts":
            print('rechts')

            motor_sensor.run_angle(500, -180)
            if eyes.distance <= 60:
                motor_sensor.run_angle(500, 90)
                if eyes.distance <= 60:
                    hub.system.shutdown()

            else:
                wachten = "nee"
                

        if welke_richting == "links":
            print('links')
            motor_sensor.run_angle(500, 90)
            if eyes.distance <= 60:
                motor_sensor.run_angle(500, 90)
                if eyes.distance <= 60:
                    hub.system.shutdown()

            else:
                wachten = "nee"
                rijden.turn(90)
                rijden.drive(1000, 100)

        if welke_richting == "midden":
            print('midden')
            motor_sensor.run_angle(500, 90)
            if eyes.distance <= 60:
                motor_sensor.run_angle(500, -180)
                if eyes.distance <= 60:
                    hub.system.shutdown()

            else:
                wachten = "nee"
                rijden.turn(90)
                rijden.drive(1000, 100)

def rond_draaien():
    if wachten == "nee":
        welke_richting = "rechts"
        print('90')
        motor_sensor.run_angle(500, 90)
    if wachten == "nee":
        welke_richting = "links"
        print('-180')
        motor_sensor.run_angle(500, -180)
        
    if wachten == "nee":
        motor_sensor.run_angle(500, 90)
        welke_richting = "midden"

while True:
    rijden.drive(1000, 100)
    rond_draaien()
    kijken()