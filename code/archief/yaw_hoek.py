from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

Motor1 = Motor(Port.B)

Motor2 = Motor(Port.D)
def hoek(hoek):
    onder_hoek = hoek - 2
    boven_hoek = hoek + 2
    if hoek > 0:
        eind_hoek = hoek - 2
    elif hoek < 0:
        eind_hoek = hoek + 2 
    while True:
        hub.imu.restet_heading(0)
        huidige_hoek = hub.imu.heading(Z)
        eind_speed = huidige_hoek - eind_hoek
        while (onder_hoek < huidige_hoek) and (boven_hoek > huidige_hoek):
            Motor1.run(eind_speed)
        print(huidige_hoek)
hoek(90)