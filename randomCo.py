import random

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
def rdmcreateco():
    x = random.randint(1674,1788)
    y = random.randint(121,147)
    return x, y

def rdmtitleco():
    x = random.randint(1281,1733)
    y = random.randint(628,650)
    return x, y

def rdmdescco():
    x = random.randint(1281,1733)
    y = random.randint(703,813)
    return x, y

def rdmprixco():
    x = random.randint(1281,1733)
    y = random.randint(989,1014)
    return x, y

def rdmbrouillonco():
    x = random.randint(1455,1660)
    y = random.randint(1271,1310)
    return x, y


#print(rdmtitleco())
#print(rdmdescco())
#print(rdmprixco())
#print(rdmbrouillonco())