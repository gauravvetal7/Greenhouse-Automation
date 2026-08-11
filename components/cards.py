import streamlit as st

def sensor_card(title, value, unit, delta, icon):
    st.metric(
        label=f"{icon} {title}",
        value=f"{value} {unit}",
        delta=delta
    )
    