import cv2
import pyautogui

while True:
    im = pyautogui.screenshot()
    im.save("im", "JPEG")
    img = cv2.imread("im")
    gr = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    black = cv2.threshold(gr, 240, 255, cv2.THRESH_TOZERO, 3)[1]
    img2 = cv2.imread("target.png")
    gr2 = cv2.cvtColor(img2, cv2.COLOR_BGRA2GRAY)
    black2 = cv2.threshold(gr2, 240, 255, cv2.THRESH_TOZERO, 3)[1]
    cv2.imwrite("target.png", img2)
    pyautogui.useImageNotFoundException()
    try:
        location = pyautogui.locateOnScreen('target.png')
        pyautogui.click(location)
    except pyautogui.ImageNotFoundException:
        pass
