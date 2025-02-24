import tkinter as tk
from PIL import Image, ImageTk
import model
import view

class Controller():
    def __init__(self, root):
        self.modele = model.Modele(600, 600)
        self.vue = view.Vue(self, self.modele.largeur, self.modele.hauteur, root)
        self.running = True
        self.loop_jeu()

    def loop_jeu(self):
        if self.running:
            # Mise à jour de la logique du jeu
            self.modele.update()
            # Actualisation de l'affichage
            self.vue.update_view()
            self.vue.root.after(16, self.loop_jeu)  # environ 60 FPS

    def stop(self):
        self.running = False
