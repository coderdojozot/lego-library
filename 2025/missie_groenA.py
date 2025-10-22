from functies import *
# dit is voor missie 5 en 6
async def missie_groenA_start():
    await rechterarm_draai(295)
    await vooruit(755)
    await links(45)
    await rechterarm_draai(-5)
    await vooruit(90)
    await links(20)
    await achteruit(50)
    await links(25)
    await vooruit(100)
    await vooruit(1000)
    await rechterarm_draai(10)
    await rechts(45)
    await vooruit(170)
    await links(45)
    await vooruit(200)
    await rechterarm_draai(-120)
    await achteruit(100)
    await links(90)
    await vooruit(1000)


# laat dit zeker staan!
if __name__ == "__main__":
    run_task(missie_groenA_start())
