from functies import *

"""
---------------
BOUWER(S): Arthus - Robi
MISSIE(S): 7 (molensteen)
PUNTEN: 30
STARTPOSITIE: Rechter startveld, Links zwarte kleine streepje, linkerkant robot

STATUS: nog te testen
TESTDATUM/ROBOT: 3/12/2025 - hub1
---------------
"""

linkerarm_gears = [30, 10]
rechterarm_gears = [30, 10]

async def missie_blauwB_start():

  await multitask(vooruit(750),linkerarm_draai(1500))
  await rechterarm_draai(270)
  await rechts(51)
  await achteruit(25)
  await linkerarm_draai(450)
  await vooruit(65) 
  await linkerarm_draai(-1200)
  await links(150)

if __name__ == "__main__":
    run_task(missie_blauwB_start())
