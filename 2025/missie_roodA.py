from functies import *

"""
---------------
BOUWER(S): Nathan - Lukas
MISSIE(S): 3 (Map Reveal)
PUNTEN: 10

STARTVELD: LINKS
STARTPOSITIE: derde dikke zwarte streepje van links

STATUS: groen gras meenemen of in het midden leggen werkt nog niet. LICHTBLAUW vervangen door PAARS!!
TESTDATUM/ROBOT: 20/12/2025 - hub1 
BATTERIJ % BIJ START: xxx
---------------
"""

async def missie_roodA_start():
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


# Deze regel zorgt ervoor dat de code uitgevoerd wordt
# verander enkel de naam van jouw missie, maar laat de code verder zoals ze is
if __name__ == "__main__":
    run_task(missie_roodA_start())
