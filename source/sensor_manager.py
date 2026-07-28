"""
sensor_manager.py

Project:
    Raspberry Pi–Based Automated Thermal Characterization Platform

Author:
    Bronson Skinner

Description:
    Discovers and manages DS18B20 digital temperature sensors connected
    to the Raspberry Pi One-Wire interface.

    Responsibilities:
        • Automatically discover connected sensors
        • Verify expected sensor count
        • Read raw temperature data
        • Convert temperature units
        • Return structured temperature measurements

Version:
    2.0
"""

from pathlib import Path
from typing import Dict, List
import time

import config


class SensorManager:
    """
    Handles discovery and communication with DS18B20 temperature sensors.
    """

    def __init__(self) -> None:
        """
        Initialize the sensor manager.
        """

        self.device_directory = config.ONEWIRE_DIRECTORY
        self.device_prefix = config.DEVICE_PREFIX
        self.expected_sensor_count = config.EXPECTED_SENSOR_COUNT

        self.sensor_paths: List[Path] = []

    # ---------------------------------------------------------
    # Sensor Discovery
    # ---------------------------------------------------------

    def discover_sensors(self) -> List[Path]:
        """
        Discover all connected DS18B20 sensors.

        Returns
        -------
        list
            Sorted list of sensor directories.
        """

        sensors = sorted(
            path
            for path in self.device_directory.iterdir()
            if path.is_dir() and path.name.startswith(self.device_prefix)
        )

        self.sensor_paths = sensors

        return sensors

    def verify_sensor_count(self) -> bool:
        """
        Verify that the expected number of sensors has been detected.

        Returns
        -------
        bool
            True if enough sensors are connected.
        """

        if not self.sensor_paths:
            self.discover_sensors()

        sensor_count = len(self.sensor_paths)

        if sensor_count < self.expected_sensor_count:

            raise RuntimeError(
                f"Expected {self.expected_sensor_count} sensors, "
                f"but detected {sensor_count}."
            )

        return True

    # ---------------------------------------------------------
    # Raw Sensor Reading
    # ---------------------------------------------------------

    @staticmethod
    def _read_raw_file(sensor_path: Path) -> List[str]:
        """
        Read the raw One-Wire sensor file.

        Parameters
        ----------
        sensor_path : Path
            Path to the sensor directory.

        Returns
        -------
        list
            Raw text returned by the Linux One-Wire driver.
        """

        device_file = sensor_path / "w1_slave"

        with device_file.open("r") as file:
            lines = file.readlines()

        return lines

    def _wait_for_valid_crc(self, sensor_path: Path) -> List[str]:
        """
        Wait until the sensor returns a valid CRC reading.

        Parameters
        ----------
        sensor_path : Path

        Returns
        -------
        list
            Valid sensor output.
        """

        lines = self._read_raw_file(sensor_path)

        while not lines[0].strip().endswith("YES"):
            time.sleep(0.2)
            lines = self._read_raw_file(sensor_path)

        return lines

    # ---------------------------------------------------------
    # Temperature Processing
    # ---------------------------------------------------------

    @staticmethod
    def _extract_celsius(lines: List[str]) -> float:
        """
        Extract the Celsius temperature from a validated
        One-Wire sensor response.

        Parameters
        ----------
        lines : list
            Raw sensor output.

        Returns
        -------
        float
            Temperature in degrees Celsius.
        """

        equals_position = lines[1].find("t=")

        if equals_position == -1:
            raise RuntimeError(
                "Temperature value could not be located "
                "within the sensor response."
            )

        temperature_string = lines[1][equals_position + 2:]

        return float(temperature_string) / 1000.0

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """
        Convert Celsius to Fahrenheit.
        """

        return (celsius * 9.0 / 5.0) + 32.0

    # ---------------------------------------------------------
    # Public Interface
    # ---------------------------------------------------------

    def read_sensor(self, sensor_path: Path) -> Dict[str, float]:
        """
        Read a single temperature sensor.

        Parameters
        ----------
        sensor_path : Path

        Returns
        -------
        dict
            Dictionary containing Celsius and Fahrenheit values.
        """

        lines = self._wait_for_valid_crc(sensor_path)

        celsius = self._extract_celsius(lines)

        fahrenheit = self.celsius_to_fahrenheit(celsius)

        return {
            "celsius": round(
                celsius,
                config.TEMPERATURE_PRECISION
            ),
            "fahrenheit": round(
                fahrenheit,
                config.TEMPERATURE_PRECISION
            )
        }

    def read_all_temperatures(self) -> Dict[str, Dict[str, float]]:
        """
        Read every detected DS18B20 sensor.

        Returns
        -------
        dict
            Dictionary containing all sensor readings.
        """

        self.verify_sensor_count()

        temperature_data: Dict[str, Dict[str, float]] = {}

        for index, sensor in enumerate(
            self.sensor_paths,
            start=1
        ):

            sensor_name = f"Sensor {index}"

            temperature_data[sensor_name] = self.read_sensor(
                sensor
            )

        return temperature_data

    def get_sensor_count(self) -> int:
        """
        Return the number of detected sensors.
        """

        return len(self.sensor_paths)

    def get_sensor_identifiers(self) -> List[str]:
        """
        Return the Linux device identifiers for each sensor.

        Useful for diagnostics and troubleshooting.
        """

        return [
            sensor.name
            for sensor in self.sensor_paths
        ]
