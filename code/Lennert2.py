####################################################################################
# Dit is een eerste versie van Lennert om de de missies te laten starten door herkenning
# van een kleur door de kleurensensor
#
# Laatste update: 15/10/2025
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
def links(x):
    drivebase.turn(-x)
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
x = 270

rechterarm.run_angle(700,300)
vooruit(750)
links(45)
rechterarm.run_angle(700,-20)
vooruit(100)
links(15)
achteruit(50)
rechterarm.run_angle(700,-100)
links(20)
vooruit(100)
links(10)
vooruit(1000)
rechterarm.run_angle(700,120)
rechts(45)
vooruit(170)
links(45)
vooruit(200)
rechterarm.run_angle(700,-120)

