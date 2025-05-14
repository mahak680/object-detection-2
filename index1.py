from ultralytics import YOLO
import cv2

#load the model
model = YOLO('yolov8n.pt')

#load the image
image = cv2.imread('image1.jpeg')

#define ROI
x, y, w, h = 100, 100, 200, 200
roi = image[y:y+h, x:x+w]

#detect objects in ROI
results = model(roi)

#extract bounding boxes and labels
boxes = results[0].boxes.xyxy   # Bounding box coordinates

labels = results[0].boxes.cls   # Class labels

#count persons in ROI
person_class_id = 0  # Class ID for 'person' in dataset
person_count = sum([1 for label in labels if label == person_class_id])

print(f'Number of persons in ROI: {person_count}')