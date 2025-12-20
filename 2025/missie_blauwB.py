from functies import *

"""
---------------
BOUWER(S): Arthus - Robi
MISSIE(S): 7 (molensteen)
PUNTEN: 30
STARTPOSITIE: Rechter startveld, Links zwarte kleine streepje, linkerkant robot
staaf omhoog!

STATUS: werkt nog niet volledig
TESTDATUM/ROBOT: 20/12/2025 - hub1
---------------
"""

linkerarm_gears = [30, 10]
rechterarm_gears = [30, 10]

async def missie_blauwB_start():

  await multitask(vooruit(750),linkerarm_draai(1500))
  await rechts(45)
  await achteruit(25)
  await linkerarm_draai(500)
  await vooruit(65) 
  await linkerarm_draai(-1200)
  await links(93)

if __name__ == "__main__":
    run_task(missie_blauwB_start())
