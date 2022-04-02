from tkinter import *
from tkinter import ttk
import random
from tkinter import colorchooser
import PIL
from PIL import Image,ImageTk

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

#ia
global listeCouleur
listeCouleur=["royal blue","red","grey"]

#joueur
global listeCouleurBoard
listeCouleurBoard=["royal blue","limegreen","grey","red"]

#liste pour les boutons du joueur pour taper le bot
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

global listeCompteur
listeCompteur=[5,4,3,3,2,5,4,3,3,2]

global difficult
difficult=0

global touche
touche=False

global compteurMoyen
compteurMoyen=0

global selectDif
selectDif=False
