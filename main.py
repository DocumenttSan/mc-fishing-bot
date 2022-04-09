from turtle import screensize
import pyautogui
from time import sleep

def fish():
    while(True):
        dingdong = pyautogui.locateOnScreen(,'E:/Minecraft_fishingBot/asset/splash.png')
        print('works')
        if dingdong:
            sleep(0.2)
            pyautogui.rightClick()
            sleep(1)
            pyautogui.rightClick()
            
def main():
    fish()
    
main()
      
        
        
        
    