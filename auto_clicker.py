import pyautogui
import keyboard
import threading
import time

clicking = True

def auto_clicker():
    while clicking:
        pyautogui.click()
        time.sleep(0.1)

def stop_clicking():
    global clicking
    keyboard.read_event()
    clicking = False

if __name__ == "__main__":

    click_thread = threading.Thread(target=auto_clicker)
    click_thread.start()

    print("Auto clicker started. Press any key to stop.")
    stop_clicking()

    click_thread.join()

    print("Auto clicker stopped.") #auto clicker has stopped
