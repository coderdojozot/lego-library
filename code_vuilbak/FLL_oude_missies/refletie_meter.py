from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

sensor = ColorSensor(Port.D)

while True:
    value = sensor.reflection()
    print(value)
    wait(200)
        