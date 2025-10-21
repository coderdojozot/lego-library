from functies import *
# dit is voor missie 5 en 6
async def missie_groen_start():
    await rechterarm_draai(300)
    await vooruit(750)
    await links(45)
    await rechterarm_draai(-20)
    await vooruit(120)
    await links(15)
    await achteruit(50)
    await rechterarm_draai(-100)
    await links(30)
    await vooruit(100)
    await vooruit(1000)
    await rechterarm_draai(120)
    await rechts(45)
    await vooruit(120)
    await links(45)
    await vooruit(200)
    await rechterarm_draai(-120)


# laat dit zeker staan!
if __name__ == "__main__":
    run_task(missie_groen_start())