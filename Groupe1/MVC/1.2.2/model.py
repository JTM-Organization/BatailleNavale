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
dep_x = 10

global dep_y
dep_y = 100

global grille
grille1 = [[0 for colonne in range(nombre_de_carres)] for ligne in range(nombre_de_carres)]
grille2 = [[0 for colonne in range(nombre_de_carres)] for ligne in range(nombre_de_carres)]

global compteur
compteur = 0

global score
score = 0  

global vainqueur 
vainqueur = 1

global tour
tour = 2

global plateau1
global plateau2
root = Tk()
root.geometry("1700x1700")
root.title("Bataille Navale")
plateau1 = Canvas(root, width = dimension, height = dimension)
plateau1.place(x=dep_x, y=dep_y)
plateau2 = Canvas(root, width = dimension, height = dimension)
plateau2.place(x=920, y=100)

global canvas1
global canvas2
global canvas3
global canvas4
global canvas5
canvas1 = Canvas(root, bg="gray", width=taille_de_carres*2-1, height=taille_de_carres-1, bd=0, highlightthickness=0)
canvas1.place(x=630, y=320)
canvas2 = Canvas(root, bg="green", width=taille_de_carres-1, height=taille_de_carres*3-1, bd=0, highlightthickness=0)
canvas2.place(x=630, y=122)
canvas3 = Canvas(root, bg="yellow", width=taille_de_carres-1, height=taille_de_carres*3-1, bd=0, highlightthickness=0)
canvas3.place(x=700, y=122)
canvas4 = Canvas(root, bg="purple", width=taille_de_carres-1, height=taille_de_carres*4-1, bd=0, highlightthickness=0)
canvas4.place(x=770, y=122)
canvas5 = Canvas(root, bg="orange", width=taille_de_carres-1, height=taille_de_carres*5-1, bd=0, highlightthickness=0)
canvas5.place(x=840, y=122)

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
    global compteur
    compteur = 0
    for i in range(nombre_de_carres):
        for j in range(nombre_de_carres):
            if grille1[i][j] == 2:
                compteur += 1
    if compteur == 17:
        vainqueur = 0
    return vainqueur

def fin_de_partie():
    for i in range(nombre_de_carres):
        for j in range(nombre_de_carres):
            grille1[i][j] = 1
            grille2[i][j] = 1
            
