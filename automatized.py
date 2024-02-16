import sys
import time
from random import randint
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os
import login

# Specify the debugging address for the already opened Chrome browser
from selenium.webdriver.common.by import By


#cmd = "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=//Users/meduzastore/PycharmProjects/session"

#os.system(cmd)
#time.sleep(20)

debugger_address = 'localhost:9222'

# Set up ChromeOptions and connect to the existing browser
c_options = Options()
c_options.add_experimental_option("debuggerAddress", debugger_address)

# Initialize the WebDriver with the existing Chrome instance
web = webdriver.Chrome(options=c_options)

# Now, you can interact with the already opened Chrome browser
web.get('https://vinted.fr')
#element = driver.find_element_by_id('element-id')
#element.click()
web.find_element(By.CSS_SELECTOR, '#__next > div > div > div.l-header.js-header > header > div > div > div.u-flexbox.u-margin-left-auto.u-align-items-center.u-position-relative.u-z-index-notification > div.u-desktops-only.u-flexbox.u-align-items-center > a.web_ui__Button__button.web_ui__Button__filled.web_ui__Button__small.web_ui__Button__primary.web_ui__Button__truncated').click()
y = randint(2,7)
time.sleep(y)
web.find_element(By.ID,'description').send_keys("Ceci est un jersey de la marque Mandatory")
y = randint(3,7)
time.sleep(y)
web.find_element(By.ID,'title').send_keys("Mandatory")
y = randint(2,7)
time.sleep(y)
web.find_element(By.ID,'price').send_keys("50")
y = randint(2,7)
time.sleep(y)
#web.find_element(By.CSS_SELECTOR,'#photos > div.web_ui__Cell__cell.web_ui__Cell__wide > div > div > div > div.media-select__input > div > button').click()
#web.find_element(By.CSS_SELECTOR,'#photos > div.web_ui__Cell__cell.web_ui__Cell__wide > div > div > div.dropzone > div.media-select__grid > div:nth-child(1) > div.u-cursor-grab > div > div > div > img').send_keys('/Users/meduzastore/Downloads/MEDUZA STORE 2/(1)Dim 11 fév.png')
#input_element = web.find_element(By.CSS_SELECTOR, 'input[type="file"]')
#input_element.send_keys("/Users/meduzastore/Downloads/MEDUZA STORE 2/(1)Dim 11 fév.png")
time.sleep(10)


web.find_element(By.CSS_SELECTOR,'#content > div > div > div:nth-child(8) > div:nth-child(1) > div > div').click()
time.sleep(3)
web.find_element(By.CSS_SELECTOR,'#catalog-5').click()
time.sleep(5)
web.find_element(By.CSS_SELECTOR,'#catalog-2050').click()
time.sleep(4)
web.find_element(By.CSS_SELECTOR,'#catalog-76').click()
time.sleep(4)
web.find_element(By.CSS_SELECTOR,'#catalog-77').click()
time.sleep(3)
web.find_element(By.CSS_SELECTOR,'#catalog-1806').click()
time.sleep(5)

web.find_element(By.CSS_SELECTOR,'#content > div > div > div:nth-child(8) > div:nth-child(3) > div.c-input__content > div').click()
time.sleep(6)
web.find_element(By.CSS_SELECTOR,'#brand-53').click()
time.sleep(2)

web.find_element(By.CSS_SELECTOR,'#content > div > div > div:nth-child(8) > div:nth-child(5) > div.c-input__content > div').click()
time.sleep(3)
web.find_element(By.CSS_SELECTOR,'#size-209').click()
time.sleep(2)

web.find_element(By.CSS_SELECTOR,'#shoulder_width').send_keys("70")
time.sleep(3)
web.find_element(By.CSS_SELECTOR,'#height').send_keys("90")
time.sleep(2)

web.find_element(By.CSS_SELECTOR,'#content > div > div > div:nth-child(8) > div:nth-child(9) > div > div').click()
time.sleep(3)
web.find_element(By.CSS_SELECTOR,'#status-2 > div.web_ui__Cell__suffix > label > span.web_ui__Radio__button').click()
time.sleep(2)

web.find_element(By.CSS_SELECTOR,'#content > div > div > div:nth-child(8) > div:nth-child(11) > div > div').click()
time.sleep(3)
web.find_element(By.CSS_SELECTOR,'#color-3 > div.web_ui__Cell__suffix > label > span').click()
time.sleep(2)
web.find_element(By.CSS_SELECTOR,'#content > div > div > div:nth-child(8) > div:nth-child(11) > div > div').click()
time.sleep(3)

web.find_element(By.CSS_SELECTOR,'#content > div > div > div:nth-child(8) > div:nth-child(13) > div.c-input.c-input--wide > div > div > span').click()
time.sleep(3)
web.find_element(By.CSS_SELECTOR,'#material-45 > div.web_ui__Cell__suffix > label > span').click()
time.sleep(5)
web.find_element(By.CSS_SELECTOR,'#content > div > div > div:nth-child(8) > div:nth-child(13) > div.c-input.c-input--wide > div > div > span').click()
time.sleep(4)

web.find_element(By.CSS_SELECTOR,'#package-size-1 > div.web_ui__Cell__suffix > label > span.web_ui__Radio__button').click()
time.sleep(8)


web.find_element(By.CSS_SELECTOR, '#content > div > div > div.form-actions.u-clearfix.u-ui-margin-bottom-x2-large > div > button.web_ui__Button__button.web_ui__Button__outlined.web_ui__Button__default.web_ui__Button__primary.web_ui__Button__inline.web_ui__Button__truncated').click()
time.sleep(login.waitTime)

# Remember to close the WebDriver when you're done
web.quit()




'''

/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=//Users/meduzastore/PycharmProjects/session

'''