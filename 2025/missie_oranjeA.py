from functies import *

linkerarm_gears = [30, 10]
rechterarm_gears = [30, 10]
# [molen steen]
# dit is voor missie [] 
# Rechter startveld, eerste zwarte streepje van links

async def missie_oranje_start():

  

  await multitask(vooruit(770), rechterarm_draai(-1000))
  await rechts(40)
  await rechterarm_draai(925)
  await multitask(vooruit(50), rechterarm_draai(-150))
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
    run_task(missie_oranje_start())
