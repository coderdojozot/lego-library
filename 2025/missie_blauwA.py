from functies import *

"""
---------------
BOUWER(S): Arthus - Robi
MISSIE(S): 7 (molensteen) - 8 (silo muur)
PUNTEN: 30, 10x3

STARTVELD: RECHTS
STARTPOSITIE: Links zwarte kleine streepje, linkerkant robot
OPGELET: staaf volledig omhoog! --> makkelijkst als je dat op voorhand doet

STATUS: werkt nog niet volledig om terug te rijden
TESTDATUM/ROBOT: 21/01/2026 - hub1
BATTERIJ % BIJ START: 89%

---------------
"""

linkerarm_gears = [30, 10]
rechterarm_gears = [30, 10]

async def missie_blauwA_start():

  await vooruit(440)
  await rechterarm.run_angle(1000,-200)   #tandwielenc uit silo 
  await rechterarm.run_angle(1000,200)
  await rechterarm.run_angle(1000,-200)
  await rechterarm.run_angle(1000,200)
  await rechterarm.run_angle(1000,-200)
  await rechterarm.run_angle(1000,200)
  await rechterarm.run_angle(1000,-200)
  await rechterarm.run_angle(1000,200)
  await links(90)
  await vooruit(70)
  await rechts(90)
  await vooruit(325)
  await rechts(53)
  await achteruit(120)
  await linkerarm_draai(1855)
  await achteruit(15)
  await vooruit(80)
  await linkerarm_draai(-1200)
  await links(133)
  await multitask(linkerarm_draai(-1000), vooruit(660))
  await links(70)
  await vooruit(45)
  await linkerarm_draai(1000)
  await achteruit(50)
  await rechts(15)  #molensteen lossen
  await achteruit(35)
  await linkerarm_draai(-1300)
  await achteruit(27)
  await vooruit(35)
  await rechts(27)
  await vooruit(625)
  await links(50)
  await vooruit(50)
  await vooruit(1000)

# Deze regel zorgt ervoor dat de code uitgevoerd wordt
# verander enkel de naam van jouw missie, maar laat de code verder zoals ze is
if __name__ == "__main__":
  run_task(missie_blauwA_start())
