from functies import *

# in deze functie komt alle code voor de missie
async def missie_geel_start():
   await vooruit(695)
   await rechts(85)
   await vooruit(355)
   wait(100)
   await links(78)
   wait(100)
   await vooruit(2)
   await rechterarm.run_angle(900,-1650)
   await rechterarm.run_angle(900,1650)
   await rechts(72)
   await multitask(vooruit(620),rechterarm.run_angle(900,-1650))
   await rechts(95)
   await rechterarm.run_angle(900,1650)
   await multitask(rechterarm.run_angle(900,-150),links(45))
   await vooruit(300)
   await achteruit(100)
   await links(56)
   await vooruit(180)
   await rechts(90)
   await multitask(rechterarm.run_angle(900,-150),vooruit(800))


# laat dit zeker staan!
if __name__ == "__main__":
    run_task(missie_geel_start())
