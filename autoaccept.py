import pyautogui
from pyautogui import locateAllOnScreen
import time


def click_accept_btn():
    
    accept_btn_location = None
    
    print('Looking for match')
    while accept_btn_location is None:
        accept_btn_location = pyautogui.locateOnScreen('accept.png', confidence=0.7)
        time.sleep(1)
    
    
    print("Match Found!")
    accept_btn_center = pyautogui.center(accept_btn_location)
    pyautogui.moveTo(accept_btn_center)
    pyautogui.click(accept_btn_center)
    
    print("Match accepted. Exiting...")
    time.sleep(5)
    exit()
    
click_accept_btn()
