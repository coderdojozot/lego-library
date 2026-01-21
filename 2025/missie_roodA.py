from functies import *

"""
---------------
BOUWER(S):  Simon - Arthur - Lennert - Lars
MISSIE(S): 12 (boot met zand) + 11 (kraan)
PUNTEN: 20 + 10 + 20 + 10

STARTVELD: LINKS
STARTPOSITIE: Rechts zwarte streepje, voorkant robot

STATUS: deel 2 werkt nog niet volledig + nog twee extra missies toevoegen
LAATSTE TESTDATUM/ROBOT: (21/01/2026 - hub1)
BATTERIJ % BIJ START: 89,17%
---------------
"""

async def missie_roodA_start():
    await vooruit(300)
    await rechterarm.run_angle(600, -182)
    await achteruit(50)
    await rechterarm.run_angle(600, 180)
    await links(90)
    await achteruit(30)
    await vooruit(200)
    await rechts(90)
    await vooruit(250)
    await achteruit(250)
    await links(90)
    await vooruit(100)  
    await rechts(90)
    await vooruit(490)
    await rechts(90)
    await vooruit(100)
    await links(15)
    await linkerarm.run_angle(600, -1200)
    await rechts(20)
    await achteruit(50)
    await links(90)
    await vooruit(900)
    #await links(135)
    #await vooruit(200)
    

# Deze regel zorgt ervoor dat de code uitgevoerd wordt
# verander enkel de naam van jouw missie, maar laat de code verder zoals ze is
if __name__ == "__main__":
    run_task(missie_roodA_start())
