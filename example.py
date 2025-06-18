import asyncio
from dex_tracker import DexTracker

async def main():
    tracker = DexTracker()

    # Set event handlers
    def on_trade(trade):
        print(f"New trade: {trade}")

    def on_connected(data):
        print(f"Connected to DexTracker: {data}")

    def on_error(error):
        print(f"DexTracker error: {error}")

    def on_disconnected(data):
        print(f"Disconnected: {data}")

    def on_reconnecting(data):
        print(f"Reconnecting attempt {data['attempt']}")

    tracker.set_on_trade(on_trade)
    tracker.set_on_connected(on_connected)
    tracker.set_on_error(on_error)
    tracker.set_on_disconnected(on_disconnected)
    tracker.set_on_reconnecting(on_reconnecting)

    # Connect to track BSC address
    await tracker.connect('0x74836cc0e821a6be18e407e6388e430b689c66e9')

    # Optional: Disconnect after 60 seconds
    await asyncio.sleep(60)
    await tracker.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
