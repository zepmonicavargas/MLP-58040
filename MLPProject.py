import torch
import cv2
import numpy as np
import pathlib
import serial
import time

# Modify the path handling for Windows
pathlib.PosixPath = pathlib.WindowsPath

# Specify the path to your YOLOv5 repository directory and weights file
yolov5_dir = r'C:\Users\Zep\yolov5'
weights_path = r'C:\Users\Zep\yolov5\best.pt'

# Load the YOLOv5 model using torch.hub.load()
model = torch.hub.load(str(yolov5_dir), 'custom', path=str(weights_path), source='local')

# Initialize webcam (0 is the primary camera, 1 is the secondary camera)
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# Initialize serial communication with Arduino
arduino_port = 'COM6'  # Replace 'COM5' with your Arduino port
arduino_baudrate = 9600
arduino = serial.Serial(arduino_port, arduino_baudrate)
time.sleep(2)  # Allow time for Arduino to initialize

save_dir = r'C:\Users\Zep\Desktop\MLP CAPTURED'

# Function to capture photo, save it, and perform object detection
def capture_and_detect():
    # Capture frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        return

    # Perform inference using the YOLOv5 model
    results = model(frame)

    # Render detection results on the frame
    annotated_frame = results.render()[0]

    # Save annotated frame
    image_name = f"{save_dir}\image_{time.strftime('%Y%m%d_%H%M%S')}_annotated.png"
    cv2.imwrite(image_name, annotated_frame)
    print(f"Annotated image saved: {image_name}")

    # Display the frame with annotations
    cv2.imshow('YOLOv5 Detection', annotated_frame)
    cv2.waitKey(1000)  # Display the window for 1 second
    cv2.destroyWindow('YOLOv5 Detection')

# Main loop for processing frames from the webcam
live_feed_active = True

while True:
    if live_feed_active:
        # Capture frame from the webcam
        ret, frame = cap.read()
        if not ret:
            break

        # Perform inference using the YOLOv5 model
        results = model(frame)

        # Extract class names and corresponding bounding boxes
        class_names = results.names
        boxes = results.xyxy[0]

        # Initialize flags for detecting Arduino, Breadboard, and InfraredRemoteControl
        Small = False
        Medium = False
        Large = False

        # Check each detection for Arduino, Breadboard, and InfraredRemoteControl
        for box in boxes:
            label = int(box[5])
            if label == 0:  # Arduino
                Small = True
            elif label == 1:  # Breadboard
                Medium = True
            elif label == 2:  # InfraredRemoteControl
                Large = True

        # Send signals to Arduino based on detection results
        if Small:
            arduino.write(b'A')  # Turn on Arduino LED
        elif Medium:
            arduino.write(b'B')  # Turn on Breadboard LED
        elif Large:
            arduino.write(b'C')  # Turn on InfraredRemoteControl LED
        else:
            arduino.write(b'D')  # Turn off all LEDs

        # Render detection results on the frame
        rendered_frames = results.render()
        if rendered_frames:
            # Get the first frame with annotations
            annotated_frame = rendered_frames[0]

            # Convert annotated_frame to NumPy array if it is not already
            if not isinstance(annotated_frame, np.ndarray):
                annotated_frame = np.array(annotated_frame)

            # Display the frame with annotations
            cv2.imshow('YOLOv5 Detection', annotated_frame)
        else:
            print("No frames to render.")

        # Check if the capture button signal is received from Arduino
        if arduino.in_waiting > 0:
            data = arduino.read()
            if data == b'P':
                capture_and_detect()
                live_feed_active = False  # Stop the live feed after capturing

        # Exit the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        # Check if the button is pressed again to restart the live feed
        if arduino.in_waiting > 0:
            data = arduino.read()
            if data == b'P':
                live_feed_active = True

# Release webcam, close OpenCV windows, and close serial connection
cap.release()
cv2.destroyAllWindows()

arduino.close()
