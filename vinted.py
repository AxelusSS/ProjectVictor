import os
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
import random
import time
import pyautogui as pg
import photo
import titres
import clipboard
import randomMouse
import randomCo


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Solution Frontend (dev de la solution Backend après avoir fini)
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def vinted(title, qwe, ids, price, gender, typeitem, taille, categorie, brand, state, matter, color, length, width, sleeve, tags, photos):
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
    driver.get('https://vinted.fr')
    time.sleep(4)
    randomCo.rdmcreateco()
    time.sleep(2.4)
    #################################### Remplissage Titre ####################################
    randomCo.rdmtitleco()
    try:
        titre = titres.autotitle(title, qwe, ids)
    except:
        titre = "None"
    for L in titre :
        driver.find_element(By.ID,'title').send_keys(L)
        i = random.uniform(0.0001 , 0.3)
        time.sleep(i)
    time.sleep(4.1)
    #################################### Remplissage Prix ####################################
    randomCo.rdmprixco()
    try:
        prix = price
    except:
        prix = "0"
    for L in prix :
        driver.find_element(By.ID,'price').send_keys(L)
        i = random.uniform(0.0001 , 0.3)
        time.sleep(i)
    time.sleep(4.1)
    #################################### Remplissage Cat ####################################
    time.sleep(1.63)
    try:
        sexe = gender
    except:
        sexe = "Homme"
    try:
        typeart = typeitem
    except:
        typeart = "Jean coupe droite"
    try:
        id = ids
    except:
        id = "123456"
    if sexe == "Homme" or sexe == "Femme":
        randomCo.jean(sexe,id)
    elif sexe == "Enfant":
        randomCo.enfant()
    #################################### Remplissage Taille ####################################
    try:
        t = taille
    except:
        t = "L"
    try:
        cat = categorie
    except:
        cat = "Jean"
    randomCo.taille(t,cat,sexe)
    #################################### Remplissage Marque ####################################
    pg.scroll(500)
    randomCo.rdmbrand()
    try:
        marque = brand
    except:
        marque = "sansnom."
    for L in brand:
        driver.find_element(By.ID, 'brand_id').send_keys(L)
        randomCo.randsleep()
    pg.press("tab")
    pg.click()
    time.sleep(4.1)
    #################################### Remplissage Taille Colis ####################################
    pg.scroll(-500)
    randomCo.rdmcolis()
    #################################### Remplissage Image ####################################
    pg.scroll(500)
    randomCo.rdmimg()
    time.sleep(1)
    #################





    chemins_locaux = photo.telecharger_et_enregistrer_photos(photos)
    chemins_absolus = [os.path.abspath(chemin) for chemin in chemins_locaux]
    input_element = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    for chemin in chemins_absolus:
        input_element.send_keys(chemin)
        time.sleep(3)
    # Supprimer les photos après utilisation
    photo.supprimer_photos(chemins_locaux)




    ################
    pg.press("esc")
    time.sleep(1.7)
    #################################### Remplissage Etat ####################################
    pg.scroll(-500)
    pg.scroll(6)
    etat = state
    #state = Recuperer l'etat de l'article de id
    randomCo.etat(etat)
    #################################### Remplissage Matiere ####################################
    mat = matter
    #mat = Recuperer la matiere de id
    randomCo.matiere(mat)
    randomMouse.rdmMouse(2050, 796)
    pg.click()
    #################################### Remplissage Couleur ####################################
    pg.scroll(-500)
    time.sleep(1.3)
    pg.scroll(6)
    couleur = color
    randomCo.couleurs(couleur)
    # Color non utilisé, utilisation de la couleur recommandé par Vinted
    #################################### Remplissage Description ####################################
    pg.scroll(500)
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
        manche = 0
    try:
        tag = tags
    except:
        tag = ""
    clipboard.clipb(categorie, qwe, marque, taille, couleur, etat, longueur, largeur, manche, tag)
    pg.hotkey('command', 'v')
    time.sleep(3.7)
#################################### Mettre en Brouillon ####################################
    pg.scroll(-500)
    time.sleep(3.1)
    randomCo.rdmbrouillonco()




#time.sleep(20)
#driver.quit()


# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=//Users/meduzastore/PycharmProjects/session