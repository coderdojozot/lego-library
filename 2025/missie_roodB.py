from functies import *

# Robi, nog bezig
# Startveld rechts, 2de zwart streepje van rechts

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
     await vooruit(260)
     await links(45)
     await vooruit(200)
     await multitask(linkerarm.run_angle(1000,-168),rechterarm.run_angle(1000,-168))
     await multitask(linkerarm.run_angle(1000,168),rechterarm.run_angle(1000,168)) 
# Deze regel zorgt ervoor dat de code uitgevoerd wordt
# verander enkel de naam van jouw missie, maar laat de code verder zoals ze is

if __name__ == "__main__":
    run_task(missie_roodB_start())

#  Code werkt! Klaar op 19/11/25