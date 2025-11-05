from functies import *

# Dit is voorbeeldcode voor de start van een nieuw
# programma. Pas deze code aan voor jouw extensie.

async def missie_roodB_start():
     await vooruit(425)
     await multitask(linkerarm.run_angle(900,-168),rechterarm.run_angle(900,-168))
     await multitask(linkerarm.run_angle(900,168),rechterarm.run_angle(900,168))
     await multitask(linkerarm.run_angle(900,-168),rechterarm.run_angle(900,-168))
     await multitask(linkerarm.run_angle(900,168),rechterarm.run_angle(900,168))
     await multitask(linkerarm.run_angle(900,-168),rechterarm.run_angle(900,-168))
     await multitask(linkerarm.run_angle(900,168),rechterarm.run_angle(900,168))
     await vooruit(-418)
# Deze regel zorgt ervoor dat de code uitgevoerd wordt
# verander enkel de naam van jouw missie, maar laat de code verder zoals ze is
if __name__ == "__main__":
    run_task(missie_roodB_start())
