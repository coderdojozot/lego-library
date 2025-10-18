from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, hub_menu, multitask,

STANDAARD_WAGEN_DRAAISNELHEID = 600
STANDAARD_WAGEN_ACCELERATIE = 600
STANDAARD_ARM_DRAAISNELHEID = 600
STANDAARD_SNELHEID = 800

hub = PrimeHub()
leftmotor = Motor(port=Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
rightmotor = Motor(port=Port.F)

drivebase = DriveBase(leftmotor, rightmotor, 62.4, 80)
drivebase.use_gyro(True)
drivebase.settings(straight_speed = STANDAARD_WAGEN_DRAAISNELHEID)
drivebase.settings(straight_acceleration = STANDAARD_WAGEN_ACCELERATIE)

rechterarm = Motor(Port.A,positive_direction=Direction.CLOCKWISE)
linkerarm = Motor(Port.E)

sensor = ColorSensor(Port.D)


async def vooruit(afstand, snelheid = STANDAARD_WAGEN_DRAAISNELHEID, acceleratie = STANDAARD_WAGEN_ACCELERATIE):
    drivebase.settings(straight_speed = snelheid)
    drivebase.settings(straight_acceleration=acceleratie)
    await drivebase.straight(afstand)

async def achteruit(afstand, snelheid = STANDAARD_WAGEN_DRAAISNELHEID, acceleratie = STANDAARD_WAGEN_ACCELERATIE):
    drivebase.settings(straight_speed = snelheid)
    drivebase.settings(straight_acceleration=acceleratie)
    await drivebase.straight(-afstand)

async def rechts(hoek, snelheid = STANDAARD_WAGEN_DRAAISNELHEID):
    drivebase.settings(turn_rate = snelheid)
    await drivebase.turn(hoek)

async def links(hoek, snelheid = STANDAARD_WAGEN_DRAAISNELHEID):
    drivebase.settings(turn_rate = snelheid)
    await drivebase.turn(-hoek)

async def rechterarm_draai(hoek):
    await rechterarm.run_angle(STANDAARD_ARM_DRAAISNELHEID, hoek)

async def linkerarm_draai(hoek):
    await linkerarm.run_angle(STANDAARD_ARM_DRAAISNELHEID, hoek)
