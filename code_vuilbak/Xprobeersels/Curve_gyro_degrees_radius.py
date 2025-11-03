from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait, multitask, run_task

# Initialize both motors. In this example, the motor on the
# left must turn counterclockwise to make the robot go forward.
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
hub = PrimeHub()
# Initialize the drive base. In this example, the wheel diameter is 56mm.
# The distance between the two wheel-ground contact points is 112mm.
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=88, axle_track=126)
drive_base.reset()
drive_base.use_gyro(True)
async def status():
    while True:
        print('afstand ' + str(drive_base.distance()) + ' angle ' + str(drive_base.angle()))
async def run():
    for teller in range(8):
        drive_base.straight(600)
        drive_base.turn(90)
async def main():
    await multitask(status(), run())
run_task(main())