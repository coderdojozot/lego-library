from functies import *

# Simon - Arthur - Lennert
# dit is voor missie 11 - enkel terugrijden nog
async def missie_geelB_start():
    await draai_rechts_met_straal(90,300)
    await vooruit(578)
    await rechts(90)
    await vooruit(150)
    await links(15)
    await rechterarm_draai(2400)
    await achteruit(150)
    await links(90)

if __name__ == "__main__": 
    run_task(missie_geelB_start())
