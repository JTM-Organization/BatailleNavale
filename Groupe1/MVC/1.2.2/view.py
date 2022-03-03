#placer ici la gestion de l'interface graphique
from tkinter import ANCHOR, CENTER, Canvas
from model import *
from random import *

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
            plateau1.itemconfigure(i * 10 + j + 1, fill="white")
            print(grille1)
            print("Ligne=", i + 1, "Colonne=", j + 1)
            label1['text'] = "Votre tour"
            label1['bg'] = "green"
        elif grille1[i][j] == 3:
            tour = 2
            grille1[i][j] = 2
            plateau1.itemconfigure(i * 10 + j + 1, fill="red")
            print(grille1)
            print("Ligne=", i + 1, "Colonne=", j + 1)
            label1['text'] = "Votre tour"
            label1['bg'] = "green"
        else:
            print("Veuillez sélectionner une autre case")
        test_victoire()
    else:
        print("Ce n'est pas votre tour")
    
def clic_plateau2(event):
    global tour
    if tour == 2:
        i = event.y//taille_de_carres
        j = event.x//taille_de_carres
        if grille2[i][j] == 0:
            tour = 1
            grille2[i][j] = 1
            plateau2.itemconfigure(i * 10 + j + 1, fill="white")
            label1['text'] = "Tour de l'adversaire"
            label1['bg'] = "red"
        else:
            print("Veuillez sélectionner une autre case")
        test_victoire()
    else:
        print("Ce n'est pas votre tour")

def tirs_facile():
    global tour
    if tour == 1 :
        i = randint(0,9)
        j = randint(0,9)
        while grille1[i][j] == 1 or grille1[i][j] == 2:
            i = randint(0,9)
            j = randint(0,9)

        if grille1[i][j] == 0:
            tour = 2
            grille1[i][j] = 1
            plateau1.itemconfigure(i * 10 + j + 1, fill="white")
            print("Ligne=", i + 1, "Colonne=", j + 1)
            label1['text'] = "Votre tour"
            label1['bg'] = "green"
        elif grille1[i][j] == 3:
            tour = 2
            grille1[i][j] = 2
            plateau1.itemconfigure(i * 10 + j + 1, fill="red")
            print("Ligne=", i + 1, "Colonne=", j + 1)
            label1['text'] = "Votre tour"
            label1['bg'] = "green"
        test_victoire()

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
    x = widget.winfo_x()
    y = widget.winfo_y()
    width = widget.winfo_width()
    height = widget.winfo_height()
    if (x + height <= 620) and (y + width <= 710) :
        widget.configure(width=height, height=width)

def identify(event):
    widget = event.widget
    x = widget.winfo_x()
    y = widget.winfo_y()
    largeur = widget.winfo_width()
    hauteur = widget.winfo_height()
    new_x = x//taille_de_carres*taille_de_carres + dep_x%taille_de_carres + 3
    new_y = y//taille_de_carres*taille_de_carres + dep_y%taille_de_carres + 3
    if dep_x < new_x < dimension + dep_x and dep_y < new_y < dimension + dep_y and x + largeur - taille_de_carres//2 < dimension + dep_x and y + hauteur - taille_de_carres//2 < dimension + dep_y:
        widget.place(x=new_x, y=new_y)
    else: 
        widget.place(x=630, y=122)

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
    bouton1.place(relx = 0.5, rely = 0.02, anchor='center')
    global bouton2
    bouton2 = Button(root, text="Quitter", command=abandon_de_partie)
    bouton2.place(relx = 0.5, rely = 0.055, anchor='center')
    global bouton3
    bouton3 = Button(root, text="Confirmer", command=confirmer_placement)
    bouton3.place(relx = 0.5, rely = 0.75, anchor='center')
    global bouton4
    bouton4 = Button(root, text="Ordi", command=tirs_facile)
    bouton4.place(x = 295, y = 50)
    
def placer_label():
    global label1
    label1 = Label(root, text="Votre tour", bg = "green")
    label1.place(relx = 0.5, rely = 0.09, anchor='center')
    global label_victoire
    label_victoire = Label(root, text="")
    label_victoire.place(relx = 0.5, rely = 0.12, anchor='center')
    global label_scoreboard
    label_scoreboard = Label(root, text="SCORE:" + str(score))
    label_scoreboard.place(x = 0, y = 0)
    
#Impossible de déplacer cette fonction dans le model!
#En effet, bouton n'y est pas défini
def test_victoire():
    global score
    score = 0
    vainqueur = victoire()
    if (vainqueur == 0):
        fin_de_partie()
        bouton1['state'] = NORMAL
        label_victoire['text'] = "VICTOIRE"
        score = score + 1
        label_scoreboard.config(text="SCORE:" + str(score))
        
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
    label_victoire['text']=""
    global tour
    tour = 1

