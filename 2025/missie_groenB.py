from functies import *

"""
---------------
BOUWERS: [Ik, snorremans, en über-snor supreme]
MISSIE(S): 2 (groen vierkanten)- 4 (schat ophalen) - 14 (schat droppen)
PUNTEN: ? , 30 + 10, ?

STARTVELD: LINKS
STARTPOSITIE: 2de linkse zwarte streepje, rechterkant robot

STATUS: rijden naar missie 2 en 4 nog te coderen (missie twee zit al in missie_2)
TESTDATUM/ROBOT: 26/11/2025 - hub1
BATTERIJ % BIJ START: xxx
---------------
"""

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

# Deze regel zorgt ervoor dat de code uitgevoerd wordt
# verander enkel de naam van jouw missie, maar laat de code verder zoals ze is
if __name__ == "__main__":
    run_task(missie_groenB_start())
