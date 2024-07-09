from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql

def exitwin():
    root.destroy()
    
def insert():
    s_id=e_s_id.get()
    s_name=e_s_name.get()
    gender=e_gender.get()
    pos=e_pos.get()
    hire_date=e_hire_date.get()
    salary=e_salary.get()   
    phone_num=e_phone_num.get()

    if(s_id=="" or s_name=="" or gender=="" or pos=="" or hire_date=="" or salary=="" or phone_num==""):
        Messagebox.showinfo("Insert Status","All fields are required!!")
    else:
        db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym1")
        cursor=db.cursor()
        cursor.execute("insert into staff values ('"+ s_id +"','"+ s_name +"','"+ gender +"','"+ pos +"','"+ hire_date +"','"+ salary +"','"+ phone_num +"')")
        cursor.execute("commit")
        
        e_s_id.delete(0,'end')
        e_s_name.delete(0,'end')
        e_gender.delete(0,'end')
        e_pos.delete(0,'end')
        e_hire_date.delete(0,'end')
        e_salary.delete(0,'end')
        e_phone_num.delete(0,'end')
        show()
        Messagebox.showinfo("Insert Status", "Insert Successfull!!")
        db.close()

def delete():
    s_id=e_s_id.get()

    if(s_id==""):
        Messagebox.showinfo("Delete Status","s_id is Compulsory for deletion!!")
    else:
        db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym1")
        cursor=db.cursor()
        cursor.execute("delete from staff where s_id='"+ e_s_id.get() +"'")
        cursor.execute("commit")
        
        e_s_id.delete(0,'end')
        e_s_name.delete(0,'end')
        e_gender.delete(0,'end')
        e_pos.delete(0,'end')
        e_hire_date.delete(0,'end')
        e_salary.delete(0,'end')
        e_phone_num.delete(0,'end')
        show()
        Messagebox.showinfo("Delete Status", "Delete Successfull!!")
        db.close()



def update_pos():

    s_id=e_s_id.get()
    pos=e_pos.get()
    if(pos==""):
        Messagebox.showinfo("Update Status","ID is Compulsory for updation")
    else:
        db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym1")
        cursor=db.cursor()
        cursor.execute("update staff set post='"+ pos +"' where s_id='"+ s_id +"'")
        cursor.execute("commit")
        
        e_s_id.delete(0,'end')
        e_s_name.delete(0,'end')
        e_gender.delete(0,'end')
        e_pos.delete(0,'end')
        e_hire_date.delete(0,'end')
        e_salary.delete(0,'end')
        e_phone_num.delete(0,'end')
        show()
        Messagebox.showinfo("Update Status", "Update Successfull!!")
        db.close()

def update_sal():

    s_id=e_s_id.get()
    salary=e_salary.get()
    if(pos==""):
        Messagebox.showinfo("Update Status","ID is Compulsory for updation")
    else:
        db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym1")
        cursor=db.cursor()
        cursor.execute("update staff set salary='"+ salary +"' where s_id='"+ s_id +"'")
        cursor.execute("commit")

        e_s_id.delete(0,'end')
        e_s_name.delete(0,'end')
        e_gender.delete(0,'end')
        e_pos.delete(0,'end')
        e_hire_date.delete(0,'end')
        e_salary.delete(0,'end')
        e_phone_num.delete(0,'end')
        show()
        Messagebox.showinfo("Update Status", "Update Successfull!!")
        db.close()

def update_phn():

    s_id=e_s_id.get()
    phone_num=e_phone_num.get()
    if(pos==""):
        Messagebox.showinfo("Update Status","ID is Compulsory for updation")
    else:
        db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym1")
        cursor=db.cursor()
        cursor.execute("update staff set phone_num='"+ phone_num +"' where s_id='"+ s_id +"'")
        cursor.execute("commit")

        e_s_id.delete(0,'end')
        e_s_name.delete(0,'end')
        e_gender.delete(0,'end')
        e_pos.delete(0,'end')
        e_hire_date.delete(0,'end')
        e_salary.delete(0,'end')
        e_phone_num.delete(0,'end')
        show()
        Messagebox.showinfo("Update Status", "Update Successfull!!")
        db.close()

