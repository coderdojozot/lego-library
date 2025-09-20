from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase  
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
yaw = 0
motorRechts = Motor(Port.D)
motorLinks = Motor(Port.E)
def gyro_rechtdoor(speed, angle):
    motorLinks.reset_angle()
    hub.imu.reset_heading(0)
    motorRechts.run(speed)
    motorLinks.run(-speed)
    
    yaw = hub.imu.heading()
    print(yaw, ' yaw')
    while abs(motorLinks.angle()) < angle:
        print(motorLinks.angle())
        while yaw > 0.1 or yaw < -0.1:
            yaw = hub.imu.heading()
            while yaw < -0.1:
                motorLinks.stop()
                motorLinks.run(-500-(abs(yaw)*100))
                yaw = hub.imu.heading()
                print(yaw, ' yaw')
            yaw = hub.imu.heading()
            while yaw > 0.1:
                motorRechts.stop()
                motorRechts.run(500+(yaw*100))
                yaw = hub.imu.heading()
                print(yaw, ' yaw')
    #while yaw > 0.1 or yaw < -0.1:
        #while yaw < -0.1:
            #motorLinks.stop()
            #motorLinks.run(-500-(abs(yaw)*100))
            #yaw = hub.imu.heading()
            #print(yaw, ' yaw')
        #while yaw > 0.1:
            #motorRechts.stop()
            #motorRechts.run(500+(yaw*100))
            #yaw = hub.imu.heading()
            #print(yaw, ' yaw')          
    yaw = hub.imu.heading()
    print(yaw)
    motorLinks.stop()
    motorRechts.stop()


gyro_rechtdoor(500, 1080)
