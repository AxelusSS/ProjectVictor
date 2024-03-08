import pyperclip
import description
# /////////////////////////////////////////////////////////////////////////
def clipb(categorie, catbrut, sexe, typeitem, qwe, marque, taille, couleur, etat, longueur, largeur, manche, tag):
    # Bloc de texte à copier dans le presse-papiers
    texte = description.autodesc(categorie, catbrut, sexe, typeitem, qwe, marque, taille, couleur, etat, longueur,
                                 largeur, manche, tag)
    # Copier le texte dans le presse-papiers
    #print(texte)
    pyperclip.copy(texte)
    #print("Le texte a été copié dans le presse-papiers.")
#tag = "#JeanLeviStrauss #JeansHomme #Taille34x30 #DenimLeviStrauss #ModeHomme #StyleDenim #Levi514 #PantalonHomme #JeanTaille34 #ClassiqueDenin"
#clipb("Maillot", "Homme > Vestes > Doudoudne", "Homme", "Doudounes", "#qwe7274","Nike", "XL", "Noir", "9/10 Excellent état", 62, 47, 62, tag)


