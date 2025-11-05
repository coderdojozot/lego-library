from functies import *

# Arthus
# dit is voor missie 9 - 10 

async def missie_roodA_start():
    
    await rechterarm_draai(260)
    await vooruit(510)
    await links(130)
    await achteruit(50)
    await rechterarm_draai(-180)
    await vooruit(240)             # verkooptafeltje omhoog zetten
    await rechts(37)
    await vooruit(90)
    await rechterarm_draai(-90)    # grijp weegschaal
    await links(45)                # trekt weegschaal
    await vooruit(200)
    await rechts(90)
    await vooruit(300)
    await links(45)
    await vooruit(50)
    await multitask(achteruit(20),rechterarm_draai(90))     # weeegschaal loslaten
    await links(10  )
    await vooruit(7000)


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
    run_task(missie_roodA_start())
