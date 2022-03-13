from inspect import Parameter
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser    


root=Tk()
root.title('Bataille Navale')
root.attributes('-fullscreen',True)

nb = ttk.Notebook(root)
nb.pack()

def select_jouer():
    global debut
    if debut==False:
        start()
        nb.hide(0)
        nb.select(4)
        debut=True
    else:
        nb.select(1)
        nb.hide(0)
        nb.hide(2)

def select_paramètres():
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
    
Base = Frame(nb, width=960, height=1000, bg="black")
Jeu = Frame(nb, width=960, height=1000)
Jeu2 = Frame(nb, width=960, height=1000)
Parametres = Frame(nb, width=960, height=1000)
Debut=Frame(nb,width=2000,height=2000)

Base.pack()
Jeu.pack()
Jeu2.pack()
Parametres.pack()
Debut.pack()

nb.add(Base)
nb.add(Jeu)
nb.add(Jeu2)
nb.add(Parametres)
nb.add(Debut)

Jouer = Button(Base, text="Jouer", command=select_jouer)
Options = Button(Base, text="Paramètres", command=select_paramètres)
Quitter = Button(Base, text="Quitter", command=root.quit)
Jouer.pack()
Options.pack()
Quitter.pack()

Plateau1 = Button(Jeu2, text="Retourner sur votre plateau", command=select_jouer)
Plateau2 = Button(Jeu, text="Observer le plateau de l'adversaire", command=select_plateau2)
Retour1 = Button(Jeu, text="Retour", command=select_retour)
Retour2 = Button(Jeu2, text="Retour", command=select_retour)
Retour3 = Button(Parametres, text="Retour", command=select_retour)
Plateau1.pack()
Plateau2.pack()
Retour1.pack()
Retour2.pack()
Retour3.pack()

nb.hide(1)
nb.hide(2)
nb.hide(3)
nb.hide(4)

global listeCouleur,matriceC1,matriceC2,L1,L2,rect,M1,currentLengthShip,debut,listeCouleurBoard,tailleBateau,compteur
tailleBateau=[5,4,3,3,2]
compteur=0
debut=False
currentLengthShip=5
listeCouleurBoard=["royal blue","limegreen"]
listeCouleur=["royal blue","yellow"]
matriceC1=[[0 for i in range(10)]for j in range(10)]
matriceC2=[[0 for i in range(10)]for j in range(10)]
L1=[[]for i in range(100)]
L2=[[]for i in range(100)]
M1=[[0 for i in range(10)] for j in range(10)]


cnv1 = Canvas(Jeu, width = 2000, height = 2000)
cnv2 = Canvas(Jeu2, width = 2000, height = 2000)
cnvParamètres = Canvas(Parametres, width = 2000, height = 2000)
cnvdebut=Canvas(Debut,width=2000,height=2000)
cnv1.pack()
cnv2.pack()
cnvdebut.pack()

