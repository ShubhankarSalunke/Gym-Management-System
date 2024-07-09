from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql


def exitwin():
    root.destroy()
def insert():
    id=e_id.get()
    name=e_name.get()
    dob=e_dob.get()
    gender=e_gender.get()
    phn_num=e_phn_num.get()
    email=e_email.get()
    start_date=e_start_date.get()
    duration=e_duration.get()   

    if(id=="" or name=="" or dob=="" or gender=="" or phn_num=="" or email==""):
        Messagebox.showinfo("Insert Status","All fields are required!!")
    else:
        db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym1")
        cursor=db.cursor()
        cursor.execute("insert into members values ('"+ id +"','"+ name +"','"+ dob +"','"+ gender +"','"+ phn_num +"','"+ email +"','"+ 'Active' +"')")
        cursor.execute("commit")
        
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_dob.delete(0,'end')
        e_gender.delete(0,'end')
        e_phn_num.delete(0,'end')
        e_email.delete(0,'end')
        e_start_date.delete(0,'end')
        e_duration.delete(0,'end')
        e_status.delete(0,'end')
        # show()
        Messagebox.showinfo("Insert Status", "Insert Successfull!!")
        cursor.execute("call END_IT('"+ start_date +"','"+ duration +"','"+ id +"')")
        cursor.execute("commit")
        db.close()

def delete():
    id=e_id.get()
    name=e_name.get()

    if(id==""):
        Messagebox.showinfo("Delete Status","ID is Compulsory for deletion!!")
    else:
        db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym1")
        cursor=db.cursor()
        cursor.execute("delete from members where id='"+ e_id.get() +"'")
        cursor.execute("commit")
        
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_dob.delete(0,'end')
        e_gender.delete(0,'end')
        e_phn_num.delete(0,'end')
        e_email.delete(0,'end')
        e_start_date.delete(0,'end')
        e_duration.delete(0,'end')
        e_status.delete(0,'end')
        # show()
        Messagebox.showinfo("Delete Status", "Delete Successfull!!")
        db.close()

def update_phn():

    id=e_id.get()
    phn_num=e_phn_num.get()
    if(id==""):
        Messagebox.showinfo("Update Status","ID is Compulsory for updation")
    else:
        db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym1")
        cursor=db.cursor()
        cursor.execute("update members set phone_num='"+ phn_num +"' where id='"+ id +"'")
        cursor.execute("commit")
        
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_dob.delete(0,'end')
        e_gender.delete(0,'end')
        e_phn_num.delete(0,'end')
        e_email.delete(0,'end')
        e_start_date.delete(0,'end')
        e_duration.delete(0,'end')
        e_status.delete(0,'end')
        # show()
        Messagebox.showinfo("Update Status", "Update Successfull!!")
        db.close()

def update_email():

    id=e_id.get()
    email=e_email.get()
    if(id==""):
        Messagebox.showinfo("Update Status","ID is Compulsory for updation")
    else:
        db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym1")
        cursor=db.cursor()
        cursor.execute("update members set email_addr='"+ email +"' where id='"+ id +"'")
        cursor.execute("commit")

        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_dob.delete(0,'end')
        e_gender.delete(0,'end')
        e_phn_num.delete(0,'end')
        e_email.delete(0,'end')
        e_start_date.delete(0,'end')
        e_duration.delete(0,'end')
        e_status.delete(0,'end')
        # show()
        Messagebox.showinfo("Update Status", "Update Successfull!!")
        db.close()

def update_phn():

    id=e_id.get()
    phn_num=e_phn_num.get()
    if(id==""):
        Messagebox.showinfo("Update Status","ID is Compulsory for updation")
    else:
        db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym1")
        cursor=db.cursor()
        cursor.execute("update members set phone_num='"+ phn_num +"' where id='"+ id +"'")
        cursor.execute("commit")
        
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_dob.delete(0,'end')
        e_gender.delete(0,'end')
        e_phn_num.delete(0,'end')
        e_email.delete(0,'end')
        e_start_date.delete(0,'end')
        e_duration.delete(0,'end')
        e_status.delete(0,'end')
        # show()
        Messagebox.showinfo("Update Status", "Update Successfull!!")
        db.close()

def update_status():

    id=e_id.get()
    status=e_status.get()
    start_date=e_start_date.get()
    duration=e_duration.get()
    if(id==""):
        Messagebox.showinfo("Update Status","ID is Compulsory for updation")
    else:
        db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym1")
        cursor=db.cursor()
        if(status=="Active"):
            cursor.execute("update members set status_val='"+ status +"' where id='"+ id +"'")
            cursor.execute("call END_IT('"+ start_date +"','"+ duration +"','"+ id +"')")
            cursor.execute("commit")
        else:
            cursor.execute("update members set status_val='"+ status +"' where id='"+ id +"'")
            cursor.execute("commit")


        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_dob.delete(0,'end')
        e_gender.delete(0,'end')
        e_phn_num.delete(0,'end')
        e_email.delete(0,'end')
        e_start_date.delete(0,'end')
        e_duration.delete(0,'end')
        e_status.delete(0,'end')
        # show()
        Messagebox.showinfo("Update Status", "Update Successfull!!")
        # cursor.execute("call END_IT('"+ start_date +"','"+ duration +"','"+ id +"')")
        cursor.execute("commit")
        db.close()

