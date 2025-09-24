from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from rijden_met_gyro_versie_lukas import gyro_rechtdoor
hub = PrimeHub


gyro_rechtdoor(500, 1000)
