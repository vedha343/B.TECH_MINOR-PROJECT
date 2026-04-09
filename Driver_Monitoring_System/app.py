import streamlit as st
import cv2
import plotly.graph_objects as go
from driver_monitoring import process_frame
import pyttsx3

# Page config
st.set_page_config(layout="wide")

# Voice engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# 🎨 ULTRA UI CSS
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}
.title {
    text-align:center;
    font-size:45px;
    color:#00FFD1;
    font-weight:bold;
}
.status {
    font-size:40px;
    text-align:center;
    font-weight:bold;
}
.active { color:#00FF00; }
.drowsy { color:#FF0000; }
.warning { color:#FFA500; }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🚗 AI DRIVER MONITORING SYSTEM</div>', unsafe_allow_html=True)

# Sidebar
run = st.sidebar.checkbox("Start System")
camera_index = st.sidebar.selectbox("Camera", [0,1,2])

# Layout
col1, col2 = st.columns([2,2])

FRAME = col1.image([])
status_box = col2.empty()
gauge_box = col2.empty()
chart_box = st.empty()

cap = cv2.VideoCapture(camera_index)

ear_history = []

while run:
    ret, frame = cap.read()
    if not ret:
        st.error("Camera not detected")
        break

    frame, status, ear, mar = process_frame(frame)

    # Show camera
    FRAME.image(frame, channels="BGR")

    # Store EAR values
    ear_history.append(ear)

    # 🎯 Gauge (Speedometer)
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=ear,
        title={'text': "EAR Level"},
        gauge={
            'axis': {'range': [0, 0.5]},
            'bar': {'color': "cyan"},
            'steps': [
                {'range': [0, 0.2], 'color': "red"},
                {'range': [0.2, 0.3], 'color': "orange"},
                {'range': [0.3, 0.5], 'color': "green"},
            ],
        }
    ))

    # ✅ FINAL FIX (dynamic key — no duplicate error)
    gauge_box.plotly_chart(
        fig,
        use_container_width=True,
        key=f"gauge_{len(ear_history)}"
    )

    # 📊 Live Graph
    chart_box.line_chart(ear_history)

    # 🚦 Status + Alerts
    if status == "DROWSY":
        status_box.markdown(
            '<div class="status drowsy">🚨 DRIVER DROWSY 🚨</div>',
            unsafe_allow_html=True
        )

        # Voice alert
        speak("Driver is drowsy")

        # Flash warning
        st.markdown(
            "<h1 style='color:red; text-align:center;'>⚠ TAKE BREAK ⚠</h1>",
            unsafe_allow_html=True
        )

    elif status == "YAWNING":
        status_box.markdown(
            '<div class="status warning">⚠ YAWNING DETECTED</div>',
            unsafe_allow_html=True
        )

    else:
        status_box.markdown(
            '<div class="status active">✅ DRIVER ACTIVE</div>',
            unsafe_allow_html=True
        )

cap.release()