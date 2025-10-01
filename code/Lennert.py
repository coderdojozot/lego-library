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


left_motor = Motor(port=Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(port=Port.E)
drivebase = DriveBase(left_motor, right_motor, 62.4, 208)

left_attachment_motor = Motor(port=Port.B)
right_attachment_motor = Motor(port=Port.F)
drivebase.use_gyro(True)
sensor = ColorSensor(Port.A)


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

def missieRood():
    vooruit(100)

  
def missieBlauw():
    achteruit(100)



laatste_kleur = Color.MAGENTA

while True:
    color =sensor.color()
    print(color)
    if color == laatste_kleur or color == Color.NONE:
        continue
    laatste_kleur = color    
    if color == Color.RED:     
         missieRood()
    if color == Color.BLUE:
        missieBlauw()
    
