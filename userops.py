from tkinter import *
from tkinter import messagebox
from subprocess import call

def feedback():
    call(["python", "feedback.py"])

# def membshpdet():
#     call(["python", "membership.py"])

# def staffdet():
#     call(["python", "staff.py"])
def additionalben():
    call(['python','addbID.py'])


root=Tk()
root.title("USER OPERATIONS")
root.geometry("300x300+480+100")
root.maxsize(300,300)
root.minsize(300,300)
root['background']='#ffe6ff'

options=Label(root,text="User operations",font=("Century Gothic",25),bg="yellow",fg="black")
options.pack()

membersb=Button(root,text="Feedback",pady=20,width=15,border=2,font=("Century Gothic",10),bg="black",fg="white",command=feedback)
membersb.place(x=80,y=80)

addb=Button(root,text="Additionalbenefits",pady=20,width=15,border=2,font=("Century Gothic",10),bg="black",fg="white",command=additionalben)
addb.place(x=80,y=180)

# membershipb=Button(root,text="Membership details",pady=20,width=15,border=2,font=("Century Gothic",10),bg="black",fg="white",command=membshpdet)
# membershipb.place(x=190,y=220)

# staffb=Button(root,text="Staff details",pady=20,width=15,border=2,font=("Century Gothic",10),bg="black",fg="white",command=staffdet)
# staffb.place(x=190,y=320)


root.mainloop()