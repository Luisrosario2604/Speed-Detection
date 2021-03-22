#!/usr/bin/env python3.7

import sys
import numpy as np
import cv2 as cv
import time

#capture = cv.VideoCapture(-1)
capture = cv.VideoCapture('video-test/ball-bounce-boing-sound-effect.mp4')
frame_width = int(capture.get(3))
frame_height = int(capture.get(4))
out = cv.VideoWriter('outpyColor.avi',cv.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))


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

    #hwnd = winGuiAuto.findTopWindow("Black&White")

    return True


def main():
    while True:
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

        if not getTheColor():
            break
        time.sleep(0.1)
    capture.release()
    out.release()
    cv.destroyAllWindows()
    return


if __name__ == "__main__":
    main()
