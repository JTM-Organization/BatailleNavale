from tkinter import *
from PIL import ImageTk, Image

#trouver un moyen de redimensionner les images pour s'adapter à n'importe quel plateau
#importer PIL pour le design???

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
    print(a)
    coordonnes = cnv.coords(a)
    print(coordonnes)
    new_x=coordonnes[0]
    new_y=coordonnes[1]
    widget.place(x=new_x, y=new_y)

window = Tk()

cnv = Canvas(window, width = 1000, height = 1000, bg="red")
cnv.place(x=0, y=0)
cnv.create_rectangle(500,500,575,580)
cnv.create_rectangle(300,300,375,380)
label = Label(window, bg="yellow", width=10, height=5)
label.place(x=0, y=0)
label2 = Label(window, bg="blue", width=10, height=5)
label2.place(x=100, y=100)

label.bind("<Button-1>",drag_start)
label.bind("<B1-Motion>",drag_motion)
label.bind("<ButtonRelease-1>",identify)

label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_motion)
label2.bind("<ButtonRelease-1>",identify)


window.mainloop()
