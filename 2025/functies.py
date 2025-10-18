from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task,hub_menu

STANDAARD_DRAAISNELHEID = 600
STANDAARD_SNELHEID = 800

hub = PrimeHub()
leftmotor = Motor(port=Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
rightmotor = Motor(port=Port.F)

drivebase = DriveBase(leftmotor, rightmotor, 62.4, 80)
drivebase.use_gyro(True)
drivebase.settings(straight_speed = STANDAARD_SNELHEID)

rechterarm = Motor(Port.A,positive_direction=Direction.CLOCKWISE)
linkerarm = Motor(Port.E)

sensor = ColorSensor(Port.D)


def vooruit(afstand):
    drivebase.straight(afstand)

def vooruit_met_snelheid(afstand, snelheid):
    drivebase.settings(straight_speed = snelheid)
    drivebase.straight(afstand)
    drivebase.settings(straight_speed = STANDAARD_SNELHEID)

def achteruit(afstand):
    drivebase.straight(-afstand)

def rechts(hoek):
    drivebase.turn(hoek)

def links(hoek):
    drivebase.turn(-hoek)

def rechterarm_draai(hoek):
    rechterarm.run_angle(STANDAARD_DRAAISNELHEID, hoek)

def linkerarm_draai(hoek):
    linkerarm.run_angle(STANDAARD_DRAAISNELHEID, hoek)

