from windowCapture import windowCapture

window_title = 'fishing.mp4'
w, h, gap = 15, 145, 13
percentage = 0.93
delay = 0.3 * percentage # default value 0.3

window = windowCapture()
window.capture(w, h, gap, delay, window_title)