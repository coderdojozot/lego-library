from functies import *

"""
---------------
BOUWER(S): Arthur
MISSIE(S): 12 (boot met zand)
PUNTEN: 20 + 10
STARTPOSITIE: Linker startveld, Rechts zwarte streepje, voorkant robot

STATUS: werkt volledig
TESTDATUM/ROBOT: 26/11/2025 - hub1
---------------
"""

async def missie_blauwA_start():
    await vooruit(300)
    await rechterarm.run_angle(600, -182)
    await achteruit(50)
    await rechterarm.run_angle(600, 180)
    await links(90)
    await vooruit(200)
    await rechts(90)
    await vooruit(250)
    await achteruit(750)

if __name__ == "__main__":
    run_task(missie_blauwA_start())
