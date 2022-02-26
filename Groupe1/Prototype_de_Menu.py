from tkinter import *
from tkinter import ttk

#Optimiser le design, gérer les variables de fenêtres...

root=Tk()
root.title('Bataille Navale')
root.geometry("1000x1000")
root.minsize(500,500)

nb = ttk.Notebook(root)
nb.pack()

def select_jouer():
    nb.select(1)
    nb.hide(0)

def select_réglages():
    nb.select(2)
    nb.hide(0)
    
def select_retour():
    nb.select(0)
    nb.hide(1)
    nb.hide(2)
    
Base = Frame(nb, width=1000, height=1000, bg="black")
Jeu = Frame(nb, width=1000, height=1000)
Réglages = Frame(nb, width=1000, height=1000)
Base.pack()
Jeu.pack()
Réglages.pack()

nb.add(Base)
nb.add(Jeu)
nb.add(Réglages)

Jouer = Button(Base, text="Jouer", command=select_jouer)
Options = Button(Base, text="Options", command=select_réglages)
Quitter = Button(Base, text="Quitter", command=root.quit)
Jouer.pack()
Options.pack()
Quitter.pack()

Retour1 = Button(Jeu, text="Retour", command=select_retour)
Retour2 = Button(Réglages, text="Retour", command=select_retour)
Retour1.pack()
Retour2.pack()

nb.hide(1)
nb.hide(2)

cnv=Canvas(Jeu, width=500, height=500, bg='ivory')
cnv.pack()

for i in range(10):
    for j in range(10):
        x, y = 50*j, 50*i
        A, B = (x,y), (x+50, y+50)
        cnv.create_rectangle(A, B, fill="royal blue")

root.mainloop()
