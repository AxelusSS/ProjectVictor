#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# La fonction connectToVinted permet au code de ce connecter directement au compte Vinted de la boutique
# REMPLACER LE LOGIN ET LE PWD DANS LE FICHIER LOGIN.PY
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# V1
def connectToVinted(session_iD, user_id):
    with requests.Session() as s:
        try:
            #.get(login.ulrConnect)
            s.submit('header--login-button')
            s.submit('auth-select-type--login-email')
            login_data = {'username' : login, 'password': pwd}
            s.post(url, data=login_data)
            print("CONNECTION A VINTED REUSSI" + colorama.Fore.GREEN + " Ready")
        except:
            print(colorama.Fore.RED + "IMPOSSIBLE DE CE CONNECTER A VINTED")
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# V2
    with requests.Session() as s:
        colorama.init(autoreset=True)
        try:
            # Accéder à la page de connexion
            response = s.get(url)
            response.raise_for_status()

            # Soumettre le formulaire de connexion
            login_data = {'login': login, 'password': pwd}
            time.sleep(2)
            response = s.post(url, data=login_data)
            time.sleep(2)
            response.raise_for_status()

            # Vérifier si la connexion a réussi
            if "Déconnexion" in response.text:
                print("CONNEXION À VINTED RÉUSSIE" + colorama.Fore.GREEN + " Prêt")
            else:
                print(colorama.Fore.RED + "ÉCHEC DE LA CONNEXION À VINTED")
        except requests.exceptions.RequestException as e:
            print(colorama.Fore.RED + "IMPOSSIBLE DE SE CONNECTER À VINTED:", str(e))





















import argparse
import os
import requests
from bs4 import BeautifulSoup
import cloudscraper
import mysql.connector
from selenium.webdriver.common.by import By

import login
import colorama
import re
from mechanize import Browser
import time
from selenium import webdriver
import undetected_chromedriver as uc

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Args
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

