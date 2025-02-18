import tkinter as tk
from PIL import Image, ImageTk
import modele
import vue


class Controleur():
    def __init__(self):     
        self.modele = modele.Modele(600,600)
        self.vue = vue.Vue(self, self.modele.largeur, self.modele.hauteur)
        self.loop_jeu()
        
    def loop_jeu(self):
        self.vue.root.after(16, self.loop_jeu) # 16 pour 60 fps
    
if __name__ == "__main__":
    c = Controleur()
    c.vue.root.mainloop()