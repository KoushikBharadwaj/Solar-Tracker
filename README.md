# Solar Tracking System

This project focuses on developing a solar tracking system to optimize the efficiency of solar panels by continuously aligning them with the direction of maximum sunlight throughout the day. The system is built using an Arduino UNO microcontroller, Light Dependent Resistors (LDRs), and a servo motor.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Hardware Components](#hardware-components)
- [Installation](#installation)
- [Usage](#usage)
- [Model and Graph](#model-and-graph)
- [Methodology](#methodology)
- [Results](#results)
- [Conclusion](#conclusion)
- [Future Work](#future-work)

## Introduction

The Solar Tracking System is designed to improve the energy absorption efficiency of solar panels. By tracking the sun's movement across the sky, the system ensures that the solar panels are always positioned to capture the maximum amount of sunlight.

## Features

- **Automatic Sun Tracking:** Uses LDRs to detect sunlight and a servo motor to adjust the panel's position.
- **Real-Time Data Visualization:** Python integration allows for real-time monitoring of LDR readings and servo angles.
- **Increased Energy Efficiency:** Enhanced solar energy capture compared to stationary solar panels.

## Hardware Components

- Arduino UNO
- Light Dependent Resistors (LDRs)
- Servo Motor (SG90)
- 10k Ohm Resistors
- Connecting Wires

## Installation

### Arduino Setup

1. Open the Arduino IDE.
2. Load the `solar_tracking.ino` file from the `code` directory.
3. Upload the code to your Arduino UNO board.

### Python Setup

1. Ensure Python 3.x is installed on your system.
2. Install the required Python libraries:
   ```bash
   pip install matplotlib pyserial
   ```
3. Run the Python script to visualize real-time data:
   ```bash
   python receive_serial_data.py
   ```

## Usage

1. Set up the hardware components as per the circuit diagram provided.
2. Power the Arduino UNO.
3. Monitor the real-time tracking and data visualization on your computer.


## Model and Graph
![Model-Top](https://github.com/user-attachments/assets/aad7b172-c662-49f3-8e99-e3af1d12a714)

![Variation-1](https://github.com/user-attachments/assets/797b4ee5-4254-42d2-8693-a30b543fc185)


## Methodology

- **System Design:** The Arduino reads values from the LDRs to detect light intensity differences and adjusts the servo motor to align the solar panel with the sun.
- **Circuit Connections:** LDRs are connected to the analog input pins, and the servo motor is connected to a PWM digital pin.
- **Data Visualization:** Python is used to plot the real-time LDR readings and servo angles, providing insights into system performance.

## Results

The Solar Tracking System successfully tracks the sun, ensuring that the solar panels receive maximum sunlight throughout the day. The real-time data visualization demonstrates the system's ability to adjust to changing light conditions.

## Conclusion

This project demonstrates a cost-effective and efficient method for enhancing solar panel performance through automated sun tracking. The system can be further optimized with additional sensors and more advanced data logging.

## Future Work

- Implement dual-axis tracking for higher efficiency.
- Integrate with cloud-based data storage for long-term performance monitoring.
- Improve the tracking algorithm for faster response times.
