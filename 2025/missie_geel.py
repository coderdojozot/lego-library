from functies import *

# in deze functie komt alle code voor de missie
async def missie_geel_start():
   await vooruit(300)
   await rechterarm_draai(180)
   await multitask(vooruit(-100), rechterarm_draai(720))
   await achteruit(200, 500, 500)


# laat dit zeker staan!
if __name__ == "__main__":
    run_task(missie_geel_start())
