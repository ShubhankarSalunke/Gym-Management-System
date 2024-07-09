from tkinter import *
from tkinter import messagebox
from subprocess import call

def open_members():
    call(["python","adminops.py"])

def getdata():
    if username.get()=="admin":
        if pwd.get()=="root":
            root.destroy()
            open_members()
        else:
            messagebox.showerror("Password Error","Wrong Password! Try Again")
            pwd.bind('<FocusIn>', on_enter_pwd)
            pwd.bind('<FocusOut>', on_leave_pwd)
    else:
        messagebox.showerror("Sign In Status","Invalid User")
        username.bind('<FocusIn>',on_enter_user)
        username.bind('<FocusOut>',on_leave_user)
        pwd.bind('<FocusIn>', on_enter_pwd)
        pwd.bind('<FocusOut>', on_leave_pwd)  

root=Tk()
root.title("LOGIN WINDOW")
root.geometry("600x500+320+50")
root['background']='#fff2e6'


bg=PhotoImage(file="images/laptop.png")
img_lbl=Label(root,image=bg,bg="#fff2e6")
img_lbl.place(x=20,y=100)

sign_in=Label(root,text="Sign In", font=('Brush Script',25),bg="#fff2e6",fg="#4d79ff")
sign_in.place(x=350,y=40)

######################-----------------------------
def on_enter_user(e):
    username.delete(0,'end')

def on_leave_user(e):
    name=username.get()
    if name=='':
        username.insert(0,'Username')

username=Entry(root,border=0,fg="black",bg="#fff2e6",font=("Arial",15,'italic'))
username.place(x=370,y=200)
username.insert(0,'Username')
username.bind('<FocusIn>',on_enter_user)
username.bind('<FocusOut>',on_leave_user)
Frame(width=250,height='1',bg='black').place(x=280,y=225)

#############################################---------------------
def on_enter_pwd(e):
    pwd.delete(0,'end')

def on_leave_pwd(e):
    password=pwd.get()
    if password=='':
        pwd.insert(0,'Password')

pwd=Entry(root,border=0,fg="black",bg="#fff2e6",font=("Arial",15,'italic'))
pwd.place(x=370,y=275)
pwd.insert(0,'Password')
pwd.bind('<FocusIn>', on_enter_pwd)
pwd.bind('<FocusOut>', on_leave_pwd)
Frame(width=250,height='1',bg='black').place(x=280,y=300)

###################---------------------------
signin = Button(root,text="Sign In",pady=7,width=10,font=("Arial",12,) , bg="#809fff",fg="black",command=getdata)
signin.place(x=350,y=350)

root.mainloop()
