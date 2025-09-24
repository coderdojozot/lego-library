# Nodige onderdelen uit Pybricks
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

hub = PrimeHub()

motorRechts = Motor(Port.D)
motorLinks = Motor(Port.E, Direction.COUNTERCLOCKWISE)

WHEEL_CIRCUMFERENCE = 196.0  

def mm_to_degrees(mm):
    return (360 * mm) / WHEEL_CIRCUMFERENCE

def gyro_rechtdoor(speed, afstand_mm):

    hub.imu.reset_heading(0)
    motorLinks.reset_angle(0)
    motorRechts.reset_angle(0)

    start_yaw = hub.imu.heading()

    Kp = 1

    target_deg = mm_to_degrees(afstand_mm)

    while abs(motorLinks.angle()) < target_deg:

        yaw = hub.imu.heading()
        print(yaw, 'yaw')

        error = start_yaw - yaw

        correction = Kp * error

        if abs(error) > 5:
            correction *= 1.5

        motorLinks.run(speed + correction)
        motorRechts.run(speed - correction)

        wait(1)

    motorLinks.stop()
    motorRechts.stop()

gyro_rechtdoor(500, 1000)
