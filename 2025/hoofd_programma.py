from functies import *
from missie_blauw import missie_blauw_start
from missie_groenA import missie_groenA_start
from missie_geelA import missie_geelA_start
from missie_geelB import missie_geelB_start
from missie_paarsA import missie_paarsA_start
from missie_paarsB import missie_paarsB_start

##########################################################################
##  NIKS AAN HET HOOFDPROGRAMMA VERANDEREN ZONDER OVERLEG MET IEDEREEN  ##
##########################################################################

laatste_kleur = Color.MAGENTA

paars = [4 ,5 ,6]
groen = [1 ,2 ,3]
geel = [17, 18, 19]
orange = [8 ,9 ,10]
blauw = [1, 2, 3]

while True:
    color = sensor.color()
    if color == laatste_kleur or color == Color.NONE:
        continue
    laatste_kleur = color    
    if sensor.reflection() in groen:
        hub.light.blink(color,[500,500])
        selected = hub_menu("A")  
       
        if selected == "A":
            hub.light.on(color)
            run_task(missie_groenA_start())
            hub.light.off()
            hub.display.off()
        
    if sensor.reflection() in blauw:
        hub.light.blink(color,[500,500])
        selected = hub_menu("A")  
        if selected == "A":
             hub.light.on(color)
             run_task(missie_blauw_start())
             hub.light.off()
             hub.display.off()

    if sensor.reflection() in geel:
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
    
    if sensor.reflection() in orange:
        hub.light.blink(color,[500,500])
        selected = hub_menu("A", "B")  
        if selected == "A":
             hub.light.on(color)
             run_task(missie_paarsA_start())
             hub.light.off()
             hub.display.off()
        if selected == "B":
             hub.light.on(color)
             run_task(missie_paarsB_start())
             hub.light.off()
             hub.display.off()
