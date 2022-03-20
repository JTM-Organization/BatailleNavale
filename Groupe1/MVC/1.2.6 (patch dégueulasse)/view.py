# -*- coding: utf-8 -*-

# Interface graphique
from model import *
from tkinter import ttk
import tkinter as tk
from tkinter import colorchooser
from PIL import *
from PIL import ImageTk, Image

# Fonctions primaires (et esthétiques) qui servent aux boutons de tout le programme
def affichage_frame(frame):
    frame.tkraise()


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


# --------------------------------------------------------------------------------------------------------------------------------

# Mise en place des différentes frames
def placement_frame():
    global frame_principal 
    frame_principal = Frame(root, bg = "red") # Frame principale
    global frame_personnalisation
    frame_personnalisation = Frame(root, bg = "green") # Frame personnalisation
    global frame_placement
    frame_placement = Frame(root, bg = "purple") # Frame de placement
    global frame_jeu
    frame_jeu = Frame(root, bg = "blue") # Frame de jeu
    global frame_reglages
    frame_reglages = Frame(root, bg = "orange") # Frame des reglages
    for frame in (frame_principal, frame_personnalisation, frame_placement, frame_jeu, frame_reglages):
        frame.grid(row = 0, column = 0, sticky = "nsew")
    affichage_frame(frame_principal)
    
    
# --------------------------------------------------------------------------------------------------------------------------------    

# Création du Menu Principal dans la Frame principale
def ecran_principal():
    bordures_principal()
    boutons_principal()
    bind_principal()


# Création des bordures des boutons du Menu Principal
def bordures_principal():
        global bordure_bouton_jouer
        bordure_bouton_jouer = Frame(frame_principal)
        bordure_bouton_jouer.place(relx = 0.5,
                                   rely = 0.4,
                                   anchor = CENTER)
        
        global bordure_bouton_options
        bordure_bouton_options = Frame(frame_principal)
        bordure_bouton_options.place(relx=0.5,
                                     rely=0.5,
                                     anchor=CENTER)
        
        global bordure_bouton_quitter
        bordure_bouton_quitter = Frame(frame_principal)
        bordure_bouton_quitter.place(relx=0.5,
                                 rely=0.6,
                                 anchor=CENTER)


# Créations des boutons du Menu Principal
def boutons_principal():
    global bouton_jouer
    bouton_jouer = Button(bordure_bouton_jouer,
                          text = "Jouer",
                          width = 15,
                          font = ("Oswald", 30),
                          bg = "#d2d4d1",
                          fg = "#fbfbfb",
                          command = lambda:affichage_frame(frame_personnalisation)) 
    bouton_jouer.pack()
    
    global bouton_options
    bouton_options = Button(bordure_bouton_options,
                            text = "Options",
                            width = 15,
                            font = ("Oswald", 30),
                            bg = "#d2d4d1",
                            fg = "#fbfbfb",
                            command = lambda:affichage_frame(frame_placement))
    bouton_options.pack()
        
    global bouton_quitter
    bouton_quitter = Button(bordure_bouton_quitter,
                            text = "Quitter",
                            width = 15,
                            font = ("Oswald",30),
                            bg = "#d2d4d1",
                            fg = "#fbfbfb",
                            command = root.quit)
    bouton_quitter.pack()
        
        
# Créations des actions clavier/souris possibles du Menu Principal        
def bind_principal():
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
    
    
# --------------------------------------------------------------------------------------------------------------------------------

# Création du Menu de personnalisation dans la Frame personnalisation
def ecran_personnalisation():
    bordures_personnalisation()
    boutons_personnalisation()
    entree_personnalisation()
    label_personnalisation()
    boutons_radios_personnalisation()
    bind_personnalisation()
    

# Permet de sélectionner une couleur qui s'appliquera à l'écriture
def choix_couleur():
    entrer_pseudo.config(fg = colorchooser.askcolor()[1]) 

      
# Booléens utiles au déverrouillage du bouton valider
flag_validation_difficulte = False
flag_validation_enregistrement = False


# Sélection d'une difficulté 
def choix_difficulte():
    if numero.get() == 0:
        description_difficulte['text'] = "FACILE"
    if numero.get() == 1:
        description_difficulte['text'] = "MOYEN"
    if numero.get() == 2:
        description_difficulte['text'] = "DIFFICILE"
    global flag_validation_difficulte
    flag_validation_difficulte = True
    deblocage_bouton_valider_personnalisation()
            
    
