import random
import pyautogui as pg
from selenium.webdriver.common.by import By
import randomMouse as rm
import time
import vinted
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Cette class vise à rendre aléatoire les coordonées du clic sur un champ
# Avec un calcul de l'air de la zone au préalable
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def randsleep():
    i = random.uniform(0.0001 , 0.3)
    time.sleep(i)
def rdmcreateco():
    x = 1730
    y = 134
    rm.rdmMouse(x,y)
    pg.click()
def rdmtitleco():
    x = random.randint(1281,1733)
    y = random.randint(628,650)
    rm.rdmMouse(x,y)
    pg.click()
def rdmdescco():
    x = random.randint(1281,1733)
    y = random.randint(664,771)
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
    x = random.randint(1284,1716)
    y = random.randint(711,729)
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
    x = random.randint(1188, 1374)
    y = random.randint(442, 475)
    rm.rdmMouse(x, y)
    pg.click()
# ////////////////////////////////// Enfant ////////////////////////////////////
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
# ////////////////////////////////// Jean ////////////////////////////////////
def jean(sexe, id):
    rdmcat()
    randsleep()
    if sexe == "Homme":
        homme()
        vetement()
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
    else:
        print("Impossible définir le sexe pour l'article " + id)
# ////////////////////////////////// Jean coupe skinny ////////////////////////////////////
def jeanskinny(sexe, id):
    jean(sexe, id)
    randsleep()
    if sexe == "Homme":
        pg.press("tab")
        randsleep()
        pg.press("tab")
        randsleep()
        pg.press("enter")
    elif sexe == "Femme":
        for i in range(6):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    else:
        print("Impossible définir le sexe pour l'article " + id)
# ////////////////////////////////// Jean droit ////////////////////////////////////
def jeandroit(sexe, id):
    jean(sexe, id)
    randsleep()
    if sexe == "Homme":
        for i in range(4):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif sexe == "Femme":
        for i in range(7):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    else:
        print("Impossible définir le sexe pour l'article " + id)
# ////////////////////////////////// Jean coupe large Femme ////////////////////////////////////
def jeanlarge(sexe, id):
    jean(sexe, id)
    randsleep()
    pg.press("tab")
    randsleep()
    pg.press("enter")
# ////////////////////////////////// Jean slim Homme ////////////////////////////////////
def jeanslim(sexe,id):
    jean(sexe, id)
    randsleep()
    for i in range(3):
        pg.press("tab")
        randsleep()
    pg.press("enter")
# ////////////////////////////////// Jean Autre ////////////////////////////////////
def jeanautre(sexe, id):
    jean(sexe, id)
    randsleep()
    for i in range(8):
        pg.press("tab")
        randsleep()
    pg.press("enter")
# ////////////////////////////////// Manteaux et Vestes ////////////////////////////////////
def manteauxetvestes(sexe, id):
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
# ////////////////////////////////// Manteau ////////////////////////////////////
def manteau(sexe, id):
    manteauxetvestes(sexe, id)
    randsleep()
    if sexe == "Homme":
        for i in range(1):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif sexe == "Femme":
        for i in range(2):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    else:
        print("Impossible définir le sexe pour l'article " + id)
# ////////////////////////////////// Parkas ////////////////////////////////////
def parkas(sexe, id):
    manteau(sexe, id)
    randsleep()
    if sexe == "Homme":
        for i in range(3):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif sexe == "Femme":
        for i in range(4):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    else:
        print("Impossible définir le sexe pour l'article " + id)
# ////////////////////////////////// Vestes ////////////////////////////////////
def vestes(sexe, id):
    manteauxetvestes(sexe, id)
    randsleep()
    if sexe == "Homme":
        for i in range(3):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif sexe == "Femme":
        for i in range(4):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    else:
        print("Impossible définir le sexe pour l'article " + id)
# ////////////////////////////////// Vestes Polaires ////////////////////////////////////
def vestespolaires(sexe, id):
    vestes(sexe, id)
    randsleep()
    for i in range(5):
        pg.press("tab")
        randsleep()
    pg.press("enter")
# ////////////////////////////////// Doudounes ////////////////////////////////////
def doudounes(sexe, id):
    vestes(sexe, id)
    randsleep()
    if sexe == "Homme":
        for i in range(7):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif sexe == "Femme":
        for i in range(6):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    else:
        print("Impossible définir le sexe pour l'article " + id)
