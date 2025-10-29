from functies import *

async def missie_blauw_start():
    await vooruit(100)

if __name__ == "__main__":
    run_task(missie_blauw_start())
