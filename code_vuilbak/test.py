from pybricks.hubs import PrimeHub           
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()

motor_rechts = Motor(Port.E)
motor_links = Motor(Port.F)

rijden = DriveBase(motor_links, motor_rechts, 56, 127)  
rijden.use_gyro(True)
hub.display.number(9)
rijden.drive(1000, 500)
wait(1000)