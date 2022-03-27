from modele import *

Base = Frame(nb, width=largeur, height=hauteur, bg="black")
Plateau = Frame(nb, width=largeur, height=hauteur)
Parametres = Frame(nb, width=largeur, height=hauteur,bg="#AAAAAA")
Debut=Frame(nb,width=largeur,height=hauteur)
Fin=Frame(nb,width=largeur,height=hauteur)
Base.pack()
Plateau.pack()
Parametres.pack()
Debut.pack()
Fin.pack()

nb.add(Base)
nb.add(Plateau)
nb.add(Parametres)
nb.add(Debut)
nb.add(Fin)

def select_jouer():
    global debut
    if debut==False:
        
        start()
        plateauBotAleatoire()
        nb.hide(0)
        nb.select(3)
        debut=True
        
    else:
        reecrire()
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
nb.hide(3)


cnv1 = Canvas(Plateau, width = largeur, height = hauteur,bg='grey')
cnvParametres = Canvas(Parametres, width = largeur, height = hauteur)
cnvdebut=Canvas(Debut,width=largeur,height=hauteur,bg='grey')
cnvfin=Canvas(Fin,width=largeur,height=hauteur,bg='grey')

cnv1.pack()
cnvParametres.pack()
cnvdebut.pack()
cnvfin.pack()