# Permet d'enregistrer le pseudo temporairement (jusqu'à validation)
def enregistrement_personnalisation():
    entrer_pseudo.config(state = DISABLED)
    global flag_validation_enregistrement
    flag_validation_enregistrement = True 
    deblocage_bouton_valider_personnalisation()
    bouton_enregistrer_personnalisation['state'] = DISABLED
    bouton_annuler_personnalisation['state'] = NORMAL
    bordure_bouton_enregistrer_personnalisation.bind("<Enter>", fin_survol_bordure_bouton)
    bordure_bouton_annuler_personnalisation.bind("<Enter>", survol_bordure_bouton)
    bordure_bouton_annuler_personnalisation.bind("<Leave>", fin_survol_bordure_bouton)
    
    
# Annule l'enregistrement du pseudo (afin de le modifier)
def annuler():
    entrer_pseudo.config(state = NORMAL)
    global flag_validation_enregistrement
    flag_validation_enregistrement = False
    deblocage_bouton_valider_personnalisation()
    bouton_enregistrer_personnalisation['state'] = NORMAL
    bouton_annuler_personnalisation['state'] = DISABLED
    bordure_bouton_annuler_personnalisation.bind("<Enter>", fin_survol_bordure_bouton)
    bordure_bouton_enregistrer_personnalisation.bind("<Enter>", survol_bordure_bouton)
    bordure_bouton_enregistrer_personnalisation.bind("<Leave>", fin_survol_bordure_bouton)
    
    
# Vérifie si une difficulté ainsi qu'un pseudo ont été sélectionné
def deblocage_bouton_valider_personnalisation():
    if flag_validation_enregistrement and flag_validation_difficulte:
        bouton_valider_personnalisation['state'] = NORMAL
        bordure_bouton_valider_personnalisation.bind("<Enter>", survol_bordure_bouton)
        bordure_bouton_valider_personnalisation.bind("<Leave>", fin_survol_bordure_bouton)
    else:
        bouton_valider_personnalisation['state'] = DISABLED
        bordure_bouton_valider_personnalisation.bind("<Enter>", fin_survol_bordure_bouton)
        
        
# Permet de passer à la page suivante tout en sauvegardant définitivement le pseudonyme
def valider_personnalisation():
    pseudo_perso = entrer_pseudo.get()
    affichage_frame(frame_placement)
    
    
# Création des bordures des boutons du Menu de personnalisation   
def bordures_personnalisation():
    global bordure_bouton_couleur
    bordure_bouton_couleur = Frame(frame_personnalisation)
    bordure_bouton_couleur.place(relx = 0.2,
                                 rely = 0.2, 
                                 anchor = CENTER)
    
    global bordure_bouton_enregistrer_personnalisation
    bordure_bouton_enregistrer_personnalisation = Frame(frame_personnalisation)
    bordure_bouton_enregistrer_personnalisation.place(relx = 0.8,
                                                      rely = 0.2,
                                                      anchor = CENTER)
    
    global bordure_bouton_annuler_personnalisation
    bordure_bouton_annuler_personnalisation = Frame(frame_personnalisation)
    bordure_bouton_annuler_personnalisation.place(relx = 0.91,
                                                  rely = 0.2,
                                                  anchor = CENTER)
    
    global bordure_bouton_retour_personnalisation
    bordure_bouton_retour_personnalisation = Frame(frame_personnalisation)
    bordure_bouton_retour_personnalisation.place(relx = 0.1,
                                                 rely = 0.9, 
                                                 anchor=CENTER)
    
    global bordure_bouton_valider_personnalisation
    bordure_bouton_valider_personnalisation = Frame(frame_personnalisation)
    bordure_bouton_valider_personnalisation.place(relx = 0.9,
                                                  rely = 0.9,
                                                  anchor = CENTER)
    
    global bordure_bouton_radio_facile
    bordure_bouton_radio_facile = Frame(frame_personnalisation)
    bordure_bouton_radio_facile.place(relx = 0.2,
                                      rely = 0.7,
                                      anchor = CENTER)
    
    global bordure_bouton_radio_normal
    bordure_bouton_radio_normal = Frame(frame_personnalisation)
    bordure_bouton_radio_normal.place(relx = 0.5,
                                      rely = 0.7,
                                      anchor = CENTER)
    
    global bordure_bouton_radio_difficile
    bordure_bouton_radio_difficile = Frame(frame_personnalisation)
    bordure_bouton_radio_difficile.place(relx = 0.8,
                                         rely = 0.7,
                                         anchor = CENTER)
    
    
