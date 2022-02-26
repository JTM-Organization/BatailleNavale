#placer ici la partie gestion de donnees
from tkinter import *

global main
global largeur
global hauteur
largeur = hauteur = 300
global nombre_de_carres
nombre_de_carres = 10
global taille_de_carres
taille_de_carres = hauteur//nombre_de_carres
global grille
grille = [[0 for colonne in range(nombre_de_carres)] for ligne in range(nombre_de_carres)]

global cnv
root = Tk()
cnv = Canvas(root, width = largeur, height = hauteur)
cnv.pack()

def reInitialisation():
    for i in range(nombre_de_carres):
        for j in range(nombre_de_carres):
            grille[i][j] = 0
            
def abandon_de_partie():
    return 0

def victoire():
    return 0
