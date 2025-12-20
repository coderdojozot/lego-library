from functies import *


"""
---------------
BOUWER(S): Nathan
MISSIE(S): 3 (Map Reveal)
PUNTEN: 10
STARTPOSITIE: Linker startveld, derde dikke zwarte streepje van links)
STATUS: naar huis linkse kant
TESTDATUM/ROBOT: 3/12/2025 - hub2
---------------
"""

async def missie_lichtblauw_start():
    await achteruit(10)
    await vooruit(770)
    await links(43)
    await vooruit(160)
    await rechterarm_draai(60)
    await achteruit(200)
    await rechterarm_draai(-40, 1000)
    await multitask(rechterarm_draai(-40, 1000),rechts(140, 1000))
    await rechts(20, 400)
    #await rechterarm_draai(-20)
    #await achteruit(100)
    #await rechterarm_draai(50)



  # Dit is voorbeeldcode voor de start van een nieuw
  # programma. Pas deze code aan voor jouw extensie.
  
  # await vooruit(100)
  # await rechts(85)
  # await links(8)
  # await rechterarm.run_angle(2100,1650)
  # await multitask(vooruit(2),rechterarm.run_angle(900,-1650))

# Deze regel zorgt ervoor dat de code uitgevoerd wordt
# verander enkel de naam van jouw missie, maar laat de code verder zoals ze is
if __name__ == "__main__":
    run_task(missie_lichtblauw_start())
