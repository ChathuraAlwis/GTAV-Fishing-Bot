import pyautogui

class getScreenShot:

    ImgPath = None
    Title = None
    x1 = x2 = y1 = y2 = None

    def setImgPath(self, path):
        self.ImgPath = path

    def setTitle(self, title):
        self.Title = title

    def setBorders(self, window):
        self.x1 = window.left
        self.y1 = window.top
        self.x2 = window.width + self.x1 
        self.y2 = window.height + self.y1

    def getPath(self):
        return self.ImgPath

    def getTitle(self):
        return self.Title

    def getBorders(self):
        return (self.x1, self.y1, self.x2, self.y2)

    def take(self):
        im = pyautogui.screenshot(self.getPath())
        im = im.crop(self.getBorders())
        im.save(self.getPath())
        return im