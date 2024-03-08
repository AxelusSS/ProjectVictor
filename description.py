def autodesc(categorie, catbrut, sexe, typeitem, qwe, marque, taille, couleur, etatbrut, longueur,
             largeur, manche, tag):
    marquetag = marque.replace(" ", "")

    chaine = etatbrut
    indice = chaine.find(" ")
    etat = chaine[indice + 3:]

    chaine = categorie
    if chaine.endswith("s"):
        typeitem = chaine[:-1]

    if "Sport" in catbrut or "sport" in catbrut:
        chaine = f"MAILLOT{taille.upper()}"
        mssize = chaine.replace(" ", "")
    else:
        chaine = f"{categorie.upper()}{taille}"
        mssize = chaine.replace(" ", "")

    if manche != "not" and manche != "None":
        desc = f"""- Marque : #{marquetag}
- Taille : {taille} {sexe}
- Couleur : {couleur}
- État : {etat}

Mensurations :
Longueur (du bas jusqu'au col) : {longueur}cm
Largeur (aisselle à aisselle) : {largeur}cm
Longueur des manches : {manche}cm

🚀 Expédition le jour même si commande avant 11H00 (jours
ouvrés uniquement)

🔥 Nos vêtements reconditionnés ont été vérifiés et nettoyés
par nos experts, afin d'être portés de nouveau. 🔥

Référence interne : {qwe.upper()} / #MSSIZE{mssize}

Conditions de vente :
🚫 Pas de réservation / Photo portée.
✅ Vêtements authentiques.
👕 Achats en lot possibles.
🔙📦 14 jours pour changer d’avis
😀 + de 5500 clients satisfait !
♻️ Engagé pour la planète !
📱Instagram : @meduzastore_fr / TikTok : @meduza_store

{tag}"""
        # print(desc)
        return desc

# ////////////////////////////////////////////////////////////////////////////////
#
# ////////////////////////////////////////////////////////////////////////////////
    elif "Bermudas" in catbrut or "Short de sport" in catbrut or "Shorts casual" in catbrut or "Shorts en jean" in catbrut or "Pantalons slim" in catbrut or "Pantalons classiques" in catbrut or "Shorts casual" in catbrut or "Jeans coupe ajustée" in catbrut or "Jeans coupe slim" in catbrut or "Pantalons cargo" in catbrut or "Pantalons slim" in catbrut or "Pantalons classiques" in catbrut or "Pantalons cargo" in catbrut or "Jeans coupe droite" in catbrut or "Jeans coupe large" in catbrut or "Jeans coupe ajustée" in catbrut :
        desc = f"""- Marque : #{marquetag}
- Taille : {taille} {sexe}
- Couleur : {couleur}
- État : {etat}

Mensurations :
Largeur de la taille : {longueur}cm
Longueur jambes intérieure : {largeur}cm
Longueur jambes extérieure : {manche}cm

🚀 Expédition le jour même si commande avant 11H00 (jours
ouvrés uniquement)

🔥 Nos vêtements reconditionnés ont été vérifiés et nettoyés
par nos experts, afin d'être portés de nouveau. 🔥

Référence interne : {qwe.upper()} / #MSSIZE{mssize}

Conditions de vente :
🚫 Pas de réservation / Photo portée.
✅ Vêtements authentiques.
👕 Achats en lot possibles.
🔙📦 14 jours pour changer d’avis
😀 + de 5500 clients satisfait !
♻️ Engagé pour la planète !
📱Instagram : @meduzastore_fr / TikTok : @meduza_store

{tag}"""
        # print(desc)
        return desc
# ////////////////////////////////////////////////////////////////////////////////
    else:
        desc = f"""- Marque : #{marquetag}
- Taille : {taille} {sexe}
- Couleur : {couleur}
- État : {etat}

Mensurations :
Longueur (du bas jusqu'au col) : {longueur}cm
Largeur (aisselle à aisselle) : {largeur}cm

🚀 Expédition le jour même si commande avant 11H00 (jours
ouvrés uniquement)

🔥 Nos vêtements reconditionnés ont été vérifiés et nettoyés
par nos experts, afin d'être portés de nouveau. 🔥

Référence interne : {qwe.upper()} / #MSSIZE{mssize}

Conditions de vente :
🚫 Pas de réservation / Photo portée.
✅ Vêtements authentiques.
👕 Achats en lot possibles.
🔙📦 14 jours pour changer d’avis
😀 + de 5500 clients satisfait !
♻️ Engagé pour la planète !
📱Instagram : @meduzastore_fr / TikTok : @meduza_store

{tag}"""
        # print(desc)
        return desc

#tag = "#JeanLeviStrauss #JeansHomme #Taille34x30 #DenimLeviStrauss #ModeHomme #StyleDenim #Levi514 #PantalonHomme #JeanTaille34 #ClassiqueDenin"
#autodesc("Maillot", "Homme > Vestes > Doudoudne", "Homme", "Doudounes", "qwe7274","Nike", "XL", "Noir", "9/10 Excellent état", 62, 47, 62, tag)






"""
"Bermudas" in catbrut or "Short de sport" in catbrut or "Shorts casual" in catbrut or "Shorts en jean" in catbrut or "Pantalons slim" in catbrut or "Pantalons classiques" in catbrut or "Shorts casual" in catbrut or "Jeans coupe ajustée" in catbrut or "Jeans coupe slim" in catbrut or "Pantalons cargo" in catbrut or "Pantalons slim" in catbrut or "Pantalons classiques" in catbrut or "Pantalons cargo" in catbrut or "Jeans coupe droite" in catbrut or "Jeans coupe large" in catbrut or "Jeans coupe ajustée" in catbrut :


"Robe" in catbrut :
"Maillots" in catbrut :
"Sweats à capuche" in catbrut :
"Pulls" in catbrut :
"Pulls polaires" in catbrut :
"Sweats à capuche" in catbrut :
"Sweats" in catbrut :
"Gilets" in catbrut :



"Chemises" in catbrut :
"""