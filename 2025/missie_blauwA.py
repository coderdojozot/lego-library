from functies import *

"""
---------------
BOUWER(S): Arthus - Robi
MISSIE(S): 7 (molensteen) - 8 (silo muur)
PUNTEN: 30, 10x3

STARTVELD: RECHTS
STARTPOSITIE: 3mm links van tweede zwarte linkse dikke streep, linkerkant robot
OPGELET: staaf volledig omhoog! --> makkelijkst als je dat op voorhand doet

STATUS: werkt volledig
TESTDATUM/ROBOT: 2/02/2026 - hub1
BATTERIJ % BIJ START: 98%

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
  await rechts(53.5)
  await achteruit(70)
  # await rechts(5)
  await linkerarm_draai(1868) #molensteen
  await vooruit(70)
  await linkerarm_draai(-1300) #molensteen opheffen
  await links(133,100)
  await multitask(linkerarm_draai(-280), vooruit(660))
  await links(55)
  await linkerarm_draai(1700)
  await achteruit(55)
  await rechts(15)  #molensteen lossen
  await achteruit(40)
  await linkerarm_draai(-300)
  await rechts(15)
  await multitask(vooruit(750),linkerarm_draai(-1200))
  await links(45)
  await vooruit(400)

# Deze regel zorgt ervoor dat de code uitgevoerd wordt
# verander enkel de naam van jouw missie, maar laat de code verder zoals ze is
if __name__ == "__main__":
  run_task(missie_blauwA_start())
