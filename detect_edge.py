#make imports
import cv2
import numpy as np

WIDTH = 640
HEIGHT = 480
def getROI(img):
    return img[HEIGHT//2:(HEIGHT*3)//4,WIDTH//4:(WIDTH*3)//4]

def getContours(image):
    image =  cv2.GaussianBlur(image,(3,3),cv2.BORDER_DEFAULT)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edged = cv2.Canny(gray, 30, 200)

    contours, hierarchy = cv2.findContours(edged,
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    return edged,contours

#return bool value if edge is close or not
def close_edge():
    vid = cv2.VideoCapture(0)
    ret, frame = vid.read()
    if(ret):
        ROI_frame = getROI(frame)
        cont_frame,contours = getContours(ROI_frame)
        print(frame.shape)
        if(len(contours) >= 1):
            return True
        else:
            return False
    else:
        print(f"CAMERA NOT WORKING {frame}")
        return False


if __name__ == '__main__':
    cnt=0
    while True:
        if(close_edge()):
            print(f"{cnt}) TRUE-------------------->")
        else:
            print(f"{cnt}) FALSE")
        cnt += 1
            


