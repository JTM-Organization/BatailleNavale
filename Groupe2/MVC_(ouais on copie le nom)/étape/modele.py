from sys import flags
from tkinter import *
from tkinter import ttk
import random
from tkinter import colorchooser

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

#liste pour les boutons du joueur 
global L1
L1=[[]for i in range(100)]

global lettre
lettre="ABCDEFGHIJ"

global debut
debut=False

global rect0,rect1,rect2,rect3,rect4

global listeBateau
listeBateau=[]

global compteurBateau
compteurBateau=[]

global tailleBateau
tailleBateau=[5,4,3,3,2]

global bateau
bateau=0

global horizOuVertical
horizOuVertical=[0,0,0,0,0]

global listeCouleurBoard
listeCouleurBoard=["royal blue","limegreen","grey","red"]

#couleur joueur
global M1
M1=[[0 for i in range(10)] for j in range(10)]

#couleur adversaire
global M2
M2=[[0 for i in range(10)] for j in range(10)]

global pasBouger
pasBouger=False

global victoireBot, victoireJoueur
victoireBot=17
victoireJoueur=17

global testVictoire
testVictoire=False
