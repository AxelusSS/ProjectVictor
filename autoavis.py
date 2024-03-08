# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=//Users/meduzastore/PycharmProjects/session

import sys
import pyperclip
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
import time
import pyautogui as pg
import randomMouse as rm
import randomCo
# /////////////////////////////////////////////////////////////////////////
def autoavis():
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
    press = 1
    for i in range(1, 40):
        try:
            driver.get('https://www.vinted.fr/wallet/balance')
        except:
            rm.rdmMouse(688,134)
            randomCo.randsleep()
            pg.click()
            time.sleep(4)
        time.sleep(10)
        element = driver.find_element(By.CSS_SELECTOR,
                                      "#content > div > div > div:nth-child(6) > div.web_ui__Cell__cell.web_ui__Cell__default")
        window_width = driver.execute_script("return window.innerWidth;")
        window_height = driver.execute_script("return window.innerHeight;")
        element_x = element.location['x']
        element_y = element.location['y']
        element_width = element.size['width']
        element_height = element.size['height']
        scroll_x = element_x - (window_width / 2) + (element_width / 2)
        scroll_y = element_y - (window_height / 2) + (element_height / 2)
        time.sleep(3)
        driver.execute_script("window.scrollTo({0}, {1});".format(scroll_x, scroll_y))
        time.sleep(4)
        rm.rdmMouse(1295, 656)
        pg.click()
        time.sleep(3)
        for i in range(press):
            pg.press("tab")
            randomCo.randsleep()
        pg.press("enter")
        time.sleep(4)
        url = driver.current_url
        if "www.vinted.fr/inbox/" in url:
            try:
                element = driver.find_element(By.CSS_SELECTOR,
                                              "#content > div > div > div.u-flexbox.u-fill-width > div.u-fill-width > div > div > div.u-flexbox > div.u-fill-width > div > div > div > div.thread__messages-wrapper > div > div > div > div.conversation-message__status.u-sticky-top.u-zindex-bump > span > div > div > div > div > div > div.web_ui__Cell__body > div.u-flexbox > div:nth-child(3)")
                time.sleep(3)
                rm.rdmMouse(1242,1095)
                time.sleep(3)
                pg.click()
                time.sleep(6)
                rm.rdmMouse(1124,450)
                time.sleep(3)
                pg.click()
                time.sleep(3)
                rm.rdmMouse(1392,534)
                time.sleep(3)
                pg.click()
                element = driver.find_element(By.CSS_SELECTOR,"#content > div > div > div:nth-child(3) > div.web_ui__Cell__content > div > span")
                pseudo = element.text
                avis = f"""Salut {pseudo} !
Merci de faire vivre la mode durable chez Meduza-Store 🦾😉
Soyez au rendez-vous chaque jour pour les nouveautés, et découvrez votre futur coup de coeur ❤️!️"""
                pyperclip.copy(avis)
                time.sleep(2)
                pg.hotkey('command', 'v')
                time.sleep(8)
                rm.rdmMouse(1443, 666)
                randomCo.randsleep()
                pg.click()
                time.sleep(2)
            except:
                print("Avis déjà envoyé")
                rm.rdmMouse(688,134)
                randomCo.randsleep()
                pg.click()
                time.sleep(4)
                press = press + 1
        else:
            driver.get('https://www.vinted.fr/wallet/balance')
            press = press + 1
    print("Fin des avis disponible")
    sys.exit()


