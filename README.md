<h1 align="center">DeepDetect</h1>
The deepfake detection system extracts frames from videos, detects and crops faces using facenet-pytorch, and classifies them as real or fake using a deep learning model like EfficientNet. The system highlights deepfake faces and provides visual analysis, leveraging PyTorch, OpenCV, and timm for model implementation.

## Execution Guide:
1. Run the following command line in the terminal:
   ```
   pip install torch torchvision torchaudio facenet-pytorch timm opencv-python numpy matplotlib pillow
   ```

2. Enter the path of the video

3. Upon running all the cells the code will provide its prediction frame by frame

## Result:

  DeepFake Video:
  
  [deepfake](https://github.com/user-attachments/assets/aa03466e-0030-4d5e-a640-0094ffb00c26)

  `Model prediction: DeepFake`

  Original Video:
  
  [original](https://github.com/user-attachments/assets/0304a40d-954e-4dfc-b0a9-5ccabe49e69a)

  `Model prediction: Original`

## Overview:
The above code performs the following key tasks:  

1. **Face Detection**:  
   Uses **MTCNN** (Multi-task Cascaded Convolutional Networks) from `facenet_pytorch` to detect faces in images or video frames.  

2. **Deepfake Classification Model**:  
   - Loads a **pretrained Xception model** from the `timm` library, which is widely used for deepfake detection.  
   - The model is fine-tuned with a single output neuron (binary classification: real or fake).  

3. **Preprocessing**:  
   - Detected faces are extracted and preprocessed before being passed to the model for classification.  

4. **Inference**:  
   The model predicts whether a given face is real or deepfake.  

This approach leverages **CNN-based face detection** and **deep learning classification** to identify manipulated media.
