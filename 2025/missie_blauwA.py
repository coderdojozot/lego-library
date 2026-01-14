from functies import *

"""
---------------
BOUWER(S): Arthur
MISSIE(S): 12 (boot met zand)
PUNTEN: 20 + 10

STARTVELD: LINKS
STARTPOSITIE: Rechts zwarte streepje, voorkant robot

STATUS: werkt volledig
LAATSTE TESTDATUM/ROBOT: (14/01/2026 - hub1)
BATTERIJ % BIJ START: 97,17%
---------------
"""

async def missie_blauwA_start():
    await vooruit(300)
    await rechterarm.run_angle(600, -182)
    await achteruit(50)
    await rechterarm.run_angle(600, 180)
    await links(90)
    await achteruit(30)
    await vooruit(200)
    await rechts(90)
    await vooruit(250)
    await achteruit(750)

# Deze regel zorgt ervoor dat de code uitgevoerd wordt
# verander enkel de naam van jouw missie, maar laat de code verder zoals ze is
if __name__ == "__main__":
    run_task(missie_blauwA_start())
