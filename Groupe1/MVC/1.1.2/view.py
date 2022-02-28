#placer ici la gestion de l'interface graphique
from model import *

#Réalisation des tirs (alliés et ennemis) :
def clic_plateau1(event):
    global tour
    print("tour=",tour)
    if tour == 1:
        i = event.y//taille_de_carres
        j = event.x//taille_de_carres
        if grille1[i][j] == 0:
            tour = 2
            grille1[i][j] = 1
            plateau1.itemconfigure(i * 10 + j + 1, fill="#80ff00")
            print(grille1)
            print("Ligne=", i + 1, "Colonne=", j + 1)
            label1['text'] = "Tour de l'adversaire"
            label1['bg'] = "red"
        else:
            print("Veuillez sélectionner une autre case")
        test_victoire()
    else:
        print("Ce n'est pas votre tour")
    
def clic_plateau2(event):
    global tour
    print("tour=",tour)
    if tour == 2:
        i = event.y//taille_de_carres
        j = event.x//taille_de_carres
        if grille2[i][j] == 0:
            tour = 1
            grille2[i][j] = 1
            plateau2.itemconfigure(i * 10 + j + 1, fill="#80ff00")
            print(grille2)
            print("Ligne=", i + 1, "Colonne=", j + 1)
            label1['text'] = "votre tour"
            label1['bg'] = "green"
        else:
            print("Veuillez sélectionner une autre case")
        test_victoire()
    else:
        print("Ce n'est pas votre tour")
        
plateau1.bind("<Button-1>", clic_plateau1)
plateau2.bind("<Button-1>", clic_plateau2)

#Mise en place des bateaux :
def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

def spiderman_do_a_flip(event):
    widget = event.widget
    width = widget.winfo_width()
    height = widget.winfo_height()
    widget.configure(width=height, height=width)

def identify(event):
    widget = event.widget
    x = widget.winfo_x()
    y = widget.winfo_y()
    new_x = x//taille_de_carres*taille_de_carres + 10%taille_de_carres + 5
    new_y = y//taille_de_carres*taille_de_carres + 100%taille_de_carres + 5
    if 10 < new_x < dimension + 10 and 100 < new_y < dimension + 100:
        widget.place(x=new_x-2, y=new_y-2)
    print(x,y)

def bateaux():
    canvas1.bind("<Button-1>",drag_start)
    canvas1.bind("<Button-3>",spiderman_do_a_flip)
    canvas1.bind("<B1-Motion>",drag_motion)
    canvas1.bind("<ButtonRelease-1>",identify)

    canvas2.bind("<Button-1>",drag_start)
    canvas2.bind("<Button-3>",spiderman_do_a_flip)
    canvas2.bind("<B1-Motion>",drag_motion)
    canvas2.bind("<ButtonRelease-1>",identify)

    canvas3.bind("<Button-1>",drag_start)
    canvas3.bind("<Button-3>",spiderman_do_a_flip)
    canvas3.bind("<B1-Motion>",drag_motion)
    canvas3.bind("<ButtonRelease-1>",identify)

    canvas4.bind("<Button-1>",drag_start)
    canvas4.bind("<Button-3>",spiderman_do_a_flip)
    canvas4.bind("<B1-Motion>",drag_motion)
    canvas4.bind("<ButtonRelease-1>",identify)

    canvas5.bind("<Button-1>",drag_start)
    canvas5.bind("<Button-3>",spiderman_do_a_flip)
    canvas5.bind("<B1-Motion>",drag_motion)
    canvas5.bind("<ButtonRelease-1>",identify)

#Création des cases :
def remplir_plateau1():
    for i in range(nombre_de_carres):
        for j in range(nombre_de_carres):
            x, y = taille_de_carres * j + 2, taille_de_carres * i + 2
            A, B = (x, y), (x + taille_de_carres, y + taille_de_carres)
            carre1=plateau1.create_rectangle(A, B, fill = "#097ade")
    
def remplir_plateau2():
    for i in range(nombre_de_carres):
        for j in range(nombre_de_carres):
            x, y = taille_de_carres * j + 2 , taille_de_carres * i + 2
            A, B = (x, y), (x + taille_de_carres, y + taille_de_carres)
            carre2=plateau2.create_rectangle(A, B, fill = "#097ade")

#Créations des boutons et des zones de texte :            
def placer_boutons():
    global bouton1
    bouton1 = Button(root, text="Rejouer", command=recommencer, state=DISABLED)
    bouton1.place(x = 750, y = 2)
    global bouton2
    bouton2 = Button(root, text="Quitter", command=abandon_de_partie)
    bouton2.place(x = 751, y = 32)
    
def placer_label():
    global label1
    label1 = Label(root, text="Votre tour", bg = "green")
    label1.place(x = 746, y = 62)
    global label_victoire
    label_victoire = Label(root, text="")
    label_victoire.place(x = 750, y = 92)
    
#Impossible de déplacer cette fonction dans le model!
#En effet, bouton n'y est pas défini
def test_victoire():
    vainqueur = victoire()
    if (vainqueur == 0):
        fin_de_partie()
        bouton1['state'] = NORMAL
        label_victoire['text'] = "VICTOIRE"
        
#Pareil ici!
def recommencer():
    for i in range(nombre_de_carres):
        for j in range(nombre_de_carres):
            if grille1[i][j]!=0:
                plateau1.itemconfigure(i * 10 + j + 1, fill="#097ade")
            if grille2[i][j]!=0:
                plateau2.itemconfigure(i * 10 + j + 1, fill="#097ade")
    reInitialisation()
    bouton1['state'] = DISABLED
    label1['text'] = "Votre tour"
    label1['bg'] = "green"
    global tour
    tour = 1
            
def affichage():
    global main
    remplir_plateau1()
    remplir_plateau2()
    placer_boutons()
    placer_label()
    bateaux()
