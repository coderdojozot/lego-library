from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Color, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialiseer hub, motors en sensoren
hub = PrimeHub()
left_motor  = Motor( Port.C, positive_direction=Direction.COUNTERCLOCKWISE )
right_motor = Motor( Port.F )
left_sensor  = ColorSensor( Port.B )
right_sensor = ColorSensor( Port.D )

# Pas kleurdetectie aan (optioneel)
Color.BLACK = Color(h=240, s=7, v=15)
my_colors = (Color.BLACK, Color.WHITE, Color.NONE)
left_sensor.detectable_colors( my_colors )
right_sensor.detectable_colors( my_colors )

def drive_until_line(speed=200):
    left_motor.run(speed)
    right_motor.run(speed)
    while True:
        if left_sensor.color() == Color.BLACK or right_sensor.color() == Color.BLACK:
            left_motor.stop()
            right_motor.stop()
            break
        wait(10)

def align_to_line(speed=100):
    left_on_line  = (left_sensor.color()  == Color.BLACK)
    right_on_line = (right_sensor.color() == Color.BLACK)
    while not (left_on_line and right_on_line):
        if not left_on_line:
            left_motor.run(speed)
        else:
            left_motor.stop()
        if not right_on_line:
            right_motor.run(speed)
        else:
            right_motor.stop()
        left_on_line  = (left_sensor.color()  == Color.BLACK)
        right_on_line = (right_sensor.color() == Color.BLACK)
        wait(10)
    left_motor.stop()
    right_motor.stop()

def back_off(distance):
    drivebase.straight(distance, then=Stop.HOLD, wait=True)

# Hoofdprogramma
drive_until_line()
for teller in range(5):
    back_off(-80)
    align_to_line()

