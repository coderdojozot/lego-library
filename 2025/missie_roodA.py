from functies import *

"""
---------------
BOUWER(S):  Simon - Arthur - Lennert - Lars
MISSIE(S): 12 (boot met zand) + 11 (kraan) + 10(scale pan) + 9 (wares)
PUNTEN: 20 + 10 + 20 + 10 + 10 + 10

STARTVELD: LINKS
STARTPOSITIE: Rechts zwarte streepje, voorkant robot

STATUS: neemt hoepel nog niet mee
LAATSTE TESTDATUM/ROBOT: (26/01/2026 - hub1)
BATTERIJ % BIJ START: 91%
---------------
"""

async def missie_roodA_start():
    await vooruit(300)
    await rechterarm.run_angle(600, -182)
    await achteruit(50)
    await rechterarm.run_angle(600, 180)
    await links(90)
    await achteruit(30)
    await vooruit(210)
    await rechts(90)
    await vooruit(250)
    await achteruit(250)
    await links(90)
    await vooruit(100)  
    await rechts(90)
    await vooruit(490)
    await rechts(90)
    await vooruit(105)
    await links(15)
    await linkerarm.run_angle(600, -1800)
    await rechts(20)
    await achteruit(80)
    await links(90)
    await vooruit(180)
    await links(45)
    await vooruit(210)
    await rechterarm.run_angle(600, -180)
    await achteruit(170)
    await rechterarm.run_angle(600, 180)
    await links(45)
    await achteruit(5)
    await rechterarm.run_angle(600, -180)
    await achteruit(120, 400)
    await links(45)
    await draai_links_met_straal(45, 300)
    await vooruit(550)
    await rechts(90)
    await vooruit(140)
    await rechts(20)
    await rechterarm.run_angle(600, 180)
    await achteruit(500)

    # await vooruit(900)
    #await links(135)
    #await vooruit(200)
    

# Deze regel zorgt ervoor dat de code uitgevoerd wordt
# verander enkel de naam van jouw missie, maar laat de code verder zoals ze is
if __name__ == "__main__":
    run_task(missie_roodA_start())