# ////////////////////////////////// Blouson Teddy ////////////////////////////////////
def teddy(sexe, id):
    vestes(sexe, id)
    randsleep()
    if sexe == "Homme":
        for i in range(11):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif sexe == "Femme":
        for i in range(10):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    else:
        print("Impossible définir le sexe pour l'article " + id)
# ////////////////////////////////// Veste Coupe-vent ////////////////////////////////////
def coupevent(sexe, id):
    vestes(sexe, id)
    randsleep()
    if sexe == "Homme":
        for i in range(12):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif sexe == "Femme":
        for i in range(11):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    else:
        print("Impossible définir le sexe pour l'article " + id)
# ////////////////////////////////// Veste en jean ////////////////////////////////////
def vestejean(sexe, id):
    vestes(sexe, id)
    randsleep()
    for i in range(3):
        pg.press("tab")
        randsleep()
    pg.press("enter")
# ////////////////////////////////// Hauts et t-shirts ////////////////////////////////////
def hautsettshirt(sexe, id):
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
# ////////////////////////////////// Chemises ////////////////////////////////////
def chemise(sexe,id):
    hautsettshirt(sexe, id)
    randsleep()
    pg.press("tab")
    randsleep()
# ////////////////////////////////// Chemises unies ////////////////////////////////////
def chemiseunies(sexe,id):
    chemise(sexe, id)
    randsleep()
    for i in range(3):
        pg.press("tab")
        randsleep()
    pg.press("enter")
# ////////////////////////////////// Hauts / Veste ////////////////////////////////////
def hautsveste(sexe, id):
    hautsettshirt(sexe, id)
    randsleep()
    for i in range(3):
        pg.press("tab")
        randsleep()
    pg.press("enter")
# ////////////////////////////////// Debardeur ////////////////////////////////////
def debardeur(sexe,id):
    hautsettshirt(sexe, id)
    randsleep()
    for i in range(4):
        pg.press("tab")
        randsleep()
    pg.press("enter")
# ////////////////////////////////// T-Shirt ////////////////////////////////////
def tshirt(sexe,id):
    hautsettshirt(sexe, id)
    randsleep()
    if sexe == "Homme":
        for i in range(2):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif sexe == "Femme":
        for i in range(4):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    else:
        print("Impossible définir le sexe pour l'article " + id)
# ////////////////////////////////// T-Shirts manches longues Homme ////////////////////////////////////
def manchelongue(sexe,id):
    tshirt(sexe, id)
    randsleep()
    for i in range(5):
        pg.press("tab")
        randsleep()
    pg.press("enter")
# ////////////////////////////////// T-Shirts Autres hauts Femme ////////////////////////////////////
def autrehaut(sexe,id):
    hautsettshirt(sexe, id)
    randsleep()
    for i in range(16):
        pg.press("tab")
        randsleep()
    pg.press("enter")
# ////////////////////////////////// Polos Homme ////////////////////////////////////
def polo(sexe,id):
    tshirt(sexe, id)
    randsleep()
    for i in range(4):
        pg.press("tab")
        randsleep()
    pg.press("enter")
# ////////////////////////////////// T-Shirts Imprimé Homme ////////////////////////////////////
def imprime(sexe,id):
    tshirt(sexe, id)
    randsleep()
    for i in range(2):
        pg.press("tab")
        randsleep()
    pg.press("enter")
# ////////////////////////////////// T-Shirts manches sans manches Homme ////////////////////////////////////
def sansmanches(sexe,id):
    hautsettshirt(sexe, id)
    randsleep()
    for i in range(3):
        pg.press("tab")
        randsleep()
    pg.press("enter")
# ////////////////////////////////// Sweats et pulls ////////////////////////////////////
def sweatsetpulls():
    rdmcat()
    randsleep()
    homme()
    vetement()
    for i in range(5):
        pg.press("tab")
        randsleep()
    pg.press("enter")
# ////////////////////////////////// Cardigans ////////////////////////////////////
def cardigans():
    sweatsetpulls()
    randsleep()
    for i in range(4):
        pg.press("tab")
        randsleep()
    pg.press("enter")
