import tkinter as tk

def afficher_selection():
    choix = option_var.get()
    print(f"Tu as sélectionné : {choix}")

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Menu déroulant avec Tkinter")

# Créer une variable de type StringVar() pour l'OptionMenu
option_var = tk.StringVar(fenetre)
option_var.set("Choisis une option")  # Valeur par défaut

# Liste des options du menu déroulant
options = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Créer le menu déroulant
menu_deroulant = tk.OptionMenu(fenetre, option_var, *options)
menu_deroulant.pack(pady=20)

# Ajouter un bouton pour afficher la sélection
btn_afficher = tk.Button(fenetre, text="Afficher la sélection", command=afficher_selection)
btn_afficher.pack(pady=10)

# Lancer la boucle principale de l'application
fenetre.mainloop()
