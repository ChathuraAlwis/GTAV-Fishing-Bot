from PIL import ImageGrab

class getScreenShot:

    ImgPath = None
    Title = None
    x1 = x2 = y1 = y2 = None

    def setImgPath(self, path):
        self.ImgPath = path

    def setTitle(self, title):
        self.Title = title

    def setBorders(self, window):
        try:
            self.x1 = window.left
            self.y1 = window.top
            self.x2 = window.width + self.x1 
            self.y2 = window.height + self.y1
        except:
            self.x1 = window[0]
            self.y1 = window[1]
            self.x2 = window[2]
            self.y2 = window[3]

    def getPath(self):
        return self.ImgPath

    def getTitle(self):
        return self.Title

    def getBorders(self):
        return (self.x1, self.y1, self.x2, self.y2)

    def take(self):
        im = ImageGrab.grab(bbox = self.getBorders())
        # im = im.crop(self.getBorders())
        # im.save(self.getPath())
        return im