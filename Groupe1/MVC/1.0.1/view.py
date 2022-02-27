#placer ici la gestion de l'interface graphique
from model import *

def clic_plateau1(event):
    i = event.y//taille_de_carres
    j = event.x//taille_de_carres
    if grille1[i][j] == 0:
        grille1[i][j] = 1
        plateau1.itemconfigure(i * 10 + j + 1, fill="#80ff00")
        print(grille1)
        print("Ligne=", i + 1, "Colonne=", j + 1)
    else:
        print("Veuillez sélectionner une autre case")
    test_victoire()
    
def clic_plateau2(event):
    i = event.y//taille_de_carres
    j = event.x//taille_de_carres
    if grille2[i][j] == 0:
        grille2[i][j] = 1
        plateau2.itemconfigure(i * 10 + j + 1, fill="#80ff00")
        print(grille2)
        print("Ligne=", i + 1, "Colonne=", j + 1)
    else:
        print("Veuillez sélectionner une autre case")
    test_victoire()
        
plateau1.bind("<Button-1>", clic_plateau1)
plateau2.bind("<Button-1>", clic_plateau2)

def remplir_plateau1():
    for i in range(nombre_de_carres):
        for j in range(nombre_de_carres):
            x, y = taille_de_carres * j, taille_de_carres * i
            A, B = (x, y), (x + taille_de_carres, y + taille_de_carres)
            carre1=plateau1.create_rectangle(A, B, fill = "#097ade")
    
def remplir_plateau2():
    for i in range(nombre_de_carres):
        for j in range(nombre_de_carres):
            x, y = taille_de_carres * j , taille_de_carres * i 
            A, B = (x, y), (x + taille_de_carres, y + taille_de_carres)
            carre2=plateau2.create_rectangle(A, B, fill = "#097ade")
            
def placer_boutons():
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
            if grille1[i][j]!=0:
                plateau1.itemconfigure(i * 10 + j + 1, fill="#097ade")
            if grille2[i][j]!=0:
                plateau2.itemconfigure(i * 10 + j + 1, fill="#097ade")
    reInitialisation()
    bouton1['state'] = DISABLED
            
def affichage():
    global main
    remplir_plateau1()
    remplir_plateau2()
    placer_boutons()
