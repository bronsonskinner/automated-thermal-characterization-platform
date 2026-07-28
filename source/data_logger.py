"""
data_logger.py

Project:
    Raspberry Pi–Based Automated Thermal Characterization Platform

Author:
    Bronson Skinner

Description:
    Handles CSV creation and automated temperature data logging
    for the thermal characterization platform.

    Responsibilities:
        • Create CSV log files
        • Write column headers
        • Record timestamped temperature measurements
        • Append new measurements throughout the experiment

Version:
    2.0
"""

import csv
from datetime import datetime
from pathlib import Path
from typing import Dict

import config


class DataLogger:
    """
    Handles CSV file creation and temperature data logging.
    """

    def __init__(self) -> None:
        """
        Initialize the data logger.
        """

        self.output_file: Path = config.CSV_FILENAME

        self._create_csv()

    # ---------------------------------------------------------
    # CSV Initialization
    # ---------------------------------------------------------

    def _create_csv(self) -> None:
        """
        Create the CSV file and write the header row if the
        file does not already exist.
        """

        if self.output_file.exists():
            return

        with self.output_file.open(
            "w",
            newline="",
            encoding="utf-8"
        ) as csv_file:

            writer = csv.writer(csv_file)

            header = ["Timestamp"]

            for sensor in range(
                1,
                config.EXPECTED_SENSOR_COUNT + 1
            ):
                header.append(f"Sensor {sensor} (°C)")
                header.append(f"Sensor {sensor} (°F)")

            writer.writerow(header)

    # ---------------------------------------------------------
    # Data Logging
    # ---------------------------------------------------------

    def log(
        self,
        temperature_data: Dict[str, Dict[str, float]]
    ) -> None:
        """
        Append one set of temperature measurements to the CSV.
        """

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        row = [timestamp]

        for sensor in temperature_data.values():

            row.append(sensor["celsius"])
            row.append(sensor["fahrenheit"])

        with self.output_file.open(
            "a",
            newline="",
            encoding="utf-8"
        ) as csv_file:

            writer = csv.writer(csv_file)

            writer.writerow(row)

    # ---------------------------------------------------------
    # Utility
    # ---------------------------------------------------------

    def get_output_file(self) -> Path:
        """
        Return the current CSV file path.
        """

        return self.output_file
