# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=//Users/meduzastore/PycharmProjects/session

import sys
from selenium import webdriver
from selenium_stealth import stealth
import time
import pyautogui as pg
import randomMouse as rm
import randomCo
# /////////////////////////////////////////////////////////////////////////
def lecconv():
    debugger_address = 'localhost:9222'
    web = webdriver.ChromeOptions()
    web.add_argument('--start-maximized')
    web.add_experimental_option("debuggerAddress", debugger_address)
    driver = webdriver.Chrome(options=web)
    stealth(driver,
            languages=["fr"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            )
    driver.execute_script("window.focus();")
    time.sleep(4)
    driver.get("https://www.vinted.fr/inbox/")
    time.sleep(2)
    rm.rdmMouse(788,343)
    randomCo.randsleep()
    pg.click()
    randomCo.randsleep()
    for i in range (1,100000) :
        url = driver.current_url
        if "www.vinted.fr/inbox/" in url:
            time.sleep(2)
            pg.press('tab')
            time.sleep(2)
            pg.press('enter')
            time.sleep(2)
        else:
            sys.exit()
lecconv()