def test_placement():
    compteur = 0
    for i in range(nombre_de_carres):
        for j in range(nombre_de_carres):
            if grille1[i][j] == 3:
                compteur += 1

    if (compteur != 17):
        recommencer()
        canvas1.place(x=630, y=320)
        canvas2.place(x=630, y=122)
        canvas3.place(x=700, y=122)
        canvas4.place(x=770, y=122)
        canvas5.place(x=840, y=122)
    elif (compteur == 17):
        plateau2.bind("<Button-1>", clic_plateau2)
        canvas1.place(x=1800, y=1800)
        canvas2.place(x=1800, y=1800)
        canvas3.place(x=1800, y=1800)
        canvas4.place(x=1800, y=1800)
        canvas5.place(x=1800, y=1800)
        bouton3.destroy()

def confirmer_placement():
    x1 = (canvas1.winfo_y() - dep_y)//taille_de_carres
    y1 = (canvas1.winfo_x() - dep_x)//taille_de_carres
    width1 = canvas1.winfo_width()
    height1 = canvas1.winfo_height()
    x2 = (canvas2.winfo_y() - dep_y)//taille_de_carres
    y2 = (canvas2.winfo_x() - dep_x)//taille_de_carres
    width2 = canvas2.winfo_width()
    height2 = canvas2.winfo_height()
    x3 = (canvas3.winfo_y() - dep_y)//taille_de_carres
    y3 = (canvas3.winfo_x() - dep_x)//taille_de_carres
    width3 = canvas3.winfo_width()
    height3 = canvas3.winfo_height()
    x4 = (canvas4.winfo_y() - dep_y)//taille_de_carres
    y4 = (canvas4.winfo_x() - dep_x)//taille_de_carres
    width4 = canvas4.winfo_width()
    height4 = canvas4.winfo_height()
    x5 = (canvas5.winfo_y() - dep_y)//taille_de_carres
    y5 = (canvas5.winfo_x() - dep_x)//taille_de_carres
    width5 = canvas5.winfo_width()
    height5 = canvas5.winfo_height()

    if (x1 and y1 <= 9):
        if (width1 > height1):
            for i in range(width1//height1):
                grille1[x1][y1+i] = 3
                plateau1.itemconfigure(x1 * 10 + y1+i + 1, fill="gray")
        elif (width1 < height1):
            for i in range(height1//width1):
                grille1[x1+i][y1] = 3
                plateau1.itemconfigure((x1+i) * 10 + y1 + 1, fill="gray")

    if (x2 and y2 <= 9):
        if (width2 > height2):
            for i in range(width2//height2):
                grille1[x2][y2+i] = 3
                plateau1.itemconfigure(x2 * 10 + y2+i + 1, fill="gray")
        elif (width2 < height2):
            for i in range(height2//width2):
                grille1[x2+i][y2] = 3
                plateau1.itemconfigure((x2+i) * 10 + y2 + 1, fill="gray")
    
    if (x3 and y3 <= 9):
        if (width3 > height3):
            for i in range(width3//height3):
                grille1[x3][y3+i] = 3
                plateau1.itemconfigure(x3 * 10 + y3+i + 1, fill="gray")
        elif (width3 < height3):
            for i in range(height3//width3):
                grille1[x3+i][y3] = 3
                plateau1.itemconfigure((x3+i) * 10 + y3 + 1, fill="gray")
    
    if (x4 and y4 <= 9):
        if (width4 > height4):
            for i in range(width4//height4):
                grille1[x4][y4+i] = 3
                plateau1.itemconfigure(x4 * 10 + y4+i + 1, fill="gray")
        elif (width4 < height4):
            for i in range(height4//width4):
                grille1[x4+i][y4] = 3
                plateau1.itemconfigure((x4+i) * 10 + y4 + 1, fill="gray")

    if (x5 and y5 <= 9):
        if (width5 > height5):
            for i in range(width5//height5):
                grille1[x5][y5+i] = 3
                plateau1.itemconfigure(x5 * 10 + y5+i + 1, fill="gray")
        elif (width5 < height5):
            for i in range(height5//width5):
                grille1[x5+i][y5] = 3
                plateau1.itemconfigure((x5+i) * 10 + y5 + 1, fill="gray")

    test_placement()

def affichage():
    global main
    remplir_plateau1()
    remplir_plateau2()
    placer_boutons()
    placer_label()
    bateaux()
