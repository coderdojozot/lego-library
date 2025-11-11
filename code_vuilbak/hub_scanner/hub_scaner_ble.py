import asyncio
from bleak import BleakScanner

async def main():
    print("🔍 Scanning for Bluetooth LE devices (10 seconds)...")
    devices = await BleakScanner.discover(timeout=10.0)
    if not devices:
        print("⚠️  Geen apparaten gevonden.")
    else:
        print("\nGevonden apparaten:")
        for d in devices:
            print(f"- {d.name or 'Onbekend'} ({d.address})")

asyncio.run(main())