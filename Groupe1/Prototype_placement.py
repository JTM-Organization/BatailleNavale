from tkinter import *
from PIL import ImageTk, Image

#trouver un moyen de redimensionner les images pour s'adapter à n'importe quel plateau
#importer PIL pour le design???

def flip(event):
    widget = event.widget
    h=widget.winfo_width()
    w=widget.winfo_height()
    print(w)
    widget.configure(width = 0, height = 0)
    widget.configure(width=w, height=h)

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
    x=widget.winfo_x()
    y=widget.winfo_y()
    a = cnv.find_closest(x, y)
    coordonnes = cnv.coords(a)
    widget.place(x=coordonnes[0], y=coordonnes[1])

window = Tk()
img = PhotoImage(file='Submarine.png')
img_zoom = img.subsample(8, 6)

DIMENSION = 600
NBR_CARRE = 10
TAILLE_CARRE = DIMENSION//NBR_CARRE
cnv = Canvas(window, width = DIMENSION, height = DIMENSION, bg="gray")
cnv.place(x=0, y=0)

for i in range(NBR_CARRE):
    for j in range(NBR_CARRE):
        x, y = TAILLE_CARRE * j, TAILLE_CARRE * i
        A, B = (x, y), (x + TAILLE_CARRE, y + TAILLE_CARRE)
        carre1 = cnv.create_rectangle(A, B, fill="#097ade")

label = Label(window, image=img_zoom, width=TAILLE_CARRE * 3, height=TAILLE_CARRE)
label.place(x=0, y=0)

label2 = Label(window, bg="blue", width=10, height=5)
label2.place(x=100, y=0)

label3 = Label(window, bg="green", width=10, height=10)
label3.place(x=200, y=0)

label4 = Label(window, bg="red", width=10, height=10)
label4.place(x=300, y=0)

label5 = Label(window, bg="purple", width=10, height=10)
label5.place(x=400, y=0)

canvas1 = Canvas(window, bg="gray", width=60, height=60)
canvas1.place(x=500, y=0)

canvas1.bind("<Button-1>",drag_start)
canvas1.bind("<Button-3>",flip)
canvas1.bind("<B1-Motion>",drag_motion)
canvas1.bind("<ButtonRelease-1>",identify)

label.bind("<Button-1>",drag_start)
label.bind("<Button-3>",flip)
label.bind("<B1-Motion>",drag_motion)
label.bind("<ButtonRelease-1>",identify)

label2.bind("<Button-1>",drag_start)
label2.bind("<Button-3>",flip)
label2.bind("<B1-Motion>",drag_motion)
label2.bind("<ButtonRelease-1>",identify)

label3.bind("<Button-1>",drag_start)
label3.bind("<Button-3>",flip)
label3.bind("<B1-Motion>",drag_motion)
label3.bind("<ButtonRelease-1>",identify)

label4.bind("<Button-1>",drag_start)
label4.bind("<Button-3>",flip)
label4.bind("<B1-Motion>",drag_motion)
label4.bind("<ButtonRelease-1>",identify)

label5.bind("<Button-1>",drag_start)
label5.bind("<Button-3>",flip)
label5.bind("<B1-Motion>",drag_motion)
label5.bind("<ButtonRelease-1>",identify)


X=label5.winfo_x()
Y=label5.winfo_y()
print(x,y)
window.mainloop()
label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_motion)
label2.bind("<ButtonRelease-1>",identify)


window.mainloop()
