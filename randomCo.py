import random
import pyautogui as pg
from selenium.webdriver.common.by import By
import randomMouse as rm
import time
import vinted


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Cette class vise a rendre aléatoire les coordonées du clic sur un champ
# Avec un calcul de l'air de la zone au préalable
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

'''
pg.moveTo(x=1281, y=703, duration=2)
time.sleep(6)
print(pg.position())
pg.moveTo(x=1733, y=813, duration=2)
'''

def randsleep():
    i = random.uniform(0.0001 , 0.3)
    time.sleep(i)

def rdmcreateco():
    x = random.randint(1674,1783)
    y = random.randint(125,139)
    rm.rdmMouse(x,y)
    pg.click()

def rdmtitleco():
    x = random.randint(1281,1733)
    y = random.randint(628,650)
    rm.rdmMouse(x,y)
    pg.click()

def rdmdescco():
    x = random.randint(1281,1733)
    y = random.randint(703,813)
    rm.rdmMouse(x,y)
    pg.click()

def rdmprixco():
    x = random.randint(1281,1733)
    y = random.randint(989,1014)
    rm.rdmMouse(x,y)
    pg.click()

def rdmbrouillonco():
    x = random.randint(1455,1660)
    y = random.randint(1121,1159)
    rm.rdmMouse(x,y)
    pg.click()

def rdmcat():
    x = random.randint(1281,1717)
    y = random.randint(891,910)
    rm.rdmMouse(x,y)
    pg.click()

def homme():
    pg.press("tab")
    randsleep()
    pg.press("tab")
    randsleep()
    pg.press("enter")

def femme():
    pg.press("tab")
    randsleep()
    pg.press("enter")

def vetement():
    pg.press("tab")
    pg.press("enter")

def rdmbrand():
    x = random.randint(1281,1732)
    y = random.randint(964,988)
    rm.rdmMouse(x,y)
    pg.click()

def rdmbrandselect():
    pg.press('tab')
    pg.press('enter')

def rdmcolis():
    x = random.randint(806, 1758)
    y = random.randint(485, 571)
    rm.rdmMouse(x, y)
    pg.click()

def rdmimg():
    x = random.randint(1192, 1381)
    y = random.randint(440, 479)
    rm.rdmMouse(x, y)
    pg.click()

#################################### Enfant ####################################

def enfant():
    rdmcat()
    for i in range(3):
        pg.press("tab")
        randsleep()
    pg.press("enter")
    for i in range(3):
        pg.press("tab")
        randsleep()
        pg.press("enter")

#################################### Jean ####################################

def jean(sexe, id):
    typejean = "Jean Droit"
    #typejean = Recuperer typejean de id
    rdmcat()
    randsleep()
    if sexe == "Homme":
        homme()
        vetement()
        pg.press("tab")
        randsleep()
        pg.press("enter")
        if typejean == "Jean troué":
            pg.press("tab")
            randsleep()
            pg.press("enter")
        elif typejean == "Jean coupe skinny":
            for i in range(2):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif typejean == "Jean coupe slim":
            for i in range(3):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif typejean == "Jeans coupe droite" or typejean == "Jeans coupe ajustée":
            for i in range(4):
                pg.press("tab")
                randsleep()
            pg.press("enter")
    elif sexe == "Femme":
        femme()
        vetement()
        for i in range(7):
            pg.press("tab")
            randsleep()
        pg.press("enter")
        if typejean == "Jean boyfriend":
            pg.press("tab")
            randsleep()
            pg.press("enter")


    else:
        print("Impossible définir le sexe pour l'article " + id)

#################################### Manteaux et Vestes ####################################

def manteauxetvestes(sexe, id):
    typemv = "Duffle-coats"
    #typemv = Recuperer typemv de id
    rdmcat()
    randsleep()
    if sexe == "Homme":
        homme()
        vetement()
        for i in range(2):
            pg.press("tab")
            randsleep()
        pg.press("enter")



    elif sexe == "Femme":
        femme()
        vetement()
        for i in range(1):
            pg.press("tab")
            randsleep()
        pg.press("enter")



    else:
        print("Impossible définir le sexe pour l'article " + id)

