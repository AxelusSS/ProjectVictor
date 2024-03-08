import pandas as pd

# Spécifiez l'URL du flux de données
url_flux = "https://www.meduzastore.com/?export=iziflux"

# Utilisez read_csv pour récupérer le flux de données
flux_data = pd.read_csv(url_flux, delimiter='|')  # Assurez-vous d'utiliser le bon délimiteur

# Affichez les types de données dans le DataFrame
print(flux_data.dtypes)

# Sélectionnez uniquement les colonnes de type chaîne de caractères
colonnes_str = flux_data.select_dtypes(include='object').columns

# Créez une nouvelle DataFrame en appliquant l'opération split uniquement sur les colonnes sélectionnées
flux_data_split = pd.DataFrame()
for col in colonnes_str:
    flux_data_split[col] = flux_data[col].str.split('|', expand=True)

# Affichez les premières lignes du DataFrame résultant
print(flux_data_split.head())

# Enregistrez le DataFrame résultant dans un fichier CSV
flux_data_split.to_csv("flux_data_separe.csv", index=False)


#/html/body/pre/text()[1]
