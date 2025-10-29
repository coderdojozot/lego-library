from functies import *

# in deze functie komt alle code voor de missie
async def missie_geel_start():
   await vooruit(695)
   await rechts(85)
   await vooruit(355)
   await links(78)
   await multitask(vooruit(2),rechterarm.run_angle(900,-1650))
   await rechterarm.run_angle(2100,1650)
   await rechts(72)
   await multitask(vooruit(620),rechterarm.run_angle(900,-1650))
   await rechts(95)
   await rechterarm.run_angle(900,1650)
   await achteruit(25)
   await multitask(rechterarm.run_angle(900,-150),links(42))
   await vooruit(350)
   await achteruit(220)
   await links(8)
   await multitask(rechterarm.run_angle(900,150),vooruit(900))


# laat dit zeker staan!
if __name__ == "__main__":
    run_task(missie_geel_start())
