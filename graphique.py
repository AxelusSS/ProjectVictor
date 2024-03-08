# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=//Users/meduzastore/PycharmProjects/session

import tkinter
import tkinter.messagebox
import customtkinter
import startchrome
import articleIdOnvinted
import iziflux
import autoavis
import para
# //////////////////////////////////////
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
# //////////////////////////////////////
class App(customtkinter.CTk):
    Vfin = True
    Vson = True
    Vtimer = 180
    def __init__(self):
        super().__init__()
        self.title("HellBot 1.0.0.py")
        self.geometry(f"{820}x{580}")
        # //////////////////////////////////////
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        # //////////////////////////////////////
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="HellBot", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,text="Mise à jour BDD", command=self.sidebar_button_update)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,text="Lancer Chrome", command=self.sidebar_button_launch)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text="Auto avis", command=self.avis)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Theme Interface:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Dark","Light","System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="Taille Interface:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        # //////////////////////////////////////
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Temps (en sec) entre chaque publication (180s par défaut)")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        # //////////////////////////////////////
        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent",text="Lancer Publication" ,border_width=2, command=self.submit, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        # //////////////////////////////////////
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # //////////////////////////////////////
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Option de Publication:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="Alerte sonore      ",command=self.sonoreon, variable=self.radio_var, value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="Aucune alerte     ",command=self.sonoreoff, variable=self.radio_var, value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")
        # //////////////////////////////////////
        self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame,text="Fin à 21h             ",command=self.fin,)
        self.checkbox_1.select()
        self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
        # //////////////////////////////////////
        self.radio_button_3.configure(state="disabled", text="En Arrière-Plan   ")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.textbox.insert("0.0", "HellBot\n\n" + "Le bot est en version 1.0.0, \n\n" + f"Après {para.coffee} cafés et {para.bear} bières bu, le HellBot vit le jour, il permet de mettre en ligne des articles sur Vinted automatique, permet de lire automatiquement les messages, de laisser des appréciations après chaque vente \n\n" + "Utilisation :\n\n"+ "- Lancer Chrome\n- Rentrer le nombre de secondes entre chaque publication\n- Lancer le programme\n- Une fois terminé, lancer la mise à jour de la BDD")
        App.focus_force(self)


    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_update(self):
        print("Update de la BDD")
        articleIdOnvinted.updatebdd()

    def sidebar_button_launch(self):
        try:
            print("Ouverture du Browser")
            startchrome.startchrome()
        except:
            print("marche pas ton truc")

    def startpublish(self,timer):
        App.Vtimer = timer
        print("Debut de publication")
        iziflux.izifluxscrap(App.Vtimer)

    def timer(self):
        print("")

    def submit(self):
        App.Vtimer = self.entry.get()
        print("Debut de publication")
        print("Timer : ", App.Vtimer)
        iziflux.izifluxscrap(App.Vtimer)

    def sonoreon(self):
        print("Sonore")
        App.Vson = True
        print(App.Vson)
    def sonoreoff(self):
        print("Sonore")
        App.Vson = False
        print(App.Vson)

    def fin(self):
        App.Vfin = not App.Vfin
        print(App.Vfin)

    def avis(self):
        print("Lancement Auto Avis")
        autoavis.autoavis()


if __name__ == "__main__":
    app = App()
    app.mainloop()