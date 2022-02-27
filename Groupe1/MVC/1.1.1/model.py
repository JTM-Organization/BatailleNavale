#placer ici la partie gestion de donnees
from tkinter import *

global main
global dimension
dimension = 600
global nombre_de_carres
nombre_de_carres = 10
global taille_de_carres
taille_de_carres = dimension//nombre_de_carres
global grille
grille1 = [[0 for colonne in range(nombre_de_carres)] for ligne in range(nombre_de_carres)]
grille2 = [[0 for colonne in range(nombre_de_carres)] for ligne in range(nombre_de_carres)]
global vainqueur 
vainqueur = 1
global tour
tour = 1

global plateau1
global plateau2
root = Tk()
root.geometry("1700x1700")
plateau1 = Canvas(root, width = dimension, height = dimension)
plateau1.pack(side = LEFT)
plateau2 = Canvas(root, width = dimension, height = dimension)
plateau2.pack(side = RIGHT)

def reInitialisation():
    for i in range(nombre_de_carres):
        for j in range(nombre_de_carres):
            grille1[i][j] = 0
            grille2[i][j] = 0
    global vainqueur 
    vainqueur = 1
            
def abandon_de_partie():
    root.quit()

def victoire():
    global vainqueur
    if grille1[0][0]==1:
        vainqueur = 0
    return vainqueur

def fin_de_partie():
    for i in range(nombre_de_carres):
        for j in range(nombre_de_carres):
            grille1[i][j] = 1
            grille2[i][j] = 1
