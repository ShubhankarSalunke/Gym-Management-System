from tkinter import *
from tkinter import messagebox
from subprocess import call
import mysql.connector as mysql
# def membdet():
#     call(["python", "members.py"])

# def membshpdet():
#     call(["python", "membership.py"])

# def staffdet():
#     call(["python", "staff.py"])
def exit():
    root.destroy()

def show():
    name=e_name.get()
    db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym1")
    cursor=db.cursor()
    cursor.execute("call find_name('"+ name +"')")
    rows=cursor.fetchall()
    list.delete(0,list.size())
    headtuple=str("M_ID") + '       ' + str("Name") + '           '+ str("Start_date") + '                 ' + str("End_Dt") + '                  ' + str("Duration")
    list.insert(0,headtuple)

    for row in rows:
        insertData=str(row[0]) + '                ' + str(row[1]) + '                 ' + str(row[2]) + '             ' + str(row[3]) + '                     ' + str(row[4])
        list.insert(list.size()+1 , insertData)


root=Tk()
root.title("Search By Name")
root.geometry("500x400+170+50")
root.maxsize(500,400)
root.minsize(500,400)
root['background']='#ffe6ff'

title=Label(root,text="Search by Name",font=('Josefin Sans',20),fg="black",bg="yellow")
title.pack()
s_name=Label(root,text="Enter Name",font=('Open Sans',15),bg="#ffe6ff")
s_name.place(x=20, y=250)

e_name=Entry(root,font=('Open Sans',15),border=3)
e_name.place(x=150,y=250)

# membersb=Button(root,text="Member details",pady=20,width=15,border=2,font=("Century Gothic",10),bg="black",fg="white",command=membdet)
# membersb.place(x=190,y=120)

# membershipb=Button(root,text="Membership details",pady=20,width=15,border=2,font=("Century Gothic",10),bg="black",fg="white",command=membshpdet)
# membershipb.place(x=190,y=220)

showb=Button(root,text="Show",pady=5,width=15,border=2,font=("Century Gothic",10),bg="black",fg="white",command=show)
showb.place(x=200,y=300)

Exitb=Button(root,text="Exit",pady=5,width=15,border=2,font=("Century Gothic",10),bg="black",fg="white",command=exit)
Exitb.place(x=200,y=350)

list=Listbox(root,width=70,bg="#ffe6cc",fg="black")
list.place(x=20,y=60)

root.mainloop()
