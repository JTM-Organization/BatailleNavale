from tkinter import *
from tkinter import ttk

#Optimiser le design, gérer les variables de fenêtres...

root=Tk()
root.title('Bataille Navale')
root.geometry("1000x1000")
root.minsize(500,500)

nb = ttk.Notebook(root)
nb.pack()

def select_jouer():
    nb.select(1)
    nb.hide(0)
    nb.hide(2)

def select_réglages():
    nb.select(3)
    nb.hide(0)
    
def select_plateau2():
    nb.select(2)
    nb.hide(1)
    
def select_retour():
    nb.select(0)
    nb.hide(1)
    nb.hide(2)
    nb.hide(3)
    
Base = Frame(nb, width=1000, height=1000, bg="black")
Jeu = Frame(nb, width=1000, height=1000)
Jeu2 = Frame(nb, width=1000, height=1000)
Réglages = Frame(nb, width=1000, height=1000)
Base.pack()
Jeu.pack()
Jeu2.pack()
Réglages.pack()

nb.add(Base)
nb.add(Jeu)
nb.add(Jeu2)
nb.add(Réglages)

Jouer = Button(Base, text="Jouer", command=select_jouer)
Options = Button(Base, text="Options", command=select_réglages)
Quitter = Button(Base, text="Quitter", command=root.quit)
Jouer.pack()
Options.pack()
Quitter.pack()

Plateau1 = Button(Jeu2, text="Retourner sur votre plateau", command=select_jouer)
Plateau2 = Button(Jeu, text="Observer le plateau de l'adversaire", command=select_plateau2)
Retour1 = Button(Jeu, text="Retour", command=select_retour)
Retour2 = Button(Jeu2, text="Retour", command=select_retour)
Retour3 = Button(Réglages, text="Retour", command=select_retour)
Plateau1.pack()
Plateau2.pack()
Retour1.pack()
Retour2.pack()
Retour3.pack()

nb.hide(1)
nb.hide(2)
nb.hide(3)



global largeur
global hauteur
largeur = hauteur = 300
global nombre_de_carres
nombre_de_carres = 10
global taille_de_carres
taille_de_carres = hauteur//nombre_de_carres
global grille
grille = [[0 for colonne in range(nombre_de_carres)] for ligne in range(nombre_de_carres)]
grille2 = [[0 for colonne in range(nombre_de_carres)] for ligne in range(nombre_de_carres)]




def clic(event):
    i = event.y//taille_de_carres
    j = event.x//taille_de_carres
    if grille[i][j] == 0:
        grille[i][j] = 1
        cnv.itemconfigure(i * 10 + j + 1, fill="#80ff00")
        print(grille)
        print("Ligne=", i + 1, "Colonne=", j + 1)
    else:
        print("Veuillez sélectionner une autre case")
        
def click(event):
    i = event.y//taille_de_carres
    j = event.x//taille_de_carres
    if grille2[i][j] == 0:
        grille2[i][j] = 1
        cnv2.itemconfigure(i * 10 + j + 1, fill="#80ff00")
        print(grille2)
        print("Ligne=", i + 1, "Colonne=", j + 1)
    else:
        print("Veuillez sélectionner une autre case")
    
    
cnv = Canvas(Jeu, width = largeur, height = hauteur)
cnv2 = Canvas(Jeu2, width = largeur, height = hauteur)
cnv.pack()
cnv2.pack()

cnv.bind("<Button-1>", clic)
cnv2.bind("<Button-1>", click)

for i in range(nombre_de_carres):
    for j in range(nombre_de_carres):
        x, y = taille_de_carres * j, taille_de_carres * i
        A, B = (x, y), (x + taille_de_carres, y + taille_de_carres)
        rect=cnv.create_rectangle(A, B, fill = "#097ade")
        rect=cnv2.create_rectangle(A, B, fill = "#097ade")
        

root.mainloop()
