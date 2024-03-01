from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from selenium_stealth import stealth
import re
import sqlite3


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Solution Backend (Front pour le moment) pour récuperer les items vendu (recup par les messages avec l'ID des messages et le QWE)
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

debugger_address = 'localhost:9222'

## Create a ChromeOptions object
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
def rsp(id):
    try:
        driver.get(f'https://www.vinted.fr/inbox/{id}')
        time.sleep(4)

        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        try:
            sale = driver.find_element(By.CSS_SELECTOR, '#content > div > div > div.u-flexbox.u-fill-width > div.u-fill-width > div > div > div.u-flexbox > div.u-fill-width > div > div > div > div.thread__messages-wrapper > div > div > div > div:nth-child(13) > span > div > div > div > div > div > div.web_ui__Cell__heading > div > h2')
            vendu = sale.text
        except:
            vendu = "Pas Vendu !"

        if vendu == "Vendu !":
            #
            # Trouver le prix exacte de vente sur vinted, extraction d'un span (ecrit en dessous de VENDU)
            #
            """
            if id != None:
                #prixbrut = WebDriverWait(driver, 10).until(
                    #driver.find_element(By.CSS_SELECTOR, '#content > div > div > div.u-flexbox.u-fill-width > div.u-fill-width > div > div > div.u-flexbox > div.u-fill-width > div > div > div > div.thread__messages-wrapper > div > div > div > div:nth-child(5) > span > div > div > div > div > div > div.web_ui__Cell__body')
                #)
                #prixbrut = " ", EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div/div/div[5]/div/div/div/div[5]/span/div/div/div/div/div/div[2]/span')).text
                prixbrut = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div/div/div[5]/div/div/div/div[5]/span/div/div/div/div/div/div[2]/span'))
                )
                pb = prixbrut.text
                #prixbrut = soup.find("span", {"class": "web_ui__Text__text web_ui__Text__body web_ui__Text__left web_ui__Text__muted"}).text
                print(pb)
                motif_regex = r'(\d{1,3}(?:,\d{3})*(?:\.\d+)?)\s*€'
                correspondances = re.findall(motif_regex, pb)
                prix = [float(montant.replace(',', '')) for montant in correspondances]
                print(prix)
            else:
                prix = soup.find("span", {"class": "web_ui__Text__text web_ui__Text__body web_ui__Text__left web_ui__Text__amplified"})
            """

            prix = soup.find("span", {
                "class": "web_ui__Text__text web_ui__Text__body web_ui__Text__left web_ui__Text__amplified"})

            if prix:
                print(prix)
                title = driver.find_element(By.CSS_SELECTOR, '#content > div > div > div.u-flexbox.u-fill-width > div.u-fill-width > div > div > div.u-flexbox > div.u-fill-width > div > div > div > div.web_ui__Cell__cell.web_ui__Cell__default > div.web_ui__Cell__content > div.web_ui__Cell__heading > div > a > div > div > h2')
                qwe = title.text[-8:]
                print(qwe)
                driver.find_element(By.CSS_SELECTOR, '#content > div > div > div.u-flexbox.u-fill-width > div.u-fill-width > div > div > div.u-flexbox > div.u-fill-width > div > div > div > div.web_ui__Cell__cell.web_ui__Cell__default > div.web_ui__Cell__content > div.web_ui__Cell__heading > div > a').click()
                link = driver.current_url
                link = link[28:28+10]
                print(link)
                print("-------------------------")
            else:
                print("Prix non trouvé")
        else :
            print("L'article n'est pas vendu")
    except Exception as e:
        print("ERROR :", str(e))

def findcon():
    sqlite_file = 'vinted.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS ID_Conv
                 (ID_Chat, ID_User)''')
    driver.get('https://www.vinted.fr/inbox')
    driver.find_element(By.CSS_SELECTOR,'#content > div > div > div.u-flexbox.u-fill-width > div.u-fill-width > div > div > div.u-flexbox > div.inbox-page__block.inbox-page__block--sidebar > div > div.u-fill-height.u-overflow-auto > div.web_ui__Cell__cell.web_ui__Cell__default.web_ui__Cell__inverseExperimental.web_ui__Cell__navigating').click()
    while 1 == 1:
        id_chat = 0
        id_user = 1
        if not c.execute("SELECT 1 FROM ID_Conv WHERE ID = ?", (id,)).fetchone():
            params = (
                id_chat, id_user
            )
            c.execute(
                "INSERT INTO Sale(ID, Qwe, Price, Sale)VALUES (?,?,?,?)",
                params)
            conn.commit()

id = 10745638876
rsp(id)
id = 10770439712
rsp(id)
driver.get('https://www.vinted.fr/')

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Solution Backend (on peut voir l'execution sur la page Chrome mais pas besoin d'avoir le tab ouvert) pour récuperer les items vendu (recup par les message avec l'ID des messages)
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def scroll_to_bottom(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)



def soldall():
    solditem = 0
    try:
        sqlite_file = 'vinted.sqlite'
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS Sale
                     (ID, Qwe, Price, Sale, RSP, Acheteur_ID, Chat_ID)''')
        driver.get("https://www.vinted.fr/member/16451173")
        time.sleep(4)
        driver.find_element(By.CSS_SELECTOR, "#content > div > div > div > div.profile__items-wrapper > div.web_ui__Container__container > div.u-flexbox.u-flex-wrap.u-align-items-center.u-justify-content-between > div.u-tablets-up-only > div.u-position-relative.u-overflow-hidden > div > div > div > button:nth-child(9) > div > span").click()
        time.sleep(4)
        old_count = len(driver.find_elements(By.CSS_SELECTOR, "[data-testid]"))
        while True:
            scroll_to_bottom(driver)
            time.sleep(2)

            elements = driver.find_elements(By.CSS_SELECTOR, "[data-testid]")
            pattern = r'\b\d{10}\b'
            unique_values = set()
            for element in elements:
                value = element.get_attribute("data-testid")
                matches = re.findall(pattern, value)
                title = element.get_attribute('title')
                prix = element.get_attribute('price')
                qwe = title[-8:]
                for match in matches:
                    if match not in unique_values:
                        unique_values.add(match)
                        vendu = True
                        solditem = solditem + 1
                        if not c.execute("SELECT 1 FROM Sale WHERE ID = ?", (match,)).fetchone():
                            params = (
                                match, qwe, prix, vendu
                            )
                            c.execute(
                                "INSERT INTO Sale(ID, Qwe, Price, Sale)VALUES (?,?,?,?)",
                                params)
                            conn.commit()
                    print("Sous-chaîne récupérée :", match)
                    print("QWE récupérée :", qwe)
                    print("Prix récupérée :", prix)
                    print("----------------------------------")

            new_count = len(driver.find_elements(By.CSS_SELECTOR, "[data-testid]"))

            if new_count == old_count:
                break

            old_count = new_count
        print(solditem)
    except Exception as e:
        print("Marche pas ton truc là...")
        print("Une erreur s'est produite :", str(e))

#soldall()



# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=//Users/meduzastore/PycharmProjects/session

# Selector bouton télécharger msg : #content > div > div > div.u-flexbox.u-fill-width > div.u-fill-width > div > div > div.u-flexbox > div.u-fill-width > div > div > div > div.thread__messages-wrapper > div > div > div > div.conversation-message__status.u-sticky-top.u-zindex-bump > span > div > div > div > div > div > div.web_ui__Cell__body > div.u-flexbox > div:nth-child(3) > button