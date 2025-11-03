from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

STRAIGHT_SPEED = 900
STRAIGHT_ACC = 300
TURN_RATE = 70
TURN_ACC = 70


left_motor = Motor(port=Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(port=Port.B)
drivebase = DriveBase(left_motor, right_motor, 62.4, 208)

left_attachment_motor = Motor(port=Port.E)
right_attachment_motor = Motor(port=Port.A)
drivebase.use_gyro(True)

def vooruit(x):
    drivebase.straight(x)
def achteruit(x):
    drivebase.straight(-x)
def rechts(x):
    drivebase.turn(x)
def links(x):
    drivebase.turn(-x)



drivebase.settings(straight_speed=STRAIGHT_SPEED,
                       straight_acceleration=STRAIGHT_ACC,
                       turn_rate=TURN_RATE,
                       turn_acceleration=TURN_ACC)
left_attachment_motor.run_angle(1000,90)
vooruit(540)
rechts(90)
achteruit(10)
links(90)
achteruit(100)
left_attachment_motor.run_angle(1000,-80)
vooruit(160)
left_attachment_motor.run_angle(1000,90)
left_attachment_motor.run_angle(1000,-90)
vooruit(100)
left_attachment_motor.run_angle(1000,90)
achteruit(400)
rechts(45)
left_attachment_motor.run_angle(1000,-90)
vooruit(600)
achteruit(200)
rechts(45)
left_attachment_motor.run_angle(1000,90)
vooruit(475)
links(90)
vooruit(650)
rechts(45)


