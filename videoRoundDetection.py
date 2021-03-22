#!/usr/bin/env python3.7

import sys
import numpy as np
import cv2 as cv
from numpy import mean
import time

#capture = cv.VideoCapture('video-test/ball-bounce-boing-sound-effect.mp4')
capture = cv.VideoCapture('outpyColor.avi')
frame_width = int(capture.get(3))
frame_height = int(capture.get(4))
out = cv.VideoWriter('outpyCircle.avi',cv.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
xArray = []
yArray = []
speedMoyenne = []
speedKmTotal = []


def getTheCircle():
    global xArray
    global yArray
    global speedMoyenne
    global speedKmTotal
    _, frame = capture.read()
    try:
        output = frame.copy()
    except:
        return False
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # detect circles in the image
    # image: The input image.
    # method: Detection method.
    # dp: the Inverse ratio of accumulator resolution and image resolution.
    # mindst: minimum distance between centers od detected circles.
    # param_1 and param_2: These are method specific parameters.
    # min_Radius: minimum radius of the circle to be detected.
    # max_Radius: maximum radius to be detected.
    if frame.shape[0] == 480 :
        detectedCircles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1,
                                          frame.shape[0], param1=200, param2=10, minRadius=30, maxRadius=100)
    else :
        detectedCircles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1,
                                    frame.shape[0], param1=200, param2=10, minRadius=30, maxRadius=60)


    try:
        for(x, y, r) in detectedCircles[0, :]:
            cv.circle(output, (x, y), r, (200, 129, 154), 3)
            cv.circle(output, (x, y), 2, (0, 255, 255), 3)
            if not xArray:
                xArray.append(x)
                yArray.append(y)
            else:
                speedX = xArray[-1] - x
                speedY = yArray[-1] - y
                xArray.append(x)
                yArray.append(y)
                speedY = abs(speedY)
                speedX = abs(speedX)
                speed = speedX + speedY
                speedMoyenne.append(speed)
                speedKm = speed * x / y
                speedKmTotal.append(speedKm)

                print ("x :",x,"  -    y :",y, "  -    speed: ", speed, "  -  speedAverage:", mean(speedMoyenne), "  -  Speed Pixel/second: ", speedKm, "  -  Average pixels/second: ",  mean(speedKmTotal))
    except:
        pass
    out.write(output)
    cv.imshow('output', output)
    return True


def getTheColor():
    _, frame = capture.read()

    try :
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    except:
        return False

    sensivity = 50
    lower_range = np.array([100 - sensivity, 130, 0])
    upper_range = np.array([140 + sensivity, 150, 255])

    mask_black_white = cv.inRange(hsv, lower_range, upper_range)
    cv.imshow('Normal', frame)
    cv.imshow('Black&White', mask_black_white)
    frame_black_and_white = cv.cvtColor(mask_black_white, cv.COLOR_GRAY2RGB)
    out.write(frame_black_and_white)

    getTheCircle(frame_black_and_white)

    #hwnd = winGuiAuto.findTopWindow("Black&White")

    return True

def main():
    while True:
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

        if not getTheCircle():
            break
        time.sleep(0.1)
    capture.release()
    out.release()
    cv.destroyAllWindows()
    return

if __name__ == "__main__":
    main()
