def autotitle(title, qwe, id, taille, sexe, color):
    titre = f"{title} {sexe} Taille {taille} {color} {qwe.upper()}/{id}"
    print(titre)
    return titre

#autotitle("Veste polaire Patagonia réversible", "#qwe7274", "60224")