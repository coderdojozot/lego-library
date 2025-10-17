from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait

# Initialize hub
hub = PrimeHub()

# Simple test sequence
print("Starting connection test...")
hub.light.on(Color.GREEN)
wait(1000)
print("Connection successful!")