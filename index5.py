# from ultralytics import YOLO
# import cv2
# import numpy as np
# colorBGR=[]
# def POINTS(event, x, y, flags, param):
#     if event == cv2.EVENT_MOUSEMOVE:
#         colorBGR.append((x,y))
        
        
# cv2.namedWindow('ROI')
# cv2.setMouseCallback('ROI', POINTS)     

# cap = cv2.VideoCapture('vid1.mp4')

# model = YOLO('yolov8n.pt')
# print("colorBGR",colorBGR)
# count = 0

# while True:
#     ret,frame = cap.read()
#     if not ret:
#         break
#     count += 1
#     if count % 3 !=0:
#         continue

#     frame = cv2.resize(frame,(1020,500))
#     results = model(frame)
#     color = (255, 0, 0) 
  
# # Line thickness of 2 px 
#     thickness = 2
#     for result in results:
#         boxes = result.boxes

#         for box in boxes: 
#             # print(box.xyxy)
#             x1,y1,x2,y2 = box.xyxy[0]
#             x1 = int(x1)
#             x2 = int(x2)
#             y1 = int(y1)
#             y2 = int(y2)
#             cv2.rectangle(frame,(x1,y1),(x2,y2),color=color,thickness=thickness)
#             # print('------------------- ',x1,y1,x2,y2)
#     # print(boxes)
#     box=boxes.cls

#     def draw_rectangle(event, x, y, flags, param):
#       global start_point, end_point, drawing

#       if event == cv2.EVENT_LBUTTONDOWN:
#         start_point = (x1, y1)
#         drawing = True
#       elif event == cv2.EVENT_MOUSEMOVE:
#         if drawing:
#             end_point = (x2, y2)
#       elif event == cv2.EVENT_LBUTTONUP:
#         end_point = (x2, y2)
#         drawing = False



#     # print(boxes.xyxy)
#     a=box.tolist()
 
#     # print(a.count)

#     # print(a)

#     cv2.imshow("ROI",frame) 

#     if cv2.waitKey(1)&0xFF==27:
#         break
# cap.release()
# cv2.destroyAllWindows()




# found coordinates for the image 
#index.5





import cv2

# Global variable to store coordinates
cordi = []

def click_event(event, x, y, flags, params):
    global cordi
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Coordinates: ({x}, {y})")
        cordi.append((x, y))
        # Draw a circle at the clicked point
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
        cv2.imshow('image', img)
        # Draw rectangle if two points are selected
        if len(cordi) == 2:
            draw_roi()

def draw_roi():
    global cordi
    # Get the two points
    x, y = cordi[0]
    x1, y1 = cordi[1]
    # Draw the rectangle
    cv2.rectangle(img, (x, y), (x1, y1), (255, 0, 0), 2)
    # Show the image
    cv2.imshow('image', img)
    # Reset coordinates list
    cordi = []

# Load the image
img = cv2.imread('image1.jpeg')
cv2.imshow('image', img)

# Set mouse callback
cv2.setMouseCallback('image', click_event)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
