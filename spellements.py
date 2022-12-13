import pyautogui
import sys
import keyboard
import time
from PIL import ImageGrab

hitter_cards = (608, 345, 730, 430)
boss_health_hitter = (150,65)
boss_health_buffer = (175, 685)
feint_card = (670,1025)
spellbook_coords = (1240,650, 1241, 651)

def check_for_enchant(cards,cast_flag):
    for relative_y in range(10,80,1):
        for relative_x in range (0,110,1):
            absolute_x, absolute_y = hitter_cards[0]+relative_x, hitter_cards[1]+relative_y
            if(cards[relative_x,relative_y][0] >= 160 and cards[relative_x,relative_y][0] <= 200 and cards[relative_x,relative_y][2] == 0):
                if(cast_flag==0):
                    pyautogui.moveTo(absolute_x,absolute_y)
                    pyautogui.click()
                elif(cast_flag==1):
                    pyautogui.moveTo(670,375)
                    pyautogui.click()
                    pyautogui.moveTo(boss_health_hitter)
                    pyautogui.click()
                pyautogui.moveTo(40,10)
                return True
    return False

def enchant_card(cards):
    R_range = range(80,110)
    G_range = range(20,35)
    B_range = range(90,130)
    for relative_y in range(10,80,1):
        for relative_x in range (0,110,2):
            absolute_x, absolute_y = hitter_cards[0]+relative_x, hitter_cards[1]+relative_y
            if(cards[relative_x,relative_y][0] in R_range and cards[relative_x,relative_y][1] in G_range and cards[relative_x,relative_y][2] in B_range):
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
    print(spellbook_coords[0],spellbook_coords[1], spellbook_pixel)
    if(spellbook_pixel[0]==174 and spellbook_pixel[1]==168):
        return True
    else:
        return False

while True:
    
    if(keyboard.is_pressed('`')):
        while True:
            pyautogui.keyDown('a')
            time.sleep(0.25)
            pyautogui.keyUp('a')

            pyautogui.click(feint_card)
            pyautogui.keyDown('a')
            time.sleep(0.25)
            pyautogui.keyUp('a')

            pyautogui.click(674,387)
            pyautogui.press('x')

            pyautogui.click(feint_card)
            pyautogui.keyDown('w')
            time.sleep(1)
            pyautogui.keyUp('w')
            time.sleep(6)

            cards = ImageGrab.grab(bbox=hitter_cards)
            if(check_for_enchant(cards.load(),0)): #click enchant
                    print("Found enchant")
                    time.sleep(0.25)
                    if(enchant_card(cards.load())): #enchant blizzard
                        print("Found zilla")
                        time.sleep(0.25)
                        check_for_enchant(cards.load(),1) #cast blizzard
                        pyautogui.moveTo(feint_card)
                        pyautogui.click()
                        time.sleep(0.75)
                        pyautogui.moveTo(boss_health_buffer)
                        pyautogui.click()
                        pyautogui.click(boss_health_hitter)
                    else:
                        print("Zilla not found")
            else:
                print("No enchant found")

            print("Waiting for battle to end...")
            while(not poll_fight()):
                time.sleep(1)
            print("Battle ended")
            time.sleep(1)
