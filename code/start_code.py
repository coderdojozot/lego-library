from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait

# Initialize hub
hub = PrimeHub()

# Test sequence with multiple colors
print("Starting connection test...")

# Try different colors to make sure we're connected
for color in [Color.RED, Color.GREEN, Color.BLUE]:
    print(f"Setting light to {color}")
    hub.light.on(color)
    wait(1000)

print("Connection test completed!")