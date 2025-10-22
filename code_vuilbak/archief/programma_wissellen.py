from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
start_stop = 0
pressed = []
while not any(pressed):
    pressed = hub.buttons.pressed()

while any(hub.buttons.pressed()):

if Button.LEFT in pressed:
    programma = programma + 1
elif Button.RIGHT in pressed:
    programma = programma - 1
elif Button.CENTER in pressed:
    if start_stop == 0:
        start_stop = 1
    if start_stop == 1:
        start_stop = 0

