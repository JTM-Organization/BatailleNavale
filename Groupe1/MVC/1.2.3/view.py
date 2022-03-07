# placer ici la gestion de l'interface graphique
from model import *
from tkinter import ttk
import tkinter as tk
from tkinter import colorchooser
from PIL import *


# MENU DE SELECTION:

# Navigation dans les pages

def show_frame(frame):
    frame.tkraise() #enlever le tk?
    
    
# Navigation dans les pages terminé
# ----------------------------------------------------    
# Ci-dessous, les différentes pages au propre!

frame_principal = Frame(root, bg = "red") # fenêtre principal
frame_personnalisation = Frame(root, bg = "green") # fenêtre personnalisation
frame_placement = Frame(root, bg = "purple") # fenêtre de placement
frame_jeu = Frame(root, bg = "blue") # fenêtre de jeu
frame_reglages = Frame(root, bg = "orange") # fenêtre des reglages

for frame in (frame_principal, frame_personnalisation, frame_placement, frame_jeu, frame_reglages):
    frame.grid(row = 0, column = 0, sticky = "nsew") #sticky: gestion de l'espace occupé par un widget dans une cellule

show_frame(frame_principal)

# Différentes pages terminées
# ----------------------------------------------------
# Ci-dessous, les fonctions graphiques pour boutons au propre!

def survol_bordure_bouton(event):
    widget = event.widget
    widget.config(highlightbackground = "white",
                  highlightthickness = 3)
    

def fin_survol_bordure_bouton(event):
    widget = event.widget
    widget['highlightthickness'] = 0
    
    
def survol_bouton(event):
    widget = event.widget
    widget.config(font = ('Oswald', 31),
                  fg = "white")
    

def fin_survol_bouton(event):
    widget = event.widget
    widget.config(font = ('Oswald', 30),
                  fg = "#fbfbfb")
    
    
# Fonctions graphiques pour boutons terminées
# ----------------------------------------------------
# Ci-dessous, l'écran principal au propre!

def ecran_principal():
    global frame_principal
    bordure_bouton_jouer = Frame(frame_principal)
    bordure_bouton_jouer.place(relx = 0.5,
                               rely = 0.4,
                               anchor = CENTER)

    bordure_bouton_options = Frame(frame_principal)
    bordure_bouton_options.place(relx=0.5,
                                 rely=0.5,
                                 anchor=CENTER)

    bordure_bouton_quitter = Frame(frame_principal)
    bordure_bouton_quitter.place(relx=0.5,
                             rely=0.6,
                             anchor=CENTER)

    bouton_jouer = Button(bordure_bouton_jouer,
                          text = "Jouer",
                          width = 15,
                          font = ("Oswald", 30),
                          bg = "#d2d4d1",
                          fg = "#fbfbfb",
                          command = lambda:show_frame(frame_personnalisation)) 
    bouton_jouer.pack()

    bouton_options = Button(bordure_bouton_options,
                            text = "Options",
                            width = 15,
                            font = ("Oswald", 30),
                            bg = "#d2d4d1",
                            fg = "#fbfbfb",
                            command = lambda:show_frame(frame_placement))
    bouton_options.pack()

    bouton_quitter = Button(bordure_bouton_quitter,
                            text = "Quitter",
                            width = 15,
                            font = ("Oswald",30),
                            bg = "#d2d4d1",
                            fg = "#fbfbfb",
                            command = root.quit)
    bouton_quitter.pack()

    bordure_bouton_jouer.bind("<Enter>", survol_bordure_bouton)
    bordure_bouton_jouer.bind("<Leave>", fin_survol_bordure_bouton)
    bouton_jouer.bind("<Enter>", survol_bouton)
    bouton_jouer.bind("<Leave>", fin_survol_bouton)

    bordure_bouton_options.bind("<Enter>", survol_bordure_bouton)
    bordure_bouton_options.bind("<Leave>", fin_survol_bordure_bouton)
    bouton_options.bind("<Enter>", survol_bouton)
    bouton_options.bind("<Leave>", fin_survol_bouton)

    bordure_bouton_quitter.bind("<Enter>", survol_bordure_bouton)
    bordure_bouton_quitter.bind("<Leave>", fin_survol_bordure_bouton)
    bouton_quitter.bind("<Enter>", survol_bouton)
    bouton_quitter.bind("<Leave>", fin_survol_bouton)


