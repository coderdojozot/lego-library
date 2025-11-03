from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#Instellingen:
hub = PrimeHub()
linker_kaaswiel = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
rechter_kaaswiel = Motor(Port.B)
Bertje = DriveBase(linker_kaaswiel, rechter_kaaswiel,62.4,88)
Bertje.use_gyro(True)
Rechter_ondernagelschimmel = Motor(Port.A)
Linker_volgroeide_wrat = Motor(Port.E)

STRAIGHT_SPEED = 900
STRAIGHT_ACC = 300
TURN_RATE = 70
TURN_ACC = 70
Bertje.settings(straight_speed=STRAIGHT_SPEED,
                       straight_acceleration=STRAIGHT_ACC,
                       turn_rate=TURN_RATE,
                       turn_acceleration=TURN_ACC)


#Code:
#print(linker_kaaswiel.angle())
Bertje.straight(570,then=Stop.HOLD,wait=True)
Bertje.curve(200, 90)
#Bertje.wait(1000)
Bertje.straight(879,then=Stop.HOLD,wait=True)
#Bertje.curve(150,-360)
#Bertje.straight(300,then=Stop.HOLD,wait=True)
Bertje.turn(-90)
Bertje.straight(51,then=Stop.HOLD,wait=True)
#Bertje.curve(505,90)
#Bertje,wait(1500)
#Bertje.turn(-197)
#Rechter_ondernagelschimmel.run_angle(6000, 60000)
#Rechter_ondernagelschimmel.run_angle(6000, 60000)