session_id = "ajd3S1RsRG5KeEZCV2dsTXhTL0NwMUI0V21TK01DdDJjalprd0d1c0s4MkhzMlRRTis5d0NiYUtYV2EyelFFQy8rSFVSS0NEOGw1N2dQMnZhMUZoMllsUFp4alZMZlJHLzlKc1U0QXFqWVpPQWpXUkNpZENvMldRM0cwMU1ZVlJLWkVFSE9YV1M2MTQ4TU84V1UxblZ3ZWpvYzJOZ1VudDFhNG1wanp2a1prQ3VaV0ZJMWh5UzQ5a2xCbUp3STBsVWF2cm45TEovY3E3K2Nma3JoMk05cXJXMHA1RE9TWkp4cGVVVmJuN2V4Zm1ta1BOK2N2eHc3bnNQR2ROSG1GdGFTNDJFRkE0ZHFYOXhjQ3U4SkQ0ajNIYWhobWVKYWJNZHIwMVA3L2U0K05EcUVJdlh0eEE3aDVlKy96ZTk0YmRIUFRUMWdJck55cXhUYzlCSHZGRDR1bXJ3ZFRPenJndWlpTkVQR3FkTWJ4eWoxbkllYmk2SzNJVER6NE96b2czcFMyUzhaTVVNOG4rN1pSMzZRWkE5K3poR3JrNFpndHRxZHNSL0tWT0hTSFlQdTd0VVcwei9EMVMxTmlmRmJnMUcxbjdYRThYdFpja1J1UHpSMXNBb21wcFNUSlhlL3crTVB4ZGs4R0RCcER2VFRIc0dDYS80c1lsNzNzWEF3UVFWRms3NEROYytpbHFNRjgvYUdYUmFUbHMwT2tjZ2laaDM0NEdpVDdrWWdNbi9yMWQweDU3bFduOVhUQ1did2xXUUlJazRaNWlzUkwxbE4vbyt1d0tsK21HY0U5UExHaEtnN1FLbnJodFh6VUh3b0ltNDRlaDQ1TDJVRHQ0QkJQZFVNRXVEak1GenA1RlgwazVSYVBEZ1VIYTJ0T0QxQUJSTC9jdEZXQzdiSUp2Ty9ZV09Oc2lSN2xHSk5jYlhwNlR0TzJTSlpnWUowUkJITzJwV2czZ1lwVi9QOUM0TFhjZXQvc1RFNEhMcWRNQm5LVVIrc0U5UlBzTUx2WHIzYW95S09JcVU1TVRWRWE3UmVlNGtreHNKT0xYZ29WZlRXdmdsRDJIcWpTam9WMUNjaUlQRXl2OFpSSTNMZHM0V3FxYUNid1pYc2Y4QUxML1ZwNGtULzBBMlZDZXUwVGxWYUV1SUorcmJlSFV3b1ZLMW45RngyMDYzbFo1RVRzeGJvd0pqUDl0VFl4SmdYQnNlakRYaTNTOC9iTFpJRGM1MCs3WWFMVlJUZnpkc2g5M1JKRENuWUdMUVJrZjdyQ0lkRHhob3FiT21TQzNNOE5HcWhnSWc2V0p2RDQzSlMxSm9JVHgvZXRSR1FOUlplRjVKNVk3aGFQUGFhcUlJcXFCdmFKdGM0enMvVEQ2aFlESVgwVE4wS0pNNkQyQkJwUnV0ZG9jc25DNS9wKzBNY0hXcndORk1odzV4ZFd1cWV3b05FY2YvbCs4QnhyS3pSbzQyR2draTNIeVZOVDRmUE5vQ3UzNitMMHNhUHdnT2lwM2dUNXNOL0Y0aW1YNXo1NU0yV054Y0ppbGw4OTZESkZvd3NhOVpmcmJVRTlnNXVKZ3MwcUhkWmo2V2ZXRUJyeHN2enVIR3NrdC9xaEVPejQzUnFUOW9IWTBTY1pjUDFnVHpWNFp5bVRiSkh5MjRJTGovZUxwMFdoNEJBc3JFcTc3UlB4OEs0RVlVM0dPdFJxT2kzRDZYdlJaWmNmRHRITG5KWjhqR0ttejVRYzE1ZUR1VFpqOVFFMWpUNERtMlhTeUp2VFdqYytaQUZlclhYZjlTR2JLQjRkZy9BT0hFNkVFRUJjdGFaUk5jTWNXMGt6bThoT1NwL2ZvUHdFVDY2S2xpUmdjckxXd2pTNCtxTXFBMm5VMXJoVkw3Uy9uVmQ3WkVlYzM1eHFLem41RjhFdGpmbmloSmNmS20vTlFzUHdKUFVBK25MU3h0SlYyaWNOS3BGakFaNlE1blV1K0JZY1hxRTZHNHFPNEY0azgzbGVEUTVxN1dvUFRiSHhyRXBVUGtrNkdVQ0QvQUVPUktNeHhVczM2T0ZpOFVLVlBEbjViSlFhaTJLSER3WUtpcHlFL0cyb2ozSkkrVTVpbjdqaVdBY21uQWNKdmRSMHltMmFkaGNnWW5QYmpZdE5jeWFBT1NuVEN0aGNQZ1VQQzRYTHNNRFVNMHljVUlTcXJnenlhczFkSllyS24rQnphV3JIaVBXMFNiU0ZYQXJUVWFjNzR0TDVMTGIzOTU5ZWpMYlVaSHpvS1BSSmE5UTVrc2haWUVyVzBRaFAydHoxekdZRmpOb1RHa2lDOHNGYkVTVmFzRXpOOFVTTWR0QTFTc0NsUS9HeEl5YU1lK2dLay9TWVhmY29NUXE1M3JDempWN040TDVSRkxERFpXSnB3RU8yVndBc2lIWC80Y3c9PS0tWHRDRURzdldjVEVsWFY5dXhLWERLdz09--31da45c1432a8226aced9b9f9a4e07033fdd79c5"
user_id = "16451173"
title = "Mandatory"
price = "60"
color1 = "rouge"
brand = "Mandatory"
status = "neuf"
size = "L"
cataid = "532"
description = "Mandatory"
gender = "Homme"

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Connection à la base de donnée de l'entreprise
# Ne pas oublier de verifier la fermeture de la connection à la fin du programmme
# REMPLACER LES VALEURS HOST/USER/PASSWORD/DATABASE PAR LES BONNES VALEURS
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
''''
db = mysql.connector.connect(
    host="meduza.store",
    user="meduza",
    password="azerty",
    database="meduza"
)
c = db.cursor()
    #db.autocommit = True
'''
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# La fonction creer_Brouillon va creer un brouille de chaque article qui ne sont pas encore sur la boutique Vinted
# En comparent les ID qui sont présent sur la BDD centrale avec celle de la BDD Vinted,
# il y ira récuperer les ID des articles qui ne ont pas encore en ligne
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def creer_Brouillon(title, description,):
        #article['description'] = description
        #article['catalog_id'] = cataid
        #article['size'] = size
        #article['status'] = status
        #article['brand'] = brand
        #article['color1'] = color1
        #article['price'] = price
        #article['title'] = title
        #article['gender'] = gender
        #setOnBdd(article)
        '''
        data = s.get("https://www.vinted.fr/items/new")
        if data.status_code == 403 or data.status_code == 404:
            # Access denied
            print( + colorama.Fore.RED + "Error: Access Denied\nCan't get content from 'https://www.vinted.fr/items/new'" + colorama.Fore.WHITE + "")
            exit(1)
        else:
            print("ACCES AU BROUILLON REUSSIE" + colorama.Fore.GREEN + " Prêt" + colorama.Fore.WHITE + "")
            data = {
                'title': title,
                'description': description,
            }
            s.post(f"https://www.vinted.nl/api/v2/users/{user_id}/items/new", data=data)
            #data = data.json()
        '''
            #
            # SIMULATION D'OUVERTURE DE TAB GOOGLE ET D'EXECUTION HUMAINE
            #
        options = webdriver.ChromeOptions()
        #options.add_argument('proxy-server=106.122.8.54:3128')
        options.add_argument('--user-data-dir=')
        web = uc.Chrome(
            #options=options
        )

        web.get('https://www.vinted.fr/member')
        #web.add_cookie(cookie)
        time.sleep(30)
        web.find_element(By.CSS_SELECTOR,
                         '#__next > div > div > div.l-header.js-header > header > div > div > div.u-flexbox.u-margin-left-auto.u-align-items-center.u-position-relative.u-z-index-notification > div > a.web_ui__Button__button.web_ui__Button__outlined.web_ui__Button__small.web_ui__Button__primary.web_ui__Button__truncated').click()
        time.sleep(30)
        web.find_element(By.CSS_SELECTOR,
                         'body > div:nth-child(58) > div > div > div > div.u-overflow-auto > div.u-ui-padding-horizontal-large.u-ui-padding-bottom-x-large > a').click()
        time.sleep(30)
        web.find_element(By.ID, 'identifierId').send_keys("")
        time.sleep(30)
        web.find_element(By.CSS_SELECTOR, '#identifierNext > div > button > span').click()
        time.sleep(30)
        web.find_element(By.CSS_SELECTOR, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input').send_keys(
            "MS2022renouveau@")
        time.sleep(30)
        web.find_element(By.CSS_SELECTOR, '#passwordNext > div > button > span').click()





        name=web.find_element('xpath','/html/body/div[1]/div/div/main/div/section/div/div[2]/section/div/div/div[5]/label[1]/div[2]/input')
        name.send_keys(title)
        time.sleep(30)
        name=web.find_element('xpath','/html/body/div[1]/div/div/main/div/section/div/div[2]/section/div/div/div[5]/label[2]/div[2]/textarea')
        name.send_keys(description)
        time.sleep(30)
        submit=web.find_element('xpath','/html/body/div[1]/div/div/main/div/section/div/div[2]/section/div/div/div[13]/div/button[1]')
        submit.click()

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# La fonction getArcticles va s'accuper de récuperer les articles présent dans la table ARTICLES
# qui ne sont pas présent dans la table VINTED
# REMPLACER ID PAR LE CODE UNIQUE ET ARTICLES/VINTED PAR LES BON NOM DE TABLES
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def getArticles():
    nb = c.execute("SELECT COUNT(*) FROM articles")
    db.commit()
    list = []
    i = 1
    while i != nb :
        try:
            list.extend(c.execute(
              "SELECT id FROM articles WHERE onvinted = FALSE")
            )
            db.commit()
            i=i+1
        except:
            print(colorama.Fore.RED + "IMPOSSIBLE DE RECUPERER LES ID DES ARTICLES" + colorama.Fore.WHITE + "")
    return list
    print("STOCKAGE DES ID REUSSI" + colorama.Fore.GREEN + " Ready" + colorama.Fore.WHITE + "")

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# La fonction connectToVinted permet au code de ce connecter directement au compte Vinted de la boutique
# REMPLACER LE LOGIN ET LE PWD DANS LE FICHIER LOGIN.PY
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def connectToVinted(session_iD, user_id):
    s = cloudscraper.create_scraper()
    s.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'fr',
        'DNT': '1',
        'Connection': 'keep-alive',
        'TE': 'Trailers',
        'Cookie': f"_vinted_fr_session={session_id};"
    }
    data = s.get(f"https://www.vinted.nl/api/v2/users/{user_id}/msg_threads")
    if data.status_code == 403:
        # Access denied
        print( + colorama.Fore.RED + f"Error: Access Denied\nCan't get content from 'https://www.vinted.fl/api/v2/users/{user_id}/msg_threads'" + colorama.Fore.WHITE + "")
        exit(1)
    else:
        print("CONNEXION À VINTED RÉUSSIE" + colorama.Fore.GREEN + " Prêt" + colorama.Fore.WHITE + "")
    data = data.json()
    return s

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# La fonction setOnBdd s'occupe de rajouter automatiquement la nouvel article à la table VINTED
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def setOnBdd(listArticles):
    ajout = 0
    for articles in listArticles :
        try:
            c.execute(
                f"UPDATE articles SET onvinted = TRUE WHERE id = {article}",
                )
            db.commit()
            ajout = ajout + 1
        except:
            print(colorama.Fore.RED + f"IMPOSSIBLE D'AJOUTER L'ARTICLE {article}")
    print(colorama.Fore.CYAN + f"{ajout} nouveau(x) article(s) ajouté sur Vinted" + colorama.Fore.WHITE + "")

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# La fonction extract_csrf_token permet de récuperer le token afin de ce connecter
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def extract_csrf_token(text):
    match = re.search(r'"CSRF_TOKEN":"([^"]+)"', text)
    if match:
        return match.group(1)
    else:
        print(colorama.Fore.RED + "TOKEN INTROUVABLE")
        return None

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# La fonction get_all_items permet de récuperer tous les articles présent sur Vinted
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
def get_all_items(s, USER_ID, total_pages, items):
    for page in range(int(total_pages)):
        page +=1
        url = f'https://www.vinted.nl/api/v2/users/{USER_ID}/items?page={page}&per_page=200000'
        r = s.get(url).json()
        print(f"Fetching page {page+1}/{r['pagination']['total_pages']}")
        items.extend(r['items'])

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# La fonction get_ugs permet de récuperer tous les ugs des articles présent sur Vinted
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def get_ugs(userids, s):
    Platform = "Vinted"
    for USER_ID in userids:
        USER_ID = USER_ID.strip()
        # Get user profile data
        url = f"https://www.vinted.nl/api/v2/users/{USER_ID}"
        r = s.get(url)
        if r.status_code == 200:
            jsonresponse = r.json()
            data = jsonresponse['user']
            #get data
            username = data['login']
            gender = data['gender']
            given_item_count = data['given_item_count']
            taken_item_count = data['taken_item_count']
            followers_count = data['followers_count']
            following_count = data['following_count']
            positive_feedback_count = data['positive_feedback_count']
            negative_feedback_count = data['negative_feedback_count']
            feedback_reputation = data['feedback_reputation']
            try:
                created_at = data['created_at']
            except KeyError:
                created_at = ""
            last_loged_on_ts = data['last_loged_on_ts']
            city_id = data['city_id']
            city = data['city']
            country_title = data['country_title']
            verification_email = data['verification']['email']['valid']
            verification_facebook = data['verification']['facebook']['valid']
            verification_google = data['verification']['google']['valid']
            verification_phone = data['verification']['phone']['valid']
            if data['photo']:
                photo = data['photo']['full_size_url']
                photo_id = data['photo']['id']
                try:
                    os.mkdir(f"downloads/Avatars/")
                except OSError:
                    print ("Creation of the directory failed or the folder already exists ")
                req = requests.get(photo)
                filepath = f'downloads/Avatars/{photo_id}.jpeg'
                if not os.path.isfile(filepath):
                    print(photo_id)
                    with open(filepath, 'wb') as f:
                        f.write(req.content)
                    print(f"Avatar saved to {filepath}")
                else:
                    print('File already exists, skipped.')
                params = (
                    username, USER_ID, gender, given_item_count, taken_item_count, followers_count, following_count,
                    positive_feedback_count, negative_feedback_count, feedback_reputation, filepath, created_at,
                    last_loged_on_ts, city_id, city, country_title, verification_email, verification_google,
                    verification_facebook, verification_phone)
                c.execute(
                    "INSERT INTO Users(Username, User_id, Gender, Given_item_count, Taken_item_count, Followers_count, Following_count, Positive_feedback_count, Negative_feedback_count, Feedback_reputation, Avatar, Created_at, Last_loged_on_ts, City_id, City, Country_title, Verification_email, Verification_facebook, Verification_google, Verification_phone)VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    params)
                conn.commit()

            else:
                # If no avatar put empty string in DB
                Avatar = ""
                params = (
                    username, USER_ID, gender, given_item_count, taken_item_count, followers_count, following_count,
                    positive_feedback_count, negative_feedback_count, feedback_reputation, Avatar, created_at,
                    last_loged_on_ts, city_id, city, country_title, verification_email, verification_google, verification_facebook,
                    verification_phone)
                c.execute(
                    "INSERT INTO Users(Username, User_id, Gender, Given_item_count, Taken_item_count, Followers_count, Following_count, Positive_feedback_count, Negative_feedback_count, Feedback_reputation, Avatar, Created_at, Last_loged_on_ts, City_id, City, Country_title, Verification_email, Verification_facebook, Verification_google, Verification_phone)VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    params)
                conn.commit()

            USER_ID = USER_ID.strip('\n')
            url = f'https://www.vinted.nl/api/v2/users/{USER_ID}/items?page=1&per_page=200000'
            print('ID=' + str(USER_ID))

            r = s.get(url)
            items = []
            print(f"Fetching page 1/{r.json()['pagination']['total_pages']}")
            items.extend(r.json()['items'])
            # products = jsonresponse['items']
            if r.json()['pagination']['total_pages'] > 1:
                print(f"User has more than {len(items)} items. fetching next page....")
                get_all_items(s, USER_ID, r.json()['pagination']['total_pages'], items)
            products = items
            print(f"Total items: {len(products)}")
            if r.status_code == 200:
                # print(jsonresponse)

                if products:
                    # Download all products
                    path= "downloads/" + str(USER_ID) +'/'
                    try:
                        os.mkdir(path)
                    except OSError:
                        print ("Creation of the directory %s failed or the folder already exists " % path)
                    else:
                        print ("Successfully created the directory %s " % path)
                    for product in products:
                            img = product['photos']
                            ID = product['id']
                            User_id = product['user_id']
                            description = product['description']
                            Gender = product['user']['gender']
                            Category = product['catalog_id']
                            size = product['size']
                            State = product['status']
                            Brand = product['brand']
                            print(''+ product['brand'])
                            Colors = product['color1']
                            Price = product['price']
                            Price = f"{Price['amount']} {Price['currency_code']}"
                            Images = product['photos']
                            title = product['title']
                            path= "downloads/" + str(User_id) +'/'

                            #print(img)
                            if Images:
                                for images in img:
                                    full_size_url = images['full_size_url']
                                    img_name = images['high_resolution']['id']
                                    #print(img_name)
                                    filepath = 'downloads/'+ str(USER_ID) +'/' + img_name +'.jpeg'
                                    if not os.path.isfile(filepath):
                                        #print(full_size_url)
                                        req = requests.get(full_size_url)
                                        params = (ID, User_id, Gender, Category, size, State, Brand, Colors, Price, filepath, description, title, Platform)
                                        c.execute("INSERT INTO Data(ID, User_id, Gender, Category, size, State, Brand, Colors, Price, Images, description, title, Platform)VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", params)
                                        conn.commit()
                                        with open(filepath, 'wb') as f:
                                            f.write(req.content)
                                        print(f"Image saved to {filepath}")
                                    else:
                                        print('File already exists, skipped.')
                if not products:
                    print('User has no products')
            elif r.status_code == 429:
                print(f"Ratelimit waiting {r.headers['Retry-After']} seconds...")
                limit = round(int(r.headers['Retry-After']) / 2)
                for i in range(limit, 0, -1):
                    print(f"{i}", end="\r", flush=True)
                    time.sleep(1)
                continue

        elif r.status_code == 429:
            print(f"Ratelimit waiting {r.headers['Retry-After']} seconds...")
            limit = round(int(r.headers['Retry-After']) / 2)
            for i in range(limit, 0, -1):
                print(f"{i}", end="\r", flush=True)
                time.sleep(1)
            continue
        else:
            print(f"User {USER_ID} does not exists")
    conn.close()
'''
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Yaourt
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#url = 'https://www.vinted.fr/items/4068440367-veja-recife-logo-chromefree-t37?homepage_session_id=9fcbf550-ddb9-4f44-9b4a-6ed95b04ef35'
# url = 'https://www.youtube.com/watch?v=wP4eWD6zmao'
#response = requests.get(url)
'''
listArticles = []
if response.ok :
    soup = BeautifulSoup(response.text, "html.parser")
    #print(soup)
    #title = soup.find('title')
    s = cloudscraper.create_scraper()
    r = s.get(url).json()
    items = (r['items'])
    Brand = items['brand']


    print(Brand)
    #print(len(tds))
'''


# Stockage des ID
#listArticles.extend(getArticles())
# Connection à Vinted

# Boucle pour inserer les valeurs et mettre en brouillon
'''
for article in listArticles:
    title = c.execute(f'SELECT title FROM ARTICLE WHERE ID = {article}') #Titre
    price = c.execute(f'SELECT price FROM ARTICLE WHERE ID = {article}') #Prix
    color1 = c.execute(f'SELECT color1 FROM ARTICLE WHERE ID = {article}') #Couleur 1
    # CREER POSSIBILITE DE DEUXIEMME COULEUR
    brand = c.execute(f'SELECT brand FROM ARTICLE WHERE ID = {article}') #Marque
    status = c.execute(f'SELECT status FROM ARTICLE WHERE ID = {article}') #Etat Bon/Mauvais
    size = c.execute('SELECT size FROM ARTICLE WHERE ID = {article}') #Taille
    cataid = c.execute(f'SELECT cataid FROM ARTICLE WHERE ID = {article}') #Id du catalogue / Categorie
    description = c.execute(f'SELECT description FROM ARTICLE WHERE id = {article}') #Description
    gender = c.execute(f'SELECT gender FROM articles WHERE id = {article}') #Genre Homme Femme Enfant
    db.commit()
'''
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Test avec valeurs en dur
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#s = connectToVinted(session_id, user_id)
time.sleep(5)
creer_Brouillon(title, description)

#db.close()
