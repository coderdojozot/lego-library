from functies import *
# dit is voor missie 
async def missie_groenB_start():
    await rechterarm_draai(400)
    await rechterarm_draai(-400)


if __name__ == "__main__":
    run_task(missie_groenB_start())

