import pandas as pd

# Les données du flux, chaque ligne représente une entrée du flux
data = {
    "code-ean": ["9507619961353"],
    "denomitation-concice": ["Blouson Patagonia"],
    "description-concice": ["<i>Nos vêtements reconditionnés ont été vérifiés par nos experts puis nettoyés afin d'être portés de nouveau.</i><br><br>Ce blouson Patagonia en taille 2XL, couleur orange, est idéal pour la randonnée. En excellent état, il offre chaleur, confort et praticité."],
    "description-complete": ["<h3>Blouson Patagonia</h3> <h4><strong>MENSURATIONS</strong></h4> <p>Longueur (du bas jusqu'au col) : 79cm</p> <p>Largeur (aisselle à aisselle) : 72cm</p> <p>Longueur des manches : 70cm</p> <p><em>* Les mensurations sont relevées manuellement sur chaque article avec une tolérance de 1cm.</em></p> <h4><strong>ÉTAT</strong></h4> <p>Ce blouson Patagonia en taille 2XL, couleur orange, est un produit d'occasion en excellent état. Nous l'avons minutieusement vérifié et nettoyé pour vous offrir un produit prêt à être porté. Bien qu'il puisse y avoir de légères traces d'usure, le blouson est 100% fonctionnel et ne présente aucun défaut majeur.</p> <h4><strong>DESCRIPTION</strong></h4> <p>Ce blouson Patagonia en taille 2XL, couleur orange, est un incontournable pour les activités en extérieur par temps froid, que ce soit pour la randonnée, le camping ou d'autres aventures en nature. Fabriqué par la marque renommée Patagonia, ce blouson offre chaleur, confort et praticité pour répondre à vos besoins lors de vos escapades en plein air.</p> <h4><strong>AVANTAGES PRODUIT</strong></h4> <p><strong><em>Chaleur et confort</em></strong><br>Le blouson Patagonia est conçu pour offrir une excellente isolation thermique, vous maintenant au chaud même par temps très froid, tout en étant confortable à porter pour une liberté de mouvement optimale.</p> <p><strong><em>Praticité</em></strong><br>Doté de poches fonctionnelles, d'une fermeture zippée et d'un design pensé pour l'activité en extérieur, ce blouson vous permet de ranger vos affaires en toute sécurité et d'être prêt(e) pour l'aventure à tout moment.</p> <p><strong><em>Respectueux de l'environnement</em></strong><br>En choisissant un produit de seconde main, vous contribuez à prolonger la durée de vie d'un vêtement déjà existant, ce qui est un geste positif pour l'environnement.</p> <h4><strong>POURQUOI CHOISIR UN PRODUIT DE SECONDE MAIN ?</strong></h4> <p>Choisir un produit d'occasion, c'est faire un geste pour l'environnement en prolongeant la durée de vie d'un objet déjà existant. De plus, c'est souvent une solution plus économique pour acquérir des produits de qualité. En optant pour ce blouson Patagonia de seconde main, vous faites un choix responsable tout en bénéficiant d'un produit de qualité à un prix abordable.</p> <h4><strong>NOTRE ENGAGEMENT QUALITÉ</strong></h4> <p>Nous sommes fiers de vous offrir des produits d'occasion en excellent état. Tous nos produits ont été soigneusement vérifiés et nettoyés par nos experts pour vous garantir une qualité irréprochable. Nous sommes également à votre disposition pour répondre à toutes vos questions et vous aider à trouver le produit qui convient le mieux à vos besoins et à votre budget.</p> <h4><strong>CONCLUSION</strong></h4> <p>Ce blouson Patagonia en taille 2XL, couleur orange, est un vêtement de seconde main en excellent état, vérifié et nettoyé par nos experts. Avec ses avantages en termes de chaleur, confort et praticité, il est idéal pour vos aventures en plein air. En optant pour ce produit, vous faites un geste pour l'environnement tout en bénéficiant d'un produit de qualité à un prix abordable. N'hésitez pas à nous contacter si vous avez des questions ou si vous souhaitez obtenir plus d'informations sur ce produit.</p>"],
    "url-article": ["https://www.meduzastore.com/produit/blouson-patagonia/"],
    "url-photo1": ["https://www.meduzastore.com/wp-content/uploads/2024/02/blouson-homme-manches-longues-orange-patagonia-col-montant-qwe3317.jpg"],
    "url-photo2": ["https://www.meduzastore.com/wp-content/uploads/2024/02/blouson-homme-manches-longues-orange-patagonia-col-montant-qwe3317-1.jpg"],
    "url-photo3": ["https://www.meduzastore.com/wp-content/uploads/2024/02/blouson-homme-manches-longues-orange-patagonia-col-montant-qwe3317-2.jpg"],
    "url-photo4": ["https://www.meduzastore.com/wp-content/uploads/2024/02/blouson-homme-manches-longues-orange-patagonia-col-montant-qwe3317-3.jpg"],
    "url-photo5": ["https://www.meduzastore.com/wp-content/uploads/2024/02/blouson-homme-manches-longues-orange-patagonia-col-montant-qwe3317-4.jpg"],
    "classification": ["Blousons > Homme > Vestes et Manteaux"],
    "disponibilite": ["Y"],
    "statut-de-disponibilite": ["S"],
    "delai-de-livraison": ["2 à 5"],
    "unite-delai-de-livraison": ["D"],
    "unite-delai-d-expedition": ["D"],
    "description-livraison": ["Livraison en point relais offerte"],
    "weight_unit": ["kg"],
    "height": ["#==#dimensions:xx,cm"],
    "dimensions_unit": ["pa_tailles:2XL#==#tailles:2XL#==#marqueDepuisTerm:Patagonia#==#couleurDepuisTerm:Orange#==#typesport:Randonnée#==#Longueur des manches:Manches Longues#==#Capuche:sans capuche#==#Fermeture:Full Zip#==#Etat du produit:8/10 - Excellent état#==#Etat Decathlon:1#==#taille:2XL#==#Matter:Polyester 100%#==#Provenance:Vietnam#==#photo6:https://www.meduzastore.com/wp-content/uploads/2024/02/blouson-homme-manches-longues-orange-patagonia-col-montant-qwe3317-5.jpg#==#photo7:https://www.meduzastore.com/wp-content/uploads/2024/02/blouson-homme-manches-longues-orange-patagonia-col-montant-qwe3317-6.jpg#==#photo8:https://www.meduzastore.com/wp-content/uploads/2024/02/blouson-homme-manches-longues-orange-patagonia-col-montant-qwe3317-7.jpg#==#photo9:https://www.meduzastore.com/wp-content/uploads/2024/02/blouson-homme-manches-longues-orange-patagonia-col-montant-qwe3317-8.jpg#==#photo10:https://www.meduzastore.com/wp-content/uploads/2024/02/blouson-homme-manches-longues-orange-patagonia-col-montant-qwe3317-9.jpg#==#photo11:https://www.meduzastore.com/wp-content/uploads/2024/02/blouson-homme-manches-longues-orange-patagonia-col-montant-qwe3317-10.jpg#==#photo12:https://www.meduzastore.com/wp-content/uploads/2024/02/blouson-homme-manches-longues-orange-patagonia-col-montant-qwe3317-11.jpg#==#photo13:https://www.meduzastore.com/wp-content/uploads/2024/02/blouson-homme-manches-longues-orange-patagonia-col-montant-qwe3317-12.jpg"],
}

# Créer un DataFrame
df = pd.DataFrame(data)

# Afficher le DataFrame
print(df)