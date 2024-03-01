def autodesc(categorie, qwe, marque, taille, couleur, etat, longueur, largeur, manche, tag):
    if manche is None :
        if categorie == "T-shirt" or categorie == "Maillot":
            desc = f"""
- Marque : #{marque}
- Taille : {taille}
- Couleur : {couleur}
- État : {etat}

Mensurations :
Longueur (du bas jusqu'au col) : {longueur}cm
Largeur (aisselle à aisselle) : {largeur}cm

🚀 Expédition le jour même si
commande avant 11H00 (jours
ouvrés uniquement)

🔥 Nos vêtements recondition
nés ont été vérifiés et nettoyés
par nos experts, afin d'être portés
de nouveau. 🔥

Référence interne : {qwe.upper()} /
#MSSIZE{categorie.upper()}{taille.upper()}

Conditions de vente :
🚫 Pas de réservation / Photo portée.
✅ Vêtements authentiques.
👕 Achats en lot possibles.
🔙📦 14 jours pour changer d’avis
😀 + de 5500 clients satisfait !
♻️ Engagé pour la planète !
📱Instagram : @meduzastore_fr / TikTok : @meduza_store

{tag}
"""
            print(desc)
            return desc


######################################################################
#
######################################################################
    else :
        if categorie == "Pantalon":
            desc = f"""
- Marque : #{marque}
- Taille : {taille}
- Couleur : {couleur}
- État : {etat}

Mensurations :
Largeur de la taille : {longueur}cm
Longueur jambes intérieure : {largeur}cm
Longueur jambes extérieure : {manche}cm

🚀 Expédition le jour même si
commande avant 11H00 (jours
ouvrés uniquement)

🔥 Nos vêtements recondition
nés ont été vérifiés et nettoyés
par nos experts, afin d'être portés
de nouveau. 🔥

Référence interne : {qwe.upper()} /
#MSSIZE{categorie.upper()}{taille.upper()}

Conditions de vente :
🚫 Pas de réservation / Photo portée.
✅ Vêtements authentiques.
👕 Achats en lot possibles.
🔙📦 14 jours pour changer d’avis
😀 + de 5500 clients satisfait !
♻️ Engagé pour la planète !
📱Instagram : @meduzastore_fr / TikTok : @meduza_store

{tag}
"""
            print(desc)
            return desc


######################################################################

        elif categorie == "Manche Longue":
            desc = f"""
- Marque : #{marque}
- Taille : {taille}
- Couleur : {couleur}
- État : {etat}

Mensurations :
Longueur () : {longueur}cm
Largeur () : {largeur}cm

🚀 Expédition le jour même si
commande avant 11H00 (jours
ouvrés uniquement)

🔥 Nos vêtements recondition
nés ont été vérifiés et nettoyés
par nos experts, afin d'être portés
de nouveau. 🔥

Référence interne : {qwe.upper()} /
#MSSIZE{categorie.upper()}{taille.upper()}

Conditions de vente :
🚫 Pas de réservation / Photo portée.
✅ Vêtements authentiques.
👕 Achats en lot possibles.
🔙📦 14 jours pour changer d’avis
😀 + de 5500 clients satisfait !
♻️ Engagé pour la planète !
📱Instagram : @meduzastore_fr / TikTok : @meduza_store

{tag}
"""
        print(desc)
        return desc


tag = "#JeanLeviStrauss #JeansHomme #Taille34x30 #DenimLeviStrauss #ModeHomme #StyleDenim #Levi514 #PantalonHomme #JeanTaille34 #ClassiqueDenin"
autodesc("Maillot", "#qwe7274","Nike", "XL", "Noir", "Neuf", 62, 47, None, tag)