# Création des boutons du Menu de personnalisation  
def boutons_personnalisation():
    global bouton_couleur
    bouton_couleur = Button(bordure_bouton_couleur, 
                            text = "Couleur",
                            width = 15,
                            font = ("Oswald", 15),
                            command = choix_couleur)
    bouton_couleur.pack()   
    
    global bouton_enregistrer_personnalisation
    bouton_enregistrer_personnalisation = Button(bordure_bouton_enregistrer_personnalisation,
                                                 text = "Enregistrer",
                                                 width = 15, 
                                                 font = ("Oswald", 15),
                                                 command = enregistrement_personnalisation)
    bouton_enregistrer_personnalisation.pack()
    
    global bouton_annuler_personnalisation
    bouton_annuler_personnalisation = Button(bordure_bouton_annuler_personnalisation,
                                             text = "Annuler",
                                             width = 15,
                                             font = ("Oswald", 15),
                                             state = DISABLED,
                                             command = annuler)
    bouton_annuler_personnalisation.pack()
    
    global bouton_retour_personnalisation
    bouton_retour_personnalisation = Button(bordure_bouton_retour_personnalisation, 
                                            text = "Retour", 
                                            width = 15,
                                            font = ("Oswald", 20),
                                            command = lambda:affichage_frame(frame_principal))
    bouton_retour_personnalisation.pack()
    
    global bouton_valider_personnalisation
    bouton_valider_personnalisation = Button(bordure_bouton_valider_personnalisation,
                                             text = "Valider", 
                                             width = 15,
                                             font = ("Oswald", 20),
                                             state = DISABLED,
                                             command = valider_personnalisation)
    bouton_valider_personnalisation.pack()
    
    
# Création de la zone d'entrée de texte du Menu de personnalisation   
def entree_personnalisation():
    global entrer_pseudo
    entrer_pseudo = Entry(frame_personnalisation,
                          font = ("Constantia", 50),
                          fg = "Black", 
                          bg = "white")
    entrer_pseudo.place(relx = 0.5,
                        rely= 0.2,
                        anchor = CENTER)
    

# Création du label du Menu de personnalisation
def label_personnalisation():
    global description_difficulte
    description_difficulte = Label(frame_personnalisation, 
                                   text = "Choisis une difficulté", 
                                   bg = "white",
                                   font = ("Impact", 50))
    description_difficulte.place(relx = 0.5,
                                 rely = 0.5, 
                                 anchor = CENTER)
      

# Création des boutons radios du Menu personnalisation
def boutons_radios_personnalisation():
    img = Image.open('raid.png')
    img_redim = img.resize((200,200))
    
    global facile
    facile = ImageTk.PhotoImage(img_redim)
    global normal
    normal = ImageTk.PhotoImage(img_redim)
    global difficile
    difficile = ImageTk.PhotoImage(img_redim)
    
    global numero
    numero = IntVar() # Permet d'appeler chaque boutons radios en fonction de leurs 'value'
    numero.set(3) # Coche le bouton 3 par défaut (n'existe pas, donc aucun bouton n'est coché)
    
    global bouton_radio_facile
    bouton_radio_facile = Radiobutton(bordure_bouton_radio_facile,
                                      text = "FACILE",
                                      variable = numero, # Appel du bouton
                                      value = 0, # Identité du bouton
                                      font = ("League Gothic", 20, "bold"),
                                      image = facile,
                                      compound = "left", # Positionne l'image à gauche du bouton radio
                                      indicatoron = 0, # Permet d'enlever les cercles 
                                      width = 350,
                                      bg = "green",
                                      command = choix_difficulte)
    bouton_radio_facile.pack()
    
    global bouton_radio_normal
    bouton_radio_normal = Radiobutton(bordure_bouton_radio_normal,
                                      text = "NORMAL",
                                      variable = numero, 
                                      value = 1, 
                                      font = ("League Gothic", 20, "bold"),
                                      image = normal,
                                      compound = "left",
                                      indicatoron = 0, 
                                      width = 350,
                                      bg = "orange",
                                      command = choix_difficulte)
    bouton_radio_normal.pack()
    
    global bouton_radio_difficile
    bouton_radio_difficile = Radiobutton(bordure_bouton_radio_difficile,
                                         text = "DIFFICILE",
                                         variable = numero,
                                         value = 2,
                                         font = ("League Gothic", 20, "bold"),
                                         image = difficile,
                                         compound = "left",
                                         indicatoron = 0,
                                         width = 350,
                                         bg = "red",
                                         command = choix_difficulte)
    bouton_radio_difficile.pack()    
    
    
