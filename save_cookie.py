from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time
import pickle

if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    #options.add_argument('proxy-server=106.122.8.54:3128')
    options.add_argument('--user-data-dir=/Users/meduzastore/Library/Application Support/Google/Chrome/Default')

    browser = uc.Chrome(
        #options=options,
    )
    browser.get('https://vinted.fr')
    time.sleep(120)

    cookies = browser.get_cookies()

    pickle.dump(cookies, open("cookies.pkl", "wb"))
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Save Cookie from gmail
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#
#if __name__ == '__main__':
    #email = "meduza.estore@gmail.com"
    #password = "MS2022renouveau@"

    #options = webdriver.ChromeOptions()
    ##options.add_argument('proxy-server=106.122.8.54:3128')
    #options.add_argument('--user-data-dir=/Users/meduzastore/Library/Application Support/Google/Chrome/Default')

    #browser = uc.Chrome(
        #options=options,
    #)
    #browser.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

    #browser.find_element(By.ID, 'identifierId').send_keys(email)

    #browser.find_element(
        #By.CSS_SELECTOR, '#identifierNext > div > button > span').click()

    #password_selector = "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input"

    #WebDriverWait(browser, 10).until(
        #EC.visibility_of_element_located((By.CSS_SELECTOR, password_selector)))

    #browser.find_element(
        #By.CSS_SELECTOR, password_selector).send_keys(password)

    #browser.find_element(
        #By.CSS_SELECTOR, '#passwordNext > div > button > span').click()

    #time.sleep(5)

    #cookies = browser.get_cookies()

    #pickle.dump(cookies, open("cookies.pkl", "wb"))

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Connection par GMAIL
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    #options.add_argument('proxy-server=106.122.8.54:3128')
    options.add_argument('--user-data-dir=/Users/meduzastore/Library/Application Support/Google/Chrome/Default')
    web = uc.Chrome(options=options)
    #web = uc.Chrome()

    web.get('https://www.vinted.fr/member/16451173-meduza-store')
    #web.add_cookie(cookie)
    time.sleep(10)
    web.find_element(By.CSS_SELECTOR,
        '#__next > div > div > div.l-header.js-header > header > div > div > div.u-flexbox.u-margin-left-auto.u-align-items-center.u-position-relative.u-z-index-notification > div > a.web_ui__Button__button.web_ui__Button__outlined.web_ui__Button__small.web_ui__Button__primary.web_ui__Button__truncated').click()
    time.sleep(5)
    web.find_element(By.CSS_SELECTOR,
                         'body > div:nth-child(58) > div > div > div > div.u-overflow-auto > div.u-ui-padding-horizontal-large.u-ui-padding-bottom-x-large > a').click()
    time.sleep(3)
    web.find_element(By.ID, 'identifierId').send_keys("meduza.estore@gmail.com")
    time.sleep(3)
    web.find_element(By.CSS_SELECTOR, '#identifierNext > div > button > span').click()
    time.sleep(10)
    web.find_element(By.CSS_SELECTOR, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input').send_keys(
            "MS2022renouveau@")
    time.sleep(3)
    web.find_element(By.CSS_SELECTOR, '#passwordNext > div > button > span').click()
'''
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Connection par Login et Mdp Vinted mais impossible le site renvoie sur un captcha
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#web.find_element(By.CSS_SELECTOR, '#__next > div > div > div.l-header.js-header > header > div > div > div.u-flexbox.u-margin-left-auto.u-align-items-center.u-position-relative.u-z-index-notification > div > a.web_ui__Button__button.web_ui__Button__outlined.web_ui__Button__small.web_ui__Button__primary.web_ui__Button__truncated').click()
#time.sleep(10)
#web.find_element(By.CSS_SELECTOR, 'body > div:nth-child(58) > div > div > div > div.u-overflow-auto > div.u-ui-padding-horizontal-large.u-ui-padding-bottom-x-large > span:nth-child(12) > span > span').click()
#time.sleep(10)
#web.find_element(By.CSS_SELECTOR, 'body > div:nth-child(58) > div > div > div > div.u-overflow-auto > div > span:nth-child(10) > span > span').click()
#time.sleep(10)
#web.find_element(By.CSS_SELECTOR, '#username').send_keys(login.login)
#time.sleep(5)
#web.find_element(By.CSS_SELECTOR, '#password').send_keys(login.pwd)
#time.sleep(10)
#web.find_element(By.CSS_SELECTOR, 'body > div:nth-child(58) > div > div > div > div.u-overflow-auto > form > div.web_ui__Cell__cell.web_ui__Cell__default > div > div > button').click()
#time.sleep(30)
#cookies = web.get_cookies()
#pickle.dump(cookies, open("cookies.pkl", "wb"))

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Brouillon Code
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
web.find_element(By.CSS_SELECTOR, '#__next > div > div > div.l-header.js-header > header > div > div > div.u-flexbox.u-margin-left-auto.u-align-items-center.u-position-relative.u-z-index-notification > div.u-desktops-only.u-flexbox.u-align-items-center > a.web_ui__Button__button.web_ui__Button__filled.web_ui__Button__small.web_ui__Button__primary.web_ui__Button__truncated').click()
time.sleep(5)
web.find_element(By.ID,'title').send_keys("Mandatory")
time.sleep(2)
web.find_element(By.ID,'description').send_keys("Ceci est un jersey de la marque Mandatory")
time.sleep(2)
web.find_element(By.CSS_SELECTOR, '#content > div > div > div.form-actions.u-clearfix.u-ui-margin-bottom-x2-large > div > button.web_ui__Button__button.web_ui__Button__outlined.web_ui__Button__default.web_ui__Button__primary.web_ui__Button__inline.web_ui__Button__truncated').click()
time.sleep(10)
'''