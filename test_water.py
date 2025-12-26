from water import WaterTankMonitor

def test_low_usage():
    w = WaterTankMonitor()
    w.record_usage("Morning", 300)
    assert w.usage_level("Morning") == "LOW"

def test_medium_usage():
    w = WaterTankMonitor()
    w.record_usage("Afternoon", 800)
    assert w.usage_level("Afternoon") == "MEDIUM"

def test_high_usage():
    w = WaterTankMonitor()
    w.record_usage("Night", 1500)
    assert w.usage_level("Night") == "HIGH"

def test_best_slot():
    w = WaterTankMonitor()
    w.record_usage("Morning", 700)
    w.record_usage("Night", 200)
    assert w.best_usage_slot() == "Night"

