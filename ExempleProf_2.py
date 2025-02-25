from tkinter import *
import tkinter as tk

class Vue():
    def __init__(self, parent, modele):
        self.controleur = parent
        self.modele = modele
        self.root = tk.Tk()
        self.dico_cadre = {}
        self.cadre_actif = None
        self.definir_cadres()
        self.afficher_cadre("splash")

    def afficher_cadre(self, nom_du_cadre):
        if self.cadre_actif:
            self.cadre_actif.pack_forget()
        self.cadre_actif = self.dico_cadre[nom_du_cadre]
        self.cadre_actif.pack()

    def definir_cadres(self):

        cadre_jeu = Frame(self.root)
        self.canvas_jeu = Canvas(cadre_jeu, width=600, height= 400, bg='white')
        self.canvas_jeu.pack()
        cadre_menu = Frame(self.root)
        self.canvas_menu = Canvas(cadre_menu, width=600, height= 400, bg='green')
        self.canvas_menu.pack()
        cadre_splash = Frame(self.root)
        self.canvas_splash = Canvas(cadre_splash, width=600, height= 400, bg='red')
        self.canvas_splash.bind("<Button>", self.demarre_jeu)
        self.canvas_splash.pack()
        self.dico_cadre["jeu"] = cadre_jeu
        self.dico_cadre["menu"] = cadre_menu
        self.dico_cadre["splash"] = cadre_splash

    def demarre_jeu(self, evt):
        self.afficher_cadre("jeu")


class Modele():
    def __init__(self, parent):
        self.controleur = parent

class Controleur():
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self, self.modele)
        self.vue.root.mainloop()

if __name__ == "__main__":
    c = Controleur()
