from getScreenShot import getScreenShot
import pygetwindow
import keyboard
from time import time
import cv2 as cv
import numpy as np

ss = getScreenShot()

ss.setImgPath("C:\\Users\\chasa\\Desktop\\screenshot.png")


loop_time = time()
while True:

    try:
        ss.setTitle(pygetwindow.getActiveWindow().title)
        ss.setBorders(pygetwindow.getWindowsWithTitle(ss.getTitle())[0])
    except:
        continue

    try:
        print('FPS {}'.format(1/(time() - loop_time)))
    except:
        pass
    loop_time = time()

    # if ss.getTitle() == 'Calculator':

    res_image = ss.take()

    res_image = np.array(res_image)
    res_image = cv.cvtColor(res_image, cv.COLOR_RGB2BGR)
    #---------OR--------
    # res_image = cv.imread(ss.getPath())

    # res_image.show(ss.getPath())
    # breakq
    cv.imshow('Computer Vision', res_image)
    cv.waitKey(1)

    if keyboard.is_pressed('q'):
        cv.destroyAllWindows()
        break