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
# print(drivebase.state())

def maak_acht():
    # drivebase.straight(distance=300, then=Stop.HOLD, wait=True)
    # drivebase.turn(angle=180, then=Stop.HOLD, wait=True)
# drivebase.curve()
    drivebase.curve(radius=200, angle=90, then=Stop.NONE, wait=True)
    await drivebase.curve(radius=100, angle=-240, then=Stop.HOLD, wait=True)
    left_attachment_motor.run_angle(speed=10, rotation_angle=1, then=Stop.HOLD, wait=True)

# run_task(maak_acht())
# print(drivebase.state()

def test():
    drivebase.straight(300)
    drivebase.turn(90)

aantal=0


    
# while aantal != 4:
    # print(aantal)
    # test()
    # wait(1)
    # aantal = aantal + 1

selected = hub_menu("1", "2")

if selected == "1":
    while True:
        for hue in range(360):
            hub.light.on(Color(hue))
            print(Color(hue))
            wait(100)
        
elif selected == "2":
    hub.speaker.volume(volume=40)
    hub.speaker.play_notes(notes=["C4/4","D4/4", "E4/4", "C4/4", "C4/4","D4/4", "E4/4", "C4/4"],tempo=120)
    print(hub.charger.current())

    