import cv2
import dlib
import numpy as np
from scipy.spatial import distance
import winsound
from utils import log_data, save_snapshot
import geocoder
from plyer import notification

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

counter = 0

def get_location():
    try:
        g = geocoder.ip('me')
        return g.latlng
    except:
        return ["Unknown", "Unknown"]

def calculate_EAR(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

def calculate_MAR(mouth):
    A = distance.euclidean(mouth[2], mouth[10])
    B = distance.euclidean(mouth[4], mouth[8])
    C = distance.euclidean(mouth[0], mouth[6])
    return (A + B) / (2.0 * C)

def process_frame(frame):
    global counter

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    status = "No Face"
    ear_val, mar_val = 0, 0

    for face in faces:
        shape = predictor(gray, face)
        coords = np.array([[shape.part(i).x, shape.part(i).y] for i in range(68)])

        left_eye = coords[36:42]
        right_eye = coords[42:48]
        mouth = coords[48:68]

        ear = (calculate_EAR(left_eye) + calculate_EAR(right_eye)) / 2.0
        mar = calculate_MAR(mouth)

        ear_val = round(ear, 2)
        mar_val = round(mar, 2)

        if ear < 0.20:
            counter += 1
        else:
            counter = 0

        if counter > 15:
            status = "DROWSY"

            # 🔔 Buzzer
            winsound.Beep(2000, 500)

            # 📸 Snapshot
            save_snapshot(frame)

            # 📍 Location
            loc = get_location()

            # 🚨 Popup Notification
            notification.notify(
                title="Drowsiness Alert!",
                message=f"Driver sleepy!\nLocation: {loc}",
                timeout=5
            )

            # 🔴 Red Screen Overlay
            overlay = frame.copy()
            cv2.rectangle(overlay, (0,0), (frame.shape[1], frame.shape[0]), (0,0,255), -1)
            frame = cv2.addWeighted(overlay, 0.3, frame, 0.7, 0)

        elif mar > 0.60:
            status = "YAWNING"
        else:
            status = "ACTIVE"

        log_data(status, ear_val, mar_val)

        # Display text
        cv2.putText(frame, f"EAR: {ear_val}", (10,30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255),2)
        cv2.putText(frame, f"MAR: {mar_val}", (10,60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255),2)
        cv2.putText(frame, f"STATUS: {status}", (10,100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),3)

    return frame, status, ear_val, mar_val