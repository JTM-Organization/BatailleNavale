from tkinter import*


root=Tk()
cnv=Canvas(root, width=800, height=800, bg='gray70')
cnv.pack()

def colorier(k):
    global matriceC,listeCouleur,L
    matriceC[k%10][k//10]=1
    w=Button(bg=str(listeCouleur[int(matriceC[k%10][k//10])]),command=lambda k=k: colorier(k))
    L[k][0].place_forget()
    L[k][0]=w
    w.place(x=k//10*80,y=k%10*80,height=80,width=80)





       

global L,l,matriceC,listeCouleur
listeCouleur=["royal blue","yellow"]

matriceC=[[0 for i in range(10)]for j in range(10)]
L=[[]for i in range(100)]
l=0


def start():
    global l,L,debut,listeCouleur
    for i in range(10):
            for j in range(10):
                w=Button(bg=str(listeCouleur[int(matriceC[i][j])]),command=lambda k=i*10+j: colorier(k))
                w.place(x=i*80,y=j*80,height=80,width=80)
                
                L[i*10+j].append(w)
                if l%2==1:
                    w.place_forget()
                    
start()
print(L[0][0])     
root.mainloop()
