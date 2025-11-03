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


drivebase.settings(straight_speed=STRAIGHT_SPEED,
                       straight_acceleration=STRAIGHT_ACC,
                       turn_rate=TURN_RATE,
                       turn_acceleration=TURN_ACC)
def vooruit(x):
    drivebase.straight(x)
def achteruit(x):
    drivebase.straight(-x)
def rechts(x):
    drivebase.turn(x)
def links(x):
    drivebase.turn(-x)

vooruit(200)
links(90)
vooruit(200)
links(90)
vooruit(200) 
links(31)
vooruit(150)
rechts(31)
vooruit(40)
rechts(90)
vooruit(40)
links(90)
achteruit(200)
drivebase.settings(straight_speed=1000)
drivebase.settings(straight_acceleration=500)
vooruit(290)
left_attachment_motor.run_angle(150,100)
vooruit(100)
achteruit(110)
left_attachment_motor.run_angle(150,-100)
vooruit(100)
left_attachment_motor.run_angle(150,100)
