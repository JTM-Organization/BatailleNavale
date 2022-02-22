from tkinter import*


root=Tk()
cnv=Canvas(root, width=800, height=800, bg='gray70')
cnv.pack()

def colorier(k):
       global matriceC
       matriceC[k//10][k%10]=1
       click()

def clear():
       global L
       for i in range(100):
              L[i][0].destroy()

def click():
       global l
       clear()
       start()

       
def clic(event):
       global l
       l+=1
       start()

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
                     cnv.create_rectangle(i*80,j*80,(i+1)*80,(j+1)*80,fill=str(listeCouleur[matriceC[i][j]]))
                     
cnv.bind("<Button-1>",clic)
start()
          
root.mainloop()
