import random
import time

import pyautogui as pg
from selenium import webdriver

def autosrcoll(pixel):
    i = 0
    while i != pixel:
        if pixel < 0 :
            pg.scroll(-1)
            i = i - 1
        else:
            pg.scroll(1)
            i = i + 1
        time.sleep(random.uniform(0.02, 0.05))

def autoscrollend(driver):
    # driver.get("https://www.meduzastore.com/")
    time.sleep(4)
    for i in range(0, 25):
        autosrcoll(-2)
        time.sleep(random.uniform(0.000001, 0.005))

def autoscrolldeb(driver):
    # driver.get("https://www.meduzastore.com/")
    time.sleep(4)
    for i in range(0, 25):
        autosrcoll(1)
        time.sleep(random.uniform(0.000001, 0.005))

