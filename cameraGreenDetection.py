#!/usr/bin/env python3.7

import sys
import numpy as np
import cv2 as cv

capture = cv.VideoCapture(-1)

def getTheCircle(imgPath):
    img = cv.imread(imgPath)
    output = img.copy()
    output2 = img.copy()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # detect circles in the image
    detectedCircles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 2, 5000)

    for(x, y, r) in detectedCircles[0, :]:
        cv.circle(output, (x, y), r, (20, 129, 154), 3)
        cv.circle(output, (x, y), 2, (0, 255, 255), 3)
        print (x, y)

    cv.imshow('img', output2)
    cv.imshow('output', output)
    cv.waitKey(0)
    cv.destroyAllWindows()


def getTheColor():
    _, frame = capture.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    sensivity = 30
    lower_range = np.array([60 - sensivity, 100, 100])
    upper_range = np.array([60 + sensivity, 255, 255])

    mask_black_white = cv.inRange(hsv, lower_range, upper_range)
    cv.imshow('Normal', frame)
    cv.imshow('Black&White', mask_black_white)

    #hwnd = winGuiAuto.findTopWindow("Black&White")

    return

def checkArguments():
    global file
    if len(sys.argv) >= 2:
        return sys.argv[1]
    else:
        sys.exit(84)


def main():
    while True:
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

        getTheColor()
        #getTheCircle("tmp.png")
    capture.release()
    cv.destroyAllWindows()
    return

if __name__ == "__main__":
    main()
