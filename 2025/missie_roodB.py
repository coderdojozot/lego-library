from functies import *

"""
---------------
BOUWERS: Robi
MISSIE(S): 8 (silo muur) - 13 (dino standbeeld)
PUNTEN: 10x3, 30
STARTPOSITIE: Rechter startveld, 2de rechtse zwarte streepje, rechterkant robot

STATUS: code voor standbeeld nog aanpassen
TESTDATUM/ROBOT: 26/11/2025 - hub1
---------------
"""

async def missie_roodB_start():
     await achteruit(15)
     await vooruit(435)
     await multitask(linkerarm.run_angle(1000,-168),rechterarm.run_angle(1000,-168))
     await multitask(linkerarm.run_angle(1000,168),rechterarm.run_angle(1000,168))
     await multitask(linkerarm.run_angle(1000,-168),rechterarm.run_angle(1000,-168))
     await multitask(linkerarm.run_angle(1000,168),rechterarm.run_angle(1000,168))
     await multitask(linkerarm.run_angle(1000,-168),rechterarm.run_angle(1000,-168))
     await multitask(linkerarm.run_angle(1000,168),rechterarm.run_angle(1000,168))
     await vooruit(-100)
     await draai_links_met_straal(90,400)
     await vooruit(296)
     await links(45)
     await vooruit(185)
     await multitask(linkerarm.run_angle(1000,-168),rechterarm.run_angle(1000,-168))
     await multitask(linkerarm.run_angle(1000,168),rechterarm.run_angle(1000,168)) 

if __name__ == "__main__":
    run_task(missie_roodB_start())