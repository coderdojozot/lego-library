from functies import *

"""
---------------
BOUWER(S): Arthus - Robi
MISSIE(S): 7 (molensteen) - 8 (silo muur)
PUNTEN: 30, 10x3

STARTVELD: RECHTS
STARTPOSITIE: Links tweede zwarte dikke streep, linkerkant robot
OPGELET: staaf volledig omhoog! --> makkelijkst als je dat op voorhand doet

STATUS: botst nog tegen klein blokje in het midden / getest tot aan molensteen neerzetten
TESTDATUM/ROBOT: 2/02/2026 - hub2
BATTERIJ % BIJ START: 91%

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
  await vooruit(90)
  await rechts(90)
  await vooruit(340)
  await rechts(45)
  await achteruit(120)
  await linkerarm_draai(1868) #molensteen
  await vooruit(80)
  await linkerarm_draai(-1300) #molensteen opheffen
  await links(133)
  await multitask(linkerarm_draai(-280), vooruit(660))
  await links(55)
  await linkerarm_draai(1680)
  await achteruit(60)
  await rechts(15)  #molensteen lossen
  await achteruit(45)
  await linkerarm_draai(-300)
  await achteruit(22)
  await vooruit(35)
  await rechts(27)
  await vooruit(625)
  await links(50)
  await vooruit(50)
  await vooruit(400)

# Deze regel zorgt ervoor dat de code uitgevoerd wordt
# verander enkel de naam van jouw missie, maar laat de code verder zoals ze is
if __name__ == "__main__":
  run_task(missie_blauwA_start())
