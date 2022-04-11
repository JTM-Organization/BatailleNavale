from modele import *

Base = Frame(nb, width=largeur, height=hauteur)
Plateau = Frame(nb, width=largeur, height=hauteur)
Parametres = Frame(nb, width=largeur, height=hauteur,bg="#AAAAAA")
Debut=Frame(nb,width=largeur,height=hauteur)
Fin=Frame(nb,width=largeur,height=hauteur)
Choix=Frame(nb,width=largeur,height=hauteur)
Credits=Frame(nb,width=largeur,height=hauteur)
Base.pack()
Plateau.pack()
Parametres.pack()
Debut.pack()
Fin.pack()
Choix.pack()
Credits.pack()
nb.add(Base)
nb.add(Plateau)
nb.add(Parametres)
nb.add(Debut)
nb.add(Fin)
nb.add(Choix)
nb.add(Credits)

def play():
    global debut
    if debut==False:
        start()
        plateauBotAleatoire()
        nb.hide(0)
        nb.select(3)
        debut=True
        #playsound(chemin+"Bismarck2.mp3",False)
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



nb.hide(1)
nb.hide(2)
nb.hide(3)
nb.hide(4)



cnv1 = Canvas(Plateau, width = largeur, height = hauteur,bg='grey')
cnvParametres = Canvas(Parametres, width = largeur, height = hauteur)
cnvdebut=Canvas(Debut,width=largeur,height=hauteur,bg='grey')
cnvfin=Canvas(Fin,width=largeur,height=hauteur,bg='grey')
cnvChoix=Canvas(Choix,width=largeur,height=hauteur,bg='grey')
cnvEcran=Canvas(Base,width=largeur,height=hauteur)
cnvCredits=Canvas(Credits,width=largeur,height=hauteur,bg='grey')

cnv1.pack()
cnvParametres.pack()
cnvdebut.pack()
cnvfin.pack()
cnvChoix.pack()
cnvEcran.pack()
cnvCredits.pack()


Jouer = Button(Base,bd=0,bg="grey",font=("Arial 30"),text="Jouer", command=play)
Options = Button(Base,bd=0, font=("Arial 20"),bg="grey",text="Paramètres", command=select_paramètres)
Quitter = Button(Base, bd=0,font=("Arial 20"),bg="grey",text="Quitter", command=root.quit)
button1_canvas = cnvEcran.create_window( largeur/2,hauteur/4+taille, width=taille*2,height=taille*2/3,window = Jouer)
button2_canvas = cnvEcran.create_window( largeur/2,hauteur/4+taille*2, width=taille*2.2,height=taille*2/3, window = Options)
button3_canvas = cnvEcran.create_window( largeur/2,hauteur/4+taille*3, width=taille*2,height=taille*2/3,window = Quitter)

