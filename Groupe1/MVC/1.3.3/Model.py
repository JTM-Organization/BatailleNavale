# -*- coding: utf-8 -*-


"""
GESTION DES DONNEES
"""


# Définition de la taille des carres du plateau
global TAILLE_DE_CARRES
TAILLE_DE_CARRES = 35

# Définition de la nombre de carres du plateau
global NOMBRE_DE_CARRES
NOMBRE_DE_CARRES = 10

# Définition de la dimension du plateau
global DIMENSION
DIMENSION = TAILLE_DE_CARRES * NOMBRE_DE_CARRES + 1

# Décalage (abscisse) du plateau de placement 
global DEP_X
DEP_X = 225

# Décalage (ordonnée) du plateau de placement
global DEP_Y
DEP_Y = 160

# Définition des matrices contenant les informations de l'état de la partie
global grille
grille1 = [[0 for colonne in range(NOMBRE_DE_CARRES)] for ligne in range(NOMBRE_DE_CARRES)]
grille2 = [[0 for colonne in range(NOMBRE_DE_CARRES)] for ligne in range(NOMBRE_DE_CARRES)]

# Définition du score
global score
score = 0

global vainqueur
vainqueur = 0

global tour
tour = 2

global niv_facile
global niv_moyen
global niv_difficile
niv_facile = False
niv_moyen = False
niv_difficile = False

global flag_partie_prete
flag_partie_prete = False

def reInitialisation():
    for i in range(NOMBRE_DE_CARRES):
        for j in range(NOMBRE_DE_CARRES):
            grille1[i][j] = 0
            grille2[i][j] = 0
    global vainqueur
    vainqueur = 1


def abandon_de_partie():
    root.quit()


def victoire1():
    global vainqueur
    vainqueur = 0
    for i in range(NOMBRE_DE_CARRES):
        for j in range(NOMBRE_DE_CARRES):
            if grille1[i][j] == 2:
                vainqueur += 1
    if vainqueur == 17:
        return True
    else:
        return False

def victoire2():
    global vainqueur
    vainqueur = 0
    for i in range(NOMBRE_DE_CARRES):
        for j in range(NOMBRE_DE_CARRES):
            if grille2[i][j] == 2:
                vainqueur += 1
    if vainqueur == 17:
        return True
    else:
        return False


def fin_de_partie():
    global flag_partie_prete
    for i in range(NOMBRE_DE_CARRES):
        for j in range(NOMBRE_DE_CARRES):
            grille1[i][j] = 4
            grille2[i][j] = 4
    flag_partie_prete = False
