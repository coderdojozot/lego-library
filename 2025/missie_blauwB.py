from functies import *

linkerarm_gears = [30, 10]
rechterarm_gears = [30, 10]
# [molen steen]
# dit is voor missie [] 
# Rechter startveld, eerste kleine streepje van links 

async def missie_blauwB_start():

  

  await multitask(vooruit(770), rechterarm_draai(-1000))
  await rechts(43)
  await rechterarm_draai(950)
  await vooruit(50) 
  await rechterarm_draai(-1200)
  await links(93)
  #await links(43)
  #await achteruit(770)
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
    run_task(missie_blauwB_start())
