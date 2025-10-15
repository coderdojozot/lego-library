####################################################################################
# Dit is een eerste versie van Lennert om de de missies te laten starten door herkenning
# van een kleur door de kleurensensor
#
# Laatste update: 24/09/2025 - eerste versie
####################################################################################

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


leftmotor = Motor(port=Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
rightmotor = Motor(port=Port.F)
drivebase = DriveBase(leftmotor, rightmotor, 62.4, 80)
drivebase.use_gyro(True)
rechterarm = Motor(Port.A,positive_direction=Direction.CLOCKWISE)

sensor = ColorSensor(Port.D)

def vooruit(x):
    drivebase.straight(x)
def achteruit(x):
    drivebase.straight(-x)
def rechts(x):
    drivebase.turn(x)

def missieRood():
    vooruit(100)

  
def missieBlauw():
    achteruit(100)



# laatste_kleur = Color.MAGENTA

# while True:
#     color =sensor.color()
#     print(color)
#     if color == laatste_kleur or color == Color.NONE:
#         continue
#     laatste_kleur = color    
#     if color == Color.YELLOW: 
#         wait(100)    
#         import missie_4_lukas_lennert
#     if color == Color.BLUE:
#         missieBlauw
x = 10000

drivebase.straight(510)
rechterarm.run_angle(10000,x)