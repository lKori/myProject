import pyautogui as pag
import keyboard as key

lcs = pag.locateCenterOnScreen
clc = pag.click
keypre = key.is_pressed
pre = pag.press

def KeyboardFishing():
    if (keypre('z')):
        clc(lcs('LL.png'))
        pre('space')
        #print("F_LL")
    elif (keypre('x')):
        clc(lcs('L.png'))
        pre('space')
        #print("F_L")
    elif (keypre('c')):
        clc(lcs('Center.png'))
        pre('space')
        #print("Center")
    elif (keypre('v')):
        clc(lcs('R.png'))
        pre('space')
        #print("F_R")
    elif (keypre('b')):
        clc(lcs('RR.png'))
        pre('space')
        #print("F_RR")

def main():
    while (True):
        KeyboardFishing()
        if (keypre('f2')):
            break

if __name__ == "__main__":
    main()