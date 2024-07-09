from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql
from subprocess import call


def exitwin():
    root.destroy()
def insert():
    fid=e_fid.get()
    id=e_id.get()
    ftype=e_ftype.get()
    fdescp=e_fdescp.get()
    f_date=e_f_date.get()

    if(fid=="" or id=="" or ftype=="" or fdescp=="" or fdescp==""):
        Messagebox.showinfo("Insert Status","All fields are required!!")
    else:
        db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym")
        cursor=db.cursor()
        cursor.execute("insert into feedback values ('"+ fid +"','"+ id +"','"+ ftype +"','"+ fdescp +"','"+ f_date +"')")
        cursor.execute("commit")
        
        e_fid.delete(0,'end')
        e_id.delete(0,'end')
        e_ftype.delete(0,'end')
        e_fdescp.delete(0,'end')
        e_f_date.delete(0,'end')
        # show()
        Messagebox.showinfo("Insert Status", "Insert Successfull!!")
        db.close()

def delete():
    fid=e_fid.get()
    id=e_id.get()

    if(fid==""):
        Messagebox.showinfo("Delete Status","ID is Compulsory for deletion!!")
    else:
        db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym")
        cursor=db.cursor()
        cursor.execute("delete from feedback where fid='"+ e_fid.get() +"'")
        cursor.execute("commit")
        
        e_fid.delete(0,'end')
        e_id.delete(0,'end')
        e_ftype.delete(0,'end')
        e_fdescp.delete(0,'end')
        e_f_date.delete(0,'end')
        # show()
        Messagebox.showinfo("Delete Status", "Delete Succesful!!")
        db.close()


def get():

    fid=e_fid.get()

    if(fid==""):
        Messagebox.showinfo("Fetch Status","ID is Compulsory for fetching!!")
    else:
        db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym")
        cursor=db.cursor()
        cursor.execute("select * from feedback where fid='"+ fid +"'")
        rows=cursor.fetchall()
        
        for row in rows:
                e_id.insert(0,row[1])
                e_ftype.insert(0,row[2])
                e_fdescp.insert(0,row[3])
                e_f_date.insert(0,row[4])

        db.close()


def showbyfeedback():
    # db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym")
    # cursor=db.cursor()
    # cursor.execute("select * from feedback")
    # rows=cursor.fetchall()
    # list.delete(0,list.size())
    # headtuple=str("FID") + '      ' + str("ID") + '             ' + str("F_type") + '               ' + str("F_Descp") + '                    ' + str("Date") 
    # list.insert(0,headtuple)

    # for row in rows:
    #     insertData=str(row[0]) + '          ' + str(row[1]) + '             ' + str(row[2]) + '               ' + str(row[3]) + '                   ' + str(row[4])
    #     list.insert(list.size()+1 , insertData)
    call(["python","feedbackbyID.py"])

root=Tk()
root.geometry("800x380+220+50")
root.maxsize(800,380)
root.minsize(800,380)
root.title("FEEDBACK")
root['background']='#ffe6ff'



# bg=PhotoImage(file="C:/Users/Shubhankar/Pictures/Saved Pictures/gym1.png")
# img_lbl=Label(root,image=bg)
# img_lbl.place(x=0,y=0,relwidth=1,relheight=1)


title=Label(root,text="Feedback Page",font=('Josefin Sans',20),fg="black",bg="yellow")
title.pack()
fid=Label(root,text="Enter FID",font=('Open Sans',15),bg="#ffe6ff")
fid.place(x=20, y=60)
id=Label(root,text="Enter id",font=('Open Sans',15),bg="#ffe6ff")
id.place(x=20,y=120)
ftype=Label(root,text="Enter ftype",font=('Open Sans',15),bg="#ffe6ff")
ftype.place(x=20, y=180)
fdescp=Label(root,text="Descpription",font=('Open Sans',15),bg="#ffe6ff")
fdescp.place(x=450,y=60)
f_date=Label(root,text="Enter Date",font=('Open Sans',15),bg="#ffe6ff")
f_date.place(x=450, y=120)


e_fid=Entry(root,font=('Arial',15))
e_fid.place(x=120,y=60)
e_id=Entry(root,font=('Arial',15))
e_id.place(x=120,y=120)
e_ftype=Entry(root,font=('Arial',15))
e_ftype.place(x=120,y=180)
e_fdescp=Entry(root,font=('Arial',15))
e_fdescp.place(x=570,y=60)
e_f_date=Entry(root,font=('Arial',15))
e_f_date.place(x=570,y=120)


insert = Button(root,text="Insert",font=("Vina Sans",10) , bg="#ccb3ff",command=insert)
insert.place(x=250,y=260)
delete = Button(root,text="Delete",font=("Vina Sans",10) , bg="#ccb3ff",command=delete)
delete.place(x=320,y=260)
get = Button(root,text="Get",font=("Vina Sans",10) , bg="#ccb3ff",command=get)
get.place(x=450,y=260)
exitwin = Button(root,text="Exit",font=("Vina Sans",10) , bg="#ccb3ff",command=exitwin)
exitwin.place(x=520,y=260)

showmyfeed = Button(root,text="Show",font=("Vina Sans",10) ,width=10,pady=5, bg="black",fg="white",command=showbyfeedback)
showmyfeed.place(x=360,y=320)

# list=Listbox(root,width=60,bg="#ffe6cc",fg="black")
# list.place(x=300,y=60)
# show()

root.mainloop()

#ecb3ff