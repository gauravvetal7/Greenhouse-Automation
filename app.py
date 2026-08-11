
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=2000, key="refresh")
import streamlit as st
from datetime import datetime
import json
from components.cards import sensor_card
import random
from components.charts import create_chart
from components.controls import device_control
import os
from components.gauges import create_gauge

st.write("Current folder:", os.getcwd())



with open("data/sensor_data.json") as file:
    data = json.load(file)



history_file = "data/sensor_history.json"

try:
    with open(history_file, "r") as file:
        history = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    history = {
        "temperature": [],
        "humidity": [],
        "soil": [],
        "light": []
    }

    with open(history_file, "w") as file:
        json.dump(history, file, indent=4)

history["temperature"].append(data["temperature"])
history["humidity"].append(data["humidity"])
history["soil"].append(data["soil"])
history["light"].append(data["light"])

MAX_POINTS = 100

history["temperature"] = history["temperature"][-MAX_POINTS:]
history["humidity"] = history["humidity"][-MAX_POINTS:]
history["soil"] = history["soil"][-MAX_POINTS:]
history["light"] = history["light"][-MAX_POINTS:]

with open(history_file, "w") as file:
    json.dump(history, file, indent=4)

temperature = data["temperature"]
humidity = data["humidity"]
soil = data["soil"]
light = data["light"]




st.set_page_config(
    page_title="Smart Greenhouse Dashboard",
    page_icon="🌿",
    layout="wide"
)

with st.sidebar:

    st.title("🌿 Smart Greenhouse")

    st.markdown("---")

    st.subheader("📡 System Status")

    st.success("ESP32 Connected")
    st.success("Flask API Running")
    st.success("Wi-Fi Connected")

    st.markdown("---")

    now = datetime.now()

    st.subheader("📅 Date")
    st.write(now.strftime("%d %B %Y"))

    st.subheader("🕒 Time")
    st.write(now.strftime("%I:%M:%S %p"))

    st.markdown("---")

    st.subheader("ℹ️ Project")

    st.write("IoT Smart Greenhouse")

# ---------------- Header ----------------

st.title("🌿 Smart Greenhouse Dashboard")
st.markdown("### Real-Time Greenhouse Monitoring System")

st.divider()

# ---------------- Date & Time ----------------

col1, col2 = st.columns(2)

with col1:
    st.info(f"📅 Date : {datetime.now().strftime('%d-%m-%Y')}")

with col2:
    st.info(f"🕒 Time : {datetime.now().strftime('%H:%M:%S')}")

st.divider()


#_____________________________________________________________________


st.subheader("🟢 Greenhouse Health")

c1, c2, c3, c4 = st.columns(4)

with c1:
    if temperature < 35:
        st.success("🌡 Temperature Normal")
    else:
        st.error("🔥 High Temperature")

with c2:
    if humidity >= 50:
        st.success("💧 Humidity Good")
    else:
        st.warning("💧 Low Humidity")

with c3:
    if soil >= 40:
        st.success("🌱 Soil Moist")
    else:
        st.error("🌱 Soil Dry")

with c4:
    if light >= 30:
        st.success("☀ Good Light")
    else:
        st.warning("☀ Low Light")

# ---------------- Sensor Cards ----------------

st.subheader("📊 Live Sensor Values")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        label="🌡 Temperature",
        value=f"{temperature:.1f} °C"
    )

with c2:
    st.metric(
        label="💧 Humidity",
        value=f"{humidity:.1f} %"
    )

with c3:
    st.metric(
        label="🌱 Soil Moisture",
        value=f"{soil} %"
    )

with c4:
    st.metric(
        label="☀ Light Intensity",
        value=f"{light} %"
    )
    
st.divider()

st.info("📡 Waiting for live ESP32 sensor data...")

st.subheader("📈 Live Sensor Graphs")


temperature_graph = history["temperature"]
humidity_graph = history["humidity"]
soil_graph = history["soil"]
light_graph = history["light"]

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(

        
        create_chart(
            "Temperature (°C)",
            temperature_graph,
            "red"
        ),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        create_chart(
            "Humidity (%)",
            humidity_graph,
            "deepskyblue"
        ),
        use_container_width=True
    )

col3, col4 = st.columns(2)

with col3:
    st.plotly_chart(
        create_chart(
            "Soil Moisture (%)",
            soil_graph,
            "green"
        ),
        use_container_width=True
    )

with col4:
    st.plotly_chart(
        create_chart(
            "Light Intensity (Lux)",
            light_graph,
            "orange"
        ),
        use_container_width=True
    )

    st.divider()

st.header("🎛 Device Control")

col1, col2, col3 = st.columns(3)

with col1:
    device_control("Fan", "🌬")

with col2:
    device_control("Water Pump", "💧")

with col3:
    device_control("Grow Light", "💡")