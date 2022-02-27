#placer ici la gestion de l'interface graphique
from model import *

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
    test_victoire()
        
cnv.bind("<Button-1>", clic)

def remplir_canvas():
    for i in range(nombre_de_carres):
        for j in range(nombre_de_carres):
            x, y = taille_de_carres * j, taille_de_carres * i
            A, B = (x, y), (x + taille_de_carres, y + taille_de_carres)
            rect=cnv.create_rectangle(A, B, fill = "#097ade")
    global bouton1
    bouton1 = Button(root, text="Rejouer", command=recommencer, state=DISABLED)
    bouton1.pack()
    global bouton2
    bouton2 = Button(root, text="J'abandonne", command=abandon_de_partie)
    bouton2.pack()
    
#Impossible de déplacer cette fonction dans le model!
#En effet, bouton n'y est pas défini
def test_victoire():
    vainqueur = victoire()
    if (vainqueur == 0):
        fin_de_partie()
        bouton1['state'] = NORMAL
        
def recommencer():
    for i in range(nombre_de_carres):
        for j in range(nombre_de_carres):
            if grille[i][j]!=0:
                cnv.itemconfigure(i * 10 + j + 1, fill="#097ade")
    reInitialisation()
    bouton1['state'] = DISABLED
            
def affichage():
    global main
    remplir_canvas()
