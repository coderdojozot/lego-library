from functies import *

"""
---------------
BOUWER(S): Arthus - Robi
MISSIE(S): 7 (molensteen) - 8 (silo muur)
PUNTEN: 30, 10x3

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

async def missie_blauwA_start():

  await vooruit(440)
  await multitask(linkerarm.run_angle(1000,-200),rechterarm.run_angle(1000,-200))  #tandwielenc uit silo 
  await multitask(linkerarm.run_angle(1000,200),rechterarm.run_angle(1000,200))
  await multitask(linkerarm.run_angle(1000,-200),rechterarm.run_angle(1000,-200))
  await multitask(linkerarm.run_angle(1000,200),rechterarm.run_angle(1000,200))
  await multitask(linkerarm.run_angle(1000,-200),rechterarm.run_angle(1000,-200))
  await multitask(linkerarm.run_angle(1000,200),rechterarm.run_angle(1000,200))
  await links(90)
  await vooruit(70)
  await rechts(90)
  await vooruit(350)
  await rechts(53)
  await achteruit(120)
  await linkerarm_draai(1850)
  await achteruit(15)
  await vooruit(80)
  await linkerarm_draai(-1200)
  await links(133)
  await multitask(linkerarm_draai(-280), vooruit(660))
  await links(70)
  await vooruit(45)
  await linkerarm_draai(1500)
  await achteruit(50)
  await rechts(15)  #molensteen lossen
  await achteruit(35)
  await linkerarm_draai(-1300)
  await achteruit(35)
  await vooruit(32.5)
  await rechts(20)
  await vooruit(600)
  await links(50)
  await vooruit(50)
  await rechts(30)
  await vooruit(50)
  await links(10)
  await vooruit(1000)

# Deze regel zorgt ervoor dat de code uitgevoerd wordt
# verander enkel de naam van jouw missie, maar laat de code verder zoals ze is
if __name__ == "__main__":
  run_task(missie_blauwA_start())
