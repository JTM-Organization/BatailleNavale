from modele import *

Base = Frame(nb, width=largeur, height=hauteur, bg="black")
Plateau = Frame(nb, width=largeur, height=hauteur)
Parametres = Frame(nb, width=largeur, height=hauteur,bg="#AAAAAA")
Debut=Frame(nb,width=largeur,height=hauteur)
Fin=Frame(nb,width=largeur,height=hauteur)
Choix=Frame(nb,width=largeur,height=hauteur)
Base.pack()
Plateau.pack()
Parametres.pack()
Debut.pack()
Fin.pack()
Choix.pack()

nb.add(Base)
nb.add(Plateau)
nb.add(Parametres)
nb.add(Debut)
nb.add(Fin)
nb.add(Choix)

def play():
    global debut
    if debut==False:
        start()
        plateauBotAleatoire()
        nb.hide(0)
        nb.select(3)
        debut=True
        playsound(r'C:\Users\colin\Downloads\MVC\Bismarck.mp3',False)
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

Jouer = Button(Base, text="Jouer", command=play)
Options = Button(Base, text="Paramètres", command=select_paramètres)
Quitter = Button(Base, text="Quitter", command=root.quit)
Jouer.pack()
Options.pack()
Quitter.pack()




nb.hide(1)
nb.hide(2)
nb.hide(3)
nb.hide(4)



cnv1 = Canvas(Plateau, width = largeur, height = hauteur,bg='grey')
cnvParametres = Canvas(Parametres, width = largeur, height = hauteur)
cnvdebut=Canvas(Debut,width=largeur,height=hauteur,bg='grey')
cnvfin=Canvas(Fin,width=largeur,height=hauteur,bg='grey')
cnvChoix=Canvas(Choix,width=largeur,height=hauteur,bg='grey')

cnv1.pack()
cnvParametres.pack()
cnvdebut.pack()
cnvfin.pack()
cnvChoix.pack()