#################################### Hauts et t-shirts ####################################

def hautsettshirt(sexe, id):
    typehaut = "Duffle-coats"
    #typehaut = Recuperer typehaut de id
    rdmcat()
    randsleep()
    if sexe == "Homme":
        homme()
        vetement()
        for i in range(3):
            pg.press("tab")
            randsleep()
        pg.press("enter")



    elif sexe == "Femme":
        femme()
        vetement()
        for i in range(6):
            pg.press("tab")
            randsleep()
        pg.press("enter")



    else:
        print("Impossible définir le sexe pour l'article " + id)

#################################### Blazers et tailleurs Femme ####################################

def blazersettailleurs(sexe, id):
    typecos = "Duffle-coats"
    #typecos = Recuperer typecos de id
    rdmcat()
    randsleep()
    if sexe == "Femme":
        femme()
        vetement()
        for i in range(3):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    else:
        print("Impossible définir le sexe pour l'article " + id)

#################################### Costumes et Blazers Homme ####################################

def costumesetblazers(sexe, id):
    typecos = "Duffle-coats"
    #typecos = Recuperer typecos de id
    rdmcat()
    randsleep()
    if sexe == "Homme":
        homme()
        vetement()
        for i in range(4):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    else:
        print("Impossible définir le sexe pour l'article " + id)

#################################### Sweats et pulls ####################################

def sweatsetpulls(sexe,id):
    typepulls = "sweats"
    #typepulls = Recuperer typepulls de id
    rdmcat()
    randsleep()
    if sexe == "Homme":
        homme()
        vetement()
        for i in range(5):
            pg.press("tab")
            randsleep()
        pg.press("enter")



    elif sexe == "Femme":
        femme()
        vetement()
        for i in range(2):
            pg.press("tab")
            randsleep()
        pg.press("enter")



    else:
        print("Impossible définir le sexe pour l'article " + id)

#################################### Pantalon ####################################

def pantalon(sexe,id):
    typepantalon = "chinos"
    #typepantalon = Recuperer typepantalon de id
    rdmcat()
    randsleep()
    if sexe == "Homme":
        homme()
        vetement()
        for i in range(6):
            pg.press("tab")
            randsleep()
        pg.press("enter")



    elif sexe == "Femme":
        femme()
        vetement()
        for i in range(8):
            pg.press("tab")
            randsleep()
        pg.press("enter")



    else:
        print("Impossible définir le sexe pour l'article " + id)

#################################### Shorts ####################################

def shorts(sexe,id):
    typeshorts = "Shorts cargo"
    #typeshorts = Recuperer typeshorts de id
    rdmcat()
    randsleep()
    if sexe == "Homme":
        homme()
        vetement()
        for i in range(7):
            pg.press("tab")
            randsleep()
        pg.press("enter")



    elif sexe == "Femme":
        femme()
        vetement()
        for i in range(9):
            pg.press("tab")
            randsleep()
        pg.press("enter")



    else:
        print("Impossible définir le sexe pour l'article " + id)

#################################### Sport ####################################

def sport(sexe,id):
    typesport = "Survêtement"
    #typesport = Recuperer typesport de id
    rdmcat()
    randsleep()
    if sexe == "Homme":
        homme()
        vetement()
        for i in range(8):
            pg.press("tab")
            randsleep()
        pg.press("enter")



    elif sexe == "Femme":
        femme()
        vetement()
        for i in range(13):
            pg.press("tab")
            randsleep()
        pg.press("enter")



    else:
        print("Impossible définir le sexe pour l'article " + id)

#################################### Robe ####################################

def robe(sexe,id):
    typesport = "Survêtement"
    #typesport = Recuperer typesport de id
    rdmcat()
    randsleep()
    if sexe == "Femme":
        femme()
        vetement()
        for i in range(4):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    else:
        print("Impossible définir le sexe pour l'article " + id)

#################################### Jupe ####################################