# Créations des actions clavier/souris possibles du Menu de personnalisation 
def bind_personnalisation():  
    bordure_bouton_couleur.bind("<Enter>", survol_bordure_bouton)
    bordure_bouton_couleur.bind("<Leave>", fin_survol_bordure_bouton)
    
    bordure_bouton_retour_personnalisation.bind("<Enter>", survol_bordure_bouton)
    bordure_bouton_retour_personnalisation.bind("<Leave>", fin_survol_bordure_bouton)
    
    bordure_bouton_radio_facile.bind("<Enter>", survol_bordure_bouton)
    bordure_bouton_radio_facile.bind("<Leave>", fin_survol_bordure_bouton)
    
    bordure_bouton_radio_normal.bind("<Enter>", survol_bordure_bouton)
    bordure_bouton_radio_normal.bind("<Leave>", fin_survol_bordure_bouton)
    
    bordure_bouton_radio_difficile.bind("<Enter>", survol_bordure_bouton)
    bordure_bouton_radio_difficile.bind("<Leave>", fin_survol_bordure_bouton)
    
    bordure_bouton_enregistrer_personnalisation.bind("<Enter>", survol_bordure_bouton)
    bordure_bouton_enregistrer_personnalisation.bind("<Leave>", fin_survol_bordure_bouton)
    
    
# --------------------------------------------------------------------------------------------------------------------------------    
"""
REVOIR LES AFFICHAGES DES LABELS DE CETTE PARTIE (LA PLUPART SERVAIENT JUSTE DE TESTS)
"""



# Création du Menu de placement dans la Frame placement
def ecran_placement():
    bordures_placement()
    bouton_placement()
    label_placement()
    plateau_placement()
    quadrillage_plateau_placement()
    bateaux_placement()
    bind_placement()
            
# Fonctions primaires qui servent aux divers déplacements des bateaux
def drag_start(event): # nom à changer
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
    new_x = widget.winfo_x()    #vraiment utile?
    new_y = widget.winfo_y()
    widget.bind("<B1-Motion>", drag_motion)
    widget.bind("<ButtonRelease-1>", drop)
    
    
def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)
    global bateau_statique
    bateau_statique = False
    return bateau_statique 

           
def spiderman_do_a_flip(event):
    widget = event.widget
    global bateau_statique
    x = widget.winfo_x()
    y = widget.winfo_y()
    width = widget.winfo_width()
    height = widget.winfo_height()   
    if not bateau_statique:
        widget.configure(width=height, height=width)
        alerte_placement['text'] = "ROTATION EFFECTUE"
    else:
        if (dep_x <= x <= dep_x + dimension) and (dep_x <= x + width <= dep_x + dimension) and (dep_x <= x + height <= dep_x + dimension) and (dep_y <= y <= dep_y + dimension) and (dep_y <= y + height <= dep_y + dimension) and (dep_y <= y + width <= dep_y + dimension):
            widget.configure(width=height, height=width)
            frame_placement.after(10, collisions, event)
            alerte_placement['text'] = "ROTATION EFFECTUE"
        else:
            alerte_placement['text'] = "ROTATION IMPOSSIBLE"
    frame_placement.after(10, test_placement, event)
 
    