def tirerJoueur(k):
    global M2,listeCouleur,L1,M1,victoireJoueur,lettre,listeCompteur,difficult
    if M2[k%10][k//10]==0:
        M2[k%10][k//10]=42
    L1[k][0].destroy()
    L1[k][0]=69
    x=(k//10+1)*taille+taille
    y=k%10*taille+40
    if M2[k%10][k//10]!=42:
        listeCompteur[(M2[k%10][k//10])-1]-=1
        w2=cnv1.create_rectangle(x,y,x+taille,y+taille,fill=str(listeCouleur[1]))
        if listeCompteur[(M2[k%10][k//10])-1]!=0:
            labelTouche=Label(cnv1,text="Vous tirez sur la case \n"+lettre[k%10]+str(k//10+1)+": touché",bg='grey')   
        else:
            labelTouche=Label(cnv1,text="Vous tirez sur la case \n"+lettre[k%10]+str(k//10+1)+": touché coulé",bg='grey')
        labelTouche.place(x=taille*13.5,y=taille*3,height=taille,width=taille*3)
        victoireJoueur-=1
        if victoireJoueur==0:
            victoire("joueur")
    else:
        w2=cnv1.create_rectangle(x,y,x+taille,y+taille,fill=str(listeCouleur[2]))
        labelTouche=Label(cnv1,text="Vous tirez sur la case \n"+lettre[k%10]+str(k//10+1)+": à l'eau",bg='grey')
        labelTouche.place(x=taille*13.5,y=taille*3,height=taille,width=taille*3)
    if difficult==0:
        tirIaFacile()
    elif difficult==1:
        tirIaMoyen()
    elif difficult==2:
        tirIaDifficile()
    else:
        tirIaImpossible()

def tirIaFacile():
    global lettre,M1,victoireBot,listeCompteur
    flag=True
    while flag:
        ordonnee=random.randint(0,9)
        abscisse=random.randint(0,9)
        flag=tirIaCode(ordonnee,abscisse)
        

def tirIaMoyen():
    global lettre,M1,victoireBot,listeCompteur,compteurTir
    flag=True
    while flag:
        if compteurTir%4==0:
            for i in range(10):
                for j in range(10):
                    if M1[j][i]>0 and M1[j][i]<42 and flag:
                        flag=tirIaCode(j,i)
        else:
            ordonnee=random.randint(0,9)
            abscisse=random.randint(0,9)
            flag=tirIaCode(ordonnee,abscisse)
        if not(flag):
            compteurTir+=1

def tirIaDifficile():
    global lettre,M1,victoireBot,listeCompteur,compteurTir
    flag=True
    while flag:
        if compteurTir%2==0:
            ordonnee=random.randint(0,9)
            abscisse=random.randint(0,9)
            flag=tirIaCode(ordonnee,abscisse)
        else:
            for i in range(10):
                for j in range(10):
                    if M1[j][i]>0 and M1[j][i]<42 and flag:
                        flag=tirIaCode(j,i)
            
        if not(flag):
            compteurTir+=1

def tirIaImpossible():
    global lettre,M1,victoireBot,listeCompteur,compteurTir
    flag=True
    while flag:
        if compteurTir%3==0:
            ordonnee=random.randint(0,9)
            abscisse=random.randint(0,9)
            flag=tirIaCode(ordonnee,abscisse)
        else:
            for i in range(10):
                for j in range(10):
                    if M1[j][i]>0 and M1[j][i]<42 and flag:
                        flag=tirIaCode(j,i)
            
        if not(flag):
            compteurTir+=1
        


def tirIaCode(ordonnee,abscisse):
    flag=True
    global M1,victoireBot,listeCompteur
    if M1[ordonnee][abscisse]==0:
        M1[ordonnee][abscisse]=67
        labelToucheBot=Label(cnv1,text="Le bot a tiré sur la case \n"+lettre[ordonnee]+str(abscisse+1)+": à l'eau",bg='grey')
        labelToucheBot.place(x=taille*13.5,y=taille*5,height=taille,width=taille*3)
        flag=False
    elif M1[ordonnee][abscisse]>0 and M1[ordonnee][abscisse]!=77 and M1[ordonnee][abscisse]!=67:
        listeCompteur[M1[ordonnee][abscisse]]-=1
        if listeCompteur[M1[ordonnee][abscisse]]!=0:
            labelToucheBot=Label(cnv1,text="Le bot a tiré sur la case \n"+lettre[ordonnee]+str(abscisse+1)+": touché",bg='grey')
        else:
            labelToucheBot=Label(cnv1,text="Le bot a tiré sur la case \n"+lettre[ordonnee]+str(abscisse+1)+": touché coulé",bg='grey')
        M1[ordonnee][abscisse]=77
        labelToucheBot.place(x=taille*13.5,y=taille*5,height=taille,width=taille*3)
        victoireBot-=1
        flag=False
        if victoireBot==0:
            victoire("bot")
    t=cnv1.find_closest(abscisse*taille+taille*18.5, ordonnee*taille+20+taille*0.5)
    cnv1.delete(t[0])
    if M1[ordonnee][abscisse]==67:
        carre=cnv1.create_rectangle(abscisse*taille+taille*18,ordonnee*taille+40,abscisse*taille+taille*19,(ordonnee+1)*taille+40,fill=str(listeCouleurBoard[2]))
    elif M1[ordonnee][abscisse]==77:
        carre=cnv1.create_rectangle(abscisse*taille+taille*18,ordonnee*taille+40,abscisse*taille+taille*19,(ordonnee+1)*taille+40,fill=str(listeCouleurBoard[3]))
    return flag

def victoire(participant):
    global testVictoire
    testVictoire=False
    nb.hide(1)
    nb.select(4)
    labelFin=Label(cnvfin,text="Victoire du "+str(participant),bg='grey',font=("Arial 50"))
    labelFin.place(x=taille*12,y=taille*6.5)


def start():
    global L1,listeCouleur,taille,lettre,listeBateau
    for i in range(10):
        for j in range(10):
            w1=Button(cnv1,bg=listeCouleur[0],command=lambda k=i*10+j: tirerJoueur(k))
            w1.place(x=(i+1)*taille+taille,y=j*taille+40,height=taille,width=taille)
            L1[i*10+j].append(w1)
            l=cnvdebut.create_rectangle(i*80+500,j*80+20,i*80+500+80,j*80+20+80)
        for k in range(2):
            labelChiffre= Label(cnv1,text=str(i+1),bg='grey')
            labelChiffre.place(x=(i+1)*taille+taille*1.3+(k*taille*16),y=15)
            labelLettre=Label(cnv1,text=lettre[i],bg='grey')
            labelLettre.place(x=3*taille/2+(k*taille*16),y=i*taille+taille*0.8+20)
    for k in range(5):
        rect=cnvdebut.create_rectangle(0,100*(k+1),80*(tailleBateau[k]),180+100*k,fill="",outline="")
        listeBateau.append(rect)

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
        x1=cnvdebut.coords(listeBateau[bateauClic])[0]
        y1=cnvdebut.coords(listeBateau[bateauClic])[1]
        for j in range(5):
            if j!=bateauClic:
                k=tailleBateau[bateauClic]
                x2,y2,x3,y3=cnvdebut.coords(listeBateau[j])
                if horizOuVertical[bateauClic]==0:
                    if not((x1<x2 and x1+80<=x2) or (x1>=x3 and x1+80>x3)):
                        if not((y1<y2 and y1+80*k<=y2) or (y1>=y3 and y1+80*k>y3)):         
                            flag=False
                else:
                    if not((x1<x2 and x1+80*k<=x2) or (x1>=x3 and x1+80*k>x3)):
                        if not((y1<y2 and y1+80<=y2) or (y1>=y3 and y1+80>y3)):          
                            flag=False
        if flag==True:
            if horizOuVertical[bateauClic]==0:
                cnvdebut.coords(listeBateau[bateauClic],x1,y1,x1+80,y1+80*tailleBateau[bateauClic])
                horizOuVertical[bateauClic]=1
                cnvdebut.itemconfig(bateauClic+6,stat='normal')
                cnvdebut.itemconfig(bateauClic+1,stat='hidden')
            else:   
                cnvdebut.coords(listeBateau[bateauClic],x1,y1,x1+80*tailleBateau[bateauClic],y1+80)
                horizOuVertical[bateauClic]=0
                cnvdebut.itemconfig(bateauClic+1,stat='normal')
                cnvdebut.itemconfig(bateauClic+6,stat='hidden')


def glisser(event):
    global listeBateau,bateau,listeImageBateauH,listeImageBateauV,horizOuVertical
    if event.x>cnvdebut.coords(listeBateau[bateau])[0] and event.x<cnvdebut.coords(listeBateau[bateau])[2] and event.y>cnvdebut.coords(listeBateau[bateau])[1] and event.y<cnvdebut.coords(listeBateau[bateau])[3]:
        cnvdebut.move(listeBateau[bateau], event.x-old[0], event.y-old[1])
        cnvdebut.move(listeImageBateauH[bateau][0],event.x-old[0], event.y-old[1])
        cnvdebut.move(listeImageBateauV[bateau][0],event.x-old[0], event.y-old[1])
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
        xB=int((listeImageBateauH[bateau][1])/2)
        if horizOuVertical[bateau]==1:
            cnvdebut.coords(listeBateau[bateau],x*80+20,y*80+20,x*80+20+80,y*80+20+tailleBateau[bateau]*80)
        else:
            cnvdebut.coords(listeBateau[bateau],x*80+20,y*80+20,x*80+20+tailleBateau[bateau]*80,y*80+20+80)
        #le +40 correspond à la moitié de la taille d'un carré. Avec cette méthode le bateau est centré car sinon il est décalé.
        #le +20 qu'on retrouve un peu partout permet juste d'avoir une marge entre le haut de la fenêtre et les tableaux.
        cnvdebut.coords(listeImageBateauH[bateau][0],x*80+20+xB, y*80+20+40)
        cnvdebut.coords(listeImageBateauV[bateau][0],x*80+20+40, y*80+20+xB)
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
                M1[int(y1//80+j)][int(x1//80-6)]=1+i
        else:
            for j in range(tailleBateau[i]):
                M1[int(y1//80)][int(x1//80-6+j)]=1+i
    for i in range(10):
        for j in range(10):
            if M1[i][j]==0:
                carre=cnv1.create_rectangle(j*taille+taille*18,i*taille+40,j*taille+taille*19,(i+1)*taille+40,fill=str(listeCouleurBoard[0]))
            else:
                carre=cnv1.create_rectangle(j*taille+taille*18,i*taille+40,j*taille+taille*19,(i+1)*taille+40,fill=str(listeCouleurBoard[1]))
    nb.hide(3)
    nb.select(5)

def suuuuu(k):
    global difficult,selectDif
    difficult=k
    selectDif=True

def gogogo():
    if selectDif==True:
        nb.hide(5)
        nb.select(1)

facile=Button(cnvChoix,bg="royal blue",font=("Arial 20"),text="facile",command=lambda k=0: suuuuu(k))
facile.place(x=0,y=0,height=hauteur*4/5,width=largeur/4)
moyen=Button(cnvChoix,bg="royal blue",font=("Arial 20"),text="moyen",command=lambda k=1: suuuuu(k))
moyen.place(x=largeur/4,y=0,height=hauteur*4/5,width=largeur/4)
difficile=Button(cnvChoix,bg="royal blue",font=("Arial 20"),text="difficile",command=lambda k=2: suuuuu(k))
difficile.place(x=largeur*2/4,y=0,height=hauteur*4/5,width=largeur/4)
impossible=Button(cnvChoix,bg="royal blue",font=("Arial 20"),text="impossible",command=lambda k=3: suuuuu(k))
impossible.place(x=largeur*3/4,y=0,height=hauteur*4/5,width=largeur/4)
confirmer=Button(cnvChoix,bg="royal blue",font=("Arial 20"),text="commencer",command=lambda: gogogo())
confirmer.place(x=0,y=hauteur*4/5,height=hauteur/5,width=largeur)

def on_enter(e):
    if difficult!=0:
        facile['background'] = 'royal blue'
    if difficult!=1:
        moyen['background'] = 'royal blue'
    if difficult!=2:
        difficile['background'] = 'royal blue'
    if difficult!=3:
        impossible['background'] = 'royal blue'
    e.widget['background'] = 'green'
    
def on_leave(e):
    if difficult==0 and e.widget["text"]=="facile":
        e.widget['background'] = 'green'
    if difficult==1 and e.widget["text"]=="moyen":
        e.widget['background'] = 'green'
    if difficult==2 and e.widget["text"]=="difficile":
        e.widget['background'] = 'green'
    if difficult==3 and e.widget["text"]=="impossible":
        e.widget['background'] = 'green'
    if e.widget["text"]=="commencer":
        e.widget['background'] = 'royal blue'
    if difficult!=0:
        facile['background'] = 'royal blue'
    if difficult!=1:
        moyen['background'] = 'royal blue'
    if difficult!=2:
        difficile['background'] = 'royal blue'
    if difficult!=3:
        impossible['background'] = 'royal blue'

facile.bind("<Enter>", on_enter)
facile.bind("<Leave>", on_leave)
moyen.bind("<Enter>", on_enter)
moyen.bind("<Leave>", on_leave)
difficile.bind("<Enter>", on_enter)
difficile.bind("<Leave>", on_leave)
impossible.bind("<Enter>", on_enter)
impossible.bind("<Leave>", on_leave)
confirmer.bind("<Enter>", on_enter)
confirmer.bind("<Leave>", on_leave)


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
                    if M2[x][y+i]>0:
                        flag=False
            else:
                flag=False
            if flag==True:
                for i in range(tailleB):
                    M2[x][y+i]=6+compteur
                compteur+=1
        else:
            if x+tailleB<10:
                for i in range(tailleB):
                    if M2[x+i][y]>0:
                        flag=False
            else:
                flag=False
            if flag==True:
                for i in range(tailleB):
                    M2[x+i][y]=6+compteur
                compteur+=1


def choose_color(k):
    global listeCouleur,listeCouleurBoard
    if k<3:
        color_code = colorchooser.askcolor(title ="Choose color") 
        listeCouleur[k]=color_code[1]
    else:
        color_code = colorchooser.askcolor(title ="Choose color") 
        listeCouleurBoard[k-3]=color_code[1]
    



def reecrire():
    global L1,M2
    for i in range(10):
        for j in range(10):
            if M1[i][j]==0:
                carre=cnv1.create_rectangle(j*taille+taille*18,i*taille+40,j*taille+taille*19,(i+1)*taille+40,fill=str(listeCouleurBoard[0]))
            elif M1[i][j]==77:
                carre=cnv1.create_rectangle(j*taille+taille*18,i*taille+40,j*taille+taille*19,(i+1)*taille+40,fill=str(listeCouleurBoard[3]))
            elif M1[i][j]==67:
                carre=cnv1.create_rectangle(j*taille+taille*18,i*taille+40,j*taille+taille*19,(i+1)*taille+40,fill=str(listeCouleurBoard[2]))
            else:
                carre=cnv1.create_rectangle(j*taille+taille*18,i*taille+40,j*taille+taille*19,(i+1)*taille+40,fill=str(listeCouleurBoard[1]))
            k=i*10+j
            x=(k//10+1)*taille+taille
            y=k%10*taille+40
            if L1[k][0]!=69:
                if M2[j][i]!=98 and M2[j][i]!=42:
                    w1=Button(cnv1,bg=str(listeCouleur[0]),command=lambda k=k: tirerJoueur(k))
                L1[k][0].place_forget()
                L1[k][0]=w1
                w1.place(x=x,y=y,height=taille,width=taille)
            else:
                if M2[k%10][k//10]==42:
                    w1=cnv1.create_rectangle(x,y,x+taille,y+taille,fill=str(listeCouleur[2]))
                elif M2[k%10][k//10]==98:
                    w1=cnv1.create_rectangle(x,y,x+taille,y+taille,fill=str(listeCouleur[1]))

def dessinerBoutonParametre():
    global hauteur
    distance=(hauteur-(hauteur/5))/3    
    couleur1 = Button(cnvParametres,bg="grey", text = "Couleur case vierge adversaire",command = lambda: choose_color(0))
    couleur1.place(x=0,y=hauteur/5,height=distance,width=largeur/2)
    couleur2 = Button(cnvParametres,bg="grey", text = "Couleur bateau touché adversaire",command = lambda:choose_color(1))
    couleur2.place(x=0,y=hauteur/5+distance,height=distance,width=largeur/2)
    couleur3 = Button(cnvParametres,bg="grey", text = "Couleur eau touchée adversaire",command = lambda:choose_color(2))
    couleur3.place(x=0,y=hauteur/5+distance*2,height=distance,width=largeur/2)

    couleur4 = Button(cnvParametres,bg="grey", text = "Couleur eau joueur",command = lambda:choose_color(3))
    couleur4.place(x=largeur/2,y=hauteur/5,height=hauteur/5,width=largeur/2)
    couleur5 = Button(cnvParametres,bg="grey", text = "Couleur bateau joueur",command = lambda:choose_color(4))
    couleur5.place(x=largeur/2,y=hauteur*2/5,height=hauteur/5,width=largeur/2)
    couleur6 = Button(cnvParametres,bg="grey", text = "Couleur eau touché joueur",command =lambda: choose_color(5))
    couleur6.place(x=largeur/2,y=hauteur*3/5,height=hauteur/5,width=largeur/2)
    couleur7 = Button(cnvParametres,bg="grey", text = "Couleur bateau touchée joueur",command =lambda: choose_color(6))
    couleur7.place(x=largeur/2,y=hauteur*4/5,height=hauteur/5,width=largeur/2)

dessinerBoutonParametre()

Retour1 = Button(cnv1,bg="#AAAAAA", text="Retour", command=select_retour)
Retour3 = Button(cnvParametres,bg="#AAAAAA", text="Retour", command=select_retour)
Retour1.place(x=largeur/2-taille/2,y=0,width=taille*2,height=taille)
Retour3.place(x=0,y=0,height=hauteur/5,width=largeur)

#bateau à l'horizontale
Ima=Image.open(r"C:\Users\colin\Downloads\MVC\bateau1.png")
new_Ima=Ima.resize((400,80),Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(new_Ima)
b1=cnvdebut.create_image((200,140), image = photo1)

Ima=Image.open(r"C:\Users\colin\Downloads\MVC\bateau2.png")
new_Ima=Ima.resize((320,80),Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(new_Ima)
b2=cnvdebut.create_image((160,240), image = photo2)

Ima=Image.open(r"C:\Users\colin\Downloads\MVC\bateau3.png")
new_Ima=Ima.resize((240,80),Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(new_Ima)
b3=cnvdebut.create_image((120,340), image = photo3)

Ima=Image.open(r"C:\Users\colin\Downloads\MVC\bateau3.png")
new_Ima=Ima.resize((240,80),Image.ANTIALIAS)
photo4 = ImageTk.PhotoImage(new_Ima)
b4=cnvdebut.create_image((120,440), image = photo4)

Ima=Image.open(r"C:\Users\colin\Downloads\MVC\petitbateau.png")
new_Ima=Ima.resize((160,80),Image.ANTIALIAS)
photo5 = ImageTk.PhotoImage(new_Ima)
b5=cnvdebut.create_image((80,540), image = photo5)

#bateau à la verticale
Ima=Image.open(r"C:\Users\colin\Downloads\MVC\bateau1V.png")
new_Ima=Ima.resize((80,400),Image.ANTIALIAS)
photo6 = ImageTk.PhotoImage(new_Ima)
b1V=cnvdebut.create_image((200,140), image = photo6)


Ima=Image.open(r"C:\Users\colin\Downloads\MVC\bateau2V.png")
new_Ima=Ima.resize((80,320),Image.ANTIALIAS)
photo7 = ImageTk.PhotoImage(new_Ima)
b2V=cnvdebut.create_image((160,240), image = photo7)


Ima=Image.open(r"C:\Users\colin\Downloads\MVC\bateau3V.png")
new_Ima=Ima.resize((80,240),Image.ANTIALIAS)
photo8 = ImageTk.PhotoImage(new_Ima)
b3V=cnvdebut.create_image((120,340), image = photo8)


Ima=Image.open(r"C:\Users\colin\Downloads\MVC\bateau3V.png")
new_Ima=Ima.resize((80,240),Image.ANTIALIAS)
photo9 = ImageTk.PhotoImage(new_Ima)
b4V=cnvdebut.create_image((120,440), image = photo9)


Ima=Image.open(r"C:\Users\colin\Downloads\MVC\petitbateauV.png")
new_Ima=Ima.resize((80,160),Image.ANTIALIAS)
photo10 = ImageTk.PhotoImage(new_Ima)
b5V=cnvdebut.create_image((80,540), image = photo10)
for i in range(5):
    cnvdebut.itemconfig(i+6,stat='hidden')

listeImageBateauH.append((b1,400))
listeImageBateauH.append((b2,320))
listeImageBateauH.append((b3,240))
listeImageBateauH.append((b4,240))
listeImageBateauH.append((b5,160))
listeImageBateauV.append((b1V,400))
listeImageBateauV.append((b2V,320))
listeImageBateauV.append((b3V,240))
listeImageBateauV.append((b4V,240))
listeImageBateauV.append((b5V,160))
