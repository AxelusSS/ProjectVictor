from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
import pyautogui as pg

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Solution Frontend pour le moment
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
'''
driver.get('https://vinted.fr')
y = randint(2,7)
time.sleep(y)
driver.find_element(By.CSS_SELECTOR, '#__next > div > div > div.l-header.js-header > header > div > div > div.u-flexbox.u-margin-left-auto.u-align-items-center.u-position-relative.u-z-index-notification > div.u-desktops-only.u-flexbox.u-align-items-center > a.web_ui__Button__button.web_ui__Button__filled.web_ui__Button__small.web_ui__Button__primary.web_ui__Button__truncated').click()
time.sleep(3)
#driver.move_to_element("#userNameField > div > input")
driver.find_element(By.ID,'description').click()
for L in "Pack Vêtements de marque de seconde main haut + pull + pantalon " :
    driver.find_element(By.ID,'description').send_keys(L)
    i = random.uniform(0.0 , 0.5)
    time.sleep(i)
time.sleep(10)
#time.sleep(3)
for L in "Pack Meduza deal" :
    driver.find_element(By.ID,'title').send_keys(L)
    i = random.uniform(0.0 , 0.5)
    time.sleep(i)
time.sleep(4)
driver.find_element(By.CSS_SELECTOR, '#content > div > div > div.form-actions.u-clearfix.u-ui-margin-bottom-x2-large > div > button.web_ui__Button__button.web_ui__Button__outlined.web_ui__Button__default.web_ui__Button__primary.web_ui__Button__inline.web_ui__Button__truncated').click()

#smolCat
time.sleep(20)
driver.quit()
'''

#time.sleep(4)
print(pg.position())
#pg.leftClick(603, 1387, 1, 1)
#pg.leftClick(98, 89, 1, 1)
#pg.moveTo(x=942, y=507)
#time.sleep(0.3)
#pg.scroll(-30)


#'''
driver.get('https://bot.incolumitas.com/')
time.sleep(0.2)
pg.moveTo(x=942, y=507, duration=2, tween=pg.easeInQuad)
time.sleep(0.3)
pg.scroll(-30)
action = ActionChains(driver)
time.sleep(0.3)
pg.moveTo(x=1021, y=756, duration=2, tween=pg.easeInBounce)
pg.click()
time.sleep(0.3)
for L in "PasUnBotDu_82" :
    driver.find_element(By.CSS_SELECTOR, "#userNameField > div > input").send_keys(L)
    i = random.uniform(0.0001 , 0.3)
    time.sleep(i)
pg.moveTo(x=840, y=835, duration=2, tween=pg.easeInQuad)
pg.click()
time.sleep(0.3)
m = driver.find_element(By.CSS_SELECTOR, "#emailField > div > input")
action = ActionChains(driver)
action.move_to_element(m)
time.sleep(0.3)
action.click(m)
for L in "Hello@gmail.com" :
    driver.find_element(By.CSS_SELECTOR, "#emailField > div > input").send_keys(L)
    i = random.uniform(0.0001 , 0.3)
    time.sleep(i)
time.sleep(0.5)
pg.moveTo(x=983, y=904, duration=2, tween=pg.easeInBounce)
pg.click()
time.sleep(0.6)
pg.moveTo(x=977, y=963, duration=2, tween=pg.easeInQuad)
pg.click()
time.sleep(0.7)
pg.moveTo(x=816, y=947, duration=2, tween=pg.easeOutQuad)
pg.click()
time.sleep(0.8)
pg.moveTo(x=911, y=985, duration=2, tween=pg.easeInElastic)
pg.click()
time.sleep(0.9)
pg.moveTo(x=821,y=1043,duration=2,tween=pg.easeOutQuad)
pg.click()
time.sleep(20)
driver.quit()
#'''



'''
# Run in headless mode
#custom_options.add_argument("--headless")
# Disable the AutomationControlled feature of Blink rendering engine
web.add_argument('--disable-blink-features=AutomationControlled')
# Disable pop-up blocking
web.add_argument('--disable-popup-blocking')
# Start the browser window in maximized mode

# Disable extensions
#custom_options.add_argument('--disable-extensions')
# Disable sandbox mode
web.add_argument('--no-sandbox')
# Disable shared memory usage
web.add_argument('--disable-dev-shm-usage')
#
web.add_experimental_option("debuggerAddress", debugger_address)

# Initialize the ChromeDriver with the appropriate service and custom options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)

# Change the property value of the navigator for webdriver to undefined
#driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# Step 3: Rotate user agents
custom_user_agents = [
    #'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    #'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36',
]

# Select a random user agent
custom_user_agent = random.choice(custom_user_agents)

# Pass in the selected user agent as an argument
web.add_argument(f'user-agent={custom_user_agent}')

# Set user agent using execute_cpd_cmd
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": custom_user_agent})

stealth(driver,
        languages=["fr"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )



driver.get('https://vinted.fr')
#element = driver.find_element_by_id('element-id')
#element.click()
driver.find_element(By.CSS_SELECTOR, '#__next > div > div > div.l-header.js-header > header > div > div > div.u-flexbox.u-margin-left-auto.u-align-items-center.u-position-relative.u-z-index-notification > div.u-desktops-only.u-flexbox.u-align-items-center > a.web_ui__Button__button.web_ui__Button__filled.web_ui__Button__small.web_ui__Button__primary.web_ui__Button__truncated').click()
y = randint(2,7)
time.sleep(y)
driver.find_element(By.ID,'description').send_keys("Ceci est un pack Mandatory")
y = randint(3,7)
time.sleep(y)
driver.find_element(By.ID,'title').send_keys("Mandatory")
y = randint(2,7)
time.sleep(y)
driver.find_element(By.ID,'price').send_keys("150")
y = randint(2,7)
time.sleep(y)
#web.find_element(By.CSS_SELECTOR,'#photos > div.web_ui__Cell__cell.web_ui__Cell__wide > div > div > div > div.media-select__input > div > button').click()
#driver.find_element(By.CSS_SELECTOR,'#photos > div.web_ui__Cell__cell.web_ui__Cell__wide > div > div > div.dropzone > div.media-select__grid > div:nth-child(1) > div.u-cursor-grab > div > div > div > img').send_keys('/Users/meduzastore/Downloads/MEDUZA STORE 2/(1)Dim 11 fév.png')
input_element = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
y = randint(2,7)
time.sleep(y)
input_element.send_keys("/Users/meduzastore/Downloads/MEDUZA STORE 2/(1)Dim 11 fév.png")
time.sleep(10)
'''


'''
# Navigate to Deezer website
driver.get('https://www.deezer.com/en/channels/explore/')

# Wait for the privacy 'Accept' pop-up button to be visible
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.ID, "gdpr-btn-accept-all")))

# Find and click the 'Accept' button on the privacy pop-up
agree_button = driver.find_element(By.XPATH, "//button[text()='Accept']")
agree_button.click()

# Scrape channel categories
categories = driver.find_elements(By.CLASS_NAME, 'picture-img')

# Print the text of each non-empty category
[print(category.text) for category in categories if category.text]






driver.quit()
'''