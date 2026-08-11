import streamlit as st

def device_control(device_name, icon):

    if f"{device_name}_status" not in st.session_state:
        st.session_state[f"{device_name}_status"] = False

    status = st.session_state[f"{device_name}_status"]

    st.subheader(f"{icon} {device_name}")

    if status:
        st.success("🟢 ON")
    else:
        st.error("🔴 OFF")

    col1, col2 = st.columns(2)

    with col1:
        if st.button(f"Turn ON", key=f"{device_name}_on"):
            st.session_state[f"{device_name}_status"] = True

    with col2:
        if st.button(f"Turn OFF", key=f"{device_name}_off"):
            st.session_state[f"{device_name}_status"] = False