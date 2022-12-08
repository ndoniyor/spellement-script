import pyautogui
#import sys
import keyboard
import time
from PIL import ImageGrab
import cv2
import numpy as np

x_pad = 0
y_pad = 0
cards_coordinates = (608, 345, 730, 430)
boss_health_coords = (74,63,75,64)
grass_coords = (480,653, 481, 654)
def check_for_enchant(cards,cast_flag):
    for y in range(10,80,1):
        for x in range (0,110,1):
            if(cards[x,y][0] >= 160 and cards[x,y][0] <= 200 and cards[x,y][2] == 0):
                print("Found enchant")
                print("Color: ", cards[x,y])
                print(cards_coordinates[0]+x,cards_coordinates[1]+y)
                pyautogui.moveTo(cards_coordinates[0]+x,cards_coordinates[1]+y)
                if(cast_flag==1):
                    pyautogui.moveTo(cards_coordinates[0]+x+10,cards_coordinates[1]+y)
                pyautogui.click()
                return True
    return False

def enchant_card(cards):
    for y in range(10,80,1):
        for x in range (0,110,2):
            #print(cards.load()[x,y])
            if(cards[x,y][0] < 100 and cards[x,y][2] > 200):
                print("Found blizzard")
                print(cards_coordinates[0]+x,cards_coordinates[1]+y)
                pyautogui.moveTo(cards_coordinates[0]+x,cards_coordinates[1]+y)
                if(cards_coordinates[0]+x > 670):
                    pyautogui.moveTo(cards_coordinates[0]+x+10,cards_coordinates[1]+y) 
                pyautogui.click()
                pyautogui.moveTo(x,y)
                return True
    return False
def poll_grass():
    print("polling...")
    grass = ImageGrab.grab(grass_coords).load()
    grass_pixel = grass[0,0]
    print(grass_pixel)
    if(grass_pixel[1] > 250):
        return 1
    else:
        return 0

while True:
    if(keyboard.is_pressed('`')):
        while True:
            pyautogui.keyDown('x')
            pyautogui.keyUp('x')
            time.sleep(13)

            pyautogui.keyDown('w')
            time.sleep(3)
            pyautogui.keyUp('w')
            
            time.sleep(8)
            cards = ImageGrab.grab(cards_coordinates)
    
            if(check_for_enchant(cards.load(),0)): #click enchant
                time.sleep(0.5)
                if(enchant_card(cards.load())): #enchant blizzard
                    time.sleep(0.5)
                    check_for_enchant(cards.load(),1) #cast blizzard
                else:
                    print("Blizzard not found")
            else:
                print("No enchant found")
            print("")

            #poll_health_bar()
            #print("done polling")
            while(poll_grass()==0):
                time.sleep(3)
                pyautogui.keyDown('d')
                time.sleep(0.5)
                pyautogui.keyUp('d')
                pyautogui.keyDown('s')
                time.sleep(5)
                pyautogui.keyUp('s')

            pyautogui.click(853,172)
            pyautogui.press('escape')
            pyautogui.click(853,172)
            for i in range(0,6):
                pyautogui.click(545,601)
            pyautogui.click(467,355)
            pyautogui.click(467,355)
            time.sleep(0.5)
            pyautogui.click(467,640)
            pyautogui.click(467,640)
            pyautogui.press('escape')

            time.sleep(2)

    if(keyboard.is_pressed('q')):
        exit()
