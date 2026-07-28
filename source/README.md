# Source Code

This directory contains the complete Python implementation for the Raspberry Pi–Based Automated Thermal Characterization Platform.

## Files

| File | Description |
|------|-------------|
| `config.py` | Centralized project configuration parameters and application settings. |
| `sensor_manager.py` | Discovers, validates, and acquires measurements from DS18B20 temperature sensors. |
| `data_logger.py` | Creates CSV log files and records timestamped temperature measurements. |
| `main.py` | Main application entry point that coordinates sensor acquisition, data logging, and user interaction. |
| `requirements.txt` | Python package dependencies required to run the project. |
| `sample_output.csv` | Example output generated during an automated temperature acquisition experiment. |

## Running the Application

Install the required dependency:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python3 main.py
```

## Hardware Requirements

- Raspberry Pi
- DS18B20 1-Wire digital temperature sensors
- 4.7 kΩ pull-up resistor
- Python 3

## License

This source code is provided under the MIT License included with this repository.
