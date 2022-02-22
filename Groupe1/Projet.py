from tkinter import *

CANVAS_SIDE=800
NB_SQUARES=10
R=CANVAS_SIDE//NB_SQUARES

def fill_board(cnv, board):
    for i in range(NB_SQUARES):
        for j in range(NB_SQUARES):
            v=board[i][j]
            if not i==j==NB_SQUARES:
                cnv.create_rectangle(j*R, i*R, (1+j)*R, (1+i)*R, fill="royal blue")

def draw():
    master=Tk()
    cnv=Canvas(master, width=CANVAS_SIDE, height=CANVAS_SIDE, bg='ivory')
    cnv.pack()

    board=[[NB_SQUARES*lin+1+col for col in range(NB_SQUARES)] for lin in range(NB_SQUARES)]
    fill_board(cnv, board)
    master.mainloop()
    

draw()
