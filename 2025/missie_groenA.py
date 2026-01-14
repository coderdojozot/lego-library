from functies import *

"""
---------------
BOUWERS: Lennert - Lucas
MISSIE(S): 1 (surface brussing)- 6 (rotsblokken) - 14 (borstel) - 5 (schuine vloer)
PUNTEN: 10 + 10 , 10, 5, 30

STARTVELD: LINKS
STARTPOSITIE: 2de linkse zwarte streepje, linkerkant robot

STATUS: werkte volledig
TESTDATUM/ROBOT: (14/01/2026 - hub1)
BATTERIJ % BIJ START: 97,63%
---------------
"""
async def missie_groenA_start():
    await rechterarm_draai(50)
    await vooruit(700,1000,500)
    await achteruit(200)
    await vooruit(250)
    await draai_rechts_met_straal(90,-125)
    await rechterarm_draai(-45)
    wait(70)
    await vooruit(20,200)
    await rechts(5)
    await vooruit(110)
    await rechterarm_draai(50)
    await draai_rechts_met_straal(90,-200)
    await achteruit(350,1000,1000)
    await vooruit(180)
    await draai_links_met_straal(45,200)
    await rechterarm_draai(-100)
    await multitask(links(10), rechterarm_draai(20))
    await multitask(rechts(10), rechterarm_draai(-20))
    await rechterarm_draai(50)
    await achteruit(80)
    await linkerarm_draai(-135)
    await links(45)
    await achteruit(200)
    await links(5)
    await vooruit(1340,800,400)
    await multitask(rechterarm_draai(50),linkerarm_draai(49))
    await links(55)
    await achteruit(140)
    await rechts(10)
    await linkerarm_draai(140)
    await vooruit(175)
    await links(45)
    await achteruit(600)
    await links(20)
    await achteruit(200)
    # await vooruit(100)
    # await links(90)
   
# Deze regel zorgt ervoor dat de code uitgevoerd wordt
# verander enkel de naam van jouw missie, maar laat de code verder zoals ze is
if __name__ == "__main__":
    run_task(missie_groenA_start())
