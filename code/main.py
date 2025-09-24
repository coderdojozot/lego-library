from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
hub = PrimeHub()
start_stop = 0
programma = 0
pressed = []
getal = 1
while True:
    pressed = []
    while not any(pressed):
        pressed = hub.buttons.pressed()
    while any(hub.buttons.pressed()):
        pass
    if Button.LEFT in pressed:
        programma = programma + 1
        print (programma)
    elif Button.RIGHT in pressed:
        programma = programma - 1
        print (programma)
    elif Button.BLUETOOTH in pressed:
        if start_stop == 0:
            start_stop = 1
        elif start_stop == 1:
            start_stop = 0
    if programma == 1 and start_stop == 1:
        start_stop = 0
        import programma1
        