# Ecran principal terminé
# ----------------------------------------------------
# Ci-dessous, l'écran personnalisation au propre!

flag_validation_difficulte = False
flag_validation_enregistrement = False

def choix_couleur():
    entrer_pseudo.config(fg = colorchooser.askcolor()[1])
    print("c'est ggoodd")
    
    
def valider():
    pseudo_perso = entrer_pseudo.get()
    show_frame(frame_placement)

      
def annuler():
    entrer_pseudo.config(state = NORMAL)
    global flag_validation_enregistrement
    flag_validation_enregistrement = False
    deblocage_bouton()
    
    
def choix_difficulte():
    if numero.get() == 0:
        description_difficulte['text'] = "TOI FIOTTE"
    if numero.get() == 1:
        description_difficulte['text'] = "TOI FORT"
    if numero.get() == 2:
        description_difficulte['text'] = "TOI GROSSE BURNASSES"
    global flag_validation_difficulte
    flag_validation_difficulte = True
    deblocage_bouton()
            

def enregistrement():
    entrer_pseudo.config(state = DISABLED)
    global flag_validation_enregistrement
    flag_validation_enregistrement = True 
    deblocage_bouton()
    

def deblocage_bouton():
    if flag_validation_enregistrement and flag_validation_difficulte:
        bouton_valider['state'] = NORMAL
        bordure_bouton_valider.bind("<Enter>", survol_bordure_bouton)
        bordure_bouton_valider.bind("<Leave>", fin_survol_bordure_bouton)
    else:
        bouton_valider['state'] = DISABLED
        
        
entrer_pseudo = Entry(frame_personnalisation,
                      font = ("Constantia", 50),
                      fg = "Black", 
                      bg = "white")
entrer_pseudo.place(relx = 0.5,
                    rely= 0.2,
                    anchor = CENTER)
    
bordure_bouton_couleur = Frame(frame_personnalisation)
bordure_bouton_couleur.place(relx = 0.2,
                             rely = 0.2, 
                             anchor = CENTER)

bordure_bouton_enregistrer = Frame(frame_personnalisation)
bordure_bouton_enregistrer.place(relx = 0.8,
                                 rely = 0.2,
                                 anchor = CENTER)

bordure_bouton_annuler = Frame(frame_personnalisation)
bordure_bouton_annuler.place(relx = 0.91,
                             rely = 0.2,
                             anchor = CENTER)

bordure_bouton_retour = Frame(frame_personnalisation)
bordure_bouton_retour.place(relx = 0.1,
                            rely = 0.9, 
                            anchor=CENTER)

bordure_bouton_valider = Frame(frame_personnalisation)
bordure_bouton_valider.place(relx = 0.9,
                             rely = 0.9,
                             anchor = CENTER)

bouton_couleur = Button(bordure_bouton_couleur, 
                        text = "Couleur",
                        width = 15,
                        font = ("Oswald", 15),
                        command = choix_couleur)
bouton_couleur.pack()   

bouton_enregistrer = Button(bordure_bouton_enregistrer,
                            text = "Enregistrer",
                            width = 15, 
                            font = ("Oswald", 15),
                            command = enregistrement)
bouton_enregistrer.pack()

bouton_annuler = Button(bordure_bouton_annuler,
                        text = "Annuler",
                        width = 15,
                        font = ("Oswald", 15),
                        command = annuler)
bouton_annuler.pack()

bouton_retour = Button(bordure_bouton_retour, 
                       text = "Retour", 
                       width = 15,
                       font = ("Oswald", 20),
                       command = lambda:show_frame(frame_principal))
bouton_retour.pack()

bouton_valider = Button(bordure_bouton_valider,
                        text = "Valider", 
                        width = 15,
                        font = ("Oswald", 20),
                        state = DISABLED,
                        command = valider)
bouton_valider.pack()

description_difficulte = Label(frame_personnalisation, 
                               text = "Choisis une difficulté", 
                               bg = "white",
                               font = ("Impact", 50))
