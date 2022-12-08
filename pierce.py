import pyautogui
import keyboard
from PIL import ImageGrab

cards_coordinates = (608, 345, 730, 430)

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
while True:
    cards = ImageGrab.grab(cards_coordinates)
    if(keyboard.is_pressed('`')):
        if(check_for_enchant(cards.load(),0)): #click enchant
            if(enchant_card(cards.load())): #enchant blizzard
                check_for_enchant(cards.load(),1) #cast blizzard
            else:
                print("Blizzard not found")
        else:
            print("No enchant found")