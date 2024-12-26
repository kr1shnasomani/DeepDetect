<h1 align="center">SkySight</h1>
The project uses YOLOv8 to identify traffic lights, people, and vehicles in aerial images. It enhances accuracy through customized filters, visualizes results with bounding boxes and labels, and saves annotated images for effective analysis of aerial scenes.

## Execution Guide:
1. Run the following command line in the terminal:
   ```
   pip install opencv-python ultralytics numpy
   ```

2. Download the YOLOv8 model from the link - **https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8x.pt**

3. Copy paste the path of the model in the code

4. Copy the path of the aerial image and paste it in the code

5. Once that is done run the code and you will get the result video by the name of `result.jpg`

## Model Prediction:

  Input Image:
  
  ![image](https://github.com/user-attachments/assets/91c628ad-0e27-4040-9d56-c2320d8f54ef)

  Output Image:
  
  ![result](https://github.com/user-attachments/assets/bbb70386-4dfb-4c03-88b1-2ff761caf03d)

## Overview:
The code performs object detection on an image using the YOLOv8 model and annotates the image with bounding boxes and class labels. Here's a breakdown of its functionality:

### Libraries:
1. **cv2 (OpenCV)**: Used for image processing, drawing bounding boxes, and adding text to the image.
2. **numpy**: Used for array handling and manipulation.
3. **ultralytics.YOLO**: The YOLOv8 model from the Ultralytics library for object detection.
4. **random**: Used to generate random colors for each detected class.

### Key Parts of the Code:
1. **Paths and Model Loading**:
   - The code defines paths for the input image (`IMAGE_PATH`), output image (`OUTPUT_PATH`), and the pre-trained YOLOv8 model (`MODEL_NAME`).
   - The YOLOv8 model is loaded from the specified path using `YOLO(MODEL_NAME)`.

2. **Color Generation**:
   - A dictionary, `class_to_color`, is used to store unique colors for each class.
   - The `get_random_color` function generates random colors (in RGB format) to assign to different classes for bounding box annotation.

3. **Image Loading**: The image is read using `cv2.imread(IMAGE_PATH)`. If the image is not found, a `FileNotFoundError` is raised.

4. **YOLOv8 Inference**:
   - The YOLOv8 model runs inference on the image using the `model.predict` method, which outputs detected objects (with bounding box coordinates, class IDs, and confidence scores).
   - Parameters for the model's inference:
     - `conf=0.15`: Minimum confidence threshold for detections.
     - `iou=0.3`: Intersection over union (IoU) threshold for non-maximum suppression.
     - `imgsz=1536`: Input image size for the model.
     - `augment=True`: Augment the image during inference for better results.

5. **Processing Detections**:
   - The code iterates through all detected objects (in the `detections.boxes` object).
   - For each detection:
     - It extracts the bounding box coordinates `(x1, y1, x2, y2)`, class ID, confidence, and class name.
     - It filters out detections based on class-specific criteria, such as confidence score and object aspect ratio (e.g., for traffic lights).
   - The detection is filtered and skipped if it doesn't meet the threshold or other conditions (like aspect ratio or size).

6. **Drawing Annotations**:
   - For each valid detection:
     - A bounding box is drawn around the object using `cv2.rectangle`.
     - The class label (name and confidence score) is displayed using `cv2.putText`.
   - The bounding box color is based on the assigned color for the class.
   - The box thickness and label positioning are adjusted to ensure readability.

7. **Saving the Result**:
   - The annotated image is saved to the specified output path (`OUTPUT_PATH`) using `cv2.imwrite`.
   - A message is printed indicating that the result is saved.

### Summary:
The script detects and annotates objects in an image using YOLOv8. It assigns different colors for each class, filters detections based on confidence and class-specific conditions (like size or aspect ratio), and saves the annotated image with bounding boxes and labels.