# ////////////////////////////////// Sweats ////////////////////////////////////
def sweat():
    sweatsetpulls()
    randsleep()
    pg.press("tab")
    randsleep()
    pg.press("enter")
# ////////////////////////////////// Pull et Pull à capuche ////////////////////////////////////
def pullacapuche():
    sweatsetpulls()
    randsleep()
    pg.press("tab")
    randsleep()
    pg.press("tab")
    randsleep()
    pg.press("enter")
# ////////////////////////////////// Sweats et sweat a capuche ////////////////////////////////////
def sweatsetsweatacapuche():
    rdmcat()
    randsleep()
    femme()
    randsleep()
    vetement()
    for i in range(2):
        pg.press("tab")
        randsleep()
    pg.press("enter")
# ////////////////////////////////// Sweats a capuches ////////////////////////////////////
def sweatcapuche():
    sweatsetsweatacapuche()
    randsleep()
    pg.press("tab")
    randsleep()
    pg.press("enter")
# ////////////////////////////////// Pantalon ////////////////////////////////////
def pantalon(sexe,id):
    rdmcat()
    randsleep()
    if sexe == "Homme":
        homme()
        randsleep()
        vetement()
        for i in range(6):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif sexe == "Femme":
        femme()
        randsleep()
        vetement()
        for i in range(8):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    else:
        print("Impossible définir le sexe pour l'article " + id)
# ////////////////////////////////// Autre Pantalon ////////////////////////////////////
def autrepantalon(sexe,id):
    pantalon(sexe,id)
    randsleep()
    if sexe == "Homme":
        for i in range(7):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif sexe == "Femme":
        for i in range(9):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    else:
        print("Impossible définir le sexe pour l'article " + id)
# ////////////////////////////////// Pantalon ajustés Femme ////////////////////////////////////
def pantalonajuste(sexe,id):
    pantalon(sexe, id)
    randsleep()
    for i in range(4):
        pg.press("tab")
        randsleep()
    pg.press("enter")
# ////////////////////////////////// Pantalon jambe large Homme ////////////////////////////////////
def pantalonjambelarge(sexe,id):
    pantalon(sexe, id)
    randsleep()
    for i in range(6):
        pg.press("tab")
        randsleep()
    pg.press("enter")
# ////////////////////////////////// Shorts ////////////////////////////////////
def shorts(sexe,id):
    rdmcat()
    randsleep()
    if sexe == "Homme":
        homme()
        randsleep()
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
# ////////////////////////////////// Shorts Jean ////////////////////////////////////
def shortjeans(sexe,id):
    shorts(sexe, id)
    randsleep()
    if sexe == "Homme":
        for i in range(3):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif sexe == "Femme":
        for i in range(4):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    else:
        print("Impossible définir le sexe pour l'article " + id)
# ////////////////////////////////// Shorts Casual ////////////////////////////////////
def shortcasual(sexe,id):
    shorts(sexe, id)
    randsleep()
    for i in range(2):
        pg.press("tab")
        randsleep()
    pg.press("enter")
# ////////////////////////////////// Autres Shorts ////////////////////////////////////
def autreshort(sexe,id):
    shorts(sexe, id)
    randsleep()
    if sexe == "Homme":
        for i in range(4):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif sexe == "Femme":
        for i in range(9):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    else:
        print("Impossible définir le sexe pour l'article " + id)
# ////////////////////////////////// Sport ////////////////////////////////////
def sport(sexe,id):
    rdmcat()
    randsleep()
    if sexe == "Homme":
        homme()
        vetement()
        for i in range(11):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif sexe == "Femme":
        femme()
        vetement()
        for i in range(14):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    else:
        print("Impossible définir le sexe pour l'article " + id)
# ////////////////////////////////// Haut de Sport ////////////////////////////////////
def hautsport(sexe,id):
    sport(sexe, id)
    time.sleep(3)
    randsleep()
    if sexe == "Homme":
        print("reach homme")
        for i in range(5):
            print("reach boucle")
            pg.press("tab")
            randsleep()
        pg.press("enter")
        print("reach end")
    elif sexe == "Femme":
        for i in range(7):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    else:
        print("Impossible définir le sexe pour l'article " + id)
