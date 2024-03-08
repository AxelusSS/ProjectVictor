# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=//Users/meduzastore/PycharmProjects/session

import datetime
from datetime import datetime
import re
import sqlite3
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import vinted
#import graphique
import pygame
# /////////////////////////////////////////////////////////////////////////


def izifluxscrap():
    timer = 30
    driver = webdriver.Chrome()
    driver.get("https://www.meduzastore.com/?export=iziflux")
    driver.implicitly_wait(5)
    element = driver.find_element(By.CSS_SELECTOR, "body > pre")
    donnees = element.text
    lignes = donnees.split('\n')
# ///////////////////////////////////////////////////////////////////////////////////|
# Recupere chaque ligne de iziflux et regarde si l'article est en "Stock" ou "Vendu" |
# ///////////////////////////////////////////////////////////////////////////////////|
    conn = sqlite3.connect('msflux.sqlite')
    cursor = conn.cursor()
    for i, ligne in enumerate(lignes):
        sections = ligne.split("|")
        disponibilite = sections[17]
        id_produit = sections[0]
        try:
            qwe_index = ligne.find("ref_qwe:")
            qwe = ligne[qwe_index:].split("#=")[0].split(":")[1]
        except:
            qwe = "BOXZ"
        cursor.execute("SELECT * FROM Flux WHERE ID = ?", (id_produit,))
        conn.commit()
        result = cursor.fetchone()
        print(i)
        print("ID :", id_produit)
        if disponibilite == "S" and "BOXZ" not in qwe and result is None:
            print("Vinted")
            # /////////////////// ID /////////////////////
            id_produit = sections[0]
            print("ID du produit :", id_produit)
            # /////////////////// Color /////////////////////
            couleur_index = ligne.find("couleurDepuisTerm:")
            couleur = ligne[couleur_index:].split("#")[0].split(":")[1]
            print("Color : ", couleur)
            # /////////////////// Title /////////////////////
            nom_produit = sections[2]
            print("Title : ", nom_produit)
            # /////////////////// Price /////////////////////
            prix = sections[18]
            print("Prix : ", prix)
            # /////////////////// Brand /////////////////////
            marque_index = ligne.find("marqueDepuisTerm:")
            marque = ligne[marque_index:].split("#")[0].split(":")[1]
            print("Marque : ", marque)
            # /////////////////// State /////////////////////
            etat_index = ligne.find("Etat du produit:")
            etat = ligne[etat_index:].split("#")[0].split(":")[1]
            print("Etat : ", etat)
            # /////////////////// QWE /////////////////////
            qwe_index = ligne.find("ref_qwe:")
            qwe = ligne[qwe_index:].split("#=")[0].split(":")[1]
            print("QWE : ", qwe)
            # /////////////////// Sexe,Categorie,Type /////////////////////
            categorie = sections[14]
            c = categorie
            lc = c.split(" > ")
            lcs = []
            for c in lc:
                if any(char.isalpha() for char in c):
                    lcs.append(c)
            lcs.sort(key=lambda x: ("Homme" not in x, "Femme" not in x, "Enfant" not in x, x))
            sexe = lcs[0]
            try:
                subcat = lcs[1]
                typeitem = lcs[2]
            except IndexError:
                subcat = ""
                typeitem = lcs[1]
            print("Sexe : ", sexe)
            print("Sous-categorie : ", subcat)
            print("TYpe Article : ", typeitem)
            # /////////////////// taille /////////////////////
            try:
                taille_index = ligne.find("tailles:")
                taille = ligne[taille_index:].split("#")[0].split(":")[1]
                print("Taille : ", taille)
            except:
                try:
                    taille_index = ligne.find("pa_tailles-pantalons-w:")
                    taille = ligne[taille_index:].split("#")[0].split(":")[1]
                    print("Taille : W", taille)
                except:
                    print("Pas de Taille")
                    taille = "L"
            # /////////////////// Length,width,sleeve /////////////////////
            if typeitem == "Jean" or typeitem == "Pantalon" or typeitem == "Short":
                largeur_regex = re.compile(r'Largeur de la taille\s*:\s*(\d+)')
                longueur_interieure_regex = re.compile(r'Longueur jambes intérieure\s*:\s*(\d+)')
                longueur_exterieure_regex = re.compile(r'Longueur jambes extérieure\s*:\s*(\d+)')
                largeur_match = largeur_regex.search(ligne)
                longueur_interieure_match = longueur_interieure_regex.search(ligne)
                longueur_exterieure_match = longueur_exterieure_regex.search(ligne)
                if largeur_match:
                    largeur_taille = largeur_match.group(1)
                    print("Largeur de la taille :", largeur_taille, "cm")
                    width = largeur_taille
                else:
                    print("Largeur de la taille non trouvée")
                    width = "None"
                if longueur_interieure_match:
                    longueur_interieure = longueur_interieure_match.group(1)
                    print("Longueur jambes intérieure :", longueur_interieure, "cm")
                    lenght = longueur_interieure
                else:
                    print("Longueur jambes intérieure non trouvée")
                    lenght = "None"
                if longueur_exterieure_match:
                    longueur_exterieure = longueur_exterieure_match.group(1)
                    print("Longueur jambes extérieure :", longueur_exterieure, "cm")
                    sleeve = longueur_exterieure
                else:
                    print("Longueur jambes extérieure non trouvée")
                    sleeve = "None"
            else:
                longueur_regex = re.compile(r"Longueur \(du bas jusqu'au col\) : (\d+)cm")
                largeur_regex = re.compile(r"Largeur \(aisselle à aisselle\) : (\d+)cm")
                longueur_manche_regex = re.compile(r"Longueur des manches : (\d+)cm")
                longueur_match = longueur_regex.search(ligne)
                largeur_match = largeur_regex.search(ligne)
                longueur_manche_match = longueur_manche_regex.search(ligne)
                if longueur_match:
                    longueur = longueur_match.group(1)
                    print("Longueur (du bas jusqu'au col) :", longueur, "cm")
                    lenght = longueur
                else:
                    print("Longueur (du bas jusqu'au col) non trouvée")
                    lenght = "None"
                if largeur_match:
                    largeur = largeur_match.group(1)
                    print("Largeur (aisselle à aisselle) :", largeur, "cm")
                    width = largeur
                else:
                    print("Largeur (aisselle à aisselle) non trouvée")
                    width = "None"
                if longueur_manche_match:
                    longueur_manche = longueur_manche_match.group(1)
                    print("Longueur des manches :", longueur_manche, "cm")
                    sleeve = longueur_manche
                else:
                    print("Longueur des manches non trouvée")
                    sleeve = "None"
            # /////////////////// Matter /////////////////////
            try:
                matiere_index = ligne.find("Matter:")
                matiere = ligne[matiere_index:].split("#")[0].split(":")[1]
                print("Matière : ", matiere)
            except:
                print("Impossible de trouver la matiere !")
                matiere = ["Polyester"]
            # /////////////////// Photo /////////////////////
            photo_urls_list = []
            photo_urls = re.findall(r'https:[^|]+?\.jpg', ligne)
            for y in photo_urls:
                print(y)
            photo_urls_list.extend(photo_urls)
            # /////////////////// Tags /////////////////////
            tags = "#Reconditionné"
            # Quand la colonne Tags sera creer, récuperer le champ tags
            # /////////////////// Lancement création brouillon /////////////////////

            #if graphique.App.Vfin:
            if 1 == 1:
                #heure_limite = datetime.time(21, 0, 0)
                #heure_actuelle = datetime.datetime.now().time()
                #print(heure_actuelle)
                #if '7' in etat or '8' in etat or '9' in etat or '10/' in etat and heure_actuelle < heure_limite:
                if '7' in etat or '8' in etat or '9' in etat or '10/' in etat :
                    vinted.vinted(nom_produit, qwe, id_produit, prix, sexe, typeitem, taille, subcat,
                                  categorie, marque, etat, matiere, couleur, lenght, width, sleeve,
                                  tags, photo_urls_list)
                elif heure_actuelle >= heure_limite:
                    print("Il est 21h passé, arrêt du programme.")
                    sys.exit()
                maintenant = datetime.now()
                params = (id_produit, qwe, maintenant)
                cursor.execute("INSERT INTO Flux (ID, QWE, DATE) VALUES (?, ?, ?)", params)
                conn.commit()
                time.sleep(timer)
            else:
                heure_actuelle = datetime.datetime.now().time()
                print(heure_actuelle)
                if '7' in etat or '8' in etat or '9' in etat or '10/' in etat:
                    vinted.vinted(nom_produit, qwe, id_produit, prix, sexe, typeitem, taille, subcat,
                                  categorie, marque, etat, matiere, couleur, lenght, width, sleeve,
                                  tags, photo_urls_list)
                maintenant = datetime.now()
                params = (id_produit, qwe, maintenant)
                cursor.execute("INSERT INTO Flux (ID, QWE, DATE) VALUES (?, ?, ?)", params)
                conn.commit()
                time.sleep(timer)
        elif disponibilite == "V":
            print("Hors Stock ------- X")
        else:
            print("Produit vendu/déjà sur vinted")
        print("----------------------------")
    #if graphique.App.Vson:
    pygame.init()
    pygame.mixer.music.load("/Users/meduzastore/PycharmProjects/ProjectVictor/alert.mp3")
    pygame.mixer.music.play()
    pygame.time.delay(4000)
    pygame.mixer.music.stop()
    pygame.quit()
    driver.quit()
    conn.close()

izifluxscrap()