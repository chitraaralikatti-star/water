import os

class WaterTankMonitor:
    def __init__(self):
        self.usage = {}

    def record_usage(self, slot, liters):
        self.usage[slot] = liters

    def usage_level(self, slot):
        liters = self.usage.get(slot, 0)
        if liters < 500:
            return "LOW"
        elif liters <= 1000:
            return "MEDIUM"
        else:
            return "HIGH"

    def best_usage_slot(self):
        return min(self.usage, key=self.usage.get)


# Jenkins entry point
if __name__ == "__main__":
    slot = os.getenv("USAGE_SLOT")
    liters = os.getenv("WATER_LITERS")

    if not slot or not liters:
        print("ERROR: Jenkins parameters missing")
        exit(1)

    liters = int(liters)

    monitor = WaterTankMonitor()
    monitor.record_usage(slot, liters)

    print("Time Slot:", slot)
    print("Water Used:", liters, "liters")
    print("Usage Level:", monitor.usage_level(slot))
