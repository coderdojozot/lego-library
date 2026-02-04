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
TESTDATUM/ROBOT: 28/01/2026 - hub1
BATTERIJ % BIJ START: 85%
---------------
"""

async def missie_geelA_start():
   await vooruit(733.5)
   await rechts(87)
   await vooruit(362)
   await links(80)
   await multitask(vooruit(2.375),rechterarm.run_angle(923.5,-2100)) # Heffen mijnkarretje
   await wait(15)    
   await multitask(vooruit(2),rechts(72))
   await vooruit(666.56)  # Arm omhoog
   await rechts(57)
   await vooruit(231.55, 900)                                      # Omhoogduwen winkelding
   await wait(10)
   await achteruit(203)
   await vooruit(231.45, 900)    
   await achteruit(1)         
   await vooruit(4) 
   await achteruit(1)
   await vooruit(2)                        # Omhoogduwen winkelding
   await wait(10)
   await achteruit(203)
   await vooruit(231.35, 900)                                      # Omhoogduwen winkelding
   await wait(10)
   await achteruit(203)
   await links(18)
   await vooruit(440)
   await rechts(45)
   await multitask(rechterarm.run_angle(900,250),vooruit(450))
   
   
# Deze regel zorgt ervoor dat de code uitgevoerd wordt
# verander enkel de naam van jouw missie, maar laat de code verder zoals ze is
if __name__ == "__main__":
    run_task(missie_geelA_start())
