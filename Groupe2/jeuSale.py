from tkinter import *
from tkinter import ttk

#Optimiser le design, gérer les variables de fenêtres...

root=Tk()
root.title('Bataille Navale')
root.geometry("800x800")
root.minsize(500,500)

nb = ttk.Notebook(root)
nb.pack()

def select_jouer():
    nb.select(1)
    nb.hide(0)
    nb.hide(2)

def select_réglages():
    nb.select(3)
    nb.hide(0)
    
def select_plateau2():
    nb.select(2)
    nb.hide(1)
    
def select_retour():
    nb.select(0)
    nb.hide(1)
    nb.hide(2)
    nb.hide(3)
    
Base = Frame(nb, width=800, height=800, bg="black")
Jeu = Frame(nb, width=800, height=800)
Jeu2 = Frame(nb, width=800, height=800)
Réglages = Frame(nb, width=800, height=800)
Base.pack()
Jeu.pack()
Jeu2.pack()
Réglages.pack()

nb.add(Base)
nb.add(Jeu)
nb.add(Jeu2)
nb.add(Réglages)

Jouer = Button(Base, text="Jouer", command=select_jouer)
Options = Button(Base, text="Options", command=select_réglages)
Quitter = Button(Base, text="Quitter", command=root.quit)
Jouer.pack()
Options.pack()
Quitter.pack()

Plateau1 = Button(Jeu2, text="Retourner sur votre plateau", command=select_jouer)
Plateau2 = Button(Jeu, text="Observer le plateau de l'adversaire", command=select_plateau2)
Retour1 = Button(Jeu, text="Retour", command=select_retour)
Retour2 = Button(Jeu2, text="Retour", command=select_retour)
Retour3 = Button(Réglages, text="Retour", command=select_retour)
Plateau1.pack()
Plateau2.pack()
Retour1.pack()
Retour2.pack()
Retour3.pack()

nb.hide(1)
nb.hide(2)
nb.hide(3)



global largeur,hauteur
largeur = hauteur = 800


global listeCouleur,matriceC1,matriceC2,L1,L2

listeCouleur=["royal blue","yellow"]

matriceC1=[[0 for i in range(10)]for j in range(10)]
matriceC2=[[0 for i in range(10)]for j in range(10)]
L1=[[]for i in range(100)]
L2=[[]for i in range(100)]


        
def colorier1(k):
    global matriceC1,listeCouleur,L1
    matriceC1[k%10][k//10]=1
    w1=Button(cnv1,bg=str(listeCouleur[int(matriceC1[k%10][k//10])]),command=lambda k=k: colorier1(k))
    L1[k][0].place_forget()
    L1[k][0]=w1
    w1.place(x=k//10*80,y=k%10*80,height=80,width=80)

def colorier2(k):
    global matriceC2,listeCouleur,L2
    matriceC2[k%10][k//10]=1
    w2=Button(cnv2,bg=str(listeCouleur[int(matriceC2[k%10][k//10])]),command=lambda k=k: colorier2(k))
    L2[k][0].place_forget()
    L2[k][0]=w2
    w2.place(x=k//10*80,y=k%10*80,height=80,width=80)
       
cnv1 = Canvas(Jeu, width = largeur, height = hauteur)
cnv2 = Canvas(Jeu2, width = largeur, height = hauteur)
cnv1.pack()
cnv2.pack()

for i in range(10):
    for j in range(10):
        w1=Button(cnv1,bg=str(listeCouleur[int(matriceC1[i][j])]),command=lambda k=i*10+j: colorier1(k))
        w1.place(x=i*80,y=j*80,height=80,width=80)
        w2=Button(cnv2,bg=str(listeCouleur[int(matriceC2[i][j])]),command=lambda k=i*10+j: colorier2(k))
        w2.place(x=i*80,y=j*80,height=80,width=80)       
        L1[i*10+j].append(w1)
        L2[i*10+j].append(w2)
        



root.mainloop()