description_difficulte.place(relx = 0.5,
                             rely = 0.5, 
                             anchor = CENTER)

# Partie à peaufiner (mettre nouvelles images, refaire descriptions...)
img = Image.open('raid.png')
resized_img = img.resize((200,200))

facile = ImageTk.PhotoImage(resized_img)
normal = ImageTk.PhotoImage(resized_img)
difficile = ImageTk.PhotoImage(resized_img)
    
bordure_bouton_radio_facile = Frame(frame_personnalisation)
bordure_bouton_radio_facile.place(relx = 0.2,
                                  rely = 0.7,
                                  anchor = CENTER)

bordure_bouton_radio_normal = Frame(frame_personnalisation)
bordure_bouton_radio_normal.place(relx = 0.5,
                                  rely = 0.7,
                                  anchor = CENTER)

bordure_bouton_radio_difficile = Frame(frame_personnalisation)
bordure_bouton_radio_difficile.place(relx = 0.8,
                                     rely = 0.7,
                                     anchor = CENTER)

numero = IntVar() # permet d'appeler chaque boutons

bouton_radio_facile = Radiobutton(bordure_bouton_radio_facile,
                                  text = "FACILE",
                                  variable = numero, # groupe les boutons ensemble s'ils ont la même variable
                                  value = 0, # chaque bouton a une identité propre,
                                  font = ("League Gothic", 20, "bold"),
                                  image = facile,
                                  compound = "left",
                                  indicatoron = 0, #enlève les cercles
                                  width = 350,
                                  command = choix_difficulte)
bouton_radio_facile.pack()

bouton_radio_normal = Radiobutton(bordure_bouton_radio_normal,
                                  text = "NORMAL",
                                  variable = numero, #groupe les boutons ensemble s'ils ont la même variable
                                  value = 1, #chaque bouton a une identité propre,
                                  font = ("League Gothic", 20, "bold"),
                                  image = normal,
                                  compound = "left",
                                  indicatoron = 0, #enlève les cercles
                                  width = 350,
                                  command = choix_difficulte)
bouton_radio_normal.pack()

bouton_radio_difficile = Radiobutton(bordure_bouton_radio_difficile,
                                     text = "DIFFICILE",
                                     variable = numero, #groupe les boutons ensemble s'ils ont la même variable
                                     value = 2, #chaque bouton a une identité propre,
                                     font = ("League Gothic", 20, "bold"),
                                     image = difficile,
                                     compound = "left",
                                     indicatoron = 0, #enlève les cercles
                                     width = 350,
                                     command = choix_difficulte)
bouton_radio_difficile.pack()
    
bordure_bouton_couleur.bind("<Enter>", survol_bordure_bouton)
bordure_bouton_couleur.bind("<Leave>", fin_survol_bordure_bouton)
bordure_bouton_enregistrer.bind("<Enter>", survol_bordure_bouton)
bordure_bouton_enregistrer.bind("<Leave>", fin_survol_bordure_bouton)
bordure_bouton_annuler.bind("<Enter>", survol_bordure_bouton)
bordure_bouton_annuler.bind("<Leave>", fin_survol_bordure_bouton)
bordure_bouton_retour.bind("<Enter>", survol_bordure_bouton)
bordure_bouton_retour.bind("<Leave>", fin_survol_bordure_bouton)
bordure_bouton_radio_facile.bind("<Enter>", survol_bordure_bouton)
bordure_bouton_radio_facile.bind("<Leave>", fin_survol_bordure_bouton)
bordure_bouton_radio_normal.bind("<Enter>", survol_bordure_bouton)
bordure_bouton_radio_normal.bind("<Leave>", fin_survol_bordure_bouton)
bordure_bouton_radio_difficile.bind("<Enter>", survol_bordure_bouton)
bordure_bouton_radio_difficile.bind("<Leave>", fin_survol_bordure_bouton)

# Ecran de personnalisation terminé
# ----------------------------------------------------
#Ci-dessous, l'écran de placement au propre!
 
