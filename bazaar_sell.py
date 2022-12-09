from pyautogui import click
from pyautogui import sleep
from pyautogui import moveTo
from keyboard import is_pressed

while True:
    if is_pressed('`'):
        click(460,523)
        click()
        sleep(0.2)
        click(613,463)
        click()