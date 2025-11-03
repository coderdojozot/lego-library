####################################################################################
# Deze file laat zien hoe je een functie geschreven in een andere python file kan gebruiken
# 
####################################################################################
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Hier doen we de import
from code_vuilbak.Xprobeersels.rijden_met_gyro_versie_lukas import gyro_rechtdoor

# niet zeker of dit nodig is, want zit ook al in de import
hub = PrimeHub

# op deze manier kunnen we de functie gebruiken
gyro_rechtdoor(500, 1000)
