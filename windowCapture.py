from getScreenShot import getScreenShot
import numpy as np
import cv2 as cv
from time import time, sleep
import pygetwindow as pw
import keyboard

class windowCapture:

    ss = None
    windowName = None
    res_img = None
    res_img_copy = None
    result = None
    loop_time = None

    def setSS(self):
        self.ss = getScreenShot()

    def setResultImg(self):
        self.res_img_copy = self.res_img = self.ss.take()
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

    def showImg(self, img, name='Computer Vision'):
        if self.ss.getTitle() != name:
            cv.imshow(name, img)
            cv.waitKey(1)

    def compare(self, template_path='C:\\Users\\chasa\\Desktop\\ver_bar.png'):
        template = cv.imread(template_path, 1)
        # self.showImg(template)
        self.result = cv.matchTemplate(self.res_img,template,cv.TM_CCORR)
        return cv.minMaxLoc(self.result)
        

    def rectangle(self, max_loc):
        w, h = 11, 120
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv.rectangle(self.result,top_left, bottom_right, 255, 2)
        # for i in range (0,17):
        #     cordinate = int(top_left[0] + w/2) + i , int(top_left[1] + 1/15 * h) + i 
            # print('i = ', i , 'color = ', self.res_img_copy.getpixel(cordinate))
        # cordinate = int(top_left[0] + w/2), int(top_left[1] + 1/15 * h)
        # print(self.res_img_copy.getpixel(cordinate))


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
                    # self.showImg(self.res_img)
                    minMaxLoc = self.compare()
                    max_val = int(minMaxLoc[1]/1000000)
                    # print(max_val)
                    if max_val <=65 and max_val >= 63:
                        # self.rectangle(minMaxLoc[3])
                        sleep(0.155)
                        keyboard.press_and_release('space')
                        break

                    # self.showImg(self.res_img)

                    if keyboard.is_pressed('q'):
                        cv.destroyAllWindows()
                        break
                
                if keyboard.is_pressed('q'):
                    break
                
            except:
                continue

            self.showFPS(time())
            # print(self.ss.getBorders())
