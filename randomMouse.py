import random
import pyautogui


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Args
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def rdmMouse(x,y):
    i = random.randint(10,15)
    j = random.randint(1,9)
    z = round(((i*j)/10)+1)
    #print(z)
    vit = random.randint(2,8)
    if z==2:
        pyautogui.moveTo(x, y, 5, pyautogui.easeInQuad)
    elif z==3:
        pyautogui.moveTo(x, y, vit, pyautogui.easeInQuad)
    elif z==4:
        pyautogui.moveTo(x, y, 3, pyautogui.easeOutQuad)
    elif z==5:
        pyautogui.moveTo(x, y, 5, pyautogui.easeOutQuad)
    elif z==6:
        pyautogui.moveTo(x, y, vit, pyautogui.easeOutQuad)
    elif z==7:
        pyautogui.moveTo(x, y, 2, pyautogui.easeInOutQuad)
    elif z==8:
        pyautogui.moveTo(x, y, 4, pyautogui.easeInOutQuad)
    elif z==9:
        pyautogui.moveTo(x, y, vit, pyautogui.easeInOutQuad)
    elif z==10:
        pyautogui.moveTo(x, y, 4, pyautogui.easeInBounce)
    elif z==11:
        pyautogui.moveTo(x, y, 8, pyautogui.easeInBounce)
    elif z==12:
        pyautogui.moveTo(x, y, vit, pyautogui.easeInBounce)
    elif z==13:
        pyautogui.moveTo(x, y, 3, pyautogui.easeInElastic)
    elif z==14:
        pyautogui.moveTo(x, y, 7, pyautogui.easeInElastic)
    elif z==15:
        pyautogui.moveTo(x, y, vit, pyautogui.easeInElastic)
    else:
        pyautogui.moveTo(x, y, 2, pyautogui.easeInQuad)



'''
pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)     # start slow, end fast
pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)    # start fast, end slow
pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutQuad)  # start and end fast, slow in middle
pyautogui.moveTo(100, 100, 2, pyautogui.easeInBounce)   # bounce at the end
pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)  # rubber band at the end
'''