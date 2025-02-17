# Configuration for available PIDs and their thresholds

PIDS = {
    'RPM': {'command': 'RPM', 'threshold': 6000},
    'SPEED': {'command': 'SPEED', 'threshold': 100},
    'COOLANT_TEMP': {'command': 'COOLANT_TEMP', 'threshold': 220},
    'OIL_TEMP': {'command': 'OIL_TEMP', 'threshold': 120},
    'OIL_PRESSURE': {'command': 'OIL_PRESSURE', 'threshold': 30},
    'BaTTERY_VOLTAGE': {'command': 'BATTERY_VOLTAGE', 'threshold': 14},
    # Add more PIDs as needed
}

# Default PIDs to display
DEFAULT_PIDS = ['RPM', 'SPEED', 'COOLANT_TEMP', 'OIL_TEMP', 'OIL_PRESSURE', 'BaTTERY_VOLTAGE']