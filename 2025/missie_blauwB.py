from functies import *

"""
---------------
BOUWER(S): Arthus - Robi
MISSIE(S): 7 (molensteen)
PUNTEN: 30

STARTVELD: RECHTS
STARTPOSITIE: Links zwarte kleine streepje, linkerkant robot
OPGELET: staaf volledig omhoog! --> makkelijkst als je dat op voorhand doet

STATUS: werkt nog niet volledig (wordt te ver gegooid door de arm)
TESTDATUM/ROBOT: 14/01/2026 - hub1
BATTERIJ % BIJ START: 96,39%
---------------
"""

linkerarm_gears = [30, 10]
rechterarm_gears = [30, 10]

async def missie_blauwB_start():

  await multitask(vooruit(750),linkerarm_draai(1500))
  await rechterarm_draai(270)
  await rechts(53)
  await achteruit(25)
  await linkerarm_draai(455)
  await vooruit(65) 
  await linkerarm_draai(-1200)
  await links(45, snelheid=500)
  await links(100, snelheid=1000)
  wait(1000)
  await links(90)
  await vooruit(450)

# Deze regel zorgt ervoor dat de code uitgevoerd wordt
# verander enkel de naam van jouw missie, maar laat de code verder zoals ze is
if __name__ == "__main__":
    run_task(missie_blauwB_start())
