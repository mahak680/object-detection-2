from ultralytics import YOLO
import cv2

#load a model
model = YOLO('yolov8n.pt')

results = model(["image3.jpeg"])

list1 = []

print(model.names)

for result in results:
    # print("result",result[0]) 
    boxes = result.boxes
    print(boxes)
    box=boxes.cls
    
    print(boxes.xyxy)
    a=box.tolist()

    print(a.count(16))

    print(a)

    names = model.names

    print(names[16])

    for i in a:
        x = names[i]
        list1.append(x)

    print(list1)

    b= set(list1)

    for j in b:
        print(list1.count(j))
        

    result.show() 
    result.save(filename="result.jpg")  