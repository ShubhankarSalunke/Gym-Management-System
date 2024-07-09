from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql
from subprocess import call

def exit():
    root.destroy()

def show():
    db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym")
    cursor=db.cursor()
    cursor.execute("select * from feedback")
    rows=cursor.fetchall()
    list.delete(0,list.size())
    headtuple=str("FID") + '      ' + str("ID") + '             ' + str("F_type") + '               ' + str("F_Descp") + '                    ' + str("Date") 
    list.insert(0,headtuple)

    for row in rows:
        insertData=str(row[0]) + '          ' + str(row[1]) + '             ' + str(row[2]) + '               ' + str(row[3]) + '                   ' + str(row[4])
        list.insert(list.size()+1 , insertData)

root=Tk()
root.geometry("450x300+170+50")
root.maxsize(450,300)
root.minsize(450,300)
root.title("FEEDBACK DETAILS")
root['background']='#ffe6ff'

title=Label(root,text="FEEDBACK DETAILS",font=('Josefin Sans',20),fg="black",bg="yellow")
title.pack()

Exitb=Button(root,text="Exit",pady=5,width=15,border=2,font=("Century Gothic",10),bg="black",fg="white",command=exit)
Exitb.place(x=160,y=250)

list=Listbox(root,width=70,bg="#ffe6cc",fg="black")
list.place(x=15,y=60)
show()

root.mainloop()