# ////////////////////////////////// Robe ////////////////////////////////////
def robe(sexe,id):
    rdmcat()
    randsleep()
    femme()
    vetement()
    for i in range(4):
        pg.press("tab")
        randsleep()
    pg.press("enter")
    for i in range(12):
        pg.press("tab")
        randsleep()
    pg.press("enter")
# ////////////////////////////////// Autre Vetement Homme ////////////////////////////////////
def autre(sexe, id):
    if sexe == "Homme":
        rdmcat()
        randsleep()
        homme()
        randsleep()
        vetement()
        randsleep()
        for i in range(13):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    if sexe == "Femme":
        rdmcat()
        randsleep()
        femme()
        randsleep()
        vetement()
        randsleep()
        for i in range(16):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    else:
        print("Impossible définir le sexe pour l'article " + id)
# ////////////////////////////////// Matiere ////////////////////////////////////
def compmat(cont,name,mat):
    if name in mat:
        x = random.randint(1286, 1710)
        y = random.randint(711, 729)
        rm.rdmMouse(x, y)
        pg.click()
        v = cont
        i = 1
        while i != v:
            pg.press("tab")
            i = i + 1
            randsleep()
        pg.press("enter")
        rm.rdmMouse(2050, 796)
        pg.click()
        time.sleep(1)
def matiere(mat):
    compmat(11,"Coton",mat)
    compmat(42, "Polyester", mat)
    compmat(21, "Feutre", mat)
    compmat(52, "Velours", mat)
    compmat(3, "Acrylique", mat)
    compmat(45, "Satin", mat)
    compmat(17, "Daim", mat)
    compmat(19, "Duvet", mat)
    compmat(30, "Mousseline", mat)
    compmat(8, "Cachemire", mat)
    compmat(22, "Flanelle", mat)
    compmat(53, "Velours Cotele", mat)
    compmat(17, "Denim", mat)
    compmat(4, "Alpaca", mat)
    compmat(56, "Élasthanne", mat)
    compmat(20, "Fourrure", mat)
    compmat(48, "Soie", mat)
    compmat(25, "Latex", mat)
    compmat(31, "Merinos", mat)
    compmat(24, "Laine", mat)
    compmat(12, "Cuir", mat)
    compmat(33, "Nylon", mat)
    compmat(13, "Cuir synthetique", mat)
    compmat(55, "Viscose", mat)
    compmat(26, "Lin", mat)
    compmat(34, "Neoprene", mat)
    compmat(18, "Dentelle", mat)
    compmat(41, "Polaire", mat)
