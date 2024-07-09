from tkinter import *
from tkinter import messagebox
from subprocess import call

def membdet():
    call(["python", "memberregister.py"])

def membshpdet():
    call(["python", "membership.py"])

def staffdet():
    call(["python", "staff.py"])

def showallfeedback():
    call(["python","allfeedback.py"])

def showaddb():
    call(["python","additionalb.py"])


root=Tk()
root.title("ADMIN OPERATIONS")
root.geometry("500x650+380+20")
root.maxsize(500,650)
root.minsize(500,650)
root['background']='#ffe6ff'

options=Label(root,text="Admin operations",font=("Century Gothic",30),bg="yellow",fg="black")
options.pack()

membersb=Button(root,text="Member details",pady=20,width=15,border=2,font=("Century Gothic",10),bg="black",fg="white",command=membdet)
membersb.place(x=190,y=120)

membershipb=Button(root,text="Membership details",pady=20,width=15,border=2,font=("Century Gothic",10),bg="black",fg="white",command=membshpdet)
membershipb.place(x=190,y=220)

staffb=Button(root,text="Staff details",pady=20,width=15,border=2,font=("Century Gothic",10),bg="black",fg="white",command=staffdet)
staffb.place(x=190,y=320)

viewfdb=Button(root,text="View Feedback",pady=20,width=15,border=2,font=("Century Gothic",10),bg="black",fg="white",command=showallfeedback)
viewfdb.place(x=190,y=420)

addbb=Button(root,text="Additional Benefits",pady=20,width=15,border=2,font=("Century Gothic",10),bg="black",fg="white",command=showaddb)
addbb.place(x=190,y=520)


root.mainloop()