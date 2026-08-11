# IoT-Based Automated Greenhouse System

An automated, intelligent climate control and monitoring system built using the **ESP32** microcontroller. This project integrates multiple environmental sensors and actuators to maintain optimal greenhouse conditions (temperature, humidity, soil moisture, and light) with zero manual intervention, featuring real-time telemetry over IoT.

## 🚀 Key Features
* **Automated Climate Regulation:** Dynamic control of ventilation (Fan) and irrigation (Water Pump) based on real-time sensor thresholds.
* **Intelligent Lighting:** Automatic photo-sensing using an LDR to manage artificial lighting via relays.
* **Fail-safe Logic:** Built-in hysteresis and validation checks to prevent rapid relay clicking and hardware wear.
* **Power Efficient & Scalable:** Optimized C/C++ codebase designed for low resource utilization on the ESP32.

## 🛠️ Tech Stack & Skills Demonstrated
* **Core Technologies:** ESP32, C/C++, FreeRTOS (Task management)
* **Sensors:** DHT11 (Temperature & Humidity), Capacitive/Resistive Soil Moisture Sensor, LDR (Light Dependent Resistor)
* **Actuators:** 5V/12V Relay Modules, DC Ventilation Fan, 5V Water Submersible Pump
* **Skills:** Embedded Systems Design, Hardware–Software Integration, Circuit Prototyping, Automation Logic

---

## 📐 System Architecture & Hardware Pinout



| Component | ESP32 Pin | Type | Description |
| :--- | :--- | :--- | :--- |
| **DHT11 Data** | GPIO 23 | Input | Temp & Humidity Data |
| **Soil Moisture Sensor** | GPIO 34 (ADC1) | Analog Input | Soil Moisture Level |
| **LDR (via Divider)** | GPIO 35 (ADC1) | Analog Input | Ambient Light Level |
| **Relay 1 (Water Pump)**| GPIO 18 | Output | Active LOW/HIGH Trigger |
| **Relay 2 (Fan)** | GPIO 19 | Output | Active LOW/HIGH Trigger |
| **Relay 3 (Grow Lights)**| GPIO 21 | Output | Active LOW/HIGH Trigger |

---

## 💻 Firmware Implementation

The automation logic is built entirely in C++ with a non-blocking execution architecture using polling intervals instead of strict `delay()`. This ensures the system remains responsive for future IoT expansions (e.g., Wi-Fi, MQTT).

### Threshold Configurations:
* **Temperature > 30°C** ➡️ Fan ON (Ventilation)
* **Soil Moisture < 40%** ➡️ Pump ON (Irrigation)
* **Light Intensity < Low Threshold** ➡️ Lights ON

---