def jupe(sexe,id):
    typesport = "Survêtement"
    #typesport = Recuperer typesport de id
    rdmcat()
    randsleep()
    if sexe == "Femme":
        femme()
        vetement()
        for i in range(5):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    else:
        print("Impossible définir le sexe pour l'article " + id)

#################################### Matiere ####################################

def matiere(mat):
    x = random.randint(1281,1716)
    y = random.randint(455,476)
    rm.rdmMouse(x,y)
    pg.click()
    i = 1
    if mat == "Coton":
        while i != 11:
            pg.press("tab")
            i = i + 1
        pg.press("enter")
    elif mat == "Polaire":
        while i != 41:
            pg.press("tab")
            i = i + 1
        pg.press("enter")
    elif mat == "Polyester" :
        while i != 42:
            pg.press("tab")
            i = i + 1
        pg.press("enter")
    elif mat == "Viscose" :
        while i != 55:
            pg.press("tab")
            i = i + 1
        pg.press("enter")
    elif mat == "Elasthanne" :
        while i != 56:
            pg.press("tab")
            i = i + 1
        pg.press("enter")

#################################### Taille ####################################

def taille(t,cat,sexe):
    x = random.randint(1281, 1716)
    y = random.randint(1043, 1066)
    rm.rdmMouse(x, y)
    pg.click()
    if sexe == "Homme":
        if t =="W23":
            pg.press("tab")
            pg.press("tab")
            pg.press("enter")
        elif t =="W24":
            for i in range(2):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="W25":
            for i in range(3):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="W26":
            for i in range(4):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="W27":
            for i in range(5):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="W28":
            for i in range(6):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="W29":
            for i in range(7):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="W30":
            for i in range(8):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="W31":
            for i in range(9):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="W32":
            for i in range(10):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="W33":
            for i in range(11):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="W34":
            for i in range(12):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="W35":
            for i in range(13):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="W36":
            for i in range(14):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="W38":
            for i in range(15):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="W39":
            for i in range(16):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="W40":
            for i in range(17):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="W42":
            for i in range(18):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="W44":
            for i in range(19):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="W46":
            for i in range(20):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="W48":
            for i in range(21):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="W50":
            for i in range(22):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="W52":
            for i in range(23):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="W54":
            for i in range(24):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="XS":
            if cat == "Pantalon" or cat == "Jean" or cat == "Short":
                for i in range(25):
                    pg.press("tab")
                randsleep()
                pg.press("enter")
            else :
                for i in range(1):
                    pg.press("tab")
                randsleep()
                pg.press("enter")
        elif t =="S" or t =="2/3 ans" or t =="8/9 ans":
            if cat == "Pantalon" or cat == "Jean" or cat == "Short":
                for i in range(26):
                    pg.press("tab")
                randsleep()
                pg.press("enter")
            else :
                for i in range(2):
                    pg.press("tab")
                randsleep()
                pg.press("enter")
        elif t =="M" or t =="4/5 ans" or t =="10/12 ans":
            if cat == "Pantalon" or cat == "Jean" or cat == "Short":
                for i in range(27):
                    pg.press("tab")
                randsleep()
                pg.press("enter")
            else :
                for i in range(3):
                    pg.press("tab")
                randsleep()
                pg.press("enter")
        elif t =="L" or t =="6/7 ans" or t =="14/16 ans":
            if cat == "Pantalon" or cat == "Jean" or cat == "Short":
                for i in range(28):
                    pg.press("tab")
                    randsleep()
                pg.press("enter")
            else :
                for i in range(4):
                    pg.press("tab")
                    randsleep()
                pg.press("enter")
        elif t =="XL" or t =="18/20 ans":
            if cat == "Pantalon" or cat == "Jean" or cat == "Short":
                for i in range(29):
                    pg.press("tab")
                    randsleep()
                pg.press("enter")
            else :
                for i in range(5):
                    pg.press("tab")
                    randsleep()
                pg.press("enter")
        elif t =="2XL":
            if cat == "Pantalon" or cat == "Jean" or cat == "Short":
                for i in range(30):
                    pg.press("tab")
                    randsleep()
                pg.press("enter")
            else :
                for i in range(6):
                    pg.press("tab")
                    randsleep()
                pg.press("enter")
        elif t =="3XL":
            if cat == "Pantalon" or cat == "Jean" or cat == "Short":
                for i in range(31):
                    pg.press("tab")
                    randsleep()
                pg.press("enter")
            else :
                for i in range(7):
                    pg.press("tab")
                    randsleep()
                pg.press("enter")
        elif t =="4XL":
            if cat == "Pantalon" or cat == "Jean" or cat == "Short":
                for i in range(32):
                    pg.press("tab")
                pg.press("enter")
            else :
                for i in range(8):
                    pg.press("tab")
                    randsleep()
                pg.press("enter")
        elif t =="5XL":
            if cat == "Pantalon" or cat == "Jean" or cat == "Short":
                for i in range(33):
                    pg.press("tab")
                    randsleep()
                pg.press("enter")
            else :
                for i in range(9):
                    pg.press("tab")
                    randsleep()
                pg.press("enter")
        elif t =="6XL":
            if cat == "Pantalon" or cat == "Jean" or cat == "Short":
                for i in range(34):
                    pg.press("tab")
                    randsleep()
                pg.press("enter")
            else :
                for i in range(10):
                    pg.press("tab")
                    randsleep()
                pg.press("enter")
        elif t =="7XL":
            if cat == "Pantalon" or cat == "Jean" or cat == "Short":
                for i in range(35):
                    pg.press("tab")
                    randsleep()
                pg.press("enter")
            else :
                for i in range(11):
                    pg.press("tab")
                    randsleep()
                pg.press("enter")
        elif t =="8XL":
            if cat == "Pantalon" or cat == "Jean" or cat == "Short":
                for i in range(36):
                    pg.press("tab")
                    randsleep()
                pg.press("enter")
            else :
                for i in range(12):
                    pg.press("tab")
                    randsleep()
                pg.press("enter")
        elif t == "Universel":
            for i in range(13):
                pg.press("tab")
                randsleep()
            pg.press("enter")
    elif sexe == "Femme":
        if t =="XXXS":
            pg.press("tab")
            pg.press("tab")
            pg.press("enter")
        elif t =="XSS":
            for i in range(2):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="XS":
            for i in range(3):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="S":
            for i in range(4):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="M":
            for i in range(5):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="L":
            for i in range(6):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="XL":
            for i in range(7):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="2XL":
            for i in range(8):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="3XL":
            for i in range(9):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="4XL":
            for i in range(10):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="5XL":
            for i in range(11):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="6XL":
            for i in range(12):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="7XL":
            for i in range(13):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="8XL":
            for i in range(14):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="9XL":
            for i in range(15):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="Taille unique":
            for i in range(16):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        else:
            for i in range(17):
                pg.press("tab")
                randsleep()
            pg.press("enter")
    elif sexe == "Enfant":
        print("Le taille n'a pas pu être défini pour les enfants")
    else:
        print("Le taille n'a pas pu être défini")

