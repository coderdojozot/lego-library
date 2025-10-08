from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.tools import wait, StopWatch
from rijden_met_gyro_versie_lukas import gyro_rechtdoor, draai_met_yaw
hub = PrimeHub()

left_attachment_motor = Motor(port=Port.F)
right_attachment_motor = Motor(port=Port.B)
gyro_rechtdoor(600, 700, 690)
draai_met_yaw(500, 35)
gyro_rechtdoor(700, 85, 0)
draai_met_yaw(500, 45)
gyro_rechtdoor(-500, 50, 0)
left_attachment_motor.run(500)
wait(500)
left_attachment_motor.stop()