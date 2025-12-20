from functies import *

"""
---------------
BOUWERS: Simon - Arthur - Lennert
MISSIE(S): 11 (kraan)
PUNTEN: 20 + 10
STARTPOSITIE: Linker startveld, Rechts 2de zwarte streepje, rechterkant robot

STATUS: rijd nog niet terug, combineren met blauwA
TESTDATUM/ROBOT: 26/11/2025 - hub1
---------------
"""

async def missie_geelB_start():
    await draai_rechts_met_straal(90,300)
    await vooruit(598)
    await rechts(90)
    await vooruit(150)
    await links(20)
    await rechterarm_draai(2400)
    await achteruit(300)
    await rechts(110)
    await vooruit(800)

if __name__ == "__main__": 
    run_task(missie_geelB_start())
