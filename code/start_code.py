from pybricks.hubs import Spikeprimehub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from rijden_met_gyro_versie_lukas.py import gyro_rechtdoor, draai_met_yaw

hub = Spikeprimehub()


gyro_rechtdoor(500, 500, 0)
print("klaar")