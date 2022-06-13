import pyautogui
import keyboard
from PIL import Image
from multiprocessing import Process, freeze_support
import pyscreenshot as ImageGrab
import pytesseract
from setuptools import find_namespace_packages
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

point1, point2 = None, None

def type():
    global point1, point2

    im = ImageGrab.grab(bbox=(point1[0], point1[1], point2[0], point2[1]))
    text = pytesseract.image_to_string(im, lang='eng')
    pyautogui.press('backspace')
    pyautogui.typewrite(text, interval=0.05)

    print("read")

def clear():
    global point1, point2
    point1, point2 = None, None

def store_point():
    global point1, point2

    if point1 is None:
        point1 = pyautogui.position()
        print('POINT1:', point1)
        return
    if point2 is None:
        point2 = pyautogui.position()
        print('POINT2:', point2)
        return

def main():
    run = True
    ctrl = False
    while run:
        global point1, point2

        if keyboard.is_pressed('ctrl'):
            ctrl = True

        if keyboard.read_key() == '[' and ctrl:
            store_point()
        if keyboard.read_key() == ']' and ctrl:
            if point1 is None or point2 is None: 
                print('Please select a region first')
            else:
                type()
                clear()

            
if __name__ == "__main__":
    freeze_support()
    Process(target=main).start()
