# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=//Users/meduzastore/PycharmProjects/session

import os
import sys

from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from autoscroll import autoscrollend
from autoscroll import autoscrolldeb
import random
import time
import pyautogui as pg
import photo
import randomMouse
import titres
import clipboard
import randomCo
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Solution Frontend (dev de la solution Backend après avoir fini)
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def vinted(title, qwe, ids, price, gender, typeitem, taille, categorie, catbrut, brand, state, matter, color, length,
           width, sleeve, tags, photos):
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
    driver.get('https://vinted.fr')
    time.sleep(4)
    randomCo.rdmcreateco()
    time.sleep(2.4)
    # /////////////////////////////////// Remplissage Prix ///////////////////////////////////
    randomCo.rdmprixco()
    try:
        prix = price
    except:
        prix = "0"
    for L in prix :
        r = random.randint(1,5)
        if r == 1 or r == 3:
            driver.find_element(By.ID,'price').send_keys(L)
            i = random.uniform(0.0001 , 0.3)
            time.sleep(i)
            pg.press("backspace")
            driver.find_element(By.ID,'price').send_keys(L)
            i = random.uniform(0.0001 , 0.3)
            time.sleep(i)
        else:
            driver.find_element(By.ID,'price').send_keys(L)
            i = random.uniform(0.0001 , 0.3)
            time.sleep(i)
    time.sleep(4.1)
    url = driver.current_url
    if "www.vinted.fr/items/new" not in url:
        sys.exit()
    # /////////////////////////////////// Remplissage Cat ///////////////////////////////////
    time.sleep(1.63)
    try:
        sexe = gender
    except:
        sexe = "Homme"
    try:
        cat = catbrut
    except:
        cat = "Homme > Chemises > Chemises classiques"
    try:
        id = ids
    except:
        id = "123456"
    if sexe == "Homme" or sexe == "Femme":
        if "Robe" in cat:
            randomCo.robe(sexe, id)
        elif "Maillots" in cat:
            randomCo.hautsport(sexe, id)
        elif "Bermudas" in cat or "Short de sport" in cat or "Shorts casual" in cat:
            randomCo.autreshort(sexe, id)
        elif "Shorts en jean" in cat:
            randomCo.shortjeans(sexe, id)
        elif "Femme" in cat and "Jeans &amp; Pantalons" in cat and "Pantalons slim" in cat:
            randomCo.pantalonajuste(sexe, id)
        elif "Femme" in cat and "Jeans &amp; Pantalons" in cat and "Pantalons classiques" in cat:
            randomCo.pantalonajuste(sexe, id)
        elif "Homme" in cat and "Shorts &amp; Bermudas" in cat and "Shorts casual" in cat:
            randomCo.shortcasual(sexe, id)
        elif "Homme" in cat and "Jeans &amp; Pantalons" in cat and "Jeans coupe ajustée" in cat:
            randomCo.jeanslim(sexe, id)
        elif "Homme" in cat and "Jeans &amp; Pantalons" in cat and "Jeans coupe slim" in cat:
            randomCo.jeanslim(sexe, id)
        elif "Homme" in cat and "Jeans &amp; Pantalons" in cat and "Pantalons cargo" in cat:
            randomCo.pantalonjambelarge(sexe, id)
        elif "Homme" in cat and "Jeans &amp; Pantalons" in cat and "Pantalons slim" in cat:
            randomCo.autrepantalon(sexe, id)
        elif "Homme" in cat and "Jeans &amp; Pantalons" in cat and "Pantalons classiques" in cat:
            randomCo.autrepantalon(sexe, id)
        elif "Femme" in cat and "Jeans &amp; Pantalons" in cat and "Pantalons cargo" in cat:
            randomCo.autrepantalon(sexe, id)
        elif "Homme" in cat and "Pulls - Sweats - Gilets" in cat and "Sweats à capuche" in cat:
            randomCo.pullacapuche()
        elif "Homme" in cat and "Pulls - Sweats - Gilets" in cat and "Pulls" in cat:
            randomCo.pullacapuche()
        elif "Homme" in cat and "Polaires" in cat and "Pulls polaires" in cat:
            randomCo.pullacapuche()
        elif "Femme" in cat and "Pulls - Sweats - Gilets" in cat and "Sweats à capuche" in cat:
            randomCo.sweatcapuche()
        elif "Femme" in cat and "Pulls - Sweats - Gilets" in cat and "Sweats" in cat:
            randomCo.sweatcapuche()
        elif "Femme" in cat and "Pulls - Sweats - Gilets" in cat and "Pulls" in cat:
            randomCo.sweatcapuche()
        elif "Femme" in cat and "Polaires" in cat and "Pulls polaires" in cat:
            randomCo.sweatcapuche()
        elif "Homme" in cat and "Pulls - Sweats - Gilets" in cat and "Sweats" in cat:
            randomCo.sweat()
        elif "Homme" in cat and "Pulls - Sweats - Gilets" in cat and "Gilets" in cat:
            randomCo.cardigans()
        elif "Polo" in cat and sexe == "Femme":
            randomCo.autrehaut(sexe, id)
        elif "Polo" in cat and sexe == "Homme":
            randomCo.polo(sexe,id)
        elif "Femme" in cat and "T-shirts &amp; Polos" in cat and "T-shirts sans manches" in cat:
            randomCo.debardeur(sexe, id)
        elif "Femme" in cat and "Vestes et Manteaux" in cat and "Vestes" in cat:
            randomCo.hautsveste(sexe, id)
        elif "Homme" in cat and "T-shirts sans manches" in cat:
            randomCo.sansmanches(sexe, id)
        elif "Homme" in cat and "T-shirts manches courtes" in cat:
            randomCo.imprime(sexe, id)
        elif "Homme" in cat and "T-shirts manches longues" in cat:
            randomCo.manchelongue(sexe, id)
        elif "Homme" in cat and "Chemise" in cat:
            randomCo.chemiseunies(sexe, id)
        elif "Homme" in cat and "Vestes en jean" in cat:
            randomCo.vestejean(sexe, id)
        elif "Coupe-vent" in cat or "Vestes légères" in cat:
            randomCo.coupevent(sexe, id)
        elif "Vestes et Manteaux > Blousons" in cat or "Vestes en cuir" in cat:
            randomCo.teddy(sexe, id)
        elif "Doudounes" in cat:
            randomCo.doudounes(sexe, id)
        elif "Vestes polaires" in cat:
            randomCo.vestespolaires(sexe, id)
        elif "Parkas" in cat:
            randomCo.parkas(sexe, id)
        elif "Jeans coupe skinny" in cat:
            randomCo.jeanskinny(sexe, id)
        elif "Jeans coupe droite" in cat:
            randomCo.jeandroit(sexe, id)
        elif "Homme" in cat and "Jeans coupe large" in cat:
            randomCo.jeandroit(sexe, id)
        elif "Femme" in cat and "Jeans coupe large" in cat:
            randomCo.jeanlarge(sexe, id)
        elif "Jeans coupe ajustée" in cat:
            randomCo.jeanautre(sexe, id)
        elif "Femme" in cat and "Chemises" in cat:
            randomCo.chemise(sexe, id)
        else:
            randomCo.autre(sexe, id)
            print("C'EST PAS BOOON")
    elif sexe == "Enfant":
        randomCo.enfant()
    else:
        print("Impossible définir le sexe pour l'article " + id)
    url = driver.current_url
    if "www.vinted.fr/items/new" not in url:
        sys.exit()
    # /////////////////////////////////// Remplissage Taille ///////////////////////////////////
    time.sleep(3)
    try:
        t = taille
    except:
        t = "L"
    try:
        cat = categorie
    except:
        cat = "Jean"
    element = driver.find_element(By.CSS_SELECTOR, "#size_id")
    window_width = driver.execute_script("return window.innerWidth;")
    window_height = driver.execute_script("return window.innerHeight;")
    element_x = element.location['x']
    element_y = element.location['y']
    element_width = element.size['width']
    element_height = element.size['height']
    scroll_x = element_x - (window_width / 2) + (element_width / 2)
    scroll_y = element_y - (window_height / 2) + (element_height / 2)
    driver.execute_script("window.scrollTo({0}, {1});".format(scroll_x, scroll_y))
    randomCo.taille(t,cat,sexe)
    url = driver.current_url
    if "www.vinted.fr/items/new" not in url:
        sys.exit()
    # /////////////////////////////////// Remplissage Marque ///////////////////////////////////
    element = driver.find_element(By.CSS_SELECTOR, "#brand_id")
    window_width = driver.execute_script("return window.innerWidth;")
    window_height = driver.execute_script("return window.innerHeight;")
    element_x = element.location['x']
    element_y = element.location['y']
    element_width = element.size['width']
    element_height = element.size['height']
    scroll_x = element_x - (window_width / 2) + (element_width / 2)
    scroll_y = element_y - (window_height / 2) + (element_height / 2)
    driver.execute_script("window.scrollTo({0}, {1});".format(scroll_x, scroll_y))
    randomCo.rdmbrand()
    try:
        marque = brand
    except:
        marque = "sansnom."
    for L in brand:
        r = random.randint(1,8)
        if r == 1 or r == 3:
            driver.find_element(By.ID,'brand_id').send_keys(L)
            i = random.uniform(0.0001 , 0.3)
            time.sleep(i)
            pg.press("backspace")
            driver.find_element(By.ID,'brand_id').send_keys(L)
            i = random.uniform(0.0001 , 0.3)
            time.sleep(i)
        else:
            driver.find_element(By.ID,'brand_id').send_keys(L)
            i = random.uniform(0.0001 , 0.3)
            time.sleep(i)
    time.sleep(3)
    pg.press("tab")
    pg.press("enter")
    time.sleep(4.1)
    url = driver.current_url
    if "www.vinted.fr/items/new" not in url:
        sys.exit()
    # /////////////////////////////////// Remplissage Titre ///////////////////////////////////
    autoscrolldeb(driver)
    randomCo.rdmtitleco()
    try:
        titre = titres.autotitle(title, qwe, ids, taille, sexe, color)
    except:
        titre = "None!"
    for L in titre :
        r = random.randint(1,6)
        if r == 1 or r == 3:
            driver.find_element(By.ID,'title').send_keys(L)
            i = random.uniform(0.0001 , 0.3)
            time.sleep(i)
            pg.press("backspace")
            driver.find_element(By.ID,'title').send_keys(L)

            i = random.uniform(0.0001 , 0.3)
            time.sleep(i)
        else:
            driver.find_element(By.ID,'title').send_keys(L)
            i = random.uniform(0.0001 , 0.3)
            time.sleep(i)
    time.sleep(4.1)
    url = driver.current_url
    if "www.vinted.fr/items/new" not in url:
        sys.exit()
    # /////////////////////////////////// Remplissage Taille Colis ///////////////////////////////////
    autoscrollend(driver)
    randomCo.rdmcolis()
    url = driver.current_url
    if "www.vinted.fr/items/new" not in url:
        sys.exit()
    # /////////////////////////////////// Remplissage Etat ///////////////////////////////////
    element = driver.find_element(By.CSS_SELECTOR, "#status_id")
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
    try:
        etat = state
    except:
        etat = "7"
    randomCo.etat(etat)
    time.sleep(3)
    url = driver.current_url
    if "www.vinted.fr/items/new" not in url:
        sys.exit()
    # /////////////////////////////////// Remplissage Matiere ///////////////////////////////////
    element = driver.find_element(By.CSS_SELECTOR, "#material")
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
    try:
        listmat = matter
        mots = listmat.split()
        mat = []
        for mot in mots:
            if any(char.isalpha() for char in mot):
                mat.append(mot)
    except:
        mat = ["Polyester"]
    randomCo.matiere(mat)
    # randomMouse.rdmMouse(2050, 796)
    # pg.click()
    # time.sleep(3)
    url = driver.current_url
    if "www.vinted.fr/items/new" not in url:
        sys.exit()
    # /////////////////////////////////// Remplissage Couleur ///////////////////////////////////
    element = driver.find_element(By.CSS_SELECTOR, "#color")
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
    time.sleep(1.3)
    # pg.scroll(6)
    couleur = color
    randomCo.colors(couleur)
    # Color non utilisé, utilisation de la couleur recommandé par Vinted
    url = driver.current_url
    if "www.vinted.fr/items/new" not in url:
        sys.exit()
    # /////////////////////////////////// Remplissage Image ///////////////////////////////////
    autoscrolldeb(driver)
    randomCo.rdmimg()
    time.sleep(1)
    # /////////////////
    chemins_locaux = photo.telecharger_et_enregistrer_photos(photos)
    chemins_absolus = [os.path.abspath(chemin) for chemin in chemins_locaux]
    input_element = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    for chemin in chemins_absolus:
        input_element.send_keys(chemin)
        time.sleep(3)
    photo.supprimer_photos(chemins_locaux)
    # ////////////////
    pg.press("esc")
    time.sleep(1.7)
    url = driver.current_url
    if "www.vinted.fr/items/new" not in url:
        sys.exit()
    # /////////////////////////////////// Remplissage Description ///////////////////////////////////
    autoscrolldeb(driver)
    element = driver.find_element(By.CSS_SELECTOR, "#description")
    window_width = driver.execute_script("return window.innerWidth;")
    window_height = driver.execute_script("return window.innerHeight;")
    element_x = element.location['x']
    element_y = element.location['y']
    element_width = element.size['width']
    element_height = element.size['height']
    scroll_x = element_x - (window_width / 2) + (element_width / 2)
    scroll_y = element_y - (window_height / 2) + (element_height / 2)
    driver.execute_script("window.scrollTo({0}, {1});".format(scroll_x, scroll_y))
    randomCo.rdmdescco()
    try:
        longueur = length
    except:
        longueur = 0
    try:
        largeur = width
    except:
        largeur = 0
    try:
        manche = sleeve
    except:
        manche = "not"
    try:
        tag = tags
    except:
        tag = ""
    clipboard.clipb(categorie, catbrut, sexe, typeitem, qwe, marque, taille, couleur, etat, longueur,
                    largeur, manche, tag)
    pg.hotkey('command', 'v')
    time.sleep(3.7)
    url = driver.current_url
    if "www.vinted.fr/items/new" not in url:
        sys.exit()
# /////////////////////////////////// Mettre en Brouillon ///////////////////////////////////
    randomMouse.rdmMouse(2050, 796)
    pg.click()
    time.sleep(1)
    autoscrollend(driver)
    time.sleep(3.1)
    randomCo.rdmbrouillonco()
    time.sleep(5)
# time.sleep(20)
# driver.quit()
# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=//Users/meduzastore/PycharmProjects/session