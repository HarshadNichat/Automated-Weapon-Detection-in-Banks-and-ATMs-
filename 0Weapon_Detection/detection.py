from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
import cv2
import numpy as np
import time
import requests
from ultralytics import YOLO
import os

class Detection(QThread):

    def __init__(self, token, location, receiver):
        super(Detection, self).__init__()

        self.token = token
        self.location = location
        self.receiver = receiver

    changePixmap = pyqtSignal(QImage)

    def run(self):
        # Load YOLOv8 model
        model_path = r'weights\best.pt'  # Relative path
        # model_path = r'E:\OneDrive\learning\A_VS_Code\MEJOR_PROJECT\Weapon_Detection_System-master\udated_weapon_detection_2\weights\best.pt'  # Absolute path

        if not os.path.exists(model_path):
            raise FileNotFoundError(f"The file does not exist: {model_path}")

        model = YOLO(model_path)  # Load the YOLO model

        self.running = True
        cap = cv2.VideoCapture(0)  # Start webcam

        self.starting_time = time.time()

        while self.running:
            ret, frame = cap.read()
            if ret:
                results = model(frame)  # Perform inference

                # Process results
                boxes = results[0].boxes.xyxy.cpu().numpy()
                confidences = results[0].boxes.conf.cpu().numpy()
                class_ids = results[0].boxes.cls.cpu().numpy().astype(int)
                labels = results[0].names

                # Draw boxes around detected objects
                for box, confidence, class_id in zip(boxes, confidences, class_ids):
                    if confidence > 0.50:  # Confidence threshold
                        x1, y1, x2, y2 = map(int, box)
                        label = f"{labels[class_id]} {confidence:.1%}"
                        color = (0, 255, 0)
                        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

                        elapsed_time = time.time() - self.starting_time

                        # Save detected frame every 10 seconds
                        if elapsed_time >= 10:
                            self.starting_time = time.time()
                            self.save_detection(frame)

                # Showing final result
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(854, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)

    def save_detection(self, frame):
        os.makedirs("saved_frame", exist_ok=True)
        cv2.imwrite("saved_frame/frame.jpg", frame)
        print('Frame Saved')
        self.post_detection()

    def post_detection(self):
        try:
            url = 'https://domjur-weapon-detection.herokuapp.com/api/images/'
            headers = {'Authorization': 'Token ' + self.token}
            files = {'image': open('saved_frame/frame.jpg', 'rb')}
            data = {'user_ID': self.token, 'location': self.location, 'alert_receiver': self.receiver}
            response = requests.post(url, files=files, headers=headers, data=data)

            if response.ok:
                print('Alert was sent to the server')
            else:
                print('Unable to send alert to the server')
        except Exception as e:
            print(f'Unable to access server: {e}')

if __name__ == "__main__":
    # Example of how to start the Detection thread
    # You should replace 'your_token', 'your_location', 'your_receiver' with actual values
    token = 'your_token'
    location = 'your_location'
    receiver = 'your_receiver'

    detection_thread = Detection(token, location, receiver)
    detection_thread.start()
