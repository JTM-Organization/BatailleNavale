from modele import *

Base = Frame(nb, width=largeur, height=hauteur, bg="black")
Plateau = Frame(nb, width=largeur, height=hauteur)
Parametres = Frame(nb, width=largeur, height=hauteur,bg="#AAAAAA")
Debut=Frame(nb,width=largeur,height=hauteur)
Base.pack()
Plateau.pack()
Parametres.pack()
Debut.pack()

nb.add(Base)
nb.add(Plateau)
nb.add(Parametres)
nb.add(Debut)

def select_jouer():
    global debut
    if debut==False:
        
        start()
        plateauBotAléatoire()
        nb.hide(0)
        nb.select(3)
        debut=True
        
    else:
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
cnvdebut=Canvas(Debut,width=largeur,height=hauteur)

cnv1.pack()
cnvParametres.pack()
cnvdebut.pack()

def tirerJoueur(k):
    global M2,listeCouleur,L1,M1
    if M2[k%10][k//10]==0:
        M2[k%10][k//10]=2
    w1=Button(cnv1,bg=str(listeCouleur[int(M2[k%10][k//10])]),command=lambda k=k: tirerJoueur(k))
    L1[k][0].place_forget()
    L1[k][0]=w1
    w1.place(x=(k//10+1)*taille+taille,y=k%10*taille+20,height=taille,width=taille)
    #placer coord ici
    if M2[k%10][k//10]==1:
        labelTouche=Label(cnv1,text="touché")
        labelTouche.place(x=taille*14,y=taille*6,height=taille,width=taille*1.5)
    else:
        labelTouche=Label(cnv1,text="à l'eau")
        labelTouche.place(x=taille*14,y=taille*6,height=taille,width=taille*1.5)
    x=random.randint(0,9)
    y=random.randint(0,9)
    if M1[x][y]==0:
        M1[x][y]=2
        labelTouche=Label(cnv1,text="à l'eau")
        labelTouche.place(x=taille*14,y=taille*6,height=taille,width=taille*1.5)
    elif M1[x][y]==1:
        M1[x][y]=3
        labelTouche=Label(cnv1,text="touché")
        labelTouche.place(x=taille*14,y=taille*6,height=taille,width=taille*1.5)
    t=cnv1.find_closest(y*taille+taille*18.5, x*taille+20+taille*0.5)
    cnv1.delete(t[0])
    carre=cnv1.create_rectangle(y*taille+taille*18,x*taille+20,y*taille+taille*19,(x+1)*taille+20,fill=str(listeCouleurBoard[int(M1[x][y])]))
    
def start():
    global L1,listeCouleur,taille,lettre,rect,M2
    for i in range(10):
        for j in range(10):
            w1=Button(cnv1,bg="royal blue",command=lambda k=i*10+j: tirerJoueur(k))
            w1.place(x=(i+1)*taille+taille,y=j*taille+20,height=taille,width=taille)
            L1[i*10+j].append(w1)
            l=cnvdebut.create_rectangle(i*80+500,j*80+20,i*80+500+80,j*80+20+80)
        for k in range(2):
            labelChiffre= Label(cnv1,text=str(i+1))
            labelChiffre.place(x=(i+1)*taille+taille*1.3+(k*taille*16),y=-5)
            labelLettre=Label(cnv1,text=lettre[i])
            labelLettre.place(x=3*taille/2+(k*taille*16),y=i*taille+taille*0.8)
    rect=cnvdebut.create_rectangle(0,0,80*5,80,fill="red")

    labelJ = Label(cnv1, text='Votre plateau de tir')
    labelJ.place(x=6*taille,y=10*taille+taille/2,height=30,width=120)

    labelA = Label(cnv1, text='Votre plateau') 
    labelA.place(x=22.3*taille,y=10*taille+taille/2,height=30,width=90)


def drawRect(hOuV):
    global currentLengthShip,rect
    if hOuV==1:
        rect=cnvdebut.create_rectangle(0,0,80,80*currentLengthShip,fill="red")
    else:
        rect=cnvdebut.create_rectangle(0,0,80*currentLengthShip,80,fill="red")

def supprimerRect():
    t=cnvdebut.find_closest(0, 0)
    cnvdebut.delete(t[0])

def clic(event):
    global rect,hOuV,pasBouger
    if event.x>cnvdebut.coords(rect)[0] and event.x<cnvdebut.coords(rect)[2] and event.y>cnvdebut.coords(rect)[1] and event.y<cnvdebut.coords(rect)[3]:
        old[0]=event.x
        old[1]=event.y
        pasBouger=True

def clic2(event):
    global rect,hOuV,pasBouger
    if pasBouger==False:
        if event.x>cnvdebut.coords(rect)[0] and event.x<cnvdebut.coords(rect)[2] and event.y>cnvdebut.coords(rect)[1] and event.y<cnvdebut.coords(rect)[3]:
            supprimerRect()
            if hOuV==0:
                rect=cnvdebut.create_rectangle(0,0,80,80*currentLengthShip,fill="red")
                hOuV+=1
            else:
                rect=cnvdebut.create_rectangle(0,0,80*currentLengthShip,80,fill="red")
                hOuV-=1

def glisser(event):
    #voir exo4 corrigé
    global rect
    if event.x>cnvdebut.coords(rect)[0] and event.x<cnvdebut.coords(rect)[2] and event.y>cnvdebut.coords(rect)[1] and event.y<cnvdebut.coords(rect)[3]:
        cnvdebut.move(rect, event.x-old[0], event.y-old[1])
        old[0]=event.x
        old[1]=event.y


def lacher(event):
    global rect,M1,currentLengthShip,tailleBateau,compteur,pasBouger
    x=int(cnvdebut.coords(rect)[0])//80
    y=int(cnvdebut.coords(rect)[1])//80
    flag=True
    if x>5 and x<16 and y>=0 and y<10:
        for i in range(currentLengthShip):
            #vérification pour voir si il n'y a pas déjà un carré
            if hOuV==1:
                if M1[y+i][x-6]==1:
                    flag=False
            else:
                if M1[y][x-6+i]==1:
                    flag=False
        if flag==True:
            if hOuV==1:
                for i in range(currentLengthShip):
                    M1[y+1][x-6]=1
                    cnvdebut.create_rectangle(x*80+20,y*80+20+80*i,x*80+80+20,y*80+80+20+80*i,fill="limegreen")
            else:
                for i in range(currentLengthShip):
                    M1[y][x-6+i]=1
                    cnvdebut.create_rectangle(x*80+20+80*i,y*80+20,x*80+80+20+80*i,y*80+80+20,fill="limegreen")
    else:
        flag=False
    #delete le rectangle pour le refaire de la bonne taille
    if compteur<4:
        if flag==True:
            compteur+=1
            currentLengthShip=tailleBateau[compteur]
        cnvdebut.move(rect,-cnvdebut.coords(rect)[0],-cnvdebut.coords(rect)[1])
        supprimerRect()
        drawRect(hOuV)
    else:
        if flag==True:
            for i in range(10):
                for j in range(10):
                    carre=cnv1.create_rectangle(j*taille+taille*18,i*taille+20,j*taille+taille*19,(i+1)*taille+20,fill=str(listeCouleurBoard[int(M1[i][j])]))
            nb.hide(3)
            nb.select(1)
        else:
            cnvdebut.move(rect,-cnvdebut.coords(rect)[0],-cnvdebut.coords(rect)[1])
            supprimerRect()
            drawRect(hOuV)
    pasBouger=False

old=[None,None]
cnvdebut.bind("<Button-1>",clic)
cnvdebut.bind("<B1-Motion>",glisser)
cnvdebut.bind("<ButtonRelease-1>",lacher)
cnvdebut.bind("<Button-3>",clic2)

def plateauBotAléatoire():
    global tailleBateau,M2
    compteur=0
    tailleB=0
    while compteur<5:
        flag=True
        x=random.randint(0,9)
        y=random.randint(0,9)
        orientation=random.randint(0,1)
        tailleB=tailleBateau[compteur]
        if orientation==0:
            if y+tailleB<10:
                for i in range(tailleB):
                    if M2[x][y+i]==1:
                        flag=False
            else:
                flag=False
            if flag==True:
                for i in range(tailleB):
                    M2[x][y+i]=1
                compteur+=1
        else:
            if x+tailleB<10:
                for i in range(tailleB):
                    if M2[x+i][y]==1:
                        flag=False
            else:
                flag=False
            if flag==True:
                for i in range(tailleB):
                    M2[x+i][y]=1
                compteur+=1



