"""
config.py

Project:
    Raspberry Pi–Based Automated Thermal Characterization Platform

Author:
    Bronson Skinner

Description:
    Central configuration file for the automated thermal
    characterization platform.

    All configurable project settings are stored here to keep the
    remainder of the software clean, readable, and maintainable.

Version:
    2.0
"""

from pathlib import Path

# ============================================================
# PROJECT INFORMATION
# ============================================================

PROJECT_NAME = "Automated Thermal Characterization Platform"
VERSION = "2.0"

# ============================================================
# TEMPERATURE SENSOR SETTINGS
# ============================================================

# Number of sensors expected for this experiment.
EXPECTED_SENSOR_COUNT = 5

# Enable automatic discovery of connected DS18B20 sensors.
AUTO_DISCOVER_SENSORS = True

# ============================================================
# DATA ACQUISITION SETTINGS
# ============================================================

# Time between consecutive measurements (seconds).
SAMPLING_INTERVAL = 5

# ============================================================
# OUTPUT SETTINGS
# ============================================================

# Directory where CSV log files will be stored.
OUTPUT_DIRECTORY = Path("data")

# Automatically create the directory if it does not exist.
OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)

# CSV filename.
CSV_FILENAME = OUTPUT_DIRECTORY / "temperature_log.csv"

# ============================================================
# DISPLAY SETTINGS
# ============================================================

SHOW_CELSIUS = True
SHOW_FAHRENHEIT = True

# Number of decimal places displayed.
TEMPERATURE_PRECISION = 2

# ============================================================
# SYSTEM SETTINGS
# ============================================================

# Linux One-Wire device directory.
ONEWIRE_DIRECTORY = Path("/sys/bus/w1/devices")

# DS18B20 device folders begin with "28-".
DEVICE_PREFIX = "28-"

# ============================================================
# LOGGING
# ============================================================

ENABLE_CONSOLE_OUTPUT = True

PRINT_SEPARATOR = "-" * 70
