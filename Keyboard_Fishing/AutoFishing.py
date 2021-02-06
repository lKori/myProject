import pyautogui as pag
import keyboard as key

def autoFishing():
    if (pag.locateAllOnScreen(r'C:\Users\yuy08\Documents\GitHub\myProject-1\F_LL.png', confidence = 0.98) == True):
        #pag.click(pag.locateCenterOnScreen('LL.png'))
        print("F_LL")
    elif (pag.locateAllOnScreen(r'C:\Users\yuy08\Documents\GitHub\myProject-1\F_L.png', confidence = 0.98) == True):
        #pag.click(pag.locateCenterOnScreen('L.png'))
        print("F_L")
    elif (pag.locateAllOnScreen(r'C:\Users\yuy08\Documents\GitHub\myProject-1\F_Center.png', confidence = 0.98) == True):
        #pag.click(pag.locateCenterOnScreen('Center.png'))
        print("Center")
    elif (pag.locateAllOnScreen(r'C:\Users\yuy08\Documents\GitHub\myProject-1\F_R.png', confidence = 0.98) == True):
        #pag.click(pag.locateCenterOnScreen('R.png'))
        print("F_R")
    elif (pag.locateAllOnScreen(r'C:\Users\yuy08\Documents\GitHub\myProject-1\F_RR.png', confidence = 0.98) == True):
        #pag.click(pag.locateCenterOnScreen('RR.png'))
        print("F_RR")

def main():
    while (True):
        autoFishing()
        if (key.is_pressed('q')):
            break

if __name__ == "__main__":
    main()