def tirerJoueur(k):
    global M2,listeCouleur,L1,M1,victoireJoueur,victoireBot,testVictoire,lettre
    if M2[k%10][k//10]==0:
        M2[k%10][k//10]=2
    L1[k][0].destroy()
    L1[k][0]=69
    x=(k//10+1)*taille+taille
    y=k%10*taille+40
    w2=cnv1.create_rectangle(x,y,x+taille,y+taille,fill=str(listeCouleur[int(M2[k%10][k//10])]))
    if M2[k%10][k//10]==1:
        labelTouche=Label(cnv1,text="Vous tirez sur la case \n"+lettre[k//10]+str(k%10)+": touchée",bg='grey')
        labelTouche.place(x=taille*13.5,y=taille*3,height=taille,width=taille*3)
        victoireJoueur-=1
        if victoireJoueur==0:
            victoire("joueur")
    else:
        labelTouche=Label(cnv1,text="Vous tirez sur la case \n"+lettre[k//10]+str(k%10)+": à l'eau",bg='grey')
        labelTouche.place(x=taille*13.5,y=taille*3,height=taille,width=taille*3)
    flag=True
    if testVictoire:
        flag=False
    while flag:
        ordonnee=random.randint(0,9)
        abscisse=random.randint(0,9)
        if M1[ordonnee][abscisse]==0:
            M1[ordonnee][abscisse]=2
            labelToucheBot=Label(cnv1,text="Le bot a tiré sur la case \n"+lettre[ordonnee]+str(abscisse)+": à l'eau",bg='grey')
            labelToucheBot.place(x=taille*13.5,y=taille*5,height=taille,width=taille*3)
            flag=False
        elif M1[ordonnee][abscisse]==1:
            M1[ordonnee][abscisse]=3
            labelToucheBot=Label(cnv1,text="Le bot a tiré sur la case \n"+lettre[ordonnee]+str(abscisse)+": touchée",bg='grey')
            labelToucheBot.place(x=taille*13.5,y=taille*5,height=taille,width=taille*3)
            victoireBot-=1
            flag=False
            if victoireBot==0:
                victoire("bot")
        t=cnv1.find_closest(abscisse*taille+taille*18.5, ordonnee*taille+20+taille*0.5)
        cnv1.delete(t[0])
        carre=cnv1.create_rectangle(abscisse*taille+taille*18,ordonnee*taille+40,abscisse*taille+taille*19,(ordonnee+1)*taille+40,fill=str(listeCouleurBoard[int(M1[ordonnee][abscisse])]))
    
def victoire(participant):
    global testVictoire
    testVictoire=False
    nb.hide(1)
    nb.select(4)
    if participant=="joueur":
        labelFin=Label(cnvfin,text="Victoire du joueur",bg='grey')
    else:
        labelFin=Label(cnvfin,text="Victoire du bot",bg='grey')
    labelFin.place(x=taille*14,y=taille*6.5)

def start():
    global L1,listeCouleur,taille,lettre,listeBateau
    for i in range(10):
        for j in range(10):
            w1=Button(cnv1,bg="royal blue",command=lambda k=i*10+j: tirerJoueur(k))
            w1.place(x=(i+1)*taille+taille,y=j*taille+40,height=taille,width=taille)
            L1[i*10+j].append(w1)
            l=cnvdebut.create_rectangle(i*80+500,j*80+20,i*80+500+80,j*80+20+80)
        for k in range(2):
            labelChiffre= Label(cnv1,text=str(i+1),bg='grey')
            labelChiffre.place(x=(i+1)*taille+taille*1.3+(k*taille*16),y=15)
            labelLettre=Label(cnv1,text=lettre[i],bg='grey')
            labelLettre.place(x=3*taille/2+(k*taille*16),y=i*taille+taille*0.8+20)
    rect0=cnvdebut.create_rectangle(0,100,80*5,180,fill="red")
    rect1=cnvdebut.create_rectangle(0,200,80*4,280,fill="red")
    rect2=cnvdebut.create_rectangle(0,300,80*3,380,fill="red")
    rect3=cnvdebut.create_rectangle(0,400,80*3,480,fill="red")
    rect4=cnvdebut.create_rectangle(0,500,80*2,580,fill="red")
    listeBateau=[rect0,rect1,rect2,rect3,rect4]

    labelJ = Label(cnv1, text='Votre plateau de tir',bg='grey')
    labelJ.place(x=6*taille,y=10*taille+taille/2+30,height=30,width=120)
    labelA = Label(cnv1, text='Votre plateau',bg='grey') 
    labelA.place(x=22.3*taille,y=10*taille+taille/2+30,height=30,width=90)

def clic(event):
    global listeBateau,bateau
    for i in range(5):
        if event.x>cnvdebut.coords(listeBateau[i])[0] and event.x<cnvdebut.coords(listeBateau[i])[2] and event.y>cnvdebut.coords(listeBateau[i])[1] and event.y<cnvdebut.coords(listeBateau[i])[3]:
            old[0]=event.x
            old[1]=event.y
            bateau=i

def clic2(event):
    global horizOuVertical,listeBateau,tailleBateau
    bateauClic=42
    flag=True
    for i in range(5):
        if event.x>cnvdebut.coords(listeBateau[i])[0] and event.x<cnvdebut.coords(listeBateau[i])[2] and event.y>cnvdebut.coords(listeBateau[i])[1] and event.y<cnvdebut.coords(listeBateau[i])[3]:
            bateauClic=i
    if(bateauClic!=42):
        x1,y1,x2,y2=cnvdebut.coords(listeBateau[bateauClic])
        for j in range(5):
            if j!=bateauClic:
                k=tailleBateau[bateauClic]
                if horizOuVertical[bateauClic]==0:
                    if (x1>cnvdebut.coords(listeBateau[j])[0] and x1<cnvdebut.coords(listeBateau[j])[2]) or (x1+80>cnvdebut.coords(listeBateau[j])[0] and x1+80<cnvdebut.coords(listeBateau[j])[2]) or ((x1<cnvdebut.coords(listeBateau[j])[0]) and (x1+80>cnvdebut.coords(listeBateau[j])[0])) or ((x1<cnvdebut.coords(listeBateau[j])[2]) and (x1+80>cnvdebut.coords(listeBateau[j])[2])):
                        if (y1>cnvdebut.coords(listeBateau[j])[1] and y1<cnvdebut.coords(listeBateau[j])[3]) or (y1+80*k>cnvdebut.coords(listeBateau[j])[1] and y1+80*k<cnvdebut.coords(listeBateau[j])[3]) or ((y1<cnvdebut.coords(listeBateau[j])[1]) and (x1+80*k>cnvdebut.coords(listeBateau[j])[1])) or ((x1<cnvdebut.coords(listeBateau[j])[3]) and (x1+80*k>cnvdebut.coords(listeBateau[j])[3])):         
                            flag=False
                else:
                    if (x1>cnvdebut.coords(listeBateau[j])[0] and x1<cnvdebut.coords(listeBateau[j])[2]) or (x1+80*k>cnvdebut.coords(listeBateau[j])[0] and x1+80*k<cnvdebut.coords(listeBateau[j])[2]) or ((x1<cnvdebut.coords(listeBateau[j])[0]) and (x1+80*k>cnvdebut.coords(listeBateau[j])[0])) or ((x1<cnvdebut.coords(listeBateau[j])[2]) and (x1+80*k>cnvdebut.coords(listeBateau[j])[2])):
                        if (y1>cnvdebut.coords(listeBateau[j])[1] and y1<cnvdebut.coords(listeBateau[j])[3]) or (y1+80>cnvdebut.coords(listeBateau[j])[1] and y1+80<cnvdebut.coords(listeBateau[j])[3]) or ((y1<cnvdebut.coords(listeBateau[j])[1]) and (x1+80>cnvdebut.coords(listeBateau[j])[1])) or ((x1<cnvdebut.coords(listeBateau[j])[3]) and (x1+80>cnvdebut.coords(listeBateau[j])[3])):            
                            flag=False
        if flag==True:
            if horizOuVertical[bateauClic]==0:
                cnvdebut.coords(listeBateau[bateauClic],x1,y1,x1+80,y1+80*tailleBateau[bateauClic])
                horizOuVertical[bateauClic]=1
            else:   
                cnvdebut.coords(listeBateau[bateauClic],x1,y1,x1+80*tailleBateau[bateauClic],y1+80)
                horizOuVertical[bateauClic]=0

def glisser(event):
    global listeBateau,bateau
    if event.x>cnvdebut.coords(listeBateau[bateau])[0] and event.x<cnvdebut.coords(listeBateau[bateau])[2] and event.y>cnvdebut.coords(listeBateau[bateau])[1] and event.y<cnvdebut.coords(listeBateau[bateau])[3]:
        cnvdebut.move(listeBateau[bateau], event.x-old[0], event.y-old[1])
        old[0]=event.x
        old[1]=event.y

def lacher(event):
    global listeBateau,M1,tailleBateau,compteurBateau,horizOuVertical,bateau
    x=int(cnvdebut.coords(listeBateau[bateau])[0])//80
    y=int(cnvdebut.coords(listeBateau[bateau])[1])//80
    x1,y1,x2,y2=cnvdebut.coords(listeBateau[bateau])
    placerCarre=True
    testPos=True
    flag2=True
    if horizOuVertical[bateau]==1:
        if x>5 and x<16 and y>=0 and y+tailleBateau[bateau]-1<10:
            testPlacer()
        else:
            placerCarre=False
            testPos=False
    elif horizOuVertical[bateau]==0:
        if x>5 and x+tailleBateau[bateau]-1<16 and y>=0 and y<10:
            testPos=testPlacer()
        else:
            placerCarre=False
            testPos=False
        #dessin
    if testPos==True and placerCarre:
        if horizOuVertical[bateau]==1:
            cnvdebut.coords(listeBateau[bateau],x*80+20,y*80+20,x*80+20+80,y*80+20+tailleBateau[bateau]*80)
        else:
            cnvdebut.coords(listeBateau[bateau],x*80+20,y*80+20,x*80+20+tailleBateau[bateau]*80,y*80+20+80)
    #compteur et si bateau pas dedans append
    for contient in range(len(compteurBateau)):
        if compteurBateau[contient]==bateau:
            flag2=False
    if flag2==True:
        compteurBateau.append(bateau)
    #changer compteur
    if not(testPos):
        if compteurBateau.__contains__(bateau):
            compteurBateau.remove(bateau)
            buttonCommencer.place_forget()
    #afficher le bouton
    if len(compteurBateau)>4 and testPos==True:
        buttonCommencer.place(x=300,y=390,width=120,height=80)
    
def testPlacer():
    global listeBateau,bateau
    flag=True
    x1,y1,x2,y2=cnvdebut.coords(listeBateau[bateau])     
    for i in range(5):
        if i!=bateau:
            if (x1>cnvdebut.coords(listeBateau[i])[0] and x1<cnvdebut.coords(listeBateau[i])[2]) or (x2>cnvdebut.coords(listeBateau[i])[0] and x2<cnvdebut.coords(listeBateau[i])[2]):
                if (y1>cnvdebut.coords(listeBateau[i])[1] and y1<cnvdebut.coords(listeBateau[i])[3]) or (y2>cnvdebut.coords(listeBateau[i])[1] and y2<cnvdebut.coords(listeBateau[i])[3]):
                    flag=False
    return flag

old=[None,None]
cnvdebut.bind("<Button-1>",clic)
cnvdebut.bind("<B1-Motion>",glisser)
cnvdebut.bind("<ButtonRelease-1>",lacher)
cnvdebut.bind("<Button-3>",clic2)

def placerBateau():
    global horizOuVertical,listeBateau,tailleBateau
    for i in range(5):
        x1,y1,x2,y2=cnvdebut.coords(listeBateau[i])
        if horizOuVertical[i]==1:
            for j in range(tailleBateau[i]):
                M1[int(y1//80+j)][int(x1//80-6)]=1
        else:
            for j in range(tailleBateau[i]):
                M1[int(y1//80)][int(x1//80-6+j)]=1
    for i in range(10):
        for j in range(10):
            carre=cnv1.create_rectangle(j*taille+taille*18,i*taille+40,j*taille+taille*19,(i+1)*taille+40,fill=str(listeCouleurBoard[int(M1[i][j])]))
    nb.hide(3)
    nb.select(1)

buttonCommencer=Button(cnvdebut,text="commencer la partie",command=placerBateau,bg='grey')
buttonCommencer.place(x=300,y=390,width=120,height=80)
buttonCommencer.place_forget()

def plateauBotAleatoire():
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


def choose_color1():
    global listeCouleur
    color_code = colorchooser.askcolor(title ="Choose color") 
    listeCouleur[0]=color_code[1]
    
def choose_color2():
    global listeCouleur
    color_code = colorchooser.askcolor(title ="Choose color") 
    listeCouleur[1]=color_code[1]

def choose_color3():
    global listeCouleur
    color_code = colorchooser.askcolor(title ="Choose color") 
    listeCouleur[2]=color_code[1]

def choose_color4():
    global listeCouleurBoard
    color_code = colorchooser.askcolor(title ="Choose color") 
    listeCouleurBoard[0]=color_code[1]

def choose_color5():
    color_code = colorchooser.askcolor(title ="Choose color") 
    listeCouleurBoard[1]=color_code[1]

def choose_color6():
    color_code = colorchooser.askcolor(title ="Choose color") 
    listeCouleurBoard[2]=color_code[1]

def choose_color7():
    color_code = colorchooser.askcolor(title ="Choose color") 
    listeCouleurBoard[3]=color_code[1]


def reecrire():
    global L1,M2
    for i in range(10):
        for j in range(10):
            carre=cnv1.create_rectangle(j*taille+taille*18,i*taille+40,j*taille+taille*19,(i+1)*taille+40,fill=str(listeCouleurBoard[int(M1[i][j])]))
            k=i*10+j
            x=(k//10+1)*taille+taille
            y=k%10*taille+40
            if L1[k][0]!=69:
                if M2[i][j]==0 or M2[i][j]==1:
                    w1=Button(cnv1,bg=str(listeCouleur[0]),command=lambda k=k: tirerJoueur(k))
                else:
                    w1=Button(cnv1,bg=str(listeCouleur[int(M2[i][j])]),command=lambda k=k: tirerJoueur(k))     
                L1[k][0].place_forget()
                L1[k][0]=w1
                w1.place(x=x,y=y,height=taille,width=taille)
            else:
                w1=cnv1.create_rectangle(x,y,x+taille,y+taille,fill=str(listeCouleur[int(M2[k%10][k//10])]))

    
    
couleur1 = Button(cnvParametres, text = "Couleur case vierge adversaire",command = choose_color1)
couleur1.pack()
couleur2 = Button(cnvParametres, text = "Couleur bateau touché adversaire",command = choose_color2)
couleur2.pack()
couleur3 = Button(cnvParametres, text = "Couleur eau touchée adversaire",command = choose_color3)
couleur3.pack()
couleur4 = Button(cnvParametres, text = "Couleur eau joueur",command = choose_color4)
couleur4.pack()
couleur5 = Button(cnvParametres, text = "Couleur bateau joueur",command = choose_color5)
couleur5.pack()
couleur6 = Button(cnvParametres, text = "Couleur eau touché joueur",command = choose_color6)
couleur6.pack()
couleur7 = Button(cnvParametres, text = "Couleur bateau touchée joueur",command = choose_color7)
couleur7.pack()



def printMatrice(M):
    for i in range(len(M)):
        for j in range(len(M)):
            print(str(M[i][j])+" ",end="")
        print()
