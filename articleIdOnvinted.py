from selenium import webdriver
from selenium.webdriver.common.by import By
import sqlite3
# /////////////////////////////////////////////////////////////////////////
def updatebdd():
    sqlite_file = 'msflux.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Flux
                 (ID, QWE)''')
    conn.commit()
    opt = webdriver.ChromeOptions()
    opt.add_argument('--headless')
    driver = webdriver.Chrome(options=opt)
    driver.get("https://www.meduzastore.com/?export=iziflux")
    driver.implicitly_wait(5)
    element = driver.find_element(By.CSS_SELECTOR, "body > pre")
    donnees = element.text
    lignes = donnees.split('\n')
    for i, ligne in enumerate(lignes):
        sections = ligne.split("|")
        disponibilite = sections[17]
        id_produit = sections[0]
        qwe_index = ligne.find("ref_qwe:")
        if qwe_index != -1:
            qwe = ligne[qwe_index:].split("#=")[0].split(":")[1]
            print(i)
            print("ID :", id_produit)
            print("QWE : ", qwe)
            print("--------------------------------------------")
            params = (id_produit, qwe)
            c.execute("INSERT INTO Flux (ID, QWE) VALUES (?, ?)", params)
            conn.commit()
        elif id_produit is not None:
            print(i)
            print("ID :", id_produit)
            print("--------------------------------------------")
            params = (id_produit, "NULL")
            c.execute("INSERT INTO Flux (ID,QWE) VALUES (?,?)", params)
            conn.commit()
        else :
            print("stockage impossible")
    conn.close()