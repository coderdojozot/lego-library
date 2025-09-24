from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.tools import wait, StopWatch
timer = StopWatch()
hub = PrimeHub()
motorRechts = Motor(Port.D)
motorLinks = Motor(Port.E, Direction.COUNTERCLOCKWISE)

def draai_met_yaw(speed, hoek):
    start_yaw = hub.imu.heading()         # beginhoek
    target_yaw = start_yaw + hoek         # doelhoek

    Kp = 6  # hoe sterk hij corrigeert (probeer tussen 2 en 10)

    while True:
        yaw = hub.imu.heading()           # huidige hoek
        print(yaw, 'yaw', timer.time(), 'time"')
        error = target_yaw - yaw          # verschil met doel

        # Als de fout heel klein is (±2°) → stoppen
        if abs(error) < 0.5:
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


draai_met_yaw(500, 90)#(speed, hoek)