#################################### Couleurs ####################################

def couleurs(color):
    #Color non utilisé, utilisation de la couleur recommandé par Vinted
    x = random.randint(1281, 1709)
    y = random.randint(351, 371)
    rm.rdmMouse(x, y)
    pg.click()
    randsleep()
    pg.press("tab")
    time.sleep(0.6)
    pg.press("enter")

######################

def colors(color):
    if color == "Noir":
        pg.press("tab")
        randsleep()
        pg.press("enter")
    elif color == "Marron" or color == "Rouille":
        for i in range(2):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif color == "Gris":
        for i in range(3):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif color == "Beige":
        for i in range(4):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif color == "Rose":
        for i in range(5):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif color == "Violet":
        for i in range(6):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif color == "Rouge":
        for i in range(7):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif color == "Jaune" or color == "Jaune fluo":
        for i in range(8):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif color == "Bleu":
        for i in range(9):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif color == "Vert fluo":
        for i in range(10):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif color == "Orange":
        for i in range(11):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif color == "Blanc":
        for i in range(12):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif color == "Argenté":
        for i in range(13):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif color == "Doré" or color == "Or":
        for i in range(14):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif color == "Multicolor":
        for i in range(15):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif color == "Kaki":
        for i in range(16):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif color == "Turquoise":
        for i in range(17):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif color == "Crème":
        for i in range(18):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif color == "Abricot":
        for i in range(19):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif color == "Corail":
        for i in range(20):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif color == "Bordeaux":
        for i in range(21):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif color == "Rose":
        for i in range(22):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif color == "Lila":
        for i in range(23):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif color == "Bleu clair":
        for i in range(24):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif color == "Marine":
        for i in range(25):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif color == "Vert":
        for i in range(26):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif color == "Moutarde":
        for i in range(27):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif color == "Menthe":
        for i in range(28):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    else:
        print("Impossible de définir la couleur")

