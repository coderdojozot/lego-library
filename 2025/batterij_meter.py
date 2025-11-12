from pybricks.hubs import PrimeHub
from pybricks.tools import wait

hub = PrimeHub()

# Get the battery voltage and calculate the percentage
voltage = hub.battery.voltage()
battery_percentage = (voltage / 8400) * 100

print(f"Battery Voltage: {voltage} mV")
print(f"Battery Percentage: {battery_percentage:.2f}%")

# A more precise calculation can be made by checking the voltage
# across a few full charges and taking the average of the maximum voltages
# For a full charge, the voltage is around 8.4 volts or 8400 millivolts.
# This can be used as a constant in your calculations.
# battery_percentage = hub.battery.voltage() / 8.4