def drop(event):
    widget = event.widget # Permet de s'appliquer à n'importe quel widget qui utilise la fonction (similaire à une classe)
    x = widget.winfo_x() # Détermine l'abscisse du point supérieur gauche du widget
    y = widget.winfo_y() # Détermine l'ordonnée du point supérieur gauche du widget
    largeur = widget.winfo_width() # Détermine la largeur du widget
    hauteur = widget.winfo_height() # Détermine la hauteur du widget
    new_x = (x + 9) // taille_de_carres * taille_de_carres + dep_x % taille_de_carres + 1 # Détermine des emplacements qui forment une grille "imaginaire" (en fonction du positionnement de la vraie grille) qui correspond exactement à la grille de notre plateau (cependant, elle s'étend à toute la fenêtre)
    new_y = (y - 11) // taille_de_carres * taille_de_carres + dep_y % taille_de_carres + 1
    if dep_x < new_x < dimension + dep_x and dep_y < new_y < dimension + dep_y and x + largeur - taille_de_carres // 2 < dimension + dep_x and y + hauteur - taille_de_carres // 2 < dimension + dep_y: # On teste içi si les points appartiennent à la grille du plateau
        widget.place(x=new_x, y=new_y)
        frame_placement.after(10, collisions, event) # Mise en place d'un timer pour d'abord placer et ensuite vérifier s'il y a collisions
    else:
        widget.place(x=x, y=y)
    frame_placement.after(20, test_placement, event) # Chaque positionnement de bateau teste la présence de tous les bateaux sur le plateau, s'ils sont tous présents alors le bouton de confirmation est déverrouillé (différence de timer pour éviter que certaines actions ne se fassent pas correctement)
    global bateau_statique
    bateau_statique = True
    return bateau_statique


# Vérifie si les bateaux sont correctements positionnés sur la grille du plateau
def test_placement(event):
    # Attribution des coordonnées des bateaux à des variables afin de connaître leurs localisations précises
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
    
    # Première vérification: On teste si le point supérieur gauche du bateau est dans un coin de quadrillage
    # On place chaque coordonnées de coin de quadrillage dans une liste
    liste_positions_x_grille = []
    for i in range(nombre_de_carres):
        liste_positions_x_grille.append(dep_x + taille_de_carres * i + 1)
    
    # Ici on effectue la vérification  
    global flag_bateau1_en_place
    if a1 in liste_positions_x_grille:
        flag_bateau1_en_place = True
        alerte_placement['text'] = "Navire 1 positionné" # Exemple d'affichage, à définir pour les autres?!?!
    else:
        flag_bateau1_en_place = False
        
    global flag_bateau2_en_place    
    if c1 in liste_positions_x_grille:
        flag_bateau2_en_place = True
    else:
        flag_bateau2_en_place = False
    
    global flag_bateau3_en_place
    if e1 in liste_positions_x_grille:
        flag_bateau3_en_place = True
    else:
        flag_bateau3_en_place = False
    
    global flag_bateau4_en_place
    if g1 in liste_positions_x_grille:
        flag_bateau4_en_place = True
    else:
        flag_bateau4_en_place = False
    
    global flag_bateau5_en_place
    if i1 in liste_positions_x_grille:
        flag_bateau5_en_place = True
    else:
        flag_bateau5_en_place = False
    
    # Attribution des valeurs de tout les flags (avec un AND) à un seul flag
    flag_bateaux_en_place = flag_bateau1_en_place and flag_bateau2_en_place and flag_bateau3_en_place and flag_bateau4_en_place and flag_bateau5_en_place
    
    # Deuxième vérification: On teste si les bateaux sont sur le plateau
    flag_bateau1_dans_grille = (dep_x <= a1 <= dep_x + dimension) and (dep_x <= a2 <= dep_x + dimension) and (dep_y <= b1 <= dep_y + dimension) and (dep_y <= b2 <= dep_y + dimension) # On teste si tous les bateaux sont dans le plateau
    flag_bateau2_dans_grille = (dep_x <= c1 <= dep_x + dimension) and (dep_x <= c2 <= dep_x + dimension) and (dep_y <= d1 <= dep_y + dimension) and (dep_y <= d2 <= dep_y + dimension)
    flag_bateau3_dans_grille = (dep_x <= e1 <= dep_x + dimension) and (dep_x <= e2 <= dep_x + dimension) and (dep_y <= f1 <= dep_y + dimension) and (dep_y <= f2 <= dep_y + dimension)
    flag_bateau4_dans_grille = (dep_x <= g1 <= dep_x + dimension) and (dep_x <= g2 <= dep_x + dimension) and (dep_y <= h1 <= dep_y + dimension) and (dep_y <= h2 <= dep_y + dimension)
    flag_bateau5_dans_grille = (dep_x <= i1 <= dep_x + dimension) and (dep_x <= i2 <= dep_x + dimension) and (dep_y <= j1 <= dep_y + dimension) and (dep_y <= j2 <= dep_y + dimension)
    
    # Attribution des valeurs de tout les flags de vérification de présence dans la grille à un seul flag
    flag_bateaux_dans_grille = flag_bateau1_dans_grille and flag_bateau2_dans_grille and flag_bateau3_dans_grille and flag_bateau4_dans_grille and flag_bateau5_dans_grille
    
    # Si tous les bateaux sont dans le plateau et qu'ils sont dans la grille alors la confirmation se déverrouille
    if flag_bateaux_dans_grille and flag_bateaux_en_place: 
        bouton_confirmer_placement['state'] = NORMAL
        bordure_bouton_confirmer_placement.bind("<Enter>", survol_bordure_bouton)
        bordure_bouton_confirmer_placement.bind("<Leave>", fin_survol_bordure_bouton)
        alerte_placement['text'] = "L'armée est en place, mon général"
    else:
        bouton_confirmer_placement['state'] = DISABLED
        bordure_bouton_confirmer_placement.bind("<Enter>", fin_survol_bordure_bouton)


