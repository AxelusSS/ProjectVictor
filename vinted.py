from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import pyautogui as pg
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
import pyautogui as pg
import randomMouse
import randomCo

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Solution Frontend (dev de la solution Backend après avoir fini)
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
debugger_address = 'localhost:9222'

## Create a ChromeOptions object
web = webdriver.ChromeOptions()
web.add_argument('--start-maximized')
#web.add_experimental_option("excludeSwitches", ["enable-automation"])
#web.add_experimental_option("useAutomationExtension", False)
web.add_experimental_option("debuggerAddress", debugger_address)

driver = webdriver.Chrome(options=web)

stealth(driver,
        languages=["fr"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        )

driver.get('https://vinted.fr')
time.sleep(4)
x, y = randomCo.rdmcreateco()
randomMouse.rdmMouse(x, y)
pg.click()
time.sleep(2.4)


####################################
x, y = randomCo.rdmdescco()
randomMouse.rdmMouse(x, y)
pg.click()
#driver.find_element(By.ID,'description').click()
for L in "Pack Vêtements de marque de seconde main haut + pull + pantalon " :
    driver.find_element(By.ID,'description').send_keys(L)
    i = random.uniform(0.0001 , 0.3)
    time.sleep(i)
time.sleep(3.7)


####################################
x, y = randomCo.rdmtitleco()
randomMouse.rdmMouse(x, y)
pg.click()
for L in "Pack Meduza deal" :
    driver.find_element(By.ID,'title').send_keys(L)
    i = random.uniform(0.0001 , 0.3)
    time.sleep(i)
time.sleep(4.1)


####################################
x, y = randomCo.rdmprixco()
randomMouse.rdmMouse(x, y)
pg.click()
for L in "150" :
    driver.find_element(By.ID,'price').send_keys(L)
    i = random.uniform(0.0001 , 0.3)
    time.sleep(i)
time.sleep(4.1)



####################################
time.sleep(3.1)
x, y = randomCo.rdmbrouillonco()
randomMouse.rdmMouse(x, y)
pg.click()




time.sleep(20)
driver.quit()
