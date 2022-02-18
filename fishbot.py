# -*- coding: utf-8 -*-
"""
This project is for demonstration purposes only
I am not responsible in any way if you get banned while using this tool

Usage : Position yourself in the game in a way your line can be casted
        Launch the bot with 'python3 fishbot.py' or execute the code in your IDE
        Alt-Tab back to the game, the bot will start 5 seconds after you've executed it (You can change this value)
        When you are done with your session, press the stop key (escape by default) and the bot will indicate how many fish you caught
    
Let me know if there is any issues with this tool and keep in mind I am not responsible if you get banned while using this tool
@author: Kapwiing
"""
import pyautogui
import keyboard
import random
from time import sleep
from sys import exit

DELAY_BEFORE_LAUNCH = 5
FISHING_KEY = 'e'
STOP_KEY = 'esc'

if (type(DELAY_BEFORE_LAUNCH) != int and type(DELAY_BEFORE_LAUNCH) != float):
    print("Error : DELAY_BEFORE_LAUNCH must be either int or float value")
    exit(84)
if (type(FISHING_KEY) != str):
    print("Error : FISHING_KEY must be str")
    exit(84)
if (type(STOP_KEY) != str):
    print("Error : STOP_KEY must be str")
    exit(84)

print(f"Fishybot starting in {DELAY_BEFORE_LAUNCH} seconds !")
sleep(DELAY_BEFORE_LAUNCH)
print("Fishybot started...")

fish_count = 0
can_catch = True

while (True):
    if (keyboard.is_pressed(STOP_KEY)):
        print("Fishy bot has stopped !")
        break
    if (can_catch):
        pyautogui.press(FISHING_KEY)
        can_catch = False
    pos = pyautogui.locateOnScreen('fish_point.png', confidence=0.8)
    if (pos != None):
        pyautogui.press('e')
        print("Fish caught !")
        fish_count += 1
        sleep(round(random.uniform(6.70, 7.50), 2))
        can_catch = True
    #957 480

print(f"Fishy bot has caught : {fish_count} fish")
