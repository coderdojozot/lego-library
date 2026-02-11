from functies import *

"""
---------------
BOUWERS: Lennert - Lucas
MISSIE(S): 1 (surface brussing)- 6 (rotsblokken) - 14 (borstel) - 5 (schuine vloer)
PUNTEN: 10 + 10 + 10 , 10 + 10 + 10, 5, 30

STARTVELD: LINKS
STARTPOSITIE: 2de linkse zwarte streepje, linkerkant robot

STATUS: laatste missie nog checken
TESTDATUM/ROBOT: 26/01/2026 - hub1
BATTERIJ % BIJ START: 91%
---------------
"""
async def missie_groenA_start():
    await multitask(rechterarm_draai(50), vooruit(700,1000,500))
    await draai_rechts_met_straal(90,-75)
    await achteruit(50)
    await rechterarm_draai(-45)
    await vooruit(150)
    await rechterarm_draai(50)
    await draai_rechts_met_straal(90,-200)
    await achteruit(300,1000,1000)
    await vooruit(180)
    await rechts(90)
    await rechterarm_draai(-55)
    await vooruit(160)
    await rechterarm_draai(45)
    await achteruit(160)
    await links(90)
    await vooruit(100,800,400)
    await links(90)
    await linkerarm_draai(60)
    await vooruit(250)
    await rechts(90)
    await vooruit(70)
    await rechterarm_draai(-55)
    await achteruit(150)
    await rechterarm_draai(-25)
    await vooruit(120)
    await achteruit(20)
    await links(45)
    await vooruit(10)
    await rechterarm_draai(100)
    await achteruit(50)
    await links(45)
    await vooruit(300,800,400)
    await rechts(2)
    await multitask(linkerarm_draai(-150), vooruit(640))
    await links(45)
    await achteruit(80)
    await linkerarm_draai(80)
    await rechts(125)
    await vooruit(700)
   
# Deze regel zorgt ervoor dat de code uitgevoerd wordt
# verander enkel de naam van jouw missie, maar laat de code verder zoals ze is
if __name__ == "__main__":
    run_task(missie_groenA_start())
