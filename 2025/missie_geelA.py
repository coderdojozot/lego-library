from functies import *

# Luca
# dit is voor missie 3, 9, 10 
# startveld link, 2de zwart streepje van links
async def missie_geelA_start():
   await vooruit(735)
   await rechts(85)
   await vooruit(362)
   await links(78)
   await multitask(vooruit(4),rechterarm.run_angle(900,-3000))    # Heffen mijnkarretje
   await multitask(vooruit(2),rechts(70))
   await vooruit(625)  # Arm omhoog
   await rechts(89)
   await vooruit(50)
   await rechterarm.run_angle(900,1670) 
   await achteruit(50)                        # Weegschaal omlaag
   await achteruit(35)
   await multitask(rechterarm.run_angle(900,-150),links(35))    # Arm omhoog
   await vooruit(270, 900)                                      # Omhoogduwen winkelding
   await wait(10)
   await achteruit(220)
   await links(10)
   await vooruit(450)
   await rechts(45)
   await multitask(rechterarm.run_angle(900,150),vooruit(450))
   


# laat dit zeker staan!
if __name__ == "__main__":
    run_task(missie_geelA_start())
