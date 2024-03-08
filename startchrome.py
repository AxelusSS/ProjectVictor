import subprocess
# //////////////////////////////////////
def startchrome():
    commande = "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=//Users/meduzastore/PycharmProjects/session"
    process = subprocess.Popen(commande, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print("Sortie de la commande :", stdout.decode())
    print("Erreurs de la commande :", stderr.decode())