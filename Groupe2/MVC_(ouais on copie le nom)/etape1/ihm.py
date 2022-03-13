from modele import *

Base = Frame(nb, width=largeur, height=hauteur, bg="black")
Plateau = Frame(nb, width=largeur, height=hauteur)
Parametres = Frame(nb, width=largeur, height=hauteur,bg="#AAAAAA")

Base.pack()
Plateau.pack()
Parametres.pack()

nb.add(Base)
nb.add(Plateau)
nb.add(Parametres)

def select_jouer():
    nb.select(1)
    nb.hide(0)
    nb.hide(2)

def select_paramètres():
    nb.select(2)
    nb.hide(0)

    
def select_retour():
    nb.select(0)
    nb.hide(1)
    nb.hide(2)

Jouer = Button(Base, text="Jouer", command=select_jouer)
Options = Button(Base, text="Paramètres", command=select_paramètres)
Quitter = Button(Base, text="Quitter", command=root.quit)
Jouer.pack()
Options.pack()
Quitter.pack()


Retour1 = Button(Plateau, text="Retour", command=select_retour)
Retour3 = Button(Parametres, text="Retour", command=select_retour)
Retour1.pack()
Retour3.pack()

nb.hide(1)
nb.hide(2)




cnv1 = Canvas(Plateau, width = largeur, height = hauteur)
cnvParametres = Canvas(Parametres, width = largeur, height = hauteur)

cnv1.pack()
cnvParametres.pack()
    
def colorier1(k):
    global matriceC1,listeCouleur,L1
    matriceC1[k%10][k//10]=1
    w1=Button(cnv1,bg=str(listeCouleur[int(matriceC1[k%10][k//10])]),command=lambda k=k: colorier1(k))
    L1[k][0].place_forget()
    L1[k][0]=w1
    w1.place(x=k//10*taille+taille,y=k%10*taille+20,height=taille,width=taille)

def start():
    global L1,L2,M1,listeCouleur,rect,taille
    for i in range(10):
        for j in range(10):
            w1=Button(cnv1,bg=str(listeCouleur[int(matriceC1[i][j])]),command=lambda k=i*10+j: colorier1(k))
            w1.place(x=i*taille+taille,y=j*taille+20,height=taille,width=taille)
            L1[i*10+j].append(w1)
            plateauJoueur=cnv1.create_rectangle(i*taille+taille*14,j*taille+20,i*taille+taille*14+taille,j*taille+20+taille,fill="#5000AA")
    labelJ = Label(cnv1, text='Votre plateau')
    labelJ.place(x=5.5*taille,y=10*taille+taille/2,height=30,width=90)
    labelA = Label(cnv1, text='Plateau adverse') 
    labelA.place(x=18.5*taille,y=10*taille+taille/2,height=30,width=90)
