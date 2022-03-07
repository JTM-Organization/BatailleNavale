#placer ici la partie gestion de donnees
from tkinter import *
from PIL import ImageTk, Image

global main
global var
var = 60
global dimension
dimension = var * 10 + 1

global nombre_de_carres
nombre_de_carres = 10

global taille_de_carres
taille_de_carres = dimension//nombre_de_carres

global dep_x
dep_x = 200

global dep_y
dep_y = 160

global grille
grille1 = [[0 for colonne in range(nombre_de_carres)] for ligne in range(nombre_de_carres)]
grille2 = [[0 for colonne in range(nombre_de_carres)] for ligne in range(nombre_de_carres)]

global score
score = 0

global vainqueur
vainqueur = 1

global tour
tour = 1

root = Tk()
root.geometry("1700x1700") #la fenêtre garde cette taille en la déplacant
root.title("Bataille Navale")
root.state('zoomed')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

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
