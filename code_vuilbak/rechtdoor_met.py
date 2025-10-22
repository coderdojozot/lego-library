####################################################################################
# Wordt deze versie nog gebruikt? dit is zonder gyro maar wel met een error correctie
# 
####################################################################################

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

Motor_d = Motor(Port.D, Direction.COUNTERCLOCKWISE)
Motor_c = Motor(Port.C)
drive_base = DriveBase(Motor_d, Motor_c, wheel_diameter=62.4, axle_track=60)
def rechtdoor(afstand):
    hub.imu.reset_heading(0)
    Motor_c.reset_angle()
    while Motor_c.angle() > afstand:
        error = hub.imu.heading()
        correction = error * -2
        move = 60 + correction
        drive_base.straight(move)
rechtdoor(1000)
