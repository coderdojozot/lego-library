from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu

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

selected = hub_menu("1","2")
def missie_opruimen():
    def arm_open():
        left_attachment_motor.run_angle(400,720)
    def arm_dicht():
        left_attachment_motor.run_angle(400,-720)
    def arm_half_open():
        left_attachment_motor.run_angle(400,360)
    def arm_half_dicht():
        left_attachment_motor.run_angle(400,-360)

    arm_open()
    drivebase.straight(440)
    drivebase.curve(200,45)
    arm_dicht()
    drivebase.straight(200)
    drivebase.curve(200,45)
    drivebase.straight(700)
    arm_open()
    drivebase.straight(200)
    arm_dicht()
    drivebase.turn(45)
    drivebase.straight(-60)
    arm_open()
    drivebase.straight(60)
    drivebase.turn(45)
    drivebase.straight(200)
    drivebase.curve(300,-45)
    drivebase.straight(300)
    


def missie_11():
    drivebase.straight(650)
    drivebase.curve(200,-45)
    drivebase.straight(150)
    drivebase.straight(-15)
    left_attachment_motor.run_angle(400,540)
    left_attachment_motor.run_angle(400,-180)
    drivebase.straight(-270)
    drivebase.curve(350,-45)
    drivebase.straight(620)
    drivebase.angle(20)
    drivebase.straight(50)
    drivebase.angle(-20)


if selected == "1":
    missie_opruimen()
elif selected == "2":
    missie_11()





    
