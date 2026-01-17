from functies import *

"""
---------------
BOUWERS: Simon - Arthur - Lennert
MISSIE(S): 11 (kraan)
PUNTEN: 20 + 10

STARTVELD: LINKS
STARTPOSITIE: Rechts 2de zwarte streepje, rechterkant robot

STATUS: rijd nog niet terug, combineren met blauwA? of missie herbouwen en van rechts starten
TESTDATUM/ROBOT: 26/11/2025 - hub1
BATTERIJ % BIJ START: xxx
---------------
"""

async def missie_geelB_start():
    await draai_rechts_met_straal(90,300)
    await vooruit(608)
    await rechts(90)
    await vooruit(150)
    await links(20)
    await rechterarm_draai(2400)
    await achteruit(274)
    await rechts(110)
    await vooruit(600)
    await draai_links_met_straal(90,300)

# Deze regel zorgt ervoor dat de code uitgevoerd wordt
# verander enkel de naam van jouw missie, maar laat de code verder zoals ze is
if __name__ == "__main__": 
    run_task(missie_geelB_start())
