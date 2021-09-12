import tkinter.messagebox
from tkinter import *
from PIL import *
from numpy import *
import pymysql as sql

def upd():
    conn=sql.connect(host='localhost',user='root',passwd='root',db='test')
    c=conn.cursor()
    f1=open('record.txt','r').readlines()
    f2=open('result.txt','r').readlines()
    f3=open('finalup.txt','w')
    st=0
    for k in f2:
        i=f1[st].rstrip("\n")
        a=f2[st].rstrip('\n')
        z=(a[0],a[1],a[2],a[3])
        c.execute('select Gameplayed,Win,Loss,Draw from record where Name=%s',i)
        s=c.fetchall()
        b=(s[0][0],s[0][1],s[0][2],s[0][3])
        for q in range(0,4):
            v=int(b[q])+int(z[q])
            f3.write(str(v))
        st=st+1
        f3.write('\n')
    f3.close()

def sq():
    f1=open('record.txt','r')
    f2=open('finalup.txt','r')
    r1=f1.readlines()
    r2=f2.readlines()
    conn=sql.connect(host='localhost',user='root',passwd='root',db='test')
    c=conn.cursor()
    z=0
    for a in r2:
        i=r1[z].rstrip("\n")
        a=a.rstrip('\n')
        if len(a)==5:
            b=(a[0:2],a[2],a[3],a[4],i)
            q='UPDATE record SET Gameplayed=%s,Win=%s,Loss=%s,Draw=%s WHERE Name=%s'
            c.execute(q,b)
            conn.commit()
        else:
            b=(a[0],a[1],a[2],a[3],i)
            q='UPDATE record SET Gameplayed=%s,Win=%s,Loss=%s,Draw=%s WHERE Name=%s'
            c.execute(q,b)
            conn.commit()
        z=z+1

upd()
sq()

#__main__
master=Tk()
master.geometry('1400x750')
master.title("Tic-Tac-Toe")
master.configure(bg="cyan")


topf=Frame(master,bg="cyan",pady=2,bd=5,width=1350,height=100,relief=RIDGE)
topf.grid(row=0,column=0,pady=4)

L2=Label(topf,text='Tic-Tac-Toe',bg='white',fg='firebrick1',justify=CENTER,relief=RIDGE,font=('Helvetica',40,'bold italic'))
L2.grid(row=0,column=0)

mainf=Frame(master,bg='cyan',bd=5,width=1350,height=650,relief=RIDGE)
mainf.grid(row=1,column=0,padx=20,pady=4)

mainhead=['Name','Gameplayed','Win','Loss','Draw']

n=0
for i in mainhead:
    
    lb=Label(mainf,text=i,width=15,height=5,relief=RIDGE).grid(row=0,column=n)
    n=n+1


conn=sql.connect(host='localhost',user='root',passwd='root',db='test')
c=conn.cursor()
qrt='select * from record'
c.execute(qrt)
data=c.fetchall()
m=0
n=1
for i in data:
    m=0
    for j in i:
        lbl=Label(mainf,text=j,width=15,height=5,relief=RIDGE).grid(row=n,column=m)
        m=m+1
    n=n+1