# test de reposition des bateaux superposés (à peaufiner)
"""
 Repositionnement à réfléchir (+ changer le noms des bateaux pour plus de clarté?)
"""

A = 800
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
            
# Sauvegarde de la position des bateaux dans une liste de liste et dans les plateaux liés au jeu  
def confirmer():
    x1 = (canvas1.winfo_x() - dep_x) // taille_de_carres
    lc1 = canvas1.winfo_width()
    y1 = (canvas1.winfo_y() - dep_y) // taille_de_carres
    hc1 = canvas1.winfo_height()
        
    x2 = (canvas2.winfo_x() - dep_x) // taille_de_carres
    lc2 = canvas2.winfo_width()
    y2 = (canvas2.winfo_y() - dep_y) // taille_de_carres
    hc2 = canvas2.winfo_height()
        
    x3 = (canvas3.winfo_x() - dep_x) // taille_de_carres
    lc3 = canvas3.winfo_width()
    y3 = (canvas3.winfo_y() - dep_y) // taille_de_carres
    hc3 = canvas3.winfo_height()
        
    x4 = (canvas4.winfo_x() - dep_x) // taille_de_carres
    lc4 = canvas4.winfo_width()
    y4 = (canvas4.winfo_y() - dep_y) // taille_de_carres
    hc4 = canvas4.winfo_height()
        
    x5 = (canvas5.winfo_x() - dep_x) // taille_de_carres
    lc5 = canvas5.winfo_width()
    y5 = (canvas5.winfo_y() - dep_y) // taille_de_carres
    hc5 = canvas5.winfo_height() 
    
    if (lc1 > hc1):
        for i in range((lc1 + 1) // taille_de_carres):
            grille1[y1][x1 + i] = 3
            plateau1.itemconfigure(y1 * 10 + x1 + i + 1,
                                   fill = "gray")
    else:
        for i in range((hc1 + 1) // taille_de_carres):
            grille1[y1 + i][x1] = 3
            plateau1.itemconfigure((y1 + i) * 10 + x1 + 1,
                                   fill="gray")
            
    if (lc2 > hc2):
        for i in range((lc2 + 1) // taille_de_carres):
            grille1[y2][x2 + i] = 3
            plateau1.itemconfigure(y2 * 10 + x2 + i + 1,
                                   fill = "green")
    else:
        for i in range((hc2 + 1) // taille_de_carres):
            grille1[y2 + i][x2] = 3
            plateau1.itemconfigure((y2 + i) * 10 + x2 + 1,
                                   fill="green")
            
    if (lc3 > hc3):
        for i in range((lc3 + 1) // taille_de_carres):
            grille1[y3][x3 + i] = 3
            plateau1.itemconfigure(y3 * 10 + x3 + i + 1,
                                   fill = "yellow")
    else:
        for i in range((hc3 + 1) // taille_de_carres):
            grille1[y3 + i][x3] = 3
            plateau1.itemconfigure((y3 + i) * 10 + x3 + 1,
                                   fill="yellow")
            
    if (lc4 > hc4):
        for i in range((lc4 + 1) // taille_de_carres):
            grille1[y4][x4 + i] = 3
            plateau1.itemconfigure(y4 * 10 + x4 + i + 1,
                                   fill = "blue")
    else:
        for i in range((hc4 + 1) // taille_de_carres):
            grille1[y4 + i][x4] = 3
            plateau1.itemconfigure((y4 + i) * 10 + x4 + 1,
                                   fill = "blue")
            
    if (lc5 > hc5):
        for i in range((lc5 + 1) // taille_de_carres):
            grille1[y5][x5 + i] = 3
            plateau1.itemconfigure(y5 * 10 + x5 + i + 1,
                                   fill = "orange")
    else:
        for i in range((hc5 + 1) // taille_de_carres):
            grille1[y5 + i][x5] = 3
            plateau1.itemconfigure((y5 + i) * 10 + x5 + 1,
                                   fill="orange")
                      
    affichage_frame(frame_jeu)


def bordures_placement():
    global bordure_bouton_confirmer_placement
    bordure_bouton_confirmer_placement = Frame(frame_placement)
    bordure_bouton_confirmer_placement.place(relx = 0.5,
                                             rely = 0.9, 
                                             anchor = CENTER)


def bouton_placement():
    global bouton_confirmer_placement
    bouton_confirmer_placement = Button(bordure_bouton_confirmer_placement, 
                                        text = "Confirmer",
                                        width = 15,
                                        font = ("Oswald", 30),
                                        bg = "#d2d4d1",
                                        fg = "#fbfbfb",
                                        state = DISABLED, 
                                        command = confirmer)
    bouton_confirmer_placement.pack()


def label_placement():
    global alerte_placement
    alerte_placement = Label(frame_placement,
                             height = 1,
                             width = 30,
                             font = ("Oswald", 30),
                             text = "Veuillez placer votre armée")
    alerte_placement.place(relx = 0.5,
                           rely = 0.1,
                           anchor = CENTER)
    
    
def plateau_placement():
    global plateau_placement
    plateau_placement = Canvas(frame_placement,
                               width = dimension, 
                               height = dimension,
                               highlightthickness = 0,
                               bg = "red")
    plateau_placement.place(x = dep_x, y = dep_y)
        
    
def quadrillage_plateau_placement():
    for i in range(nombre_de_carres):
        for j in range(nombre_de_carres):
            x, y = taille_de_carres * j, taille_de_carres * i 
            A, B = (x, y), (x + taille_de_carres, y + taille_de_carres)
            plateau_placement.create_rectangle(A, B, fill="#097ade") 
            
            
def bateaux_placement():
    # Modif le nom des bateaux
    global canvas1
    canvas1 = Canvas(frame_placement, bg = "gray", width=taille_de_carres-1, height=taille_de_carres*2-1, bd = 0, highlightthickness = 0)
    canvas1.place(x = 950, y = 390)
    global canvas2
    canvas2 = Canvas(frame_placement, bg = "green", width=taille_de_carres-1, height=taille_de_carres*3-1, bd = 0, highlightthickness = 0)
    canvas2.place(x = 1100, y = 390)
    global canvas3
    canvas3 = Canvas(frame_placement, bg = "yellow", width=taille_de_carres-1, height=taille_de_carres*3-1, bd = 0, highlightthickness = 0)
    canvas3.place(x = 1250, y = 390)
    global canvas4
    canvas4 = Canvas(frame_placement, bg = "blue", width=taille_de_carres-1, height=taille_de_carres*4-1, bd = 0, highlightthickness = 0)
    canvas4.place(x = 1400, y = 390)
    global canvas5
    canvas5 = Canvas(frame_placement, bg = "orange", width=taille_de_carres-1, height=taille_de_carres*5-1, bd = 0, highlightthickness = 0)
    canvas5.place(x = 1550, y = 390)
    

def bind_placement():
    canvas1.bind("<Button-1>", drag_start)    
    canvas1.bind("<Button-3>", spiderman_do_a_flip)
    
    canvas2.bind("<Button-1>", drag_start)
    canvas2.bind("<Button-3>", spiderman_do_a_flip)
        
    canvas3.bind("<Button-1>", drag_start)
    canvas3.bind("<Button-3>", spiderman_do_a_flip)
        
    canvas4.bind("<Button-1>", drag_start)
    canvas4.bind("<Button-3>", spiderman_do_a_flip)
        
    canvas5.bind("<Button-1>", drag_start)
    canvas5.bind("<Button-3>", spiderman_do_a_flip)


# --------------------------------------------------------------------------------------------------------------------------------    

# Création du Menu de jeu dans la Frame jeu
def ecran_jeu():
    boutons_jeu()
    labels_jeu()
    plateau_jeu1()
    plateau_jeu2()
    quadrillage_plateau_jeu1()
    quadrillage_plateau_jeu2()
    bind_jeu()
    
    
def boutons_jeu():
    global bouton1
    bouton1 = Button(frame_jeu, text="Rejouer", command=recommencer, state=DISABLED)
    bouton1.place(relx=0.5, rely=0.02, anchor='center')
    global bouton2
    bouton2 = Button(frame_jeu, text="Quitter", command=abandon_de_partie)
    bouton2.place(relx=0.5, rely=0.055, anchor='center')


def labels_jeu():
    global label1
    label1 = Label(frame_jeu, text="Votre tour", bg="green")
    label1.place(relx=0.5, rely=0.09, anchor='center')
    global label_victoire
    label_victoire = Label(frame_jeu, text="")
    label_victoire.place(relx=0.5, rely=0.12, anchor='center')
    global label_scoreboard
    label_scoreboard = Label(frame_jeu, text="SCORE:" + str(score))
    label_scoreboard.place(relx = 0.2, rely = 0.1, anchor = CENTER)   


# Réaction suite à un clic sur le plateau
def clic_plateau_jeu1(event):
    global tour
    print("tour=", tour)
    if tour == 1:
        i = event.y // taille_de_carres
        j = event.x // taille_de_carres
        if grille1[i][j] == 0:
            tour = 2
            grille1[i][j] = 1
            plateau1.itemconfigure(i * 10 + j + 1, fill="#eb4034")
            print(grille1)
            print("Ligne=", i + 1, "Colonne=", j + 1)
            label1['text'] = "Tour de l'adversaire"
            label1['bg'] = "red"
        elif grille1[i][j] == 3:
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


def clic_plateau_jeu2(event):
    global tour
    print("tour=", tour)
    if tour == 2:
        i = event.y // taille_de_carres
        j = event.x // taille_de_carres
        if grille2[i][j] == 0:
            tour = 1
            grille2[i][j] = 1
            plateau2.itemconfigure(i * 10 + j + 1, fill="#eb4034")
            print(grille2)
            print("Ligne=", i + 1, "Colonne=", j + 1)
            label1['text'] = "Votre tour"
            label1['bg'] = "green"
        elif grille1[i][j] == 3:
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
    
    
def plateau_jeu1():
    global plateau1
    plateau1 = Canvas(frame_jeu, width = dimension, height = dimension)
    plateau1.place(x=dep_x, y=dep_y)


def plateau_jeu2():
    global plateau2
    plateau2 = Canvas(frame_jeu, width = dimension, height = dimension)
    plateau2.place(x=920, y=dep_y)
    

def quadrillage_plateau_jeu1():
    for i in range(nombre_de_carres):
        for j in range(nombre_de_carres):
            x, y = taille_de_carres * j + 2, taille_de_carres * i + 2
            A, B = (x, y), (x + taille_de_carres, y + taille_de_carres)
            plateau1.create_rectangle(A, B, fill="#097ade")


def quadrillage_plateau_jeu2():
    for i in range(nombre_de_carres):
        for j in range(nombre_de_carres):
            x, y = taille_de_carres * j + 2, taille_de_carres * i + 2
            A, B = (x, y), (x + taille_de_carres, y + taille_de_carres)
            plateau2.create_rectangle(A, B, fill="#097ade")

      
def bind_jeu():
    plateau1.bind("<Button-1>", clic_plateau_jeu1)
    plateau2.bind("<Button-1>", clic_plateau_jeu2)
    
"""
Ces deux fonctions sont à améliorer (+ revoir le design)
"""
# Actualisation du score visuel et déblocage du bouton 'rejouer'
def test_victoire():
    global score
    vainqueur = victoire()
    if (vainqueur == 0):
        fin_de_partie()
        bouton1['state'] = NORMAL
        label_victoire['text'] = "VICTOIRE"
        score = score + 1
        label_scoreboard.config(text="SCORE:" + str(score))

# Réinitialisation des listes de listes (on replace les bateaux? on les laisse ainsi? 2 options différentes)
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


# --------------------------------------------------------------------------------------------------------------------------------    

# Appel de toutes les fonctions du programme permettant l'affichage complet du jeu
def affichage():    
    placement_frame()
    ecran_principal()
    ecran_personnalisation()
    ecran_placement()
    ecran_jeu()