def get():
    e_name.delete(0,'end')
    e_dob.delete(0,'end')
    e_gender.delete(0,'end')
    e_phn_num.delete(0,'end')
    e_email.delete(0,'end')
    e_start_date.delete(0,'end')
    e_duration.delete(0,'end')
    e_status.delete(0,'end')
    id=e_id.get()

    if(id==""):
        Messagebox.showinfo("Fetch Status","ID is Compulsory for fetching!!")
    else:
        db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym1")
        cursor=db.cursor()
        cursor.execute("select * from members where id='"+ id +"'")
        rows=cursor.fetchall()
        
        for row in rows:
                e_name.insert(0,row[1])
                e_dob.insert(0,row[2])
                e_gender.insert(0,row[3])
                e_phn_num.insert(0,row[4])
                e_email.insert(0,row[5])

        db.close()


# def show():
#     db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym")
#     cursor=db.cursor()
#     cursor.execute("select * from members")
#     rows=cursor.fetchall()
#     list.delete(0,list.size())
#     headtuple=str("ID") + '      ' + str("Name") + '        ' + str("DOB") + '          ' + str("Gender") + '           ' + str("Phn_Num") + '             ' + str("Email") 
#     list.insert(0,headtuple)

#     for row in rows:
#         insertData=str(row[0]) + '          ' + str(row[1]) + '         ' + str(row[2]) + '         ' + str(row[3]) + '               ' + str(row[4]) + '         ' + str(row[5])
#         list.insert(list.size()+1 , insertData)


root=Tk()
root.geometry("950x430+220+50")
root.maxsize(950,430)
root.minsize(950,430)
root.title("MEMBERS")
root['background']='#ffe6ff'


# bg=PhotoImage(file="C:/Users/Shubhankar/Pictures/Saved Pictures/gym1.png")
# img_lbl=Label(root,image=bg)
# img_lbl.place(x=0,y=0,relwidth=1,relheight=1)


title=Label(root,text="MEMBER DETAILS",font=('Josefin Sans',20),fg="black",bg="yellow")
title.pack()
id=Label(root,text="Enter ID",font=('Open Sans',15),bg="#ffe6ff")
id.place(x=20, y=60)
name=Label(root,text="Enter name",font=('Open Sans',15),bg="#ffe6ff")
name.place(x=20,y=120)
dob=Label(root,text="Enter DOB",font=('Open Sans',15),bg="#ffe6ff")
dob.place(x=20, y=180)
gnd=Label(root,text="Enter Gender",font=('Open Sans',15),bg="#ffe6ff")
gnd.place(x=20,y=240)
phn_num=Label(root,text="Enter Phn_Num",font=('Open Sans',15),bg="#ffe6ff")
phn_num.place(x=450, y=60)
email=Label(root,text="Enter email",font=('Open Sans',15),bg="#ffe6ff")
email.place(x=450, y=120)
start_date=Label(root,text="Enter Start_date",font=('Open Sans',15),bg="#ffe6ff")
start_date.place(x=450,y=180)
duration=Label(root,text="Enter duration",font=('Open Sans',15),bg="#ffe6ff")
duration.place(x=450,y=240)
status=Label(root,text="Enter status",font=('Open Sans',15),bg="#ffe6ff")
status.place(x=300,y=300)


e_id=Entry(root,font=('Arial',15))
e_id.place(x=160,y=60)
e_name=Entry(root,font=('Arial',15))
e_name.place(x=160,y=120)
e_dob=Entry(root,font=('Arial',15))
e_dob.place(x=160,y=180)
e_gender=Entry(root,font=('Arial',15))
e_gender.place(x=160,y=240)
e_phn_num=Entry(root,font=('Arial',15))
e_phn_num.place(x=600,y=60)
e_email=Entry(root,font=('Arial',15))
e_email.place(x=600,y=120)
e_start_date=Entry(root,font=('Arial',15))
e_start_date.place(x=600,y=180)
e_duration=Entry(root,font=('Arial',15))
e_duration.place(x=600,y=240)
e_status=Entry(root,font=('Arial',15))
e_status.place(x=430,y=300)

insert = Button(root,text="Insert",font=("Vina Sans",10) , bg="#ccb3ff",command=insert)
insert.place(x=250,y=340)
updatephn = Button(root,text="Update Phn",font=("Vina Sans",10) , bg="#ccb3ff",command=update_phn)
updatephn.place(x=320,y=340)
updateeml = Button(root,text="Update email",font=("Vina Sans",10) , bg="#ccb3ff",command=update_email)
updateeml.place(x=430,y=340)
delete = Button(root,text="Delete",font=("Vina Sans",10) , bg="#ccb3ff",command=delete)
delete.place(x=550,y=340)
get = Button(root,text="Get",font=("Vina Sans",10) , bg="#ccb3ff",command=get)
get.place(x=620,y=340)
exitwin = Button(root,text="Exit",font=("Vina Sans",10) , bg="#ccb3ff",command=exitwin)
exitwin.place(x=450,y=380)
updatestat = Button(root,text="Update status",font=("Vina Sans",10) , bg="#ccb3ff",command=update_status)
updatestat.place(x=550,y=380)

# list=Listbox(root,width=70,bg="#ffe6cc",fg="black")
# list.place(x=300,y=60)
# show()

root.mainloop()

#ecb3ff