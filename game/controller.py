import tkinter as tk
from PIL import Image, ImageTk
from game import model
from game import view


class Controller():
    def __init__(self):     
        self.modele = model.Modele(600,600)
        self.vue = view.Vue(self, self.modele.largeur, self.modele.hauteur)
        self.running = True
        self.loop_jeu()
        
    def loop_jeu(self):
        if self.running:
            # Mettre à jour la logique du jeu
            self.modele.update()      
            # Actualiser l'affichage
            self.vue.update_view()
            self.vue.root.after(16, self.loop_jeu) # 16 pour 60 fps
    
    def stop(self):
        self.running = False


