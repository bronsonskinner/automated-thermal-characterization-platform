"""
main.py

Project:
    Raspberry Pi–Based Automated Thermal Characterization Platform

Author:
    Bronson Skinner

Description:
    Main application entry point for the automated thermal
    characterization platform.

    Responsibilities:
        • Initialize the application
        • Discover connected temperature sensors
        • Create the experiment data logger
        • Continuously acquire temperature measurements
        • Display live measurements
        • Store results to CSV
        • Handle graceful program termination

Version:
    2.0
"""

import time

import config
from data_logger import DataLogger
from sensor_manager import SensorManager


# ============================================================
# Display Functions
# ============================================================

def print_banner() -> None:
    """
    Display the application banner.
    """

    print()
    print("=" * 60)
    print(config.PROJECT_NAME)
    print(f"Version {config.VERSION}")
    print("=" * 60)
    print()


def display_measurements(temperature_data: dict) -> None:
    """
    Display one complete set of temperature measurements.
    """

    print(config.PRINT_SEPARATOR)

    for sensor_name, values in temperature_data.items():

        print(sensor_name)

        if config.SHOW_CELSIUS:
            print(
                f"  Celsius:     "
                f"{values['celsius']:.2f} °C"
            )

        if config.SHOW_FAHRENHEIT:
            print(
                f"  Fahrenheit:  "
                f"{values['fahrenheit']:.2f} °F"
            )

        print()

    print(config.PRINT_SEPARATOR)
    print()


# ============================================================
# Main Application
# ============================================================

def main() -> None:
    """
    Execute the automated thermal characterization platform.
    """

    print_banner()

    print("Initializing system...")
    print()

    sensor_manager = SensorManager()

    print("Discovering connected temperature sensors...")

    sensor_manager.discover_sensors()

    sensor_manager.verify_sensor_count()

    print(
        f"{sensor_manager.get_sensor_count()} "
        "temperature sensors detected."
    )

    print()

    print("Initializing data logger...")

    logger = DataLogger()

    print(
        "Logging data to:"
    )

    print(
        f"  {logger.get_output_file()}"
    )

    print()

    print(
        "Beginning automated temperature acquisition..."
    )

    print()

    try:

              while True:

            temperature_data = (
                sensor_manager.read_all_temperatures()
            )

            display_measurements(
                temperature_data
            )

            logger.log(
                temperature_data
            )

            time.sleep(
                config.SAMPLE_INTERVAL_SECONDS
            )

    except KeyboardInterrupt:

        print()
        print(
            "Temperature acquisition stopped by user."
        )

    finally:

        print(
            "Program terminated successfully."
        )


if __name__ == "__main__":
    main()
