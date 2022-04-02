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
    global lettre,M1,victoireBot,listeCompteur,compteurMoyen
    flag=True
    while flag:
        if compteurMoyen%4==0:
            for i in range(10):
                for j in range(10):
                    if M1[j][i]>0 and M1[j][i]<42 and flag:
                        flag=tirIaCode(j,i)
        else:
            ordonnee=random.randint(0,9)
            abscisse=random.randint(0,9)
            flag=tirIaCode(ordonnee,abscisse)
        if not(flag):
            compteurMoyen+=1

def tirIaDifficile():
    global lettre,M1,victoireBot,listeCompteur,compteurMoyen
    flag=True
    while flag:
        if compteurMoyen%2==0:
            ordonnee=random.randint(0,9)
            abscisse=random.randint(0,9)
            flag=tirIaCode(ordonnee,abscisse)
        else:
            for i in range(10):
                for j in range(10):
                    if M1[j][i]>0 and M1[j][i]<42 and flag:
                        flag=tirIaCode(j,i)
            
        if not(flag):
            compteurMoyen+=1

def tirIaImpossible():
    global lettre,M1,victoireBot,listeCompteur,compteurMoyen
    flag=True
    while flag:
        if compteurMoyen%3==0:
            ordonnee=random.randint(0,9)
            abscisse=random.randint(0,9)
            flag=tirIaCode(ordonnee,abscisse)
        else:
            for i in range(10):
                for j in range(10):
                    if M1[j][i]>0 and M1[j][i]<42 and flag:
                        flag=tirIaCode(j,i)
            
        if not(flag):
            compteurMoyen+=1
        


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
