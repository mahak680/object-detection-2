from ultralytics import YOLO
import cv2
import numpy as np

colorBGR=[]

# Global variable to store coordinates
cordi = []

def POINTS(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cordi.append((x, y))
        
        
cv2.namedWindow('ROI')
cv2.setMouseCallback('ROI', POINTS)     

cap = cv2.VideoCapture('vid1.mp4')

model = YOLO('yolov8n.pt')
print("colorBGR",colorBGR)
count = 0

while True:
    ret,frame = cap.read()
    if not ret:
        break
    count += 1
    if count % 3 !=0:
        continue

    frame = cv2.resize(frame,(1020,500))
    results = model(frame)
    color = (255, 0, 0) 
  
# Line thickness of 2 px 
    thickness = 2
    for result in results:
        boxes = result.boxes

        for box in boxes: 
            # print(box.xyxy)
            x1,y1,x2,y2 = box.xyxy[0]
            x1 = int(x1)
            x2 = int(x2)
            y1 = int(y1)
            y2 = int(y2)
            cv2.rectangle(frame,(x1,y1),(x2,y2),color=color,thickness=thickness)
            # print('------------------- ',x1,y1,x2,y2)
    # print(boxes)
    box=boxes.cls

    

    
    # print(boxes.xyxy)
    a=box.tolist()
 
    # print(a.count)

    # print(a)

    cv2.imshow("ROI",frame) 

    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()