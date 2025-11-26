from functies import *

"""
---------------
BOUWER(S): Arthus - Robi
MISSIE(S): 7 (molensteen)
PUNTEN: 30
STARTPOSITIE: Rechter startveld, Links zwarte kleine streepje, linkerkant robot

STATUS: nog te testen
TESTDATUM/ROBOT: 26/11/2025 - hub1
---------------
"""

linkerarm_gears = [30, 10]
rechterarm_gears = [30, 10]

async def missie_blauwB_start():

  await multitask(vooruit(770), rechterarm_draai(-1000))
  await rechts(43)
  await rechterarm_draai(950)
  await vooruit(50) 
  await rechterarm_draai(-1200)
  await links(93)

if __name__ == "__main__":
    run_task(missie_blauwB_start())
