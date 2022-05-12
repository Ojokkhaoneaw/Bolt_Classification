import cv2
import os
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH,640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
DATAPATH = os.path.join(os.getcwd(),'dataset')
if not os.path.exists(DATAPATH) :
    os.makedirs(DATAPATH)
count = len([file for file in os.listdir(DATAPATH)])
while True:
    _,image = camera.read()
#Line to add effect
    cv2.imshow('camera',image)
    key = cv2.waitKey(1)
    if key==ord('c') :
        filename = "data" + str(count) + ".png"
        cv2.imshow('captured',image)
        cv2.imwrite(os.path.join(DATAPATH,filename), image)
        count += 1
        print(f'image_{count} is captured')
    if key==ord('q'):
        break
camera.release()
cv2.destroyAllWindows()