
from tkinter import *     
import tkinter as tk
from tkinter import messagebox



window=Tk()
window.geometry("680x655")
counter=0
var = tk.IntVar()
board = [ [None]*3 for _ in range(3) ]


board=[    ['','','',],
           ['','','',],
           ['','','',]]
            
def value2():
    global counter
    counter=1      
    
def Choose_player():
    checkGroup = LabelFrame(window, text = "Choose Player", padx=20, pady=20,borderwidth=10 ,font=("Arial", 25),highlightbackground="black")
    checkGroup.grid(row=0,column=5)

    checkbutton1 = Checkbutton(checkGroup, text="X" ,font=("Arial", 15),variable=var,onvalue=0)
    checkbutton1.grid(row = 0, column = 0, sticky = W, pady = 2)

    checkbutton2 = Checkbutton(checkGroup, text="O", font=("Arial", 15),variable=var,onvalue=1,command=value2)
    checkbutton2.grid(row = 1, column = 0, sticky = W, pady = 2)

    comfirmbtn=Button(checkGroup,text="comfirm",width=20,font=("Arial", 17),borderwidth=3,command=lambda:[window.quit(),borad_Game()])
    comfirmbtn.grid(row = 3, column = 0, sticky = W, pady = 2)

def destruct():
    global window,winnerWindow
    window.destroy()
    winnerWindow.destroy()


def displayWinner(winner):
    global t,winnerWindow,ID    
    winnerWindow=Tk()
    winnerWindow.title("Winner Window")
    winnerWindow.configure(bg="Black")
    l1=Label(winnerWindow,text="THE WINNER IS: ",font=("COMIC SANS MS",15),bg="Black",fg="White")
    l1.pack()
    l2=Label(winnerWindow,text=winner,font=("COMIC SANS MS",15),bg="Black",fg="White")
    l2.pack()
    bproceed=Button(winnerWindow,text="Proceed",font=("COMIC SANS MS",10,"bold"),command=destruct)
    bproceed.pack()
        
def checkWinner():
    global count,board
    if (board[0][0]==board[0][1]==board[0][2]=="X" or board[1][0]==board[1][1]==board[1][2]=="X" or board[2][0]==board[2][1]==board[2][2]=="X" or
        board[0][0]==board[1][0]==board[2][0]=="X" or board[0][1]==board[1][1]==board[2][1]=="X" or board[0][2]==board[1][2]==board[2][2]=="X" or
        board[0][0]==board[1][1]==board[2][2]=="X" or board[0][2]==board[1][1]==board[2][0]=="X"):
            displayWinner("Player X")
    elif (board[0][0]==board[0][1]==board[0][2]=="O" or board[1][0]==board[1][1]==board[1][2]=="O" or board[2][0]==board[2][1]==board[2][2]=="O" or
          board[0][0]==board[1][0]==board[2][0]=="O" or board[0][1]==board[1][1]==board[2][1]=="O" or board[0][2]==board[1][2]==board[2][2]=="O" or
          board[0][0]==board[1][1]==board[2][2]=="O" or board[0][2]==board[1][1]==board[2][0]=="O"):
            displayWinner("Player O")
    elif counter==9:
        displayWinner("NONE! IT IS A TIE!")

    

def BTN (event,i,j):
 

    global counter
    if event['text']=="":
        color = "O" if counter%2 else "X"
        event.config(text=color)
        board[i][j]=color
        counter += 1
    if counter >=5:
        checkWinner()
    else: 
        pass


Choose_player()
def borad_Game(): 
    b1=Button(window,text="",height=4,width=8,bg="white",activebackground="white",fg="black",font="Times 15 bold",command=lambda: BTN(b1,0,0))
    b1.bind(checkWinner)
    b2=Button(window,text="",height=4,width=8,bg="white",activebackground="white",fg="black",font="Times 15 bold",command=lambda: BTN(b2,0,1))
    b2.bind(checkWinner)
    b3=Button(window,text="",height=4,width=8,bg="white",activebackground="white",fg="black",font="Times 15 bold",command=lambda: BTN(b3,0,2))
    b3.bind(checkWinner)
    b4=Button(window,text="",height=4,width=8,bg="white",activebackground="white",fg="black",font="Times 15 bold",command=lambda: BTN(b4,1,0))
    b4.bind(checkWinner)
    b5=Button(window,text="",height=4,width=8,bg="white",activebackground="white",fg="black",font="Times 15 bold",command=lambda: BTN(b5,1,1))
    b5.bind(checkWinner)
    b6=Button(window,text="",height=4,width=8,bg="white",activebackground="white",fg="black",font="Times 15 bold",command=lambda: BTN(b6,1,2))
    b6.bind(checkWinner)
    b7=Button(window,text="",height=4,width=8,bg="white",activebackground="white",fg="black",font="Times 15 bold",command=lambda: BTN(b7,2,0))
    b7.bind(checkWinner)
    b8=Button(window,text="",height=4,width=8,bg="white",activebackground="white",fg="black",font="Times 15 bold",command=lambda: BTN(b8,2,1))
    b8.bind(checkWinner)
    b9=Button(window,text="",height=4,width=8,bg="white",activebackground="white",fg="black",font="Times 15 bold",command=lambda: BTN(b9,2,2))
    b9.bind(checkWinner)
    b1.grid(row=2,column=0)
    b2.grid(row=2,column=1)
    b3.grid(row=2,column=2)

    b4.grid(row=3,column=0)
    b5.grid(row=3,column=1)
    b6.grid(row=3,column=2)

    b7.grid(row=4,column=0)
    b8.grid(row=4,column=1)
    b9.grid(row=4,column=2)

    window.mainloop()


    


    
    
window.mainloop()
