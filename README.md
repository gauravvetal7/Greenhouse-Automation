# 🌿 IoT-Based Smart Greenhouse Automation System

An IoT-based greenhouse monitoring and automation system built using **ESP32, Embedded C/C++, Flask, and Streamlit**. The system monitors temperature, humidity, soil moisture, and light intensity in real time and automatically controls the fan, water pump, and grow lights.

A web-based Streamlit dashboard provides live sensor monitoring, graphical visualization, system status, and manual device control.

## 🚀 Key Features

- **Real-Time Monitoring:** Continuously monitors temperature, humidity, soil moisture, and light intensity using ESP32 sensors.
- **Automatic Control:** Automatically controls the fan, water pump, and grow lights based on predefined environmental conditions.
- **Manual Control:** Allows the user to manually control greenhouse devices from the dashboard.
- **IoT Communication:** Sends sensor data from ESP32 to a Flask REST API over Wi-Fi.
- **Live Dashboard:** Streamlit dashboard displays real-time sensor values and system information.
- **Interactive Visualization:** Plotly graphs and gauge-style visualizations display current and historical sensor data.
- **System Status:** Displays ESP32, Wi-Fi, Flask API, and sensor connection status.
- **Historical Data:** Stores sensor readings and displays trends over time.
- **Responsive Automation:** Reduces manual intervention and helps maintain suitable greenhouse conditions.

---

## 🛠️ Technologies & Skills

### Hardware
- ESP32
- DHT11
- Soil Moisture Sensor
- LDR
- Relay Module
- DC Fan
- Water Pump
- Grow Light

### Software
- Embedded C/C++
- Arduino IDE
- Python
- Flask
- Streamlit
- Plotly
- REST API
- JSON
- Wi-Fi / HTTP

### Skills Demonstrated
- Embedded Systems
- Microcontroller Programming
- Sensor Interfacing
- Actuator Control
- IoT-Based System Development
- Hardware–Software Integration
- REST API Integration
- Real-Time Data Monitoring
- Data Visualization
- Automation Logic

---

## 📐 System Architecture

```text
                    ┌──────────────────────┐
                    │       Sensors        │
                    │                      │
                    │ DHT11                │
                    │ Soil Moisture        │
                    │ LDR                  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │        ESP32         │
                    │                      │
                    │ Sensor Reading        │
                    │ Automation Logic      │
                    │ Actuator Control      │
                    │ Wi-Fi Communication   │
                    └──────────┬───────────┘
                               │
                            HTTP/JSON
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Flask API       │
                    │                      │
                    │ Receive Sensor Data  │
                    │ Process / Store Data │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Streamlit Dashboard │
                    │                      │
                    │ Live Sensor Values   │
                    │ Plotly Graphs        │
                    │ Gauge Visualization  │
                    │ System Status        │
                    │ Device Control       │
                    └──────────────────────┘
