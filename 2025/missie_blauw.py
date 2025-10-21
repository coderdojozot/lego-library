from functies import *

async def missie_blauw_start():
    await vooruit(100)
    await achteruit(100)
    await vooruit(100,snelheid=50)

if __name__ == "__main__":
    run_task(missie_blauw_start())
