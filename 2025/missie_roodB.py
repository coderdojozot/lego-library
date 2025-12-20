from functies import *

"""
---------------
BOUWERS: Robi & Lukas
MISSIE(S): 8 (silo muur) - 13 (dino standbeeld)
PUNTEN: 10x3, 30

STARTVELD: RECHTS
STARTPOSITIE: 2de rechtse zwarte streepje, rechterkant robot

STATUS: silo werkt, dino nog niet volledig (harder slaan, of met volle batterij testen)
TESTDATUM/ROBOT: 20/12/2025 - hub1
BATTERIJ % BIJ START: xxx
---------------
"""

frequentie = 50
duur = 300

async def missie_roodB_start():
     await achteruit(15)
     await vooruit(435)
     await multitask(linkerarm.run_angle(1000,-200),rechterarm.run_angle(1000,-200))  #tandwielenc uit silo 
     await hub.speaker.beep(frequentie, duur)
     await multitask(linkerarm.run_angle(1000,200),rechterarm.run_angle(1000,200))
     await multitask(linkerarm.run_angle(1000,-200),rechterarm.run_angle(1000,-200))
     await hub.speaker.beep(frequentie, duur)
     await multitask(linkerarm.run_angle(1000,200),rechterarm.run_angle(1000,200))
     await multitask(linkerarm.run_angle(1000,-200),rechterarm.run_angle(1000,-200))
     await hub.speaker.beep(frequentie, duur)
     await multitask(linkerarm.run_angle(1000,200),rechterarm.run_angle(1000,200))      #done
     await vooruit(-100)                                 #rijden naar dino skelet
     await draai_links_met_straal(90,400)
     await vooruit(296)
     await links(44)
     await vooruit(178)                          #done
     await multitask(linkerarm.run_angle(1000,-240),rechterarm.run_angle(1000,-250)) #dino skelet omhoog
     rechterarm.hold()    
     await vooruit(40)
     #await multitask(linkerarm.run_angle(1000,240),rechterarm.run_angle(1000,250))       #done

# Deze regel zorgt ervoor dat de code uitgevoerd wordt
# verander enkel de naam van jouw missie, maar laat de code verder zoals ze is
if __name__ == "__main__":
    run_task(missie_roodB_start())