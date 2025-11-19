from functies import *

# Arthur
# dit is voor missie 12 -- werkt volledig
async def missie_blauw_start():
    await vooruit(300)
    await rechterarm.run_angle(600, -182)
    await achteruit(50)
    await rechterarm.run_angle(600, 180)
    await links(90)
    await vooruit(200)
    await rechts(90)
    await vooruit(250)
    await achteruit(750)

if __name__ == "__main__":
    run_task(missie_blauw_start())
