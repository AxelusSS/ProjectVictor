# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# PROJECT VICTOR 1.0
# --OnVinted.py
# Code crée en très grande partie avec le code scraper.py de Gertje823
# GitHub code : https://github.com/Gertje823/Vinted-Scraper/blob/main/LICENSE
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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
sqlite_file = 'vinted.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
# Create Data table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS Data
             (ID, User_id, Sold, Gender, Category, subcategory, size, State, Brand, Colors, Price, Image, Images, Description, Title, Platform, Sale)''')
c.execute('''CREATE TABLE IF NOT EXISTS Depop_Data
             (ID, User_id, Sold, Gender, Category, subcategory, size, State, Brand, Colors, Price, Description, Title, Platform, Address, discountedPriceAmount, dateUpdated)''')
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


def get_all_depop_items(data, baseurl, slugs, args, begin):
    # Start from slug args.start_from (-b)
    if args.start_from:
        for i in data['products']:
            # Prevent duplicates
            if not i['slug'] in slugs:
                if args.start_from == i['slug'] or begin == True:
                    begin = True
                    slugs.append(i['slug'])
    else:
        # start from 0
        for i in data['products']:
            # Prevent duplicates
            if not i['slug'] in slugs:
                slugs.append(i['slug'])
    while True:
        url = baseurl + f"&offset_id={data['meta']['last_offset_id']}"
        print(url)
        try:
            data = requests.get(url).json()
            # print(data)
        except:
            print(requests.get(url).text)
            exit()
            break
        # Start from slug args.start_from (-b)
        if args.start_from:
            for i in data['products']:
                # Prevent duplicates
                if not i['slug'] in slugs:
                    if args.start_from == i['slug'] or begin == True:
                        begin = True
                        slugs.append(i['slug'])
            if data['meta']['end'] == True:
                break
        else:
            # start from 0
            for i in data['products']:
                # Prevent duplicates
                if not i['slug'] in slugs:
                    slugs.append(i['slug'])
            if data['meta']['end'] == True:
                break
    return slugs


def download_depop_data(userids):
    Platform = "Depop"
    for userid in userids:
        userid = userid.strip()
        print(userid)
        slugs = []
        # Get userid from username
        url = f"https://webapi.depop.com/api/v1/shop/{userid}/"
        print(url)
        data = requests.get(url).json()
        id = str(data['id'])
        last_seen = str(data['last_seen'])
        bio = str(data['bio']).encode("UTF-8")
        followers = str(data['followers'])
        following = str(data['following'])
        try:
            initials = str(data['initials']).encode("UTF-8")
        except UnicodeEncodeError:
            initials = None
        items_sold = str(data['items_sold'])
        last_name = str(data['last_name']).encode("UTF-8")
        first_name = str(data['first_name']).encode("UTF-8")
        reviews_rating = str(data['reviews_rating'])
        reviews_total = str(data['reviews_total'])
        username = str(data['username'])
        verified = str(data['verified'])
        website = str(data['website'])
        filepath = None
        if len(data['picture']) > 0:
            photo = data['picture']['300'][:-6] + "U0.jpg"
            print(photo)
            try:
                os.mkdir(f"downloads/Avatars/")
            except OSError:
                print("Creation of the directory failed or the folder already exists ")
            req = requests.get(photo)
            filepath = f'downloads/Avatars/{id}.jpeg'
            if not os.path.isfile(filepath):
                with open(filepath, 'wb') as f:
                    f.write(req.content)
                print(f"Avatar saved to {filepath}")
        else:
            print('File already exists, skipped.')
        params = (username, id, bio, first_name, followers, following, initials, items_sold, last_name, last_seen, reviews_rating, reviews_total, verified,website)
        c.execute(
            "INSERT OR IGNORE INTO Depop_Users(Username, User_id, bio, first_name, followers, following, initials, items_sold, last_name, last_seen, reviews_rating, reviews_total, verified, website) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            params)
        conn.commit()
        baseurl = f"https://webapi.depop.com/api/v1/shop/{id}/products/?limit=200"
        data = requests.get(baseurl).json()
        print("Fetching all produts...")
        begin = False
        slugs = get_all_depop_items(data, baseurl, slugs, args, begin)
        if args.sold_items:
            baseurl = f"https://webapi.depop.com/api/v1/shop/{id}/filteredProducts/sold?limit=200"
            data = requests.get(baseurl).json()
            get_all_depop_items(data, baseurl, slugs, args, begin)
        print("Got all products. Start Downloading...")
        print(len(slugs))
        path = "downloads/" + str(userid) + '/'
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of the directory %s failed or the folder already exists " % path)
        for slug in slugs:
            url = f"https://webapi.depop.com/api/v2/product/{slug}"
            print(slug)
            try:
                product_data = requests.get(url)
                if product_data.status_code == 200:
                    product_data = product_data.json()
                elif product_data.status_code == 429:
                    print(f"Ratelimit waiting 60 seconds...")
                    limit = 60
                    for i in range(limit, 0, -1):
                        print(f"{i}", end="\r", flush=True)
                        time.sleep(1)
                    continue
                elif product_data.status_code == 404:
                    print("Product not found")
                    continue
            except ValueError:
                print("Error decoding JSON data. Skipping...")
                continue
            product_id = product_data['id']
            try:
                Gender = product_data['gender']
            except KeyError:
                Gender = None
            try:
                Gender = product_data['gender']
            except KeyError:
                Gender = None
            try:
                Category = product_data['group']
            except KeyError:
                Category = product_data['categoryId']
            try:
                subcategory = product_data['productType']
            except KeyError:
                subcategory = None
            address = product_data['address']
            dateUpdated = product_data['dateUpdated']
            try:
                State = product_data['condition']['name']
            except KeyError:
                State = None
            Price = product_data['price']['priceAmount'] + product_data['price']['currencyName']
            description = product_data['description']
            Sold = product_data['status']
            title = slug.replace("-"," ")
            Colors = []
            # Get discountedPriceAmount if available
            try:
               discountedPriceAmount = product_data['price']['discountedPriceAmount']
            except KeyError:
                discountedPriceAmount = None
                pass
            # Get colors if available
            try:
                for color in product_data['colour']:
                    Colors.append(color['name'])
                    print(color)
            except KeyError:
                pass
            # Get brand if available
            try:
                Brand = product_data['brand']
                print(Brand)
            except:
                Brand = None
            sizes = []
            # Get size if available
            try:
                for size in product_data['sizes']:
                    sizes.append(size['name'])
            except KeyError:
                pass
            # Download images
            for images in product_data['pictures']:
                for i in images:
                    full_size_url = i['url']
                    img_name = i['id']
                filepath = 'downloads/' + str(userid) + '/' + str(img_name) + '.jpg'
                if not args.disable_file_download:
                    if not os.path.isfile(filepath):
                        c.execute(
                            f"SELECT ID FROM Depop_Data WHERE ID = {product_id}")
                        result = c.fetchone()
                        if result:
                            # Already exists
                            c.execute('''UPDATE Depop_Data SET Image = ? WHERE ID = ?''', (filepath, product_id))
                            conn.commit()
                            req = requests.get(full_size_url)
                            with open(filepath, 'wb') as f:
                                f.write(req.content)
                            print(f"Image saved to {filepath}")
                        else:
                            print(img_name)
                            print(full_size_url)
                            req = requests.get(full_size_url)
                            params = (
                            product_id, id, Sold, Gender, Category, subcategory, ','.join(sizes), State, Brand, ','.join(Colors), Price, description, title, Platform, address, discountedPriceAmount, dateUpdated)
                            c.execute(
                                "INSERT OR IGNORE INTO Depop_Data(ID, User_id, Sold, Gender, Category, subcategory, size, State, Brand, Colors, Price, Description, Title, Platform, Address, discountedPriceAmount, dateUpdated)VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                params)
                            conn.commit()
                            with open(filepath, 'wb') as f:
                                f.write(req.content)
                            print(f"Image saved to {filepath}")
                    else:
                        print('File already exists, skipped.')
                elif args.disable_file_download:
                    c.execute(
                        f"SELECT ID FROM Depop_Data WHERE ID = {product_id}")
                    result = c.fetchone()
                    if result:
                        #Already exists
                        continue
                    else:
                        params = (
                            product_id, Sold, id, Gender, Category, subcategory, ','.join(sizes), State, Brand, ','.join(Colors),
                            Price, description, title, Platform, address, discountedPriceAmount, dateUpdated)
                        c.execute(
                            "INSERT OR IGNORE INTO Depop_Data(ID, Sold, User_id, Gender, Category, subcategory, size, State, Brand, Colors, Price, description, title, Platform, Address, discountedPriceAmount, dateUpdated)VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                            params)
                        conn.commit()
            # Download videos
            if len(product_data['videos']) > 0:
                for x in product_data['videos']:
                    for source in x['sources']:
                        if source['format'] == 'MP4':
                            video_url = source['url']
                            file_name = video_url.split('/')[5]
                            filepath = 'downloads/' + str(userid) + '/' + str(file_name)
                            if not args.disable_file_download:
                                if not os.path.isfile(filepath):
                                    req = requests.get(video_url)
                                    print(video_url)
                                    params = (
                                        product_id, Sold, id, Gender, Category, subcategory, ','.join(sizes), State, Brand,
                                        ','.join(Colors), Price, description, title, Platform, address, discountedPriceAmount, dateUpdated)
                                    c.execute(
                                        "INSERT OR IGNORE INTO Depop_Data(ID, Sold, User_id, Gender, Category, subcategory, size, State, Brand, Colors, Price, description, title, Platform, Address, discountedPriceAmount, dateUpdated)VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                        params)
                                    conn.commit()
                                    with open(filepath, 'wb') as f:
                                        f.write(req.content)
                                    print(f"Video saved to {filepath}")
                                else:
                                    if not args.disable_file_download:
                                        print('File already exists, skipped.')
                            elif args.disable_file_download:
                                c.execute(
                                    f"SELECT ID FROM Depop_Data WHERE ID = {product_id}")
                                result = c.fetchone()
                                if result:
                                    # Already exists
                                    continue
                                else:
                                    params = (
                                        product_id, Sold, id, Gender, Category, subcategory, ','.join(sizes), State,
                                        Brand, ','.join(Colors),
                                        Price, description, title, Platform, address, discountedPriceAmount, dateUpdated)
                                    c.execute(
                                        "INSERT OR IGNORE INTO Depop_Data(ID, Sold, User_id, Gender, Category, subcategory, size, State, Brand, Colors, Price, description, title, Platform, Address, discountedPriceAmount, dateUpdated)VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                        params)
                                    conn.commit()


# Import users from txt file
with open('users.txt', 'r', encoding='utf-8') as list_of_users:
            userids = list_of_users.readlines()
if args.Depop:
    download_depop_data(userids)
elif args.priv_msg:
    if args.user_id and args.session_id:
        user_id = args.user_id
        session_id = args.session_id
    else:
        print("Please use option -u and -s")
        exit()
else:
    session = vinted_session()
    download_vinted_data(userids, session)

"""
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

# Récupération de tous les IDs une seule fois avant la boucle
ids_result = c.execute("SELECT ID FROM Data").fetchall()

for id_row in ids_result:
    id = id_row[0]
    title_result = c.execute("SELECT Title FROM Data WHERE ID = ?", (id,)).fetchone()
    if title_result:
        title = title_result[0]
        qwe = title[-8:]
        params = (id, qwe)
        if not c.execute("SELECT 1 FROM OnVinted WHERE ID = ?", (id,)).fetchone():
            c.execute("INSERT INTO OnVinted(ID, QWE) VALUES (?, ?)", params)

# Commit en dehors de la boucle
conn.commit()


#
# Creer la fonction OnSale pour determiner quel article est en vente
# Exemple : Certain articles Vinted sont présent sur le site mais plus en vente
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


"""