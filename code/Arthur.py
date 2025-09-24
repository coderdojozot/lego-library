from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

#linker motor
left_motor = Motor(port=Port.E, positive_direction=Direction.COUNTERCLOCKWISE)
#rechter motor
right_motor = Motor(port=Port.D)
#wielbasis getal 1 is diameter van 1 wiel, getal 2 is de afstand van het midden van wiel 1 naar wiel 2, alles in mm
drive_base = DriveBase(left_motor, right_motor, 62.4, 80)
#hier zeg je dat hij de gyro moet gebruiken
drive_base.use_gyro(True)

#hij gaat 1000mm naar voor 
drive_base.straight(1000)