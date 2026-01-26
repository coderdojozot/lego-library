from functies import *

"""
---------------
BOUWERS: Luca, Nielspookie
MISSIE(S): 3 (mijnkarretje) - 9 (winkel met dak) - 10 (weegschaal)
PUNTEN: 30, 20, 20

STARTVELD: LINKS
STARTPOSITIE: 2de linkse zwarte streepje, linkerkant robot
ARM?

STATUS: 2de keer laatste missie rijdt nog te ver vooruit
TESTDATUM/ROBOT: 26/01/2026 - hub1
BATTERIJ % BIJ START: 91%
---------------
"""

async def missie_geelA_start():
   await vooruit(733.5)
   await rechts(85)
   await vooruit(362)
   await links(78)
   await multitask(vooruit(2.375),rechterarm.run_angle(923.5,-2000)) # Heffen mijnkarretje
   await wait(15)    
   await multitask(vooruit(2),rechts(70))
   await vooruit(625)  # Arm omhoog
   await rechts(91)
   await vooruit(29.99)
   await rechterarm.run_angle(900,1695)                         
   await achteruit(41.39)                                      # Weegschaal omlaag
   await multitask(rechterarm.run_angle(900,-250),links(34))   # Arm omhoog
   await vooruit(229.65, 900)                                      # Omhoogduwen winkelding
   await wait(10)
   await achteruit(200)
   await vooruit(350)
   await links(2.75)
   await achteruit(222)
   await links(18)
   await vooruit(450)
   await rechts(45)
   await multitask(rechterarm.run_angle(900,250),vooruit(450))
   
   
# Deze regel zorgt ervoor dat de code uitgevoerd wordt
# verander enkel de naam van jouw missie, maar laat de code verder zoals ze is
if __name__ == "__main__":
    run_task(missie_geelA_start())
