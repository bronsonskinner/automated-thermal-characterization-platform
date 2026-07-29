<p align="center">
  <img src="images/repository_banner_v1.0.png"
       alt="Automated Raspberry Pi Thermal Characterization Platform"
       width="100%">
</p>

![License](https://img.shields.io/badge/License-MIT-green.svg)
![Python](https://img.shields.io/badge/Python-3-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi-red.svg)

# Automated Raspberry Pi Thermal Characterization Platform

### Designed, Built, and Documented by Bronson Skinner

> A reusable embedded data acquisition platform for automated thermal characterization, experimental validation, and engineering analysis using Raspberry Pi, Python, and multiple DS18B20 digital temperature sensors.

---

## Project Overview

This repository documents the design, implementation, and validation of an automated thermal characterization platform developed using a Raspberry Pi, Python, and multiple DS18B20 digital temperature sensors.

Rather than serving as a single experiment, this platform was engineered as a reusable test system capable of collecting synchronized temperature measurements from multiple sensors while reducing manual measurement error through software automation.

The project emphasizes embedded systems integration, engineering documentation, experimental repeatability, technical communication, and continuous improvement. It serves as the first project in an expanding engineering portfolio focused on controls engineering, industrial automation, embedded systems, advanced manufacturing, semiconductor manufacturing, and life sciences.

---

## System Architecture

```mermaid
flowchart LR

A[DS18B20 Temperature Sensors]
B[GPIO Interface]
C[sensor_manager.py]
D[config.py]
E[main.py]
F[data_logger.py]
G[CSV Output]
H[Engineering Analysis]

A --> B
B --> C
D --> E
C --> E
E --> F
F --> G
G --> H
```

---

## Engineering Guide

📄 **Engineering_Guide_v1.0.pdf**

The complete engineering guide documents every stage of the project, including:

- Project objectives
- Hardware architecture
- Wiring configuration
- Python software implementation
- Experimental methodology
- Experimental controls
- Results and observations
- Engineering conclusions
- Future development roadmap

The guide was written so another engineer can understand, evaluate, reproduce, and expand upon the published experiment.

---

## Demonstration Videos

📁 **Video demonstrations**

Browse all demonstration videos in the repository:

[Open the Videos Folder](videos/)

---

## Hardware

- Raspberry Pi
- Breadboard
- DS18B20 Digital Temperature Sensors
- GPIO Interface
- Pull-Up Resistor
- Jumper Wire Interconnections
- Aluminum Heatsinks
- Copper Heatsinks
- Stainless Steel Sensor Calibration Fixture

---

## Software

- Python
- Raspberry Pi OS
- One-Wire Interface
- GPIO
- GNU Nano

---

## Future Development

Potential enhancements for future iterations of this platform include:

- Development of a real-time dashboard for live temperature visualization.
- MQTT integration for remote monitoring and Industrial IoT applications.
- SQLite database support for long-term experimental data storage.
- Closed-loop PID thermal control for automated temperature regulation.
- Browser-based web interface for remote experiment management.
- Multi-threaded sensor acquisition for improved scalability and timing precision.
- Statistical analysis and automatic report generation.
- Support for additional environmental sensors including humidity and airflow.
- Automated calibration routines.
- Cloud synchronization and remote experiment logging.

---

## Technical Competencies Demonstrated

- Embedded Systems Development
- Python Programming
- Automated Data Acquisition
- Thermal Characterization
- Experimental Design
- Experimental Controls
- Sensor Integration
- Hardware Prototyping
- GPIO Configuration
- Engineering Documentation
- Technical Writing
- Troubleshooting
- Engineering Analysis
- Engineering Reproducibility
- Continuous Improvement

---

## Repository Contents

```text
Engineering_Guide_v1.0.pdf

README.md

images/
    repository_banner_v1.0.png
    experimental_test_platform_overview.jpeg
    experimental_data_collection.png
    python_temperature_acquisition_software.png
    automated_temperature_monitoring.png
    raspberry_pi_gpio_connections.jpeg
    sensor_wiring_configuration.png
    breadboard_wiring_configuration.png
    sensor_calibration_fixture.jpeg
    one_wire_pullup_resistor.jpeg
    future_heatsink_test_collection.png

videos/
    automated_temperature_data_acquisition.mp4
    live_sensor_response_demonstration.mp4
    portrait_heatsink_experimental_setup.mp4
    portrait_heatsink_sensor_placement.mp4
    landscape_heatsink_sensor_placement.mp4

source/
    (future Python source code)
```

---

## Future Development

This platform was intentionally designed to serve as a foundation for future expansion. Planned enhancements include:

- Real-time web dashboard for live temperature visualization
- MQTT publishing for industrial IoT integration
- SQLite database storage for long-term experiment logging
- PID-controlled thermal experiments
- Browser-based monitoring and control interface
- Multi-threaded sensor acquisition for improved scalability

These enhancements would further extend the platform into a more capable experimental and industrial automation test system while maintaining the modular software architecture established in Version 1.0.

---

## Purpose

The objective of this repository extends beyond demonstrating a Raspberry Pi project.

Its purpose is to document the complete engineering process involved in designing, building, validating, and documenting a repeatable experimental platform capable of supporting future thermal engineering investigations.

The long-term vision is to build a growing portfolio of engineering projects demonstrating practical experience in controls engineering, embedded systems, industrial automation, advanced manufacturing, semiconductor manufacturing, and life sciences.

---

## Engineering Lessons Learned

This project provided practical experience in:

- Embedded Python development
- Experimental automation
- Hardware integration
- Sensor validation
- Data acquisition
- Software architecture
- Engineering documentation
- Git version control
- Reproducible experimental design

---

## License

This project is released under the MIT License.

---

## Author

**Bronson Skinner**

**Areas of Interest**

- Controls Engineering
- Embedded Systems
- Industrial Automation
- Thermal Engineering
- Advanced Manufacturing
- Semiconductor Manufacturing
- Life Sciences

📧 **Email:** bronsonskinner4@gmail.com

---

*Thank you for taking the time to review this project. Feedback, technical discussion, and professional connections are always welcome.*
