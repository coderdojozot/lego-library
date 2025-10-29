from functies import *
from missie_blauw import missie_blauw_start
from missie_groenA import missie_groen_start
from missie_geel import missie_geel_start
laatste_kleur = Color.MAGENTA

while True:
    color =sensor.color()
    if color == laatste_kleur or color == Color.NONE:
        continue
    laatste_kleur = color    
    if color == Color.GREEN: 
        hub.light.blink(color,[500,500])
        selected = hub_menu("A", "F")  
        if selected == "A":
             hub.light.on(color)
             run_task(missie_groen_start())
             hub.light.off()
             hub.display.off()
              
        
    if color == Color.BLUE:
        hub.light.blink(color,[500,500])
        selected = hub_menu("A", "F")  
        if selected == "A":
             hub.light.on(color)
             run_task(missie_blauw_start())
             hub.light.off()
             hub.display.off()

    if color == Color.YELLOW:
        hub.light.blink(color,[500,500])
        selected = hub_menu("A", "F")  
        if selected == "A":
             hub.light.on(color)
             run_task(missie_geel_start())
             hub.light.off()
             hub.display.off()