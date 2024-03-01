import pyperclip
import description


def clipb(categorie, qwe, marque, taille, couleur, etat, longueur, largeur, manche, tag):
    # Bloc de texte à copier dans le presse-papiers
    texte = description.autodesc(categorie, qwe, marque, taille, couleur, etat, longueur, largeur, manche, tag)
    # Copier le texte dans le presse-papiers
    pyperclip.copy(texte)

    print("Le texte a été copié dans le presse-papiers.")


