import tkinter.messagebox
from tkinter import *
from PIL import *
from numpy import *


#__main__
master=Tk()
master.geometry('1350x750')
master.title("Tic-Tac-Toe")
master.configure(bg="cyan")


topf=Frame(master,bg="cyan",pady=2,width=1350,height=100,relief=RIDGE)
topf.grid(row=0,column=0,pady=4)

L2=Label(topf,text='Tic-Tac-Toe',bg='white',fg='firebrick1',justify=CENTER,relief='sunken',font=('Helvetica',40,'bold italic'))
L2.grid(row=0,column=0)

mainf=Frame(master,bg='cyan', bd=5, width=1350,height=650,relief=RIDGE)
mainf.grid(row=1, column=0, padx=105, pady=4)

leftf=Frame(mainf,bg='cyan',bd=5,width=780,height=650,relief=RIDGE)
leftf.pack(side=LEFT)

rightf=Frame(mainf,bg='cyan',bd=5,width=570,height=650,relief=RIDGE)
rightf.pack(side=RIGHT)

px=IntVar()
po=IntVar()
mm=IntVar()
dr=IntVar()

px.set(0)
po.set(0)
mm.set(0)
dr.set(0)

def showresult():
    file=open("result.txt","w")
    x=(mm.get())
    y=(px.get())
    z=(dr.get())    
    l=(x-y-z)
    file.write(str(x))
    file.write(str(y))
    file.write(str(l))
    file.write(str(z))
    file.write('\n')
    x=(mm.get())
    y=(po.get())
    z=(dr.get())
    l=(x-y-z)
    file.write(str(x))
    file.write(str(y))
    file.write(str(l))
    file.write(str(z))
    file.close()
    import finalresult
    

def reset():
    global player,stop_game,count
    for i in range(3):
        for j in range(3):
            b[i][j].config(text=' ',bg='powder blue')
            sta[i][j]=0
    player='X'
    stop_game=False
    count=0


nom=Label(rightf,text='No. of matches',bg='white',fg='firebrick1',width=15,justify=CENTER,relief='sunken',font=('Helvetica',20,'bold italic'))
nom.grid(row=0,column=0,sticky=W,pady=6,padx=4)
nm=Entry(rightf,bd=2,fg='black',textvariable=mm,width=15,justify=LEFT).grid(row=0,column=2)

nod=Label(rightf,text='No. of Draws',bg='white',fg='firebrick1',width=15,justify=CENTER,relief='sunken',font=('Helvetica',20,'bold italic'))
nod.grid(row=1,column=0,sticky=W,pady=6,padx=4)
nd=Entry(rightf,bd=2,fg='black',textvariable=dr,width=15,justify=LEFT).grid(row=1,column=2,padx=2)

Lx=Label(rightf,text='Player1: X',bg='white',fg='firebrick1',width=15,justify=CENTER,relief='sunken',font=('Helvetica',20,'bold italic'))
Lx.grid(row=2,column=0,sticky=W,pady=6,padx=4)
e1=Entry(rightf,bd=2,fg='black',textvariable=px,width=15,justify=LEFT).grid(row=2,column=2,padx=2)

Lo=Label(rightf,text='Player2: O',bg='white',fg='firebrick1',width=15,justify=CENTER,relief='sunken',font=('Helvetica',20,'bold italic'))
Lo.grid(row=3,column=0,sticky=W,pady=6,padx=4)
e2=Entry(rightf,bd=2,fg='black',textvariable=po,width=15,justify=LEFT).grid(row=3,column=2,padx=2)

newg=Button(rightf,text='Show Records',fg='blue',bg='white',width=15,height=3,font=('Helvetica',20,'bold italic'),command=showresult)
newg.grid(row=5,column=0,columnspan=3,pady=6)

restg=Button(rightf,text='Reset Game',fg='blue',bg='white',width=15,height=3,font=('Helvetica',20,'bold italic'),command=reset)
restg.grid(row=4,column=0,columnspan=3,pady=6)

def ckeck():
    global stop_game
    for i in range(3):
        if sta[i][0]==sta[i][1]==sta[i][2]!=0:
            stop_game=True
            return True
    for i in range(3):
        if sta[0][i]==sta[1][i]==sta[2][i]!=0:
            stop_game=True
            return True
    if sta[0][0]==sta[1][1]==sta[2][2]!=0:
        stop_game=True
        return True
    if sta[2][0]==sta[1][1]==sta[0][2]!=0:
        stop_game=True
        return True

count=0
def callback(r,c):
    global player,stop_game,count
    
    if player=='X' and sta[r][c]==0 and stop_game==False:
        b[r][c].config(text='X',bg='white')
        sta[r][c]='X'
        player='O'
        count+=1
        if ckeck()==True:
            n=int(px.get())
            score=1+n
            px.set(score)
            n=int(mm.get())
            ss=n+1
            mm.set(ss)
            tkinter.messagebox.showinfo('Won!!','Player 1 won this round!!')
    if player=='O' and sta[r][c]==0 and stop_game==False:
        b[r][c].config(text='O',bg='white')
        sta[r][c]='O'
        player='X'
        count+=1
        if ckeck()==True:
            n=int(po.get())
            score=1+n
            po.set(score)
            n=int(mm.get())
            ss=n+1
            mm.set(ss)
            tkinter.messagebox.showinfo('Won!!','Player 2 won this round!!')
    elif stop_game==False and count==9:
        n=int(dr.get())
        s=n+1
        dr.set(s)
        n=int(mm.get())
        ss=n+1
        mm.set(ss)
        tkinter.messagebox.showinfo('Draw!!','This round was a tie!!')
    



b=[[0,0,0],
   [0,0,0],
   [0,0,0]]

sta=[[0,0,0],
   [0,0,0],
   [0,0,0]]

for i in range(3):
    for j in range(3):
        b[i][j]=Button(leftf,font=('Arial',30),width=10,height=4,bg='powder blue',command=lambda r=i,c=j:callback(r,c))
        b[i][j].grid(row=i,column=j)

player='X'
stop_game=False


mainloop()





