from tkinter import *

def clic(event):
    i=event.y//100
    j=event.x//100
    nro=board[i][j]
    rect, txt = items[nro]
    cnv.itemconfigure(rect, fill="red")
    
NB_SQUARES=10

board=[[NB_SQUARES*lin+col for col in range(NB_SQUARES)] for lin in range(NB_SQUARES)]


master=Tk()
cnv=Canvas(master, width=1000, height=1000, bg='gray70')
cnv.pack()

cnv.bind("<Button-1>",clic)

items=[None for i in range(100)]

for i in range(10):
    for j in range(10):
        x, y=100*j, 100*i
        A, B=(x, y), (x+100, y+100)
        rect=cnv.create_rectangle(A, B, fill="royal blue")
        board[i][j]
        nro=board[i][j]
        items[nro]=(rect, txt)

master.mainloop()
