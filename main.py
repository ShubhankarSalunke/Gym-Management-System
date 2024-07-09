from tkinter import *
from tkinter import messagebox
from subprocess import call

def openadminlogin():
    root.destroy()
    call(['python','login.py'])

def openuserops():
    root.destroy()
    call(['python','userops.py'])

root=Tk()

root.title("MAIN")
root.geometry("300x300+475+100")
root.maxsize(300,300)
root.minsize(300,300)
root['background']='#ffe6ff'

mylabel=Label(root,text="GYM MANAGEMENT",font=("Arial",20),bg="Yellow",fg="black")
mylabel.pack()

userbutton=Button(root,text="USER",border=3,pady=10,width=15,font=('Century Gothic',15),bg='black',fg="white",command=openuserops)
userbutton.place(x=55,y=90)
adminbutton=Button(root,text="ADMIN",border=3,pady=10,width=15,font=('Century Gothic',15),bg='black',fg="white",command=openadminlogin)
adminbutton.place(x=55,y=180)

root.mainloop()