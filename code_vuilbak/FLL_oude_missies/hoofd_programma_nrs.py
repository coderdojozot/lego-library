# from functies import *
# from missie_blauwA import missie_blauwA_start
# from missie_groenA import missie_groenA_start
# from missie_geelA import missie_geelA_start
# from missie_geelB import missie_geelB_start
# from missie_oranjeA import missie_oranjeA_start
# from missie_paarsA import missie_paarsA_start
# from missie_paarsB import missie_paarsB_start
# from pybricks.pupdevices import ColorSensor
# from pybricks.parameters import Port
# from pybricks.tools import wait

# ##########################################################################
# ##  NIKS AAN HET HOOFDPROGRAMMA VERANDEREN ZONDER OVERLEG MET IEDEREEN  ##
# ##########################################################################
# sensor = ColorSensor(Port.D)

# laatste_reflection = -1

# # Reflection value ranges for different colors
# paars = [12, 13, 14]
# groen = [5, 6, 7]
# geel = [39, 40, 41]
# orange = [8, 9, 10]
# blauw = [10, 11, 12]

# while True:
#     value = sensor.reflection()
#     print(value)
    
#     # Skip if same reflection value as before (to avoid repeated triggers)
#     if value == laatste_reflection:
#         continue
#     laatste_reflection = value    
    
#     if value in groen:
#         hub.light.blink(Color.GREEN,[500,500])
#         selected = hub_menu("A")  
       
#         if selected == "A":
#             hub.light.on(Color.GREEN)
#             run_task(missie_groenA_start())
#             hub.light.off()
#             hub.display.off()
        
#     if value in blauw:
#         hub.light.blink(Color.BLUE,[500,500])
#         selected = hub_menu("A")  
#         if selected == "A":
#             hub.light.on(Color.BLUE)
#             run_task(missie_blauwA_start())
#             hub.light.off()
#             hub.display.off()

#     if value in geel:
#         hub.light.blink(Color.YELLOW,[500,500])
#         selected = hub_menu("A", "B")  
#         if selected == "A":
#              hub.light.on(Color.YELLOW)
#              run_task(missie_geelA_start())
#              hub.light.off()
#              hub.display.off()
#         if selected == "B":
#              hub.light.on(Color.YELLOW)
#              run_task(missie_geelB_start())
#              hub.light.off()
#              hub.display.off()
    
#     if value in paars:
#         hub.light.blink(Color.MAGENTA,[500,500])
#         selected = hub_menu("A", "B")  
#         if selected == "A":
#              hub.light.on(Color.MAGENTA)
#              run_task(missie_paarsA_start())
#              hub.light.off()
#              hub.display.off()
#         if selected == "B":
#              hub.light.on(Color.MAGENTA)
#              run_task(missie_paarsB_start())
#              hub.light.off()
#              hub.display.off()
    
#     if value in orange:
#         hub.light.blink(Color.ORANGE,[500,500])
#         selected = hub_menu("A")  
#         if selected == "A":
#              hub.light.on(Color.ORANGE)
#              run_task(missie_oranjeA_start())
#              hub.light.off()
#              hub.display.off()
