from functies import *
from missie_blauwA import missie_blauwA_start
from missie_blauwB import missie_blauwB_start
from missie_groenA import missie_groenA_start
from missie_groenB import missie_groenB_start
from missie_geelA import missie_geelA_start
from missie_geelB import missie_geelB_start
from missie_roodA import missie_roodA_start
from missie_roodB import missie_roodB_start
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

##########################################################################
##  NIKS AAN HET HOOFDPROGRAMMA VERANDEREN ZONDER OVERLEG MET IEDEREEN  ##
##########################################################################

"""
---------------
CODE: Lucas - Lennert

Dit is het hoofdprogramma dat de missies aanroept op basis van de gedetecteerde kleur.
Elke kleur heeft twee missies (A en B), die geselecteerd kunnen worden via het hub-menu.

STATUS: werkt volledig
TESTDATUM/ROBOT: 26/11/2025 - hub1
---------------
"""

laatste_kleur = Color.MAGENTA
color =sensor.color()
print(color)

while True:
    color =sensor.color()
    print(color)
    if color == laatste_kleur or color == Color.NONE:
        continue
    laatste_kleur = color    
    
    if color == Color.GREEN: 
        hub.light.blink(color,[500,500])
        selected = hub_menu("A", "B")  
        if selected == "A":
            hub.light.on(color)
            run_task(missie_groenA_start())
            hub.light.off()
            hub.display.off()
        if selected == "B":
            hub.light.on(color)
            run_task(missie_groenB_start())
            hub.light.off()
            hub.display.off()
              
    if color == Color.BLUE:
        hub.light.blink(color,[500,500])
        selected = hub_menu("A", "B")  
        if selected == "A":
             hub.light.on(color)
             run_task(missie_blauwA_start())
             hub.light.off()
             hub.display.off()
        if selected == "B":
             hub.light.on(color)
             run_task(missie_blauwB_start())
             hub.light.off()
             hub.display.off()

    if color == Color.YELLOW:
        hub.light.blink(color,[500,500])
        selected = hub_menu("A", "B")  
        if selected == "A":
             hub.light.on(color)
             run_task(missie_geelA_start())
             hub.light.off()
             hub.display.off()
        if selected == "B":
             hub.light.on(color)
             run_task(missie_geelB_start())
             hub.light.off()
             hub.display.off()

    if color == Color.RED:
        hub.light.blink(color,[500,500])
        selected = hub_menu("A", "B")  
        if selected == "A":
             hub.light.on(color)
             run_task(missie_roodA_start())
             hub.light.off()
             hub.display.off()
        if selected == "B":
             hub.light.on(color)
             run_task(missie_roodB_start())
             hub.light.off()
             hub.display.off()