def tirerJoueur(k):
    global M2,listeCouleur,L1,M1,victoireJoueur,lettre,listeCompteur,difficult,progresBot,tour
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
        progresBot["length"]-=taille/2
        labelTouche.place(x=taille*13.5,y=taille*3,height=taille,width=taille*3)
        victoireJoueur-=1
        if victoireJoueur==0:
            victoire("joueur")
    else:
        w2=cnv1.create_rectangle(x,y,x+taille,y+taille,fill=str(listeCouleur[2]))
        labelTouche=Label(cnv1,text="Vous tirez sur la case \n"+lettre[k%10]+str(k//10+1)+": à l'eau",bg='grey')
        labelTouche.place(x=taille*13.5,y=taille*3,height=taille,width=taille*3)
    labelStat=Label(cnv1,text="Vous tirez avec "+str(round((17-victoireJoueur)/tour*100,2))+str("%")+" de précision",bg='grey')
    labelStat2=Label(cnv1,text="Vous avez "+str(round((victoireJoueur)/(100-tour)*100,2))+str("%")+" change de toucher",bg='grey')
    labelStat.place(x=taille*13,y=taille*4,height=taille,width=taille*4)
    labelStat2.place(x=taille*13,y=taille*5,height=taille,width=taille*4)
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
        if compteurTir%5==0:
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
    global progresJoueur,tour
    flag=True
    global M1,victoireBot,listeCompteur
    if M1[ordonnee][abscisse]==0:
        M1[ordonnee][abscisse]=67
        labelToucheBot=Label(cnv1,text="Le bot a tiré sur la case \n"+lettre[ordonnee]+str(abscisse+1)+": à l'eau",bg='grey')
        labelToucheBot.place(x=taille*13.5,y=taille*7,height=taille,width=taille*3)
        flag=False
    elif M1[ordonnee][abscisse]>0 and M1[ordonnee][abscisse]!=77 and M1[ordonnee][abscisse]!=67:
        listeCompteur[M1[ordonnee][abscisse]]-=1
        if listeCompteur[M1[ordonnee][abscisse]]!=0:
            labelToucheBot=Label(cnv1,text="Le bot a tiré sur la case \n"+lettre[ordonnee]+str(abscisse+1)+": touché",bg='grey')
        else:
            labelToucheBot=Label(cnv1,text="Le bot a tiré sur la case \n"+lettre[ordonnee]+str(abscisse+1)+": touché coulé",bg='grey')
        progresJoueur["length"]-=taille/2
        M1[ordonnee][abscisse]=77
        labelToucheBot.place(x=taille*13.5,y=taille*7,height=taille,width=taille*3)
        victoireBot-=1
        flag=False
        if victoireBot==0:
            victoire("bot")
    if not(flag):
        labelStat=Label(cnv1,text="Le bot tire avec "+str(round((17-victoireBot)/tour*100,2))+str("%")+" de précision",bg='grey')
        labelStat2=Label(cnv1,text="Il a "+str(round((victoireBot)/(100-tour)*100,2))+str("%")+" change de toucher",bg='grey')
        labelStat.place(x=taille*13,y=taille*8,height=taille,width=taille*4)
        labelStat2.place(x=taille*13,y=taille*9,height=taille,width=taille*4)

    t=cnv1.find_closest(abscisse*taille+taille*18.5, ordonnee*taille+20+taille*0.5)
    cnv1.delete(t[0])
    if M1[ordonnee][abscisse]==67:
        carre=cnv1.create_rectangle(abscisse*taille+taille*18,ordonnee*taille+40,abscisse*taille+taille*19,(ordonnee+1)*taille+40,fill=str(listeCouleurBoard[2]))
    elif M1[ordonnee][abscisse]==77:
        carre=cnv1.create_rectangle(abscisse*taille+taille*18,ordonnee*taille+40,abscisse*taille+taille*19,(ordonnee+1)*taille+40,fill=str(listeCouleurBoard[3]))
    tour+=1
    return flag

def afficherCredits():
    global labelCredits
    nb.hide(4)
    nb.select(6)
    textCredits="""Tout d'abord, merci d'avoir joué à notre jeu.\n Ce projet aura été une épreuve très intéressante nous permettant d'apprendre de nouvelles choses. 
    Cependant, nous n'aurions pas réussi à finir ce projet sans l'aide de divers personnes et c'est pourquoi nous aimerions les remercier ici.\n \n
    Major aussi connu sous le nom de Titouan. Son aide nous aura été précieuse tout au long du projet notamment pour le côté graphique du projet.\n \n
    Jafar que l'on appelle Joseph dans certains contrées lointaines. Il nous a permis de corriger nos erreurs en testant le jeu à de multiples reprises afin de trouver les bugs. \n \n
    Aubergine qui nous aura permis de nous rendre compte que notre programme ne marchait pas sur les petits écrans.\n \n
    Guany, un membre de discord qui nous a donné de son temps pour nous faire de superbes pixel art de bateaux.\n \n
    Illidanou, un membre de discord qui nous a donné son avis sur le jeu et un comparateur de texte pour trouver les erreurs entre les versions du code.\n \n
    Le groupe de musique Sabaton à qui on a pris la musique sans demander.\n \n
    Les fans de World of warship pour les fonds d'écrans.\n \n
    Zyzz pour le courage et l'honneur et la bonne mentalité qu'il nous a apporté en toute circonstances. C'est pourquoi nous l'avons mis sur le bouton impossible.\n \n
    Explications pour les boutons:\n
    Bulbizarre est le pokémon avec lequel il est le plus simple de finir les jeux pokémons de la première générations.\n
    Un imposteur de Amon Us parce que le niveau moyen est déjà très dur.\n
    Celeste car c'est le meilleur jeu du monde et qu'il est très difficile. Cependant il reste accessible pour qui garde la foi.
    """
    labelCredits=Label(cnvCredits,bg="grey",text=textCredits,font="Arial 15")
    labelCredits.place(x=-40,y=0,width=largeur+40,height=hauteur)
    Quitter = Button(cnvCredits, bd=1,font=("Arial 20"),bg="grey",text="Quitter", command=root.quit)
    Quitter.place(x=largeur/2-taille,y=hauteur-2*taille)


def victoire(participant):
    global testVictoire,largeur,taille
    testVictoire=False
    nb.hide(1)
    nb.select(4)
    cnvfin.create_text(largeur/2, taille*6.5, text="Victoire du "+str(participant), fill="black", font=('Arial 50'))
    credit=Button(cnvfin,font=("Arial 20 bold"), text="Continuer",command=lambda: afficherCredits())
    credit.place(x=largeur/2-taille,y=taille*7.5)

def start():
    global L1,listeCouleur,taille,lettre,listeBateau
    for i in range(10):
        for j in range(10):
            w1=Button(cnv1,bg=listeCouleur[0],command=lambda k=i*10+j: tirerJoueur(k))
            w1.place(x=(i+1)*taille+taille,y=j*taille+40,height=taille,width=taille)
            L1[i*10+j].append(w1)
            l=cnvdebut.create_rectangle(i*80+500,j*80+20,i*80+500+80,j*80+20+80)
            cnvdebut.tag_lower(l)
        for k in range(2):
            cnv1.create_text((i+1)*taille+taille*1.5+(k*taille*16), 20, text=str(i+1), fill="black", font=('Arial 15'))
            cnv1.create_text(3*taille/2+(k*taille*16),i*taille+taille*0.8+20, text=lettre[i], fill="black", font=('Arial 15'))
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
            testPos=testPlacer()
        else:
            placerCarre=False
    elif horizOuVertical[bateau]==0:
        if x>5 and x+tailleBateau[bateau]-1<16 and y>=0 and y<10:
            testPos=testPlacer()
        else:
            placerCarre=False
        #dessin
    if testPos and placerCarre:
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
        buttonCommencer.place(x=300,y=390,width=160,height=80)
    
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
    global difficult,selectDif,listeDif,listeImageDif
    difficult=k
    listeDif[k]["image"]=listeImageDif[k]
    for i in range(4):
        if i!=k:
            if listeDif[i]["image"]!="":
                listeDif[i]["image"]=""
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
listeDif=[facile,moyen,difficile,impossible]
def on_enter(e):
    for i in range(4):
        if difficult!=i:
            listeDif[i]['background']='royal blue'
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
    for i in range(4):
        if difficult!=i:
            listeDif[i]['background']='royal blue'
    

for l in range(4):
    listeDif[l].bind("<Enter>", on_enter)
    listeDif[l].bind("<Leave>", on_leave)

buttonCommencer=Button(cnvdebut,font=("Arial 12 bold"),text="commencer la partie",command=placerBateau,bg='grey')
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
    dessinerBoutonParametre()

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
    global hauteur,listeCouleurBoard,listeCouleur
    distance=(hauteur-(hauteur/5))/3    
    couleur1 = Button(cnvParametres,font=("Arial 30"),bg=str(listeCouleur[0]), text = "Couleur case vierge adversaire",command = lambda: choose_color(0))
    couleur1.place(x=0,y=hauteur/5,height=distance,width=largeur/2)
    couleur2 = Button(cnvParametres,font=("Arial 30"),bg=str(listeCouleur[1]), text = "Couleur bateau touché adversaire",command = lambda:choose_color(1))
    couleur2.place(x=0,y=hauteur/5+distance,height=distance,width=largeur/2)
    couleur3 = Button(cnvParametres,font=("Arial 30"),bg=str(listeCouleur[2]), text = "Couleur eau touchée adversaire",command = lambda:choose_color(2))
    couleur3.place(x=0,y=hauteur/5+distance*2,height=distance,width=largeur/2)

    couleur4 = Button(cnvParametres,font=("Arial 30"),bg=str(listeCouleurBoard[0]), text = "Couleur eau joueur",command = lambda:choose_color(3))
    couleur4.place(x=largeur/2,y=hauteur/5,height=hauteur/5,width=largeur/2)
    couleur5 = Button(cnvParametres,font=("Arial 30"),bg=str(listeCouleurBoard[1]), text = "Couleur bateau joueur",command = lambda:choose_color(4))
    couleur5.place(x=largeur/2,y=hauteur*2/5,height=hauteur/5,width=largeur/2)
    couleur6 = Button(cnvParametres,font=("Arial 30"),bg=str(listeCouleurBoard[2]), text = "Couleur eau touché joueur",command =lambda: choose_color(5))
    couleur6.place(x=largeur/2,y=hauteur*3/5,height=hauteur/5,width=largeur/2)
    couleur7 = Button(cnvParametres,font=("Arial 30"),bg=str(listeCouleurBoard[3]), text = "Couleur bateau touchée joueur",command =lambda: choose_color(6))
    couleur7.place(x=largeur/2,y=hauteur*4/5,height=hauteur/5,width=largeur/2)

dessinerBoutonParametre()

Retour1 = Button(cnv1,font=("Arial 30"),bg="#AAAAAA", text="Retour", command=select_retour)
Retour3 = Button(cnvParametres,font=("Arial 30"),bg="#AAAAAA", text="Retour", command=select_retour)
Retour1.place(x=largeur/2-taille,y=0,width=taille*2,height=taille)
Retour3.place(x=0,y=0,height=hauteur/5,width=largeur)

#image de bateau à l'horizontale
Ima=Image.open(chemin+"bateau1.png")
photo1 = ImageTk.PhotoImage(Ima.resize((400,80),Image.ANTIALIAS))
b1=cnvdebut.create_image((200,140), image = photo1)

Ima=Image.open(chemin+"bateau2.png")
photo2 = ImageTk.PhotoImage(Ima.resize((320,80),Image.ANTIALIAS))
b2=cnvdebut.create_image((160,240), image = photo2)

Ima=Image.open(chemin+"bateau3.png")
photo3 = ImageTk.PhotoImage(Ima.resize((240,80),Image.ANTIALIAS))
b3=cnvdebut.create_image((120,340), image = photo3)

Ima=Image.open(chemin+"bateau3.png")
photo4 = ImageTk.PhotoImage(Ima.resize((240,80),Image.ANTIALIAS))
b4=cnvdebut.create_image((120,440), image = photo4)

Ima=Image.open(chemin+"petitbateau.png")
photo5 = ImageTk.PhotoImage(Ima.resize((160,80),Image.ANTIALIAS))
b5=cnvdebut.create_image((80,540), image = photo5)

#image de bateau à la verticale
Ima=Image.open(chemin+"bateau1V.png")
photo6 = ImageTk.PhotoImage(Ima.resize((80,400),Image.ANTIALIAS))
b1V=cnvdebut.create_image((200,140), image = photo6)

Ima=Image.open(chemin+"bateau2V.png")
photo7 = ImageTk.PhotoImage(Ima.resize((80,320),Image.ANTIALIAS))
b2V=cnvdebut.create_image((160,240), image = photo7)

Ima=Image.open(chemin+"bateau3V.png")
photo8 = ImageTk.PhotoImage(Ima.resize((80,240),Image.ANTIALIAS))
b3V=cnvdebut.create_image((120,340), image = photo8)

Ima=Image.open(chemin+"bateau3V.png")
photo9 = ImageTk.PhotoImage(Ima.resize((80,240),Image.ANTIALIAS))
b4V=cnvdebut.create_image((120,440), image = photo9)

Ima=Image.open(chemin+"petitbateauV.png")
photo10 = ImageTk.PhotoImage(Ima.resize((80,160),Image.ANTIALIAS))
b5V=cnvdebut.create_image((80,540), image = photo10)


fond2=Image.open(chemin+"fond victoire.jpg")
imageFin = ImageTk.PhotoImage(fond2.resize((largeur,hauteur),Image.ANTIALIAS))
fondDebut=cnvfin.create_image((largeur/2,hauteur/2), image = imageFin)

fond=Image.open(chemin+"fond debut.jpg")
imageDebut = ImageTk.PhotoImage(fond.resize((largeur,hauteur),Image.ANTIALIAS))
fondDebut=cnvEcran.create_image((largeur/2,hauteur/2), image = imageDebut)


imgFacile=Image.open(chemin+"bulbizar.png")
imageFacile = ImageTk.PhotoImage(imgFacile.resize((int(largeur/4),(int(hauteur*4/5))),Image.ANTIALIAS))
imgMoyen=Image.open(chemin+"amogus.png")
imageMoyen = ImageTk.PhotoImage(imgMoyen.resize((int(largeur/4),(int(hauteur*4/5))),Image.ANTIALIAS))
imgDifficile=Image.open(chemin+"celeste.png")
imageDifficile = ImageTk.PhotoImage(imgDifficile.resize((int(largeur/4),(int(hauteur*4/5))),Image.ANTIALIAS))
imgImpossible=Image.open(chemin+"zyzz.png")
imageImpossible = ImageTk.PhotoImage(imgImpossible.resize((int(largeur/4),(int(hauteur*4/5))),Image.ANTIALIAS))
listeImageDif=[imageFacile,imageMoyen,imageDifficile,imageImpossible]

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

for i in range(5):
    cnvdebut.itemconfig(i+6,stat='hidden')

progresJoueur = ttk.Progressbar(cnv1,orient = HORIZONTAL, length = taille/2*17, mode = 'determinate') 
progresJoueur.place(x=taille*3,y=taille*12)
progresBot = ttk.Progressbar(cnv1, orient = HORIZONTAL, length = taille/2*17, mode = 'determinate') 
progresBot.place(x=taille*19,y=taille*12)

cnvEcran.create_text(largeur/2, 100, text="Bataille Navale", fill="black", font=('Helvetica 50'))

