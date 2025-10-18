from functies import *
from missie_blauw import missie_blauw_start
from missie_groen import missie_groen_start
laatste_kleur = Color.MAGENTA

while True:
    color =sensor.color()
    print(color)
    if color == laatste_kleur or color == Color.NONE:
        continue
    laatste_kleur = color    
    if color == Color.GREEN: 
        wait(500)    
        missie_groen_start()
    if color == Color.BLUE:
        missie_blauw_start()
