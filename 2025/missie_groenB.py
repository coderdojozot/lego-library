from functies import *

# [Ik, snorremans, en über-snor supreme]
# dit is voor missie [02,04,(14)] 

async def linkerarm_draai_louche(hoek_ongeveer):
  gemeten_afwijking = -0.2
  percentage_volgens_doos = gemeten_afwijking / ( (2 * 3.1415 * 2 ) / (360 / hoek_ongeveer))
  print("De afwijking is: " + str(gemeten_afwijking) )  
  print("Dat is: " + str(gemeten_afwijking) + "% van wat we wouden.")
  hoek_correctie = hoek_ongeveer * (( 100 - percentage_volgens_doos ) / 100 )
  print("Dus de gecorrigeerde hoek is: " + str(hoek_correctie))  
  await linkerarm_draai(hoek_correctie)

async def missie_groenB_start():
    await vooruit(170) 
    await linkerarm_draai_louche(-180)
    wait(50)
    await vooruit(-170)


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
    run_task(missie_groenB_start())
