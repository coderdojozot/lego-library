# Nodige onderdelen uit Pybricks
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase



hub = PrimeHub()

motorRechts = Motor(Port.A)
motorLinks = Motor(Port.E, Direction.COUNTERCLOCKWISE)

WHEEL_CIRCUMFERENCE = 196.0  

def mm_to_degrees(mm):
    return (360 * mm) / WHEEL_CIRCUMFERENCE

def gyro_rechtdoor(speed, afstand_mm, acceleration):
    # Reset sensoren
    hub.imu.reset_heading(0)
    motorLinks.reset_angle(0)
    motorRechts.reset_angle(0)

    # Als acceleration = 0, gebruik standaardinstellingen (geen beperking)
    if acceleration > 0:
        motorLinks.control.limits(speed, acceleration)
        motorRechts.control.limits(speed, acceleration)
    else:
        motorLinks.control.limits(None, None)
        motorRechts.control.limits(None, None)

    target_deg = mm_to_degrees(afstand_mm)
    start_yaw = hub.imu.heading()
    Kp = 0.5

    while abs(motorLinks.angle()) < target_deg:
        yaw = hub.imu.heading()
        error = start_yaw - yaw
        correction = Kp * error

        motorLinks.run(speed + correction)
        motorRechts.run(speed - correction)

        print("Yaw:", yaw, "Error:", error)
        wait(10)

    motorLinks.stop()
    motorRechts.stop()
def draai_met_yaw(speed, hoek):
    hub.imu.reset_heading(0)
    start_yaw = hub.imu.heading()         # beginhoek
    target_yaw = start_yaw + hoek         # doelhoek

    Kp = 8  # hoe sterk hij corrigeert (probeer tussen 2 en 10)

    while True:
        yaw = hub.imu.heading()           # huidige hoek
        print(yaw, 'yaw')
        error = target_yaw - yaw          # verschil met doel

        # Als de fout heel klein is (±2°) → stoppen
        if abs(error) < 0.05:
            break

        # Correctiesnelheid berekenen
        turn_speed = Kp * error

        # Beperk de snelheid tot de max (positief of negatief)
        if turn_speed > speed:
            turn_speed = speed
        if turn_speed < -speed:
            turn_speed = -speed

        # Motoren draaien in tegengestelde richting
        motorLinks.run(turn_speed)
        motorRechts.run(-turn_speed)

        wait(10)

    # Motoren stoppen netjes
    motorLinks.stop()
    motorRechts.stop()




