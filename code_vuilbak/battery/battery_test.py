from pybricks.hubs import PrimeHub
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub()
# This is a linear approximation. 
# The real battery discharge curve is nonlinear, especially near the low end.
# For a more accurate reading, Pybricks does not (currently) 
# expose a native battery percentage function.

def get_battery_percentage():
    voltage = hub.battery.voltage()  # in millivolts
    # Clamp voltage to avoid values outside expected range
    voltage = max(6200, min(8200, voltage))
    percent = (voltage - 6200) / (8200 - 6200) * 100
    return round(percent)

# Example usage
while True:
    print("Battery:", get_battery_percentage(), "%")
    wait(5000)