def get():

    s_id=e_s_id.get()

    if(pos==""):
        Messagebox.showinfo("Fetch Status","ID is Compulsory for fetching!!")
    else:
        db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym1")
        cursor=db.cursor()
        cursor.execute("select * from staff where s_id='"+ s_id +"'")
        rows=cursor.fetchall()
        
        for row in rows:
                e_s_name.insert(0,row[1])
                e_gender.insert(0,row[2])
                e_pos.insert(0,row[3])
                e_hire_date.insert(0,row[4])
                e_salary.insert(0,row[5])
                e_phone_num.insert(0,row[6])

        db.close()

def show():
    db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym1")
    cursor=db.cursor()
    cursor.execute("select * from staff")
    rows=cursor.fetchall()
    list.delete(0,list.size())
    headtuple=str("s_id") + '       ' + str("Name") + '        ' + str("Gender")+ '         '+ str("Position") + '             ' + str("Hire_Dt") + '                ' + str("Salary") + '                  ' + str("Phn_Num") 
    list.insert(0,headtuple)

    for row in rows:
        insertData=str(row[0]) + '               ' + str(row[1]) + '                 ' + str(row[2]) + '                ' + str(row[3]) + '             ' + str(row[4]) + '             ' + str(row[5]) + '                ' + str(row[6])
        list.insert(list.size()+1 , insertData)

# bg=PhotoImage(file="C:/Users/Shubhankar/Pictures/Saved Pictures/gym1.png")
# img_lbl=Label(root,image=bg)
# img_lbl.place(x=0,y=0,relwidth=1,relheight=1)

root=Tk()
root.geometry("900x380+170+50")
root.maxsize(900,380)
root.minsize(900,380)
root.title("STAFF")
root['background']='#ffe6ff'

title=Label(root,text="Staff Details",font=('Josefin Sans',20),fg="black",bg="yellow")
title.pack()
s_id=Label(root,text="Enter s_id",font=('Open Sans',10),bg="#ffe6ff")
s_id.place(x=20, y=60)
s_name=Label(root,text="Enter s_name",font=('Open Sans',10),bg="#ffe6ff")
s_name.place(x=20,y=90)
gender=Label(root,text="Enter Gender",font=('Open Sans',10),bg="#ffe6ff")
gender.place(x=20, y=120)
pos=Label(root,text="Enter Pos",font=('Open Sans',10),bg="#ffe6ff")
pos.place(x=20,y=150)
hire_date=Label(root,text="Enter Hire_date",font=('Open Sans',10),bg="#ffe6ff")
hire_date.place(x=20, y=180)
salary=Label(root,text="Enter Salary",font=('Open Sans',10),bg="#ffe6ff")
salary.place(x=20,y=210)
phone_num=Label(root,text="Enter Phn_num",font=('Open Sans',10),bg="#ffe6ff")
phone_num.place(x=20,y=240)

e_s_id=Entry()
e_s_id.place(x=120,y=60)
e_s_name=Entry()
e_s_name.place(x=120,y=90)
e_gender=Entry()
e_gender.place(x=120,y=120)
e_pos=Entry()
e_pos.place(x=120,y=150)
e_hire_date=Entry()
e_hire_date.place(x=120,y=180)
e_salary=Entry()
e_salary.place(x=120,y=210)
e_phone_num=Entry()
e_phone_num.place(x=120,y=240)

insert = Button(root,text="Insert",font=("Vina Sans",10) , bg="#ccb3ff",command=insert)
insert.place(x=50,y=290)
updatepos = Button(root,text="Update Position",font=("Vina Sans",10) , bg="#ccb3ff",command=update_pos)
updatepos.place(x=135,y=290)
updatesal = Button(root,text="Update salary",font=("Vina Sans",10) , bg="#ccb3ff",command=update_sal)
updatesal.place(x=300,y=290)
updatephn = Button(root,text="Update Phone_num",font=("Vina Sans",10) , bg="#ccb3ff",command=update_phn)
updatephn.place(x=450,y=290)
delete = Button(root,text="Delete",font=("Vina Sans",10) , bg="#ccb3ff",command=delete)
delete.place(x=95,y=330)
get = Button(root,text="Get",font=("Vina Sans",10) , bg="#ccb3ff",command=get)
get.place(x=250,y=330)

exitwin = Button(root,text="Exit",font=("Vina Sans",10) , bg="#ccb3ff",command=exitwin)
exitwin.place(x=400,y=330)

list=Listbox(root,width=85,bg="#ffe6cc",fg="black")
list.place(x=300,y=60)
show()

root.mainloop()