#changer la couleur de la case en fonction du plateau de l'adversaire (pas encore fini)        
def colorier1(k):
    global matriceC1,listeCouleur,L1
    matriceC1[k%10][k//10]=1
    w1=Button(cnv1,bg=str(listeCouleur[int(matriceC1[k%10][k//10])]),command=lambda k=k: colorier1(k))
    L1[k][0].place_forget()
    L1[k][0]=w1
    w1.place(x=k//10*80+80,y=k%10*80+20,height=80,width=80)

#changer la couleur de la case en fonction du plateau de l'adversaire (pas encore fini)  
def colorier2(k):
    global matriceC2,listeCouleur,L2
    matriceC2[k%10][k//10]=1
    w2=Button(cnv2,bg=str(listeCouleur[int(matriceC2[k%10][k//10])]),command=lambda k=k: colorier2(k))
    L2[k][0].place_forget()
    L2[k][0]=w2
    w2.place(x=k//10*80+80,y=k%10*80+20,height=80,width=80)
       
#initialisation  
def start():
    global L1,L2,M1,listeCouleur,rect
    for i in range(10):
        for j in range(10):
            w1=Button(cnv1,bg=str(listeCouleur[int(matriceC1[i][j])]),command=lambda k=i*10+j: colorier1(k))
            w1.place(x=i*80+80,y=j*80+20,height=80,width=80)
            L1[i*10+j].append(w1)
            l2=cnv2.create_rectangle(i*80+560,j*80+20,i*80+640,j*80+100,fill="orange")
            l=cnvdebut.create_rectangle(i*80+500,j*80+20,i*80+500+80,j*80+20+80)
    rect=cnvdebut.create_rectangle(0,0,80*5,80,fill="red")

#plateau de début    


def clic(event):
    global rect
    if event.x>cnvdebut.coords(rect)[0] and event.x<cnvdebut.coords(rect)[2] and event.y>cnvdebut.coords(rect)[1] and event.y<cnvdebut.coords(rect)[3]:
        old[0]=event.x
        old[1]=event.y
    #en fonction du clic on refait le rectangle horizontalement ou verticalement
    t=cnvdebut.find_closest(0, 0)
    cnvdebut.delete(t[0])
    if event.num==1:
        rect=cnvdebut.create_rectangle(0,0,80*currentLengthShip,80,fill="red")
    else:
        rect=cnvdebut.create_rectangle(0,0,80,80*currentLengthShip,fill="red")

def glisser(event):
    #voir exo4 corrigé
    global rect
    if event.x>cnvdebut.coords(rect)[0] and event.x<cnvdebut.coords(rect)[2] and event.y>cnvdebut.coords(rect)[1] and event.y<cnvdebut.coords(rect)[3]:
        cnvdebut.move(rect, event.x-old[0], event.y-old[1])
        old[0]=event.x
        old[1]=event.y

def matrice(M):
    for i in range(10):
        for j in range(10):
            print(str(M1[i][j])+" ",end="")
        print("")
    print("")
def lacher(event):
    global rect,M1,currentLengthShip,tailleBateau,compteur
    x=int(cnvdebut.coords(rect)[0])//80
    y=int(cnvdebut.coords(rect)[1])//80
    flag=True
    if x>5 and x<16 and y>=0 and y<10:
        for i in range(currentLengthShip):
            #vérification pour voir si il n'y a pas déjà un carré
            if M1[y][x-6+i]==1:
                flag=False
        if flag==True:
            for i in range(currentLengthShip):
                M1[y][x-6+i]=1
                cnvdebut.create_rectangle(x*80+20+80*i,y*80+20,x*80+80+20+80*i,y*80+80+20,fill="limegreen")
    else:
        flag=False  
    #delete le rectangle pour le refaire de la bonne taille. Horizontal
    print(compteur)
    if compteur<4:
        if flag==True:
            compteur+=1
            currentLengthShip=tailleBateau[compteur]
        cnvdebut.move(rect,-cnvdebut.coords(rect)[0],-cnvdebut.coords(rect)[1])
        t=cnvdebut.find_closest(0, 0)
        cnvdebut.delete(t[0])
        rect=cnvdebut.create_rectangle(0,0,80*currentLengthShip,80,fill="red")
    else:
        if flag==True:
            for i in range(10):
                for j in range(10):
                    carre=cnv1.create_rectangle(j*80+1040,i*80+20,j*80+1120,i*80+80+20,fill=str(listeCouleurBoard[int(M1[i][j])]))
            nb.hide(4)
            nb.select(1)
        else:
            cnvdebut.move(rect,-cnvdebut.coords(rect)[0],-cnvdebut.coords(rect)[1])
            t=cnvdebut.find_closest(0, 0)
            cnvdebut.delete(t[0])
            rect=cnvdebut.create_rectangle(0,0,80*currentLengthShip,80,fill="red")

def lacher2(event):
    global rect,M1,currentLengthShip,tailleBateau,compteur
    x=int(cnvdebut.coords(rect)[0])//80
    y=int(cnvdebut.coords(rect)[1])//80
    flag=True
    if x>5 and x<16 and y>=0 and y<10:
        for i in range(currentLengthShip):
            #vérification pour voir si il n'y a pas déjà un carré
            if M1[y+i][x-6]==1:
                flag=False
        if flag==True:
            for i in range(currentLengthShip):
                M1[y+i][x-6]=1
                cnvdebut.create_rectangle(x*80+20,y*80+20+80*i,x*80+80+20,y*80+80+20+80*i,fill="limegreen")
    else:
        flag=False        
    #delete le rectangle pour le refaire de la bonne taille. Vertical
    if compteur<4:
        if flag==True:
            compteur+=1
            currentLengthShip=tailleBateau[compteur]
        cnvdebut.move(rect,-cnvdebut.coords(rect)[0],-cnvdebut.coords(rect)[1])
        t=cnvdebut.find_closest(0, 0)
        cnvdebut.delete(t[0])
        rect=cnvdebut.create_rectangle(0,0,80,80*currentLengthShip,fill="red")
    else:
        if flag==True:
            for i in range(10):
                for j in range(10):
                    carre=cnv1.create_rectangle(j*80+1040,i*80+20,j*80+1120,i*80+80+20,fill=str(listeCouleurBoard[int(M1[i][j])]))
            nb.hide(4)
            nb.select(1)
        else:
            cnvdebut.move(rect,-cnvdebut.coords(rect)[0],-cnvdebut.coords(rect)[1])
            t=cnvdebut.find_closest(0, 0)
            cnvdebut.delete(t[0])
            rect=cnvdebut.create_rectangle(0,0,80,80*currentLengthShip,fill="red")
    
old=[None,None]

cnvdebut.bind("<B1-Motion>",glisser)
cnvdebut.bind("<Button-1>",clic)
cnvdebut.bind("<ButtonRelease-1>",lacher)

cnvdebut.bind("<B3-Motion>",glisser)
cnvdebut.bind("<Button-3>",clic)
cnvdebut.bind("<ButtonRelease-3>",lacher2)



root.mainloop()

#arrondir x et y, diviser par 80.
#print(cnv.coords(rect)
