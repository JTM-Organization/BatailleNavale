# -*- coding: utf-8 -*-

# Gestion de Données
from tkinter import *


global TAILLE_DE_CARRES
TAILLE_DE_CARRES = 35

global NOMBRE_DE_CARRES
NOMBRE_DE_CARRES = 10

global DIMENSION
DIMENSION = TAILLE_DE_CARRES * NOMBRE_DE_CARRES + 1

global DEP_X
DEP_X = 225

global DEP_Y
DEP_Y = 160

global grille
grille1 = [[0 for colonne in range(NOMBRE_DE_CARRES)] for ligne in range(NOMBRE_DE_CARRES)]
grille2 = [[0 for colonne in range(NOMBRE_DE_CARRES)] for ligne in range(NOMBRE_DE_CARRES)]

global score
score = 0

global vainqueur
vainqueur = 0

global tour
tour = 2

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
    for i in range(NOMBRE_DE_CARRES):
        for j in range(NOMBRE_DE_CARRES):
            grille1[i][j] = 4
            grille2[i][j] = 4
