from getScreenShot import getScreenShot
import pygetwindow
import keyboard

ss = getScreenShot()

ss.setImgPath("C:\\Users\\chasa\\Desktop\\screenshot.png")

while True:

    try:
        ss.setTitle(pygetwindow.getActiveWindow().title)
    except:
        continue

    if ss.getTitle() == 'Calculator' and keyboard.is_pressed("q"):
        ss.setBorders(pygetwindow.getWindowsWithTitle(ss.getTitle())[0])
        res_image = ss.take()
        res_image.show(ss.getPath())
        break