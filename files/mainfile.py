from tkinter import *
import pymysql as sql

def ext():
    exit()

def imp():
    import connecting
play=False
def playd():
    global play
    p1=e1.get()
    checkname(p1.capitalize())
    p2=e2.get()
    checkname(p2.capitalize())
    fi(p1,p2)
    play=True
    imp()
    ext()

def fi(x,y):
    file=open("record.txt","w")
    file.write(x.capitalize()+'\n'+y.capitalize())
    file.close()
 
def checkname(x):
    if x!='':
        x=(x,)
        conn=sql.connect(host='localhost',user='root',passwd='root',db='test')
        c=conn.cursor()
        c.execute('select Name from record')
        data=c.fetchall()
        for i in data:
            if x==i:
                break
        else:
            conn=sql.connect(host='localhost',user='root',passwd='root',db='test')
            c=conn.cursor()
            v=(x,0,0,0,0)
            c.execute('insert into record values(%s,%s,%s,%s,%s)',v)
            conn.commit()

#__main__
master=Tk()
master.geometry('600x600')
master.title("Tic-Tac-Toe")
master.configure(bg="cyan")

L1=Label(master,text='Tic-Tac-Toe',fg='firebrick1',bg='snow3',relief='sunken',
         font=('times',40,'bold italic'))
L2=Label(master,text='Player1',fg='firebrick1',relief='sunken',
         font=('Helvetica',40,'bold italic'))
L3=Label(master,text='Player2',fg='firebrick1',relief='sunken',
         font=('Helvetica',40,'bold italic'))
L4=Label(master,bg="cyan")
L5=Label(master,bg="cyan")

e1=Entry(master,width=40)
e2=Entry(master,width=40)

b1=Button(master,text='Play',fg='blue',bg='white',relief='sunken',
          font=('times',30,'bold italic'),command=playd)
b2=Button(master,text='Exit',fg='blue',bg='white',relief='sunken',
          font=('times',30,'bold italic'),command=ext)

L1.grid(row=0,column=1,columnspan=2,pady=25,padx=150)
L2.grid(row=2,column=1,sticky = W,padx=10,pady=10)
L3.grid(row=4,column=1,sticky = W,padx=10,pady=10)
e1.grid(row=2,column=2)
e2.grid(row=4,column=2)
b1.grid(row=6,column=1)
b2.grid(row=6,column=2)
L4.grid(row=3,column=1,padx=10,pady=20)
L5.grid(row=5,column=1,padx=20,pady=40)

master.mainloop()







