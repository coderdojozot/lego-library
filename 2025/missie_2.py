from functies import *


"""
---------------
BOUWER(S): Nathan
MISSIE(S): 3 (Map Reveal)
PUNTEN: 10
STARTPOSITIE: Linker startveld, derde dikke zwarte streepje van links)
STATUS: bezig
TESTDATUM/ROBOT: 3/12/2025 - hub2
---------------
"""

async def missie_lichtblauw_start():
    await vooruit(800)


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
