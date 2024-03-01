import os
import requests


def telecharger_et_enregistrer_photos(liens):
    chemins_locaux = []

    dossier_temp = "temp"
    if not os.path.exists(dossier_temp):
        os.makedirs(dossier_temp)

    for lien in liens:
        try:
            # Télécharger l'image depuis le lien
            reponse = requests.get(lien)
            if reponse.status_code == 200:
                # Créer un nom de fichier local unique en utilisant le nom du fichier dans l'URL
                nom_fichier = lien.split('/')[-1]
                chemin_local = os.path.join("temp", nom_fichier)

                # Enregistrer l'image localement
                with open(chemin_local, 'wb') as f:
                    f.write(reponse.content)

                # Ajouter le chemin local à la liste
                chemins_locaux.append(chemin_local)
        except Exception as e:
            print("Erreur lors du téléchargement et de l'enregistrement de l'image :", str(e))

    return chemins_locaux


def supprimer_photos(chemins_locaux):
    for chemin in chemins_locaux:
        try:
            # Supprimer le fichier local
            os.remove(chemin)
        except Exception as e:
            print("Erreur lors de la suppression de l'image :", str(e))




