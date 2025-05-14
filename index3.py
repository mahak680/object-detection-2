from ultralytics import YOLO
import cv2

# Load a model
model = YOLO("yolov8n.pt")  # pretrained YOLOv8n model


results = model(["image1.jpeg"])  # return a list of Results objects

print(model.names)
# Process results list
for result in results:
    # print("result",result[0])
    boxes = result.boxes  # Boxes object for bounding box outputs
    print(boxes.cls) # Masks object for segmentation masks outputs
    
    print(boxes.xyxy)
    # obb = result.obb  # Oriented boxes object for OBB outputs
    # result.show()  # display to screen
    # result.save(filename="result.jpg")  # ave to disk

    