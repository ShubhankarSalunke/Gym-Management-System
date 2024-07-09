from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql
from subprocess import call


def show():
    db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym1")
    cursor=db.cursor()
    cursor.execute("select * from additionalbenefits")
    rows=cursor.fetchall()
    list.delete(0,list.size())
    headtuple=str("ID") + '       ' + str("P_ID") + '           '+ str("Nutri_name") + '                 ' + str("Sauna") + '                  ' + str("Start_date")+ '               '+ str("End_date")
    list.insert(0,headtuple)

    for row in rows:    
        insertData=str(row[0]) + '              ' + str(row[1]) + '                 ' + str(row[2]) + '                            ' + str(row[3]) + '                   ' + str(row[4]) + '                 '+ str(row[5])
        list.insert(list.size()+1 , insertData)

root=Tk()
root.geometry("500x300+170+50")
root.maxsize(500,300)
root.minsize(500,300)
root.title("ADDITIONAL BENEFITS DETAILS")
root['background']='#ffe6ff'

title=Label(root,text="ADDITIONAL BENEFITS DETAILS",font=('Josefin Sans',20),fg="black",bg="yellow")
title.pack()

list=Listbox(root,width=75,bg="#ffe6cc",fg="black")
list.place(x=20,y=60)
show()

root.mainloop()