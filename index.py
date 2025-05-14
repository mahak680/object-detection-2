from ultralytics import YOLO
import cv2

#load yolo model
model =YOLO('yolov8n.pt')

#load video
video_path = './test.mp4'
cap = cv2.VideoCapture(video_path)

#read frames
ret =True
while ret:
    ret,frame  = cap.read()

#detect objects
#track objects
results = model.track(frame, persist = True)

#plot results
frame = results[0].plot()

#visualie
cv2.imshow('frame', frame_)
if cv2.waitKey(25) & 0xFF == ord('q'):
    break