#################################
#    if mat == "Coton":         #
#        while i != 11:         #
#            pg.press("tab")    #
#            i = i + 1          #
#        pg.press("enter")      #
#    elif mat == "Polaire":     #
#        while i != 41:         #
#            pg.press("tab")    #
#            i = i + 1          #
#        pg.press("enter")      #
#    elif mat == "Polyester" :  #
#        while i != 42:         #
#           pg.press("tab")     #
#            i = i + 1          #
#        pg.press("enter")      #
#    elif mat == "Viscose" :    #
#        while i != 55:         #
#            pg.press("tab")    #
#            i = i + 1          #
#        pg.press("enter")      #
#    elif mat == "Elasthanne" : #
#        while i != 56:         #
#            pg.press("tab")    #
#            i = i + 1          #
#        pg.press("enter")      #
#################################
# ////////////////////////////////// Taille ////////////////////////////////////
def taille(t,cat,sexe):
    x = random.randint(1281, 1712)
    y = random.randint(712, 729)
    rm.rdmMouse(x, y)
    pg.click()
    if sexe == "Homme" or sexe == "Enfant":
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
                for i in range(2):
                    pg.press("tab")
                randsleep()
                pg.press("enter")
        elif t =="S" or "2/3 ans" in t or "8/9 ans" in t:
            if cat == "Pantalon" or cat == "Jean" or cat == "Short":
                for i in range(26):
                    pg.press("tab")
                randsleep()
                pg.press("enter")
            else :
                for i in range(3):
                    pg.press("tab")
                randsleep()
                pg.press("enter")
        elif t =="M" or "4/5 ans" in t or "10/12 ans" in t:
            if cat == "Pantalon" or cat == "Jean" or cat == "Short":
                for i in range(27):
                    pg.press("tab")
                randsleep()
                pg.press("enter")
            else :
                for i in range(4):
                    pg.press("tab")
                randsleep()
                pg.press("enter")
        elif t =="L" or "6/7 ans" in t or "14/16 ans" in t:
            if cat == "Pantalon" or cat == "Jean" or cat == "Short":
                for i in range(28):
                    pg.press("tab")
                    randsleep()
                pg.press("enter")
            else :
                for i in range(5):
                    pg.press("tab")
                    randsleep()
                pg.press("enter")
        elif t =="XL" or "18/20 ans" in t:
            if cat == "Pantalon" or cat == "Jean" or cat == "Short":
                for i in range(29):
                    pg.press("tab")
                    randsleep()
                pg.press("enter")
            else :
                for i in range(6):
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
                for i in range(7):
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
                for i in range(8):
                    pg.press("tab")
                    randsleep()
                pg.press("enter")
        elif t =="4XL":
            if cat == "Pantalon" or cat == "Jean" or cat == "Short":
                for i in range(32):
                    pg.press("tab")
                pg.press("enter")
            else :
                for i in range(9):
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
                for i in range(10):
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
                for i in range(11):
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
                for i in range(12):
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
                for i in range(13):
                    pg.press("tab")
                    randsleep()
                pg.press("enter")
        elif t == "Universel":
            for i in range(14):
                pg.press("tab")
                randsleep()
            pg.press("enter")
    elif sexe == "Femme":
        if t =="XXXS":
            pg.press("tab")
            pg.press("tab")
            pg.press("enter")
        elif t =="XSS":
            for i in range(3):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="XS":
            for i in range(4):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="S":
            for i in range(5):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="M":
            for i in range(6):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="L":
            for i in range(7):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="XL":
            for i in range(8):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="2XL":
            for i in range(9):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="3XL":
            for i in range(10):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="4XL":
            for i in range(11):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="5XL":
            for i in range(12):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="6XL":
            for i in range(13):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="7XL":
            for i in range(14):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="8XL":
            for i in range(15):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="9XL":
            for i in range(16):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        elif t =="Taille unique":
            for i in range(17):
                pg.press("tab")
                randsleep()
            pg.press("enter")
        else:
            for i in range(18):
                pg.press("tab")
                randsleep()
            pg.press("enter")
    #elif sexe == "Enfant":
        #print("Le taille n'a pas pu être défini pour les enfants")
        #pg.press("esc")
    else:
        print("Le taille n'a pas pu être défini")
        pg.press("esc")
# ////////////////////////////////// Couleurs ////////////////////////////////////
def couleurs(color):
    #Couleursr non utilisé, utilisation de la couleur recommandé par Vinted
    x = random.randint(1281, 1709)
    y = random.randint(708, 727)
    rm.rdmMouse(x, y)
    pg.click()
    randsleep()
    pg.press("tab")
    time.sleep(0.6)
    pg.press("enter")
# //////////////////////////////////
def colors(color):
    x = random.randint(1295, 1707)
    y = random.randint(717, 726)
    rm.rdmMouse(x, y)
    pg.click()
    randsleep()
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
        pg.press("tab")
        randsleep()
        pg.press("enter")
###################################
# Marron : Maron et Rouille      #
# Jaune : Jaune et Jaune Fluo    #
# Vert foncé : Vert              #
# Vert : Vert Fluo               #
# Doré : Doré et Or              #
##################################
# ////////////////////////////////// Etat ////////////////////////////////////
def etat(state):
    x = random.randint(1281, 1711)
    y = random.randint(711, 724)
    rm.rdmMouse(x, y)
    pg.click()
    randsleep()
    if "10/10" in state:
        for i in range(1):
            pg.press("tab")
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif "9" in state:
        for i in range(2):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif "8" in state or "7" in state:
        for i in range(3):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    elif "6" in state:
        for i in range(4):
            pg.press("tab")
            randsleep()
        pg.press("enter")
    else:
        print("Aucun matching pour l'Etat")
        pg.press("tab")
        randsleep()
        pg.press("enter")
# ////////////////////////////////// Brand ////////////////////////////////////
# Inutile une autre façon est utilisé, je le laisse au cas ou, le matching est déjà fait
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
        pg.press("enter")