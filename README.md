# 🚗 AI Driver Monitoring System

## 📌 Overview
The **AI Driver Monitoring System** is a real-time computer vision application designed to detect driver drowsiness and improve road safety. It analyzes facial features like eyes and mouth to determine alertness and provides instant alerts.

---

## 🎯 Features

- 👁 Real-time face detection  
- 😴 Drowsiness detection using EAR (Eye Aspect Ratio)  
- 😮 Yawning detection using MAR (Mouth Aspect Ratio)  
- 🔔 Buzzer alert  
- 🔊 Voice alert  
- 🔴 Red visual warning  
- 📸 Snapshot capture  
- 📊 Live dashboard with graph  
- 🎯 Speedometer-style EAR gauge  
- 📁 Data logging  

---

## 🧠 Technologies Used

- Python  
- OpenCV  
- dlib  
- Streamlit  
- Plotly  
- NumPy  
- SciPy  

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/driver-monitoring-system.git
cd driver-monitoring-system
2️⃣ Install Dependencies
py -3.12 -m pip install opencv-python dlib streamlit plotly numpy scipy pyttsx3
3️⃣ Download Required Model

Download the file:

shape_predictor_68_face_landmarks.dat

From:
https://github.com/davisking/dlib-models

Place it in the project folder.

▶️ Run the Application
py -3.12 -m streamlit run app.py

Open browser:

http://localhost:8501
📊 Working
Capture live video from camera
Detect face using dlib
Extract 68 facial landmarks
Calculate EAR and MAR
Classify driver state:
ACTIVE
DROWSY
YAWNING
Trigger alerts if needed
Display results on dashboard
📈 Threshold Values
Parameter	Value	Meaning
EAR < 0.20	Eyes closed	Drowsy
MAR > 0.60	Mouth open	Yawning
📂 Project Structure
Driver_Monitoring_System/
│
├── app.py
├── driver_monitoring.py
├── utils.py
├── logs.csv
├── snapshots/
├── shape_predictor_68_face_landmarks.dat
🚨 Alerts
🔔 Sound alert
🔊 Voice alert
🔴 Visual warning
📸 Snapshot capture
📌 Applications
Smart vehicles
Driver safety systems
Accident prevention
⚠️ Limitations
Requires good lighting
Camera stability needed
Depends on hardware performance
🚀 Future Scope
GPS tracking
Mobile integration
Cloud storage
Advanced AI models
🏁 Conclusion

This project demonstrates an effective AI-based solution for detecting driver drowsiness and enhancing road safety using real-time monitoring and intelligent alerts.

👨‍💻 Author
Your Name
Your College

---

# 🎯 HOW TO USE IN GITHUB

1. Go to your repo  
2. Click **Add file → Create new file**  
3. Name it:

```text
README.md
Paste above content
Click Commit
🔥 RESULT

