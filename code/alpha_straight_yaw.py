from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu, run_task

hub = PrimeHub()

#Drivebase settings: verander hier de snelheid, versnelling, draaisnelheid van de robot
STRAIGHT_SPEED = 900
STRAIGHT_ACC = 300
TURN_RATE = 70
TURN_ACC = 70


left_sensor = ColorSensor(Port.B)
left_sensor = ColorSensor(Port.D)

left_motor = Motor(port=Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(port=Port.F)
drivebase = DriveBase(left_motor, right_motor, 62.4, 80)

left_attachment_motor = Motor(port=Port.E)
right_attachment_motor = Motor(port=Port.A)
drivebase.use_gyro(True)

drivebase.settings(straight_speed=STRAIGHT_SPEED,
                       straight_acceleration=STRAIGHT_ACC,
                       turn_rate=TURN_RATE,
                       turn_acceleration=TURN_ACC)

def drive_straight(speed, distance):
    hub.imu.reset_heading(0)
    left_motor.reset_angle(0)
    while left_motor.angle() < distance:
        error = hub.imu.heading()
        correction = error * -2
        left_motor.run(speed + correction)
        right_motor.run(speed - correction)
    drivebase.brake()

drive_straight(900, 1500)