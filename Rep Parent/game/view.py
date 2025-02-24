import tkinter as tk
from PIL import Image, ImageTk

class Vue():
    def __init__(self, controleur, largeur, hauteur, root):
        self.controleur = controleur
        self.root = root
        self.root.title("Trenches")
        self.creer_cadre_jeu(largeur, hauteur)

    def creer_cadre_jeu(self, largeur, hauteur):
        self.cadrePrincipal = tk.Frame(self.root, width=largeur, height=hauteur)
        self.cadrePrincipal.grid(column=0, row=0)
        self.canevas = tk.Canvas(self.cadrePrincipal, width=largeur, height=hauteur, bg="white")
        self.canevas.pack()

    def update_view(self):
        # Mettez ici le code de rafraîchissement de l'affichage du jeu.
        pass
