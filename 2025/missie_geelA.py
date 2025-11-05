from functies import *

# Luca
# dit is voor missie 3, 9, 10 
async def missie_geelA_start():
   await vooruit(695)
   await rechts(85)
   await vooruit(362)
   await links(78)
   await multitask(vooruit(4),rechterarm.run_angle(900,-1670))
   await rechterarm.run_angle(2100,1670)
   await multitask(vooruit(2),rechts(70))
   await multitask(vooruit(625),rechterarm.run_angle(900,-1670))
   await rechts(89)
   await rechterarm.run_angle(900,1670)
   await achteruit(35)
   await multitask(rechterarm.run_angle(900,-150),links(29.5))
   await vooruit(302,900)
   await achteruit(220)
   await links(10)
   await vooruit(450)
   await rechts(45)
   await multitask(rechterarm.run_angle(900,150),vooruit(450))
   


# laat dit zeker staan!
if __name__ == "__main__":
    run_task(missie_geelA_start())
