import tkinter as tk
from tkinter import messagebox

class Settings:
    def __init__(self):
        self.vin = False
        self.scr = False
        self.upd = False
        self.headless_status = False

settings = Settings()

def publi_vinted():
    if button1_var.get():
        print("1 - Publication sure Vinted . . .")
        settings.vin = True
    else:
        print("1 - Stop")
        settings.vin = False

def scraping():
    if button2_var.get():
        print("2 - Scraping . . .")
        settings.scr = True
    else:
        print("2 - Stop")
        settings.scr = False

def update_bdd():
    if button3_var.get():
        print("3 - Update de la Bdd . . .")
        settings.upd = True
    else:
        print("3 - Stop")
        settings.upd = False

def toggle_headless():
    settings.headless_status = not settings.headless_status
    if settings.headless_status:
        headless_button.config(text="Headless: ON", bg="#FF5252", fg="#FFFFFF")
        print("4 - Headless . . .")
    else:
        headless_button.config(text="Headless: OFF", bg="#4CAF50", fg="#FFFFFF")
        print("4 - Stop")

def submit():
    selected_actions = [action for action, var in zip([publi_vinted, scraping, update_bdd], [button1_var, button2_var, button3_var]) if var.get()]
    print(f"Execution de : {[action.__name__ for action in selected_actions]}")
    tmp = entry.get()
    if settings.vin and (not tmp or int(tmp) < 3):
        messagebox.showinfo("INVALID", "Impossible de publier plus rapidement que à raison de 1 publication toutes les 3 minutes")
    elif settings.vin and tmp:
        print(f"Publication tous les : {tmp} minutes")
    else:
        print("Aucune action cochée")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Victor Alpha")
root.configure(bg="#37474F")

# Création des styles
button_style = {"bg": "#4CAF50", "fg": "#FFFFFF", "activebackground": "#43A047", "activeforeground": "#FFFFFF", "highlightbackground": "#37474F", "font": ("Arial", 12, "bold")}
checkbox_style = {"bg": "#37474F", "activebackground": "#37474F", "highlightbackground": "#37474F"}
entry_style = {"bg": "#455A64", "fg": "#FFFFFF", "insertbackground": "#FFFFFF", "highlightbackground": "#455A64", "font": ("Arial", 12, "bold")}

# Création des variables pour les boutons à cocher
button1_var = tk.BooleanVar()
button2_var = tk.BooleanVar()
button3_var = tk.BooleanVar()

# Création des éléments d'interface
button1 = tk.Checkbutton(root, text="Publi Vinted", variable=button1_var, onvalue=True, offvalue=False, command=publi_vinted, **checkbox_style)
button2 = tk.Checkbutton(root, text="Scraping", variable=button2_var, onvalue=True, offvalue=False, command=scraping, **checkbox_style)
button3 = tk.Checkbutton(root, text="Update Bdd", variable=button3_var, onvalue=True, offvalue=False, command=update_bdd, **checkbox_style)

headless_button = tk.Button(root, text="Headless: OFF", command=toggle_headless, **button_style)

entry_label = tk.Label(root, text="Publi toute les (min) :", bg="#37474F", fg="#FFFFFF", font=("Arial", 12, "bold"))
entry = tk.Entry(root, **entry_style)

submit_button = tk.Button(root, text="Executer", command=submit, **button_style)

# Petit texte en bas pour afficher la version du logiciel
version_text = tk.StringVar()
version_text.set("Version 0.1")
version_label = tk.Label(root, textvariable=version_text, bg="#37474F", fg="#FF9800", font=("Arial", 10))

# Placement des éléments dans la fenêtre
button1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
button2.grid(row=1, column=0, padx=10, pady=5, sticky="w")
button3.grid(row=2, column=0, padx=10, pady=5, sticky="w")

headless_button.grid(row=3, column=0, padx=10, pady=5, sticky="we")

entry_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry.grid(row=5, column=0, padx=10, pady=5, sticky="we")

submit_button.grid(row=6, column=0, padx=10, pady=10, sticky="we")

version_label.grid(row=7, column=0, padx=10, pady=5, sticky="se")

# Lancement de la boucle principale
root.mainloop()
