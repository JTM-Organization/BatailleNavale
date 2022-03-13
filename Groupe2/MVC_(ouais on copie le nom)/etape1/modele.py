from tkinter import *
from tkinter import ttk
from ihm import *


root=Tk()
root.title('Bataille Navale')
root.attributes('-fullscreen',True)

nb = ttk.Notebook(root)
nb.pack()

#enlever l'accès au notebook
style=ttk.Style()
style.layout("TNotebook.Tab", [])

global largeur
largeur= root.winfo_screenwidth()

global hauteur
hauteur = root.winfo_screenheight()

global taille
taille=int(min(largeur,hauteur)/14)

global listeCouleur
listeCouleur=["royal blue","yellow"]

#matrice d'état des boutons du joueur
global matriceC1
matriceC1=[[0 for i in range(10)]for j in range(10)]

#liste pour les boutons du joueur 
global L1
L1=[[]for i in range(100)]