def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
    new_x = widget.winfo_x()    # coord de tests
    new_y = widget.winfo_y()
    print(new_x,new_y)
    
    
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
    if (x + height <= 620) and (y + width <= 710): # Modif à faire!
        widget.configure(width=height, height=width)    
    
    
def identify(event):
    widget = event.widget
    x = widget.winfo_x()
    y = widget.winfo_y()
    largeur = widget.winfo_width()
    hauteur = widget.winfo_height()
    new_x = x // taille_de_carres * taille_de_carres + dep_x % taille_de_carres + 3
    new_y = y // taille_de_carres * taille_de_carres + dep_y % taille_de_carres + 3
    if dep_x < new_x < dimension + dep_x and dep_y < new_y < dimension + dep_y and x + largeur - taille_de_carres // 2 < dimension + dep_x and y + hauteur - taille_de_carres // 2 < dimension + dep_y:
        widget.place(x=new_x, y=new_y)
        collisions(event)
    else:
        widget.place(x=x, y=y)
        
        
bouton_placement = Button(frame_placement, text = "Confirmer", command = lambda:show_frame(frame_jeu))
bouton_placement.place(relx = 0.5, rely = 0.1, anchor = CENTER)
    
plateau_placement = Canvas(frame_placement, width = dimension, height = dimension)
plateau_placement.place(x = dep_x, y = dep_y)
    
    # modif le nom des canvas
canvas1 = Canvas(frame_placement, bg = "gray", width=taille_de_carres-1, height=taille_de_carres*2-1, bd = 0, highlightthickness = 0)
canvas1.place(x = 950, y = 390)
canvas2 = Canvas(frame_placement, bg = "green", width=taille_de_carres-1, height=taille_de_carres*3-1, bd = 0, highlightthickness = 0)
canvas2.place(x = 1100, y = 390)
canvas3 = Canvas(frame_placement, bg = "yellow", width=taille_de_carres-1, height=taille_de_carres*3-1, bd = 0, highlightthickness = 0)
canvas3.place(x = 1250, y = 390)
canvas4 = Canvas(frame_placement, bg = "blue", width=taille_de_carres-1, height=taille_de_carres*4-1, bd = 0, highlightthickness = 0)
canvas4.place(x = 1400, y = 390)
canvas5 = Canvas(frame_placement, bg = "orange", width=taille_de_carres-1, height=taille_de_carres*5-1, bd = 0, highlightthickness = 0)
canvas5.place(x = 1550, y = 390)
    
for i in range(nombre_de_carres):
    for j in range(nombre_de_carres):
        x, y = taille_de_carres * j + 2, taille_de_carres * i + 2
        A, B = (x, y), (x + taille_de_carres, y + taille_de_carres)
        plateau_placement.create_rectangle(A, B, fill="#097ade") 
    

    # test de reposition des bateaux superposés
A = 100
B = 100
places_occupées = 0
    
    # Mise en place des bateaux :
