import keyboard
import pyautogui
import sys

print("hi")
while True:
    if(keyboard.is_pressed('`')):
        for i in range(int(sys.argv[1])):
            pyautogui.click();
        print("Done")