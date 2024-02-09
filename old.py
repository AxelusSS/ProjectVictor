#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# La fonction connectToVinted permet au code de ce connecter directement au compte Vinted de la boutique
# REMPLACER LE LOGIN ET LE PWD DANS LE FICHIER LOGIN.PY
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# V1
def connectToVinted(session_iD, user_id):
    with requests.Session() as s:
        try:
            #.get(login.ulrConnect)
            s.submit('header--login-button')
            s.submit('auth-select-type--login-email')
            login_data = {'username' : login, 'password': pwd}
            s.post(url, data=login_data)
            print("CONNECTION A VINTED REUSSI" + colorama.Fore.GREEN + " Ready")
        except:
            print(colorama.Fore.RED + "IMPOSSIBLE DE CE CONNECTER A VINTED")
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# V2
    with requests.Session() as s:
        colorama.init(autoreset=True)
        try:
            # Accéder à la page de connexion
            response = s.get(url)
            response.raise_for_status()

            # Soumettre le formulaire de connexion
            login_data = {'login': login, 'password': pwd}
            time.sleep(2)
            response = s.post(url, data=login_data)
            time.sleep(2)
            response.raise_for_status()

            # Vérifier si la connexion a réussi
            if "Déconnexion" in response.text:
                print("CONNEXION À VINTED RÉUSSIE" + colorama.Fore.GREEN + " Prêt")
            else:
                print(colorama.Fore.RED + "ÉCHEC DE LA CONNEXION À VINTED")
        except requests.exceptions.RequestException as e:
            print(colorama.Fore.RED + "IMPOSSIBLE DE SE CONNECTER À VINTED:", str(e))