###################################
# Marron : Maron et Rouille      #
# Jaune : Jaune et Jaune Fluo    #
# Vert foncé : Vert              #
# Vert : Vert Fluo               #
# Doré : Doré et Or              #
##################################

#################################### Etat ####################################

def etat(state):
    x = random.randint(1281, 1716)
    y = random.randint(307, 327)
    rm.rdmMouse(x, y)
    pg.click()
    randsleep()
    if state == "10":
        for i in range(1):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif state == "9":
        for i in range(2):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif state =="8" or state =="7":
        for i in range(3):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif state =="6":
        for i in range(4):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    else:
        print("Aucun matching pour l'Etat")

#################################### Brand ####################################
# Inutile une autre façon est utilisé, je le laisse au casou, le matching est déjà fait

def marque(brand):
    rdmbrand()
    randsleep()
    if brand == "Shein":
        for i in range(1):
            pg.press("tab")
        pg.press("enter")
    elif brand == "Kiabi":
        for i in range(2):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Zara":
        for i in range(3):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Orchestra":
        for i in range(4):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Pokémon":
        for i in range(5):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "H&M":
        for i in range(6):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Tape à l'oeil":
        for i in range(7):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Nike":
        for i in range(8):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Okaïdi":
        for i in range(9):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Playmobil":
        for i in range(10):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Sergent Major":
        for i in range(11):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Vertbaudet":
        for i in range(12):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Adidas":
        for i in range(13):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Disney":
        for i in range(14):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Gémo":
        for i in range(15):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Petit Bateau":
        for i in range(16):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Puma":
        for i in range(17):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Obaïdi":
        for i in range(18):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Lacoste":
        for i in range(19):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Jennyfer":
        for i in range(20):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Decathlon":
        for i in range(21):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Pull & Bear":
        for i in range(22):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "In Extenso":
        for i in range(23):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Primark":
        for i in range(24):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "VTech":
        for i in range(25):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Pimkie":
        for i in range(26):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Camaïeu":
        for i in range(27):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "LEGO":
        for i in range(28):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Tissaia":
        for i in range(29):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Naf Naf":
        for i in range(30):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Boutique Parisienne":
        for i in range(31):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Mango":
        for i in range(32):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Bershka":
        for i in range(33):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "C&A":
        for i in range(34):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Nintendo":
        for i in range(35):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Celio":
        for i in range(36):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Ravensburger":
        for i in range(37):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Cache Cache":
        for i in range(38):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Fait Main":
        for i in range(39):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Jordan":
        for i in range(40):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Levi's":
        for i in range(41):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Jules":
        for i in range(42):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Quechua":
        for i in range(43):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Converse":
        for i in range(44):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Promod":
        for i in range(45):
            pg.press("tab")
            randsleep()
        pg.press("Kaporal")
    elif brand == "Jordan":
        for i in range(46):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "sansnom.":
        for i in range(47):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "La Halle":
        for i in range(48):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Jacadi":
        for i in range(49):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "TEX":
        for i in range(50):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif brand == "Sans marque":
        for i in range(50):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    else:
        for L in brand:
            vinted.driver.find_element(By.ID, 'brand_id').send_keys(L)
            randsleep()
        pg.press("tab")
        pg.click()
