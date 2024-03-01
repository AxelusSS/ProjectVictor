import re
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.meduzastore.com/?export=iziflux")
driver.implicitly_wait(10)
element = driver.find_element(By.CSS_SELECTOR, "body > pre")
donnees = element.text
lignes = donnees.split('\n')

#####################################################################################|
# Recupere chaque ligne de iziflux et regarde si l'article est en "Stock" ou "Vendu" |
#####################################################################################|
for i, ligne in enumerate(lignes):
    # Divise la chaîne en sections en utilisant le caractère "|"
    sections = ligne.split("|")
    # Récupère le champ de disponibilité qui se trouve à l'index 28
    disponibilite = sections[17]
    id_produit = sections[0]
    #vars()["ligne" + str(i+1)] = ligne
    print(i)
    if disponibilite == "S" and id_produit != "60495" and id_produit != "60467" and id_produit != "60303" and id_produit != "60297" and id_produit != "69659":
        print("Vinted")
##################### ID #####################
        id_produit = sections[0]
        print("ID du produit :", id_produit)
##################### Color #####################
        couleur_index =  ligne.find("couleurDepuisTerm:")
        couleur =  ligne[couleur_index:].split("#")[0].split(":")[1]
        print("Color : ", couleur)
##################### Title #####################
        nom_produit = sections[2]
        print("Title : ", nom_produit)
##################### Price #####################
        prix = sections[18]
        print("Prix : ", prix)
##################### Brand #####################
        marque_index =  ligne.find("marqueDepuisTerm:")
        marque =  ligne[marque_index:].split("#")[0].split(":")[1]
        print("Marque : ", marque)
##################### State #####################
        etat_index = ligne.find("Etat du produit:")
        etat = ligne[etat_index:].split("#")[0].split(":")[1]
        print("Etat : ", etat)
##################### QWE #####################
        qwe = ligne[-13:-6]
        print("QWE : ", qwe)
##################### Categorie #####################
        categorie = sections[14]
        segments = categorie.split("> ")
        subcat = sexe = segments[1]
##################### Gender #####################
        sexe = segments[0]
##################### Type Article #####################
        typeitem = segments[2]
        if "Enfant" in subcat or "Homme" in subcat or "Femme" in subcat:
            change = sexe
            sexe = subcat
            subcat = typeitem
            typeitem = change
            print("Sexe : ", sexe)
            print("Categorie : ", subcat)
            print("Type article : ", typeitem)
        else:
            print("Sexe : ", sexe)
            print("Categorie : ", subcat)
            print("Type article : ", typeitem)

##################### taille #####################
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
##################### Length,width,sleeve #####################
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
##################### Matter #####################
        matiere_index = ligne.find("Matter:")
        matiere = ligne[matiere_index:].split("#")[0].split(":")[1]
        print("Matière : ", matiere)
##################### Photo #####################
        photo_urls_list = []
        photo_urls = re.findall(r'https:[^|]+?\.jpg', ligne)
        for i in photo_urls:
            print(i)
        photo_urls_list.extend(photo_urls)
##################### Lancement création brouillon #####################
        #if etat <= 6:
            #vinted.vinted(nom_produit, qwe, id_produit, prix, sexe, typeitem, taille, categorie, marque, etat, matiere,
                        #couleur, lenght, width, sleeve, tags)



    elif disponibilite == "V":
        print("Hors Stock ------- X")
    print("----------------------------")



driver.quit()
