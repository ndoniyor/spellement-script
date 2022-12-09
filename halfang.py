import pyautogui
import sys
import keyboard
import time
from PIL import ImageGrab
#import cv2
#import numpy as np

cards_coordinates = (608, 345, 730, 430)
grass_coords = (480,653, 481, 654)
spellbook_coords = (1240,650, 1241, 651)
lamp_post = (305,405,306,406)

def check_for_enchant(cards,cast_flag):
    for relative_y in range(10,80,1):
        for relative_x in range (0,110,1):
            absolute_x, absolute_y = cards_coordinates[0]+relative_x, cards_coordinates[1]+relative_y
            if(cards[relative_x,relative_y][0] >= 160 and cards[relative_x,relative_y][0] <= 200 and cards[relative_x,relative_y][2] == 0):
                if(cast_flag==0):
                    pyautogui.moveTo(absolute_x,absolute_y)
                elif(cast_flag==1):
                    pyautogui.moveTo(670,375)
                pyautogui.click()
                pyautogui.moveTo(40,10)
                return True
    return False

def enchant_card(cards):
    for relative_y in range(10,80,1):
        for relative_x in range (0,110,2):
            absolute_x, absolute_y = cards_coordinates[0]+relative_x, cards_coordinates[1]+relative_y
            if(cards[relative_x,relative_y][0] < 100 and cards[relative_x,relative_y][2] > 200):
                pyautogui.moveTo(absolute_x,absolute_y)
                if(absolute_x > 670):
                    pyautogui.moveTo(absolute_x+10,absolute_y) 
                pyautogui.click()
                pyautogui.moveTo(40,10)
                return True
    return False

def poll_fight():
    spellbook = ImageGrab.grab(bbox=spellbook_coords).load()
    spellbook_pixel=spellbook[0,0]
    if(spellbook_pixel[0]>=220 and spellbook_pixel[1]>=210):
        return True
    else:
        return False

def poll_grass():
    grass = ImageGrab.grab(bbox=grass_coords).load()
    grass_pixel = grass[0,0]
    if(grass_pixel[1] > 250):
        return True
    else:
        return False

def poll_lamp():
    lamp = ImageGrab.grab(bbox=lamp_post).load()
    lamp_pixel = lamp[0,0]
    #print(lamp_pixel)
    if(lamp_pixel[0]>250 and lamp_pixel[1]>240 and lamp_pixel[2]<170):
        return True
    else:
        return False

def change_realm():
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


print("Press ` to start...")
while True:
    if(keyboard.is_pressed('`')):
        while True:
            pyautogui.keyDown('x')
            pyautogui.keyUp('x')
            time.sleep(2)

            print("Waiting to enter boss room...")
            while(poll_lamp()):
                time.sleep(1)
            
            time.sleep(2)
            print("Entered boss room")
            pyautogui.keyDown('w')
            time.sleep(3)
            pyautogui.keyUp('w')
            
            time.sleep(7)
            cards = ImageGrab.grab(bbox=cards_coordinates)

            if(check_for_enchant(cards.load(),0)): #click enchant
                print("Found enchant")
                time.sleep(0.25)
                if(enchant_card(cards.load())): #enchant blizzard
                    print("Found blizzard")
                    time.sleep(0.25)
                    check_for_enchant(cards.load(),1) #cast blizzard
                else:
                    print("Blizzard not found")
            else:
                print("No enchant found")
            

            print("Waiting for battle to end...")
            while(not poll_fight()):
                time.sleep(1)
            print("Battle ended")

            pyautogui.keyDown('d')
            time.sleep(0.5)
            pyautogui.keyUp('d')
            pyautogui.keyDown('s')
            time.sleep(5)
            pyautogui.keyUp('s')
            
            print("Checking for outside...")
            while(not poll_grass):
                time.sleep(1)
            print("Outside detected")
            #time.sleep(1)
            #change_realm()

            time.sleep(2)

    if(keyboard.is_pressed('q')):
        exit()
