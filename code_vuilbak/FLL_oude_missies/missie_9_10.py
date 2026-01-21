from functies import *

"""
---------------
BOUWERS: 
MISSIE(S): 9 - 10
PUNTEN: 

STARTVELD: RECHTS
STARTPOSITIE: streepje 3.1 van rechts, rechterkant robot

STATUS: Deze missie kan gecombineerd worden met Blauw A - Hier bestaat geen stuk meer voor!!!
TESTDATUM/ROBOT: 
BATTERIJ % BIJ START: xxx
---------------
"""

async def missie_9_10_start():     
    
           # molen ARM
    await multitask(vooruit(770),linkerarm_draai(-1000))
    await rechts (50)
    await linkerarm(950)
    await vooruit(50)
    await linkerarm_draai(-1200)
    await links(93)
    await rechterarm_draai(260)
    await vooruit(150)
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
    await links(10)
    await vooruit(7000)  

# Deze regel zorgt ervoor dat de code uitgevoerd wordt
# verander enkel de naam van jouw missie, maar laat de code verder zoals ze is
if __name__ == "__main__":
    run_task(missie_9_10_start())
