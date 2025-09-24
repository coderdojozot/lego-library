from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task,hub_menu


hub = PrimeHub()

STRAIGHT_SPEED = 900
STRAIGHT_ACC = 300
TURN_RATE = 70
TURN_ACC = 70

hub.speaker.volume(50)

melody = [
    "C4/4", "C4/4", "G4/4", "G4/4",
    "A4/4", "A4/4", "G4/2",
    "F4/4", "F4/4", "E4/4", "E4/4",
    "D4/4", "D4/4", "C4/2",

    # Tweede deel van het lied
    "G4/4", "G4/4", "F4/4", "F4/4",
    "E4/4", "E4/4", "D4/2",
    "G4/4", "G4/4", "F4/4", "F4/4",
    "E4/4", "E4/4", "D4/2",

    "C4/4", "C4/4", "G4/4", "G4/4",
    "A4/4", "A4/4", "G4/2",
    "F4/4", "F4/4", "E4/4", "E4/4",
    "D4/4", "D4/4", "C4/2"
]

left_motor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F)
left_attachment_motor = Motor(port=Port.E)
right_attachment_motor = Motor(port=Port.A)
left_sensor = ColorSensor(Port.B)
richt_sensor = ColorSensor(Port.D)

aantal=0

def drive_straight(speed, distance):
    hub.imu.reset_heading(0)
    left_motor.reset_angle(0)
    while left_motor.angle() < distance:
        error = hub.imu.heading()
        correction = error * -2
        left_motor.run(speed + correction)
        right_motor.run(speed - correction)
    left_motor.brake()
    right_motor.brake()


# while aantal != 4:
    # print(aantal)
    # test()
    # wait(1)
    # aantal = aantal + 1

selected = hub_menu("1", "2")

if selected == "1":
    for teller in range(8):
        drive_straight(500, 500)
        
elif selected == "2":
    hub.speaker.play_notes(melody, tempo=120)
