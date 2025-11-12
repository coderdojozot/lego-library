from functies import *

# Dit is voorbeeldcode voor de start van een nieuw
# programma. Pas deze code aan voor jouw extensie.


# Robi, code is klaar.
# Startveld rechts, 2de zwart streepje van rechts

async def missie_roodB_start():
     await achteruit(15)
     await vooruit(440)
     await multitask(linkerarm.run_angle(1000,-168),rechterarm.run_angle(1000,-168))
     await multitask(linkerarm.run_angle(1000,168),rechterarm.run_angle(1000,168))
     await multitask(linkerarm.run_angle(1000,-168),rechterarm.run_angle(1000,-168))
     await multitask(linkerarm.run_angle(1000,168),rechterarm.run_angle(1000,168))
     await multitask(linkerarm.run_angle(1000,-168),rechterarm.run_angle(1000,-168))
     await multitask(linkerarm.run_angle(1000,168),rechterarm.run_angle(1000,168))
     await vooruit(-418)
     
# Deze regel zorgt ervoor dat de code uitgevoerd wordt
# verander enkel de naam van jouw missie, maar laat de code verder zoals ze is

if __name__ == "__main__":
    run_task(missie_roodB_start())
