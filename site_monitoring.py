import cv2
import numpy as np

def detect_anomalies(image_data):
    image = cv2.imdecode(np.frombuffer(image_data.read(), np.uint8), cv2.IMREAD_COLOR)
    # Simulated anomaly detection
    anomaly_detected = "Yes" if np.mean(image) < 100 else "No"
    return anomaly_detected
