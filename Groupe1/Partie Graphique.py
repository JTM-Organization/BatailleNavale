from tkinter import *

global largeur
global hauteur
largeur = hauteur = 300
global nombre_de_carres
nombre_de_carres = 10
global taille_de_carres
taille_de_carres = hauteur//nombre_de_carres
global grille
grille = [[0 for colonne in range(nombre_de_carres)] for ligne in range(nombre_de_carres)]
print(grille)




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
    
    
root = Tk()
cnv = Canvas(root, width = largeur, height = hauteur)
cnv.pack()

cnv.bind("<Button-1>", clic)

def remplir_canvas():
    for i in range(nombre_de_carres):
        for j in range(nombre_de_carres):
            x, y = taille_de_carres * j, taille_de_carres * i
            A, B = (x, y), (x + taille_de_carres, y + taille_de_carres)
            rect=cnv.create_rectangle(A, B, fill = "#097ade")

remplir_canvas()
root.mainloop()
