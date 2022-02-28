from tkinter import *
from PIL import ImageTk, Image

#trouver un moyen de redimensionner les images pour s'adapter à n'importe quel plateau
#importer PIL pour le design???

def co(event):
    print(event.x, event.y)

def spiderman_do_a_flip(event):
    widget = event.widget
    width = widget.winfo_width()
    height = widget.winfo_height()
    widget.configure(width=height, height=width)

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

def identify(event):
    widget = event.widget
    x = widget.winfo_x()
    y = widget.winfo_y()
    new_x = x//TAILLE_CARRE*TAILLE_CARRE + DEP_X%TAILLE_CARRE + 3
    new_y = y//TAILLE_CARRE*TAILLE_CARRE + DEP_Y%TAILLE_CARRE + 3
    if DEP_X < new_x < DIMENSION + DEP_X and DEP_Y < new_y < DIMENSION + DEP_X:
        widget.place(x=new_x, y=new_y)
    print(x,y)

window = Tk()

var = 60
DIMENSION = var * 10 + 1
NBR_CARRE = 10
TAILLE_CARRE = DIMENSION//NBR_CARRE
DEP_X = 200
DEP_Y = 200
cnv = Canvas(window, width = DIMENSION, height = DIMENSION, bg="red")
cnv.place(x=DEP_X, y=DEP_Y)

for i in range(NBR_CARRE):
    for j in range(NBR_CARRE):
        x, y = TAILLE_CARRE * j + 2, TAILLE_CARRE * i + 2
        A, B = (x, y), (x + TAILLE_CARRE, y + TAILLE_CARRE)
        carre1 = cnv.create_rectangle(A, B, fill="#097ade", width=1, outline="black")

canvas1 = Canvas(window, bg="gray", width=TAILLE_CARRE-1, height=TAILLE_CARRE*2-1, bd=0, highlightthickness=0)
canvas1.place(x=800, y=0)

canvas2 = Canvas(window, bg="green", width=TAILLE_CARRE-1, height=TAILLE_CARRE*3-1, bd=0, highlightthickness=0)
canvas2.place(x=900, y=0)

canvas3 = Canvas(window, bg="yellow", width=TAILLE_CARRE-1, height=TAILLE_CARRE*3-1, bd=0, highlightthickness=0)
canvas3.place(x=1000, y=0)

canvas4 = Canvas(window, bg="purple", width=TAILLE_CARRE-1, height=TAILLE_CARRE*4-1, bd=0, highlightthickness=0)
canvas4.place(x=1100, y=0)

canvas5 = Canvas(window, bg="orange", width=TAILLE_CARRE-1, height=TAILLE_CARRE*5-1, bd=0, highlightthickness=0)
canvas5.place(x=1200, y=0)

canvas1.bind("<Button-1>",drag_start)
canvas1.bind("<Button-3>",spiderman_do_a_flip)
canvas1.bind("<B1-Motion>",drag_motion)
canvas1.bind("<ButtonRelease-1>",identify)

canvas2.bind("<Button-1>",drag_start)
canvas2.bind("<Button-3>",spiderman_do_a_flip)
canvas2.bind("<B1-Motion>",drag_motion)
canvas2.bind("<ButtonRelease-1>",identify)

canvas3.bind("<Button-1>",drag_start)
canvas3.bind("<Button-3>",spiderman_do_a_flip)
canvas3.bind("<B1-Motion>",drag_motion)
canvas3.bind("<ButtonRelease-1>",identify)

canvas4.bind("<Button-1>",drag_start)
canvas4.bind("<Button-3>",spiderman_do_a_flip)
canvas4.bind("<B1-Motion>",drag_motion)
canvas4.bind("<ButtonRelease-1>",identify)

canvas5.bind("<Button-1>",drag_start)
canvas5.bind("<Button-3>",spiderman_do_a_flip)
canvas5.bind("<B1-Motion>",drag_motion)
canvas5.bind("<ButtonRelease-1>",identify)

window.bind("<Button-1>",co)

window.mainloop()
