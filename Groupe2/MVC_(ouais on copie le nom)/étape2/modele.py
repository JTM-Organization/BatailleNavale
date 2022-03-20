from cmath import rect
from tkinter import *
from tkinter import ttk
import random


root=Tk()
root.title('Bataille Navale')
root.attributes('-fullscreen',True)
nb = ttk.Notebook(root)
nb.pack()

#enlever l'accès au notebook
style=ttk.Style()
style.layout("TNotebook.Tab", [])

global taille

global largeur

global hauteur

global x,y
x=screen_width = root.winfo_screenwidth()
y=screen_height = root.winfo_screenheight()
if x/30*13<y:
    taille=x/30
    largeur= x
    hauteur = y
else:
    largeur=900
    hauteur=500
    taille=40

global listeCouleur
listeCouleur=["royal blue","red","grey"]

#matrice d'état des boutons du joueur
global matriceC1
matriceC1=[[0 for i in range(10)]for j in range(10)]

#liste pour les boutons du joueur 
global L1
L1=[[]for i in range(100)]

global lettre
lettre="ABCDEFGHIJ"

global debut
debut=False

global rect


global currentLengthShip
currentLengthShip=5

global compteur
compteur=0

global tailleBateau
tailleBateau=[5,4,3,3,2]

global hOuV
hOuV=0

global listeCouleurBoard
listeCouleurBoard=["royal blue","limegreen"]

global M1
M1=[[0 for i in range(10)] for j in range(10)]

global M2
M2=[[0 for i in range(10)] for j in range(10)]

global pasBouger
pasBouger=False