def collisions(event):
    a1 = canvas1.winfo_x() 
    a2 = canvas1.winfo_x() + canvas1.winfo_width()
    b1 = canvas1.winfo_y()
    b2 = canvas1.winfo_y() + canvas1.winfo_height()
        
    c1 = canvas2.winfo_x() 
    c2 = canvas2.winfo_x() + canvas2.winfo_width()
    d1 = canvas2.winfo_y()
    d2 = canvas2.winfo_y() + canvas2.winfo_height()
        
    e1 = canvas3.winfo_x() 
    e2 = canvas3.winfo_x() + canvas3.winfo_width()
    f1 = canvas3.winfo_y()
    f2 = canvas3.winfo_y() + canvas3.winfo_height()
        
    g1 = canvas4.winfo_x() 
    g2 = canvas4.winfo_x() + canvas4.winfo_width()
    h1 = canvas4.winfo_y()
    h2 = canvas4.winfo_y() + canvas4.winfo_height()
        
    i1 = canvas5.winfo_x() 
    i2 = canvas5.winfo_x() + canvas5.winfo_width()
    j1 = canvas5.winfo_y()
    j2 = canvas5.winfo_y() + canvas5.winfo_height()  
        
    widget = event.widget
        
    global places_occupées
        
    if a2 >= c1 and b2 >= d1 and c2 >= a1 and d2 >= b1: 
        print("canvas1 et canvas2 se touchent")
        widget.place(x=A+100*places_occupées, y=B+100*places_occupées)
        places_occupées = places_occupées + 1 
    elif a2 >= e1 and b2 >= f1 and e2 >= a1 and f2 >= b1:
        print("canvas1 et canvas3 se touchent")
        widget.place(x=A+100*places_occupées, y=B+100*places_occupées)
        places_occupées = places_occupées + 1 
    elif a2 >= g1 and b2 >= h1 and g2 >= a1 and h2 >= b1:
        print("canvas1 et canvas4 se touchent")
        widget.place(x=A+100*places_occupées, y=B+100*places_occupées)
        places_occupées = places_occupées + 1 
    elif a2 >= i1 and b2 >= j1 and i2 >= a1 and j2 >= b1:
        print("canvas1 et canvas5 se touchent")
        widget.place(x=A+100*places_occupées, y=B+100*places_occupées)
        places_occupées = places_occupées + 1 
    elif c2 >= e1 and d2 >= f1 and e2 >= c1 and f2 >= d1:
        print("canvas2 et canvas3 se touchent")
        widget.place(x=A+100*places_occupées, y=B+100*places_occupées)
        places_occupées = places_occupées + 1 
    elif c2 >= g1 and d2 >= h1 and g2 >= c1 and h2 >= d1:
        print("canvas2 et canvas4 se touchent")
        widget.place(x=A+100*places_occupées, y=B+100*places_occupées)
        places_occupées = places_occupées + 1 
    elif c2 >= i1 and d2 >= j1 and i2 >= c1 and j2 >= d1:
        print("canvas2 et canvas5 se touchent")
        widget.place(x=A+100*places_occupées, y=B+100*places_occupées)
        places_occupées = places_occupées + 1
    elif e2 >= g1 and f2 >= h1 and g2 >= e1 and h2 >= f1:
        print("canvas3 et canvas4 se touchent")
        widget.place(x=A+100*places_occupées, y=B+100*places_occupées)
        places_occupées = places_occupées + 1 
    elif e2 >= i1 and f2 >= j1 and i2 >= e1 and j2 >= f1:
        print("canvas3 et canvas5 se touchent")
        widget.place(x=A+100*places_occupées, y=B+100*places_occupées)
        places_occupées = places_occupées + 1 
    elif g2 >= i1 and h2 >= j1 and i2 >= g1 and j2 >= h1:
        print("canvas4 et canvas5 se touchent")
        widget.place(x=A+100*places_occupées, y=B+100*places_occupées)
        places_occupées = places_occupées + 1 
    else:
        print("Aucune collision détecté")
        if places_occupées > 0:
            places_occupées = places_occupées - 1
            print(places_occupées)
        
canvas1.bind("<Button-1>", drag_start)
canvas1.bind("<Button-3>", spiderman_do_a_flip)
canvas1.bind("<B1-Motion>", drag_motion)
canvas1.bind("<ButtonRelease-1>", identify)
    
canvas2.bind("<Button-1>", drag_start)
canvas2.bind("<Button-3>", spiderman_do_a_flip)
canvas2.bind("<B1-Motion>", drag_motion)
canvas2.bind("<ButtonRelease-1>", identify)
    
canvas3.bind("<Button-1>", drag_start)
canvas3.bind("<Button-3>", spiderman_do_a_flip)
canvas3.bind("<B1-Motion>", drag_motion)
canvas3.bind("<ButtonRelease-1>", identify)
    
canvas4.bind("<Button-1>", drag_start)
canvas4.bind("<Button-3>", spiderman_do_a_flip)
canvas4.bind("<B1-Motion>", drag_motion)
canvas4.bind("<ButtonRelease-1>", identify)
    
canvas5.bind("<Button-1>", drag_start)
canvas5.bind("<Button-3>", spiderman_do_a_flip)
canvas5.bind("<B1-Motion>", drag_motion)
canvas5.bind("<ButtonRelease-1>", identify)

# Améliorations à faire pour l'écran de placement (réintégré la grille, regérer le positionnment...)
# ----------------------------------------------------
# Ci-dessous, l'écran de jeu   

