from tkinter import *
import tkinter as tk

class Vue(): #Ou on dessine
    def __init__(self, controleur, modele):
        self.controleur = controleur
        self.modele = modele
        self.root = tk.Tk()
        self.root.title("Mon premier TD")
        self.creer_fenetre()
        self.dessine_statique()
    def afficher_jeu(self):
        creep = self.modele.creep
        self.tableau_jeu.delete("creep")
        self.tableau_jeu.create_oval(creep.x - creep.taille,
                                     creep.y - creep.taille,
                                     creep.x + creep.taille,
                                     creep.y + creep.taille,
                                     fill = "green",
                                     tags=("creep"))


    def dessine_statique(self):
        for i,j in self.modele.chemin.items():
            self.tableau_jeu.create_line(j[0],j[1],width=7)

    def creer_fenetre(self):
        self.menu_jeu = tk.Canvas(self.root, width=800, height=100, bg="pink")
        self.tableau_jeu = tk.Canvas(self.root, width=800, height=600, bg="red")
        self.menu_jeu.pack()
        self.tableau_jeu.pack()
        btn = tk.Button(self.menu_jeu, text="GO")
        btn.bind("<Button>",self.demarre_jeu)
        self.menu_jeu.create_window(400,60,anchor="center", window=btn)
        
    def demarre_jeu(self,evt):
        self.controleur.demarre_jeu()


class Modele():
    def __init__(self,controleur):
        self.controleur = controleur
        self.chemin = {0:[[0,100],[300,100]],
                       1:[[300,100],[300,500]],
                       2:[[300,500],[800,500]]}
        self.creep = Creep(self.chemin)

    def bouger(self):
        self.creep.bouger()

class Creep():
    def __init__(self, chemin):
        self.chemin = chemin
        self.x = 0
        self.y = 100
        self.taille = 10
        self.vitesse = 5
        self.no_troncon_courant = -1
        self.orientation = None

    def bouger(self):

        
        if self.no_troncon_courant != -1:
            if self.orientation == "horizontale":
                tronconx = self.chemin[self.no_troncon_courant]
                self.x += self.vitesse
                if self.x > tronconx[0]: #A faire
                    self.orientation = "verticale"
                    self.no_troncon_courant += 1
                
            elif self.orientation == "verticale":
                troncony = self.chemin[self.no_troncon_courant]
                self.y += self.vitesse
                if self.y > self.chemin[self.no_troncon_courant:[0][0]]: #A faire
                    self.orientation = "horizontale"
                    self.no_troncon_courant += 1
        else:
            self.no_troncon_courant += 1
            self.troncon_courant = self.chemin[self.no_troncon_courant]
            self.orientation = "horizontale"


class Controleur():
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self, self.modele)
        self.vue.root.mainloop()

    def demarre_jeu(self):
        self.modele.bouger()
        self.vue.afficher_jeu()
        self.vue.root.after(100,self.demarre_jeu)

if __name__ == "__main__":
    c = Controleur()
