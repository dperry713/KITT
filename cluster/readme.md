# KITT Instrument Cluster

A modern, futuristic instrument cluster interface for vehicles using OBD-II data. This project creates a digital dashboard display with real-time vehicle metrics, data logging, and voice alerts.

## Features

- Real-time OBD-II data visualization
- Customizable PID display selection
- Visual gauges and histograms
- Voice alerts for threshold warnings
- Data logging to CSV
- Touch interface support
- Cross-platform compatibility (Windows & Raspberry Pi)

## Requirements

- Python 3.x
- OBD-II adapter
- Display screen (800x480 resolution recommended)

### Dependencies

```bash
pip install obd pygame pyttsx3



For Raspberry Pi, additional GPIO library:

pip install RPi.GPIO



Usage
Connect your OBD-II adapter to your vehicle
Run the instrument cluster:
python instrument_cluster.py



Display Interface
Main screen shows real-time gauges and histogram
Touch the top-right corner to access PID selection menu
Select/deselect PIDs by touching them
Press Enter to return to main display
Data Logging
The system automatically logs all PID data to datalog.csv with timestamps.

Configuration
PID thresholds and commands can be configured in pid_config.py

Hardware Setup
Raspberry Pi Configuration
Connect display via HDMI
Connect OBD-II adapter via USB
Ensure proper GPIO connections if using additional hardware
Windows Configuration
Connect display normally
Connect OBD-II adapter via USB
Contributing
Feel free to submit issues and pull requests to enhance the functionality.