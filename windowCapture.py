from getScreenShot import getScreenShot
import numpy as np
import cv2 as cv
from time import sleep, time
import pygetwindow as pw
import keyboard

class windowCapture:

    ss = None
    window = None
    w = h = None
    gap = None
    windowName = None
    res_img = res_img_copy = None
    loop_time = None

    def setSS(self, w, h, gap):
        self.ss = getScreenShot()
        self.w, self.h ,self.gap = w, h, gap

    def setResultImg(self):
        self.res_img_copy = self.res_img = self.ss.take()
        self.res_img = np.array(self.res_img)
        self.res_img = cv.cvtColor(self.res_img, cv.COLOR_RGB2BGR)
    
    def setLoopTime(self):
        self.loop_time = time()

    def setSSsettings(self):
        self.ss.setTitle(pw.getActiveWindow().title)
        self.window = pw.getWindowsWithTitle(self.ss.getTitle())[0]
        self.ss.setBorders(self.window, self.w, self.h, self.gap)
    
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

    def isGreen(self, color):
        if color[1] > color[0] + color[2]:
            return True
        return False

    def isRed(self, color):
        if color[0] > 190 and color[1] + color[2] < 10:
            return True
        return False

    def found(self):
        cordinate = (
            (int(self.w/2), int(self.w/2)), 
            (int(self.w/2), int(self.h/2)), 
            (int(self.w/2), int(self.h - self.w/2))
        )
        
        top = self.res_img_copy.getpixel(cordinate[0])
        mid = self.res_img_copy.getpixel(cordinate[1])
        bot = self.res_img_copy.getpixel(cordinate[2])

        n=1
        for rect in cordinate:
            top_left = rect[0]-n, rect[1]-n
            bot_right = rect[0]+n, rect[1]+n
            cv.rectangle(self.res_img, top_left, bot_right, 255, 1)

        if self.isGreen(top) and self.isRed(mid) and self.isRed(bot):
            return True
        return False
        


    def capture(self, w, h, gap, delay, windowName='default'):
        self.setSS(w, h, gap)
        self.setLoopTime()

        while True:

            try:
       
                self.setSSsettings()
                if windowName == 'default' or self.ss.getTitle() == windowName:
                    
                    self.setResultImg()
                    
                    if self.found():
                        sleep(delay)
                        keyboard.press_and_release('space')
                        
                        while not keyboard.is_pressed('space'):
                            continue
             
                    self.showImg()

                    if keyboard.is_pressed('q'):
                        cv.destroyAllWindows()
                        break
                
                else: cv.destroyAllWindows()

                if keyboard.is_pressed('q'):
                    break
                
            except:
                continue

            self.showFPS(time())