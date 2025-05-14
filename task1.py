import cv2
import numpy as np


# Load YOLO
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
classes = open("coco.names").read().strip().split("\n")


#load image or video

cap = cv2.VideoCapture("video.mp4")
while True:
    ret,frame = cap.read()
    if not ret:
        break

    
    height, width, channels = frame.shape
    
#     # Define ROI
#     x_start, y_start, x_end, y_end = 100, 50, 400, 300  # Example coordinates
#     roi = frame[y_start:y_end, x_start:x_end]
    
#     # Detecting objects
#     blob = cv2.dnn.blobFromImage(roi, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
#     net.setInput(blob)
#     outs = net.forward(output_layers)
    
#     # Initializing variables
#     class_ids = []
#     confidences = []
#     boxes = []
    
#     # Extract information from detections
#     for out in outs:
#         for detection in out:
#             scores = detection[5:]
#             class_id = np.argmax(scores)
#             confidence = scores[class_id]
#             if confidence > 0.5 and classes[class_id] == "person":
#                 center_x = int(detection[0] * (x_end - x_start))
#                 center_y = int(detection[1] * (y_end - y_start))
#                 w = int(detection[2] * (x_end - x_start))
#                 h = int(detection[3] * (y_end - y_start))
                
#                 x = int(center_x - w / 2)
#                 y = int(center_y - h / 2)
                
#                 boxes.append([x, y, w, h])
#                 confidences.append(float(confidence))
#                 class_ids.append(class_id)
    
#     # Apply Non-Max Suppression to filter overlapping boxes
#     indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    
#     person_count = len(indexes)
    
#     # Display the count on the frame
#     cv2.putText(frame, f'Persons in ROI: {person_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
#     cv2.rectangle(frame, (x_start, y_start), (x_end, y_end), (0, 255, 0), 2)
    
#     cv2.imshow("Frame", frame)
    
#     key = cv2.waitKey(1)
#     if key == 27:  # Press 'ESC' to exit
#         break

# cap.release()
# cv2.destroyAllWindows()