plateau1 = Canvas(frame_jeu, width = dimension, height = dimension)
plateau1.place(x=dep_x, y=dep_y)
plateau2 = Canvas(frame_jeu, width = dimension, height = dimension)
plateau2.place(x=920, y=dep_y)

def clic_plateau1(event):
    global tour
    print("tour=", tour)
    if tour == 1:
        i = event.y // taille_de_carres
        j = event.x // taille_de_carres
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
    print("tour=", tour)
    if tour == 2:
        i = event.y // taille_de_carres
        j = event.x // taille_de_carres
        if grille2[i][j] == 0:
            tour = 1
            grille2[i][j] = 1
            plateau2.itemconfigure(i * 10 + j + 1, fill="#80ff00")
            print(grille2)
            print("Ligne=", i + 1, "Colonne=", j + 1)
            label1['text'] = "Votre tour"
            label1['bg'] = "green"
        else:
            print("Veuillez sélectionner une autre case")
        test_victoire()
    else:
        print("Ce n'est pas votre tour")
        
        
        
def remplir_plateau1():
    for i in range(nombre_de_carres):
        for j in range(nombre_de_carres):
            x, y = taille_de_carres * j + 2, taille_de_carres * i + 2
            A, B = (x, y), (x + taille_de_carres, y + taille_de_carres)
            plateau1.create_rectangle(A, B, fill="#097ade")


def remplir_plateau2():
    for i in range(nombre_de_carres):
        for j in range(nombre_de_carres):
            x, y = taille_de_carres * j + 2, taille_de_carres * i + 2
            A, B = (x, y), (x + taille_de_carres, y + taille_de_carres)
            plateau2.create_rectangle(A, B, fill="#097ade")


plateau1.bind("<Button-1>", clic_plateau1)
plateau2.bind("<Button-1>", clic_plateau2)
# Créations des boutons et des zones de texte :
def placer_boutons():
    global bouton1
    bouton1 = Button(root, text="Rejouer", command=recommencer, state=DISABLED)
    bouton1.place(relx=0.5, rely=0.02, anchor='center')
    global bouton2
    bouton2 = Button(root, text="Quitter", command=abandon_de_partie)
    bouton2.place(relx=0.5, rely=0.055, anchor='center')
    global bouton3
    bouton3 = Button(frame3, text="Confirmer", command=confirmer_placement)
    bouton3.place(relx = 0.5, rely = 0.1, anchor=CENTER)


def placer_label():
    global label1
    label1 = Label(root, text="Votre tour", bg="green")
    label1.place(relx=0.5, rely=0.09, anchor='center')
    global label_victoire
    label_victoire = Label(root, text="")
    label_victoire.place(relx=0.5, rely=0.12, anchor='center')
    global label_scoreboard
    label_scoreboard = Label(root, text="SCORE:" + str(score))
    label_scoreboard.place(x=0, y=0)   
    
    
# Fin du MENU DE SELECTION
# Réalisation des tirs (alliés et ennemis) :


# Création des cases :
    

# Impossible de déplacer cette fonction dans le model!
# En effet, bouton n'y est pas défini
def test_victoire():
    global score
    vainqueur = victoire()
    if (vainqueur == 0):
        fin_de_partie()
        bouton1['state'] = NORMAL
        label_victoire['text'] = "VICTOIRE"
        score = score + 1
        label_scoreboard.config(text="SCORE:" + str(score))


# Pareil ici!
def recommencer():
    for i in range(nombre_de_carres):
        for j in range(nombre_de_carres):
            if grille1[i][j] != 0:
                plateau1.itemconfigure(i * 10 + j + 1, fill="#097ade")
            if grille2[i][j] != 0:
                plateau2.itemconfigure(i * 10 + j + 1, fill="#097ade")
    reInitialisation()
    bouton1['state'] = DISABLED
    label1['text'] = "Votre tour"
    label1['bg'] = "green"
    label_victoire['text'] = ""
    global tour
    tour = 1


def affichage():
    ecran_principal()
    remplir_plateau1()
    remplir_plateau2()
    #placer_boutons()
    #placer_label()
    #bateaux()
