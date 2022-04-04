# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
import random
from tkinter import colorchooser
import PIL
from PIL import Image,ImageTk
from playsound import playsound

root=Tk()
root.title('Bataille Navale')
#on met le jeu en plein écran
root.attributes('-fullscreen',True)
#initialisation du notebook. Il permet d'avoir plusieurs fenêtres et de naviguer entre elles.
nb = ttk.Notebook(root)
nb.pack()

#enlever l'accès au notebook
style=ttk.Style()
style.layout("TNotebook.Tab", [])

#taille d'un carré
global taille

#largeur des canvas
global largeur

#hauteur des canvas
global hauteur

#on définit la taille des carrés à partir de la taille de l'écran. Si l'écran n'a pas les dimensions requises on prend une taille de canvas et une taille de carré par défaut.
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

#liste des couleurs du plateau de l'ordinateur. 
#Dans l'ordre: couleur par défaut, couleur de l'eau une fois touchée, couleur des cases de bateau une fois touchées.
global listeCouleur
listeCouleur=["royal blue","red","grey"]

#liste des couleurs du plateau du joueur. 
#Dans l'ordre: couleur de l'eau, couleur des cases de bateau, couleur de l'eau une fois touchée, couleur des cases de bateau une fois touchées.
global listeCouleurBoard
listeCouleurBoard=["royal blue","limegreen","grey","red"]

#liste des boutons du plateau de l'adversaire sur lesquels on clique pour tirer.
global L1
L1=[[]for i in range(100)]

#sert à afficher les lettres sur le côté des plateaux et à indiquer quelle case a été touchée.
global lettre
lettre="ABCDEFGHIJ"

#variable permettant de vérifier si le placement a déjà été fait. Si ce n'est pas le cas appuyer sur le bouton start enverra le joueur sur le plateau de placement des bateaux.
global debut
debut=False

#liste comprenant les bateaux pendant le placement. Elle permet de les manipuler pendant des boucles à partir de leur indice.
global listeBateau
listeBateau=[]

#liste avec les bateaux présents sur le plateau pendant le placement. Si elle a 5 éléments le jeu peut commencer.
global compteurBateau
compteurBateau=[]

#taille des bateaux pour faciliter le placement.
global tailleBateau
tailleBateau=[5,4,3,3,2]

#numero du bateau sur lequel on clique.
global bateau
bateau=0

#orientation des bateaux pendant le placement
global horizOuVertical
horizOuVertical=[0,0,0,0,0]

#Matrice d'état du plateau du joueur.
global M1
M1=[[0 for i in range(10)] for j in range(10)]

#Matrice d'état du plateau adverse.
global M2
M2=[[0 for i in range(10)] for j in range(10)]

#nombre de cases de bateau restantes par joueur.
global victoireBot, victoireJoueur
victoireBot=17
victoireJoueur=17

#si testVictoire est vraie le jeu s'arrête et l'écran de victoire s'affiche.
global testVictoire
testVictoire=False

#liste du nombre de cases de bateau restantes par bateau. En premier ceux du joueur et après ceux de l'ordinateur.
global listeCompteur
listeCompteur=[5,4,3,3,2,5,4,3,3,2]

#niveau de difficulté. Une variable de tir différente sera appelé en fonction de sa valeur.
global difficult
difficult=0

#booléen pour savoir quand arrêter le while quand on cherche à toucher un bateau à tous les coups.
global touche
touche=False

#compteur pour savoir où tirer. Il commence à 1 pour ne pas tirer directement sur un bateau en difficulté moyenne et difficile.
global compteurTir
compteurTir=1

#permet de savoir si on peut commencer la partie ou non à la sélection de la difficulté.
global selectDif
selectDif=False

global listeImageBateauH,liseImageBateauV
#liste des images horizontales pour le placement.
listeImageBateauH=[]
#liste des images verticales pour le placement.
listeImageBateauV=[]
