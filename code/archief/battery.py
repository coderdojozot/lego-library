from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

# Initialize Voltage Sensor
voltage_sensor = hub.battery.voltage()

# Calibration data (replace with your actual values)
voltage_at_100_percent = 7.3  # Example
voltage_at_0_percent = 4.0 # Example

# Get current voltage
voltage = hub.battery.voltage()

# Calculate percentage (simple linear approximation)
percentage = ((voltage - voltage_at_0_percent) / (voltage_at_100_percent - voltage_at_0_percent)) * 100

print(f"Battery Percentage: {percentage:.2f}%")

# Estimate mAh (very basic - requires calibration)
# Assuming a 1000mAh battery and a linear drop
# You WILL need to calibrate this value!
mah_capacity = 2100
mah_remaining = mah_capacity * (percentage / 100)
print(f"Estimated mAh remaining: {mah_remaining:.2f} mAh")

wait(2000) # Wait 2 seconds before next reading