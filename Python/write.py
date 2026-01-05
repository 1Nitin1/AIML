import pyautogui
import time

time.sleep(5)  # Gives you 3 seconds to click where you want to type
pyautogui.write('''Hello, this is 
    being typed by 
    pyautogui!''', interval=0.1)