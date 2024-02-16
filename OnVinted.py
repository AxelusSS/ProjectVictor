#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# PROJECT VICTOR 1.0
# --OnVinted.py
# Code crée en très grande partie avec le code scraper.py de Gertje823
# GitHub code : https://github.com/Gertje823/Vinted-Scraper/blob/main/LICENSE
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import mysql
import requests
import json
import os.path
import os
import sqlite3
import argparse
import time
import cloudscraper
import re

# ArgParse
parser = argparse.ArgumentParser(description='Vinted & Depop Scraper/Downloader. Default downloads Vinted')
parser.add_argument('--depop','-d',dest='Depop', action='store_true', help='Download Depop data.')
parser.add_argument('--private_msg','-p',dest='priv_msg', action='store_true', help='Download images from private messages from Vinted')
parser.add_argument('--user_id','-u',dest='user_id', action='store', help='Your own userid', required=False)
parser.add_argument('--session_id','-s',dest='session_id', action='store', help='Session id cookie for Vinted', required=False)
parser.add_argument('--disable-file-download','-n',dest='disable_file_download', action='store_true', help='Disable file download (Currently only working for depop)', required=False)
parser.add_argument('--sold_items','-g',dest='sold_items', action='store_true', help='Also download sold items (depop)', required=False)
parser.add_argument('--start_from','-b',dest='start_from', action='store', help='Begin from a specific item (depop)', required=False)
args = parser.parse_args()


# create downlods folders
if not os.path.exists('downloads'):
    os.makedirs('downloads')

try:
    os.mkdir(f"downloads/Avatars/")
except OSError:
    print("Creation of the directory failed or the folder already exists ")


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Create Database qui recalte toute les infos sur les articles présent sur Vinted
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
sqlite_file = 'data.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
# Create Data table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS Data
             (ID, User_id, Sold, Gender, Category, subcategory, size, State, Brand, Colors, Price, Image, Images, Description, Title, Platform)''')
# Create Users table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS Users
             (Username, User_id, Gender, Given_item_count, Taken_item_count, Followers_count, Following_count, Positive_feedback_count, Negative_feedback_count, Feedback_reputation, Avatar, Created_at, Last_loged_on_ts, City_id, City, Country_title, Verification_email, Verification_facebook, Verification_google, Verification_phone, Platform)''')


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Recupere la session Vinted
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def vinted_session():
    s = cloudscraper.create_scraper()
    s.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en',
        'DNT': '1',
        'Connection': 'keep-alive',
        'TE': 'Trailers',
    }
    req = s.get("https://www.vinted.nl/")
    csrfToken = extract_csrf_token(req.text)
    s.headers['X-CSRF-Token'] = csrfToken
    return s

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# recupere le token
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def extract_csrf_token(text):
    match = re.search(r'"CSRF_TOKEN":"([^"]+)"', text)
    if match:
        return match.group(1)
    else:
        return None

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Recupere tous les articles sur Vinted
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def get_all_items(s, USER_ID, total_pages, items):
    for page in range(int(total_pages)):
        page +=1
        url = f'https://www.vinted.nl/api/v2/users/{USER_ID}/items?page={page}&per_page=200000'
        r = s.get(url).json()
        print(f"Fetching page {page+1}/{r['pagination']['total_pages']}")
        items.extend(r['items'])

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Telecharge toute les donnée sur les articles présent sur vinted
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def download_vinted_data(userids, s):
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
                            Colors = product['color1']
                            Price = product['price']
                            Price = f"{Price['amount']} {Price['currency_code']}"
                            Images = product['photos']
                            title = product['title']
                            #sidebar > div.web_ui__Cell__cell.web_ui__Cell__default.web_ui__Cell__success > div > div
                            #Onsale = product['status'] Trouver un moyen de recolter si oui ou non l'article est déjà vendu !
                            path= "downloads/" + str(User_id) +'/'

                            params = (ID, User_id, Gender, Category, size, State, Brand, Colors, Price, description, title, Platform)
                            c.execute("INSERT INTO Data(ID, User_id, Gender, Category, size, State, Brand, Colors, Price, description, title, Platform)VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", params)
                            conn.commit()
                            with open(filepath, 'wb') as f:
                                f.write(req.content)
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



#Import users from txt file
with open('users.txt', 'r', encoding='utf-8') as list_of_users:
            userids = list_of_users.readlines()


session = vinted_session()
download_vinted_data(userids, session)


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Recupere les QWE de chaque articles et pour comparer ceux présent sur le site ou non
# Créée la table OnVinted qui detmine quel QWE est présent sur vinted
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
c.execute('''CREATE TABLE IF NOT EXISTS OnVinted
             (ID, QWE)''')
conn.commit()

line = c.execute("SELECT COUNT(*) FROM Data").fetchone()[0]
conn.commit()

for i in range(line) :
    id_result = c.execute("SELECT ID FROM Data LIMIT 1").fetchone()
    if id_result:
        id = id_result[0]
        title_result = c.execute("SELECT Title FROM Data WHERE ID = ?", (id,)).fetchone()
        if title_result:
            title = title_result[0]
            qwe = title[-8:]
            params = (id, qwe)
            c.execute(f"INSERT OR IGNORE INTO OnVinted(ID, QWE) VALUES (?, ?)", params)
            conn.commit()
            c.execute(f"DELETE FROM Data WHERE ID = {id}")
            conn.commit()


#
# Creer la fonction OnSale pour determiner quel article est en vente
# Exemple : Cdertain articles Vinted sont présent sur le site mais plus en vente
# Creer la colonne OnSale sur la vrai BDD (Bool False par defaut)
# Mettre le Boolean à True si il est en vente
#

def OnSale():
    db = mysql.connector.connect(
        host="meduza.store",
        user="meduza",
        password="azerty",
        database="meduza"
    )
    d = db.cursor()

    line = c.execute("SELECT COUNT(*) FROM Data").fetchone()[0]
    conn.commit()
    for i in range(line):
        id_result = c.execute("SELECT ID FROM Data LIMIT 1").fetchone()
        if id_result:
            id = id_result[0]
            onsale_result = c.execute("SELECT OnSale FROM Data WHERE ID = ?", (id,)).fetchone()
            if onsale_result:
                onsale = onsale_result[0]
                d.execute("UPDATE BD SET OnSale TRUE WHERE ID = ?", (id,))
                conn.commit()
                c.execute(f"DELETE FROM OnVinted WHERE ID = {id}")
                conn.commit()
    conn.close()



#
# Creer la Colonne OnVinted sur la vrai BDD (Bool False par defaut)
# Mettre le Boolean à True si le QWE est présent
# Puis effacer toute la BdSqlite
#


