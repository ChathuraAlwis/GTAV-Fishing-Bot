from PIL import ImageGrab

class getScreenShot:

    ImgPath = None
    Title = None
    mid = None
    x1 = x2 = y1 = y2 = None

    def setImgPath(self, path):
        self.ImgPath = path

    def setTitle(self, title):
        self.Title = title

    def setBorders(self, window, w, h, gap):
        # try:
        self.mid = (window.left + window.width/2, window.top + window.height/2)
        self.x1 = self.mid[0] - w/2
        self.y1 = self.mid[1] - h - gap
        self.x2 = self.mid[0] + w/2
        self.y2 = self.mid[1] - gap
        # except:
        #     self.x1 = window.left
        #     self.y1 = window.top
        #     self.x2 = window.width + self.x1 
        #     self.y2 = window.height + self.y1

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