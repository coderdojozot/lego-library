from functies import *
# dit is voor missie 
async def missie_groenB_start():
    await rechterarm_draai(50)
    await vooruit(700,1000,500)
    await achteruit(200)
    await vooruit(250)
    await draai_rechts_met_straal(90,-125)
    await rechterarm_draai(-47)
    wait(50)
    await vooruit(20,200)
    await rechts(5)
    await vooruit(100)
    await rechterarm_draai(50)
    await achteruit(100)
    await rechts(180)
    await vooruit(100)
    await rechterarm_draai(-68)
    await achteruit(150)
    await rechts(90)
    await vooruit(500)

if __name__ == "__main__":
    run_task(missie_groenB_start())
