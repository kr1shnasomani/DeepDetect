# Import the required libraries
import cv2
import numpy as np
from ultralytics import YOLO
import random

# Define paths
IMAGE_PATH = r"C:\Users\krish\OneDrive\Desktop\image.jpg"
OUTPUT_PATH = r"C:\Users\krish\OneDrive\Desktop\result.jpg"
MODEL_NAME = r"C:\Users\krish\OneDrive\Desktop\Projects\yolov8x.pt"

# Load the YOLOv8 model
model = YOLO(MODEL_NAME)

# A dictionary to store the color for each detected class
class_to_color = {}

def get_random_color():
    return tuple(random.randint(0, 255) for _ in range(3))

# Load the image
image = cv2.imread(IMAGE_PATH)
if image is None:
    raise FileNotFoundError(f"Image not found at path: {IMAGE_PATH}")

# Run YOLOv8 inference with optimized parameters
results = model.predict(
    source=IMAGE_PATH,
    conf=0.15,
    iou=0.3,
    imgsz=1536,
    augment=True,
    verbose=False
)

# Process results
detections = results[0]
annotated_image = image.copy()

# Iterate through all detections
for detection in detections.boxes:
    x1, y1, x2, y2 = map(int, detection.xyxy[0])
    class_id = int(detection.cls[0])
    conf = float(detection.conf[0])
    class_name = model.names[class_id]

    # Apply class-specific confidence thresholds and filtering
    if class_name == 'traffic light':
        if conf < 0.35: 
            continue

        box_height = y2 - y1
        box_width = x2 - x1
        aspect_ratio = box_height / box_width if box_width != 0 else 0
        
        if aspect_ratio < 1.5 or box_width > 100:
            continue
            
    elif class_name == 'person' and conf < 0.15:
        continue
    elif conf < 0.2: 
        continue

    # Get or assign color for the class
    if class_name not in class_to_color:
        class_to_color[class_name] = get_random_color()
    color = class_to_color[class_name]

    # Draw bounding box
    thickness = 3 if class_name in ['traffic light', 'person'] else 2
    cv2.rectangle(annotated_image, (x1, y1), (x2, y2), color, thickness)

    # Add label with better visibility
    label = f"{class_name} {conf:.2f}"
    label_size, _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
    cv2.rectangle(annotated_image, (x1, y1 - label_size[1] - 10), (x1 + label_size[0], y1), color, -1)
    cv2.putText(annotated_image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

# Save the result
cv2.imwrite(OUTPUT_PATH, annotated_image)
print(f"Detection result saved at {OUTPUT_PATH}")