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
        self.x1 = window.left
        self.y1 = window.top
        self.x2 = window.width + self.x1 
        self.y2 = window.height + self.y1
        # midpoint = (window.left + window.width/2, window.top + window.height/2)
        # hor_gap = (0.00878477306 * window.width) +50
        # self.x1 = midpoint[0] - hor_gap
        # self.y1 = midpoint[1] - (0.1953125 * window.height)+100
        # self.x2 = midpoint[0] + hor_gap
        # self.y2 = midpoint[1]

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