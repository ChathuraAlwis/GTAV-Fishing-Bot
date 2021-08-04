from getScreenShot import getScreenShot
import numpy as np
import cv2 as cv
from time import time
import pygetwindow as pw
import keyboard

class windowCapture:

    ss = None
    windowName = None
    res_img = None
    loop_time = None

    def setSS(self):
        self.ss = getScreenShot()

    def setResultImg(self):
        self.res_img = self.ss.take()
        self.res_img = np.array(self.res_img)
        self.res_img = cv.cvtColor(self.res_img, cv.COLOR_RGB2BGR)
    
    def setLoopTime(self):
        self.loop_time = time()

    def setSSsettings(self):
        self.ss.setTitle(pw.getActiveWindow().title)
        self.ss.setBorders(pw.getWindowsWithTitle(self.ss.getTitle())[0])

    def getSS(self):
        return self.ss

    def getResultImg(self):
        return self.res_img

    def getLoopTime(self):
        return self.loop_time

    def showImg(self, name='Computer Vision'):
        if self.ss.getTitle() != name:
            cv.imshow(name, self.res_img)
            cv.waitKey(1)

    def showFPS(self, time):
        try:
            print('FPS {}'.format(1/(time - self.loop_time)))
        except:
            pass
        self.loop_time = time

    def capture(self, windowName='default'):
        self.setSS()
        self.setLoopTime()

        while True:

            try:
                self.setSSsettings()
                if windowName == 'default' or self.ss.getTitle() == windowName:
                    self.setResultImg()
                    self.showImg()

                    if keyboard.is_pressed('q'):
                        cv.destroyAllWindows()
                        break
                
                if keyboard.is_pressed('q'):
                    break
                
            except:
                continue

            self.showFPS(time())