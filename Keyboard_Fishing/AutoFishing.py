import pyautogui as pag
import keyboard as key
from PIL import ImageGrab

while (1):
    #print(pag.position()) # 현재 마우스 좌표 출력
    screen = ImageGrab.grab()
    print(screen.getpixel(pag.position())) #현재 마우스 좌표의 색상 출력
    if ((178, 255, 178) == screen.getpixel(pag.position())): #해당 색상과 같을 경우 클릭
        pag.click(242, 323)