# from tkinter import *
# import tkinter.messagebox as Messagebox
# import mysql.connector as mysql
# from subprocess import call

# def exitwin():
#     root.destroy()
    
# def insert():
#     m_id=e_m_id.get()
#     b_tkm=e_b_tkm.get()
#     # status=e_status.get()
#     id=e_id.get()
#     start_date=e_start_date.get()
#     end_date=e_end_date.get()   
#     typem=e_typem.get()

#     if(m_id=="" or b_tkm=="" or id=="" or start_date=="" or end_date=="" or typem==""):
#         Messagebox.showinfo("Insert Status","All fields are required!!")
#     else:
#         db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym")
#         cursor=db.cursor()
#         cursor.execute("insert into membership values ('"+ m_id +"','"+ b_tkm +"','"+ id +"','"+ start_date +"','"+ end_date +"','"+ typem +"')")
#         cursor.execute("commit")
        
#         e_m_id.delete(0,'end')
#         e_b_tkm.delete(0,'end')
#         # e_status.delete(0,'end')
#         e_id.delete(0,'end')
#         e_start_date.delete(0,'end')
#         e_end_date.delete(0,'end')
#         e_typem.delete(0,'end')
#         show()
#         Messagebox.showinfo("Insert Status", "Insert Successfull!!")
#         db.close()

# def delete():
#     m_id=e_m_id.get()

#     if(m_id==""):
#         Messagebox.showinfo("Delete Status","M_ID is Compulsory for deletion!!")
#     else:
#         db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym")
#         cursor=db.cursor()
#         cursor.execute("delete from membership where id='"+ e_m_id.get() +"'")
#         cursor.execute("commit")
        
#         e_m_id.delete(0,'end')
#         e_b_tkm.delete(0,'end')
#         # e_status.delete(0,'end')
#         e_id.delete(0,'end')
#         e_start_date.delete(0,'end')
#         e_end_date.delete(0,'end')
#         e_typem.delete(0,'end')
#         show()
#         Messagebox.showinfo("Delete Status", "Delete Successfull!!")
#         db.close()



# def update_start_dt():

#     id=e_id.get()
#     start_date=e_start_date.get()
#     if(id==""):
#         Messagebox.showinfo("Update Status","ID is Compulsory for updation")
#     else:
#         db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym")
#         cursor=db.cursor()
#         cursor.execute("update membership set start_date='"+ start_date +"' where id='"+ id +"'")
#         cursor.execute("commit")
        
#         e_m_id.delete(0,'end')
#         e_b_tkm.delete(0,'end')
#         # e_status.delete(0,'end')
#         e_id.delete(0,'end')
#         e_start_date.delete(0,'end')
#         e_end_date.delete(0,'end')
#         e_typem.delete(0,'end')
#         show()
#         Messagebox.showinfo("Update Status", "Update Successfull!!")
#         db.close()

# def update_end_dt():

#     id=e_id.get()
#     end_date=e_end_date.get()
#     if(id==""):
#         Messagebox.showinfo("Update Status","ID is Compulsory for updation")
#     else:
#         db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym")
#         cursor=db.cursor()
#         cursor.execute("update membership set end_date='"+ end_date +"' where id='"+ id +"'")
#         cursor.execute("commit")

#         e_id.delete(0,'end')
#         e_b_tkm.delete(0,'end')
#         # e_status.delete(0,'end')
#         e_id.delete(0,'end')
#         e_start_date.delete(0,'end')
#         e_end_date.delete(0,'end')
#         e_typem.delete(0,'end')
#         show()
#         Messagebox.showinfo("Update Status", "Update Successfull!!")
        # db.close()

# def get():

#     m_id=e_m_id.get()

#     if(id==""):
#         Messagebox.showinfo("Fetch Status","ID is Compulsory for fetching!!")
#     else:
#         db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym")
#         cursor=db.cursor()
#         cursor.execute("select * from membership where m_id='"+ m_id +"'")
#         rows=cursor.fetchall()
        
#         for row in rows:
#                 e_b_tkm.insert(0,row[1])
#                 # e_status.insert(0,row[2])
#                 e_id.insert(0,row[3])
#                 e_start_date.insert(0,row[4])
#                 e_end_date.insert(0,row[5])
#                 e_typem.insert(0,row[6])

#         db.close()

# def searchbyname():
#     call(['python','searchbyID.py'])

# def show():
#     db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym")
#     cursor=db.cursor()
#     cursor.execute("select * from membership")
#     rows=cursor.fetchall()
#     list.delete(0,list.size())
#     headtuple=str("M_ID") + '       ' + str("B_TKM") + '           '+ str("ID") + '            ' + str("Start_Dt") + '               ' + str("End_dt") + '                    ' + str("Type") 
#     list.insert(0,headtuple)

#     for row in rows:
#         insertData=str(row[0]) + '              ' + str(row[1]) + '                 ' + str(row[3]) + '           ' + str(row[4]) + '         ' + str(row[5]) + '            ' + str(row[6])
#         list.insert(list.size()+1 , insertData)

# bg=PhotoImage(file="C:/Users/Shubhankar/Pictures/Saved Pictures/gym1.png")
# img_lbl=Label(root,image=bg)
# img_lbl.place(x=0,y=0,relwidth=1,relheight=1)

# root=Tk()
# root.geometry("850x380+170+50")
# root.maxsize(850,380)
# root.minsize(850,380)
# root.title("MEMBERSHIP")

# title=Label(root,text="Membership Details",font=('Josefin Sans',20),fg="black",bg="yellow")
# title.pack()
# m_id=Label(root,text="Enter M_ID",font=('Open Sans',10),bg="#ffe6ff")
# m_id.place(x=20, y=60)
# b_tkm=Label(root,text="Enter b_tkm",font=('Open Sans',10),bg="#ffe6ff")
# b_tkm.place(x=20,y=90)
# # status=Label(root,text="Enter Status",font=('Open Sans',10),bg="#ffe6ff")
# # status.place(x=20, y=120)
# id=Label(root,text="Enter ID",font=('Open Sans',10),bg="#ffe6ff")
# id.place(x=20,y=150)
# start_date=Label(root,text="Start_date",font=('Open Sans',10),bg="#ffe6ff")
# start_date.place(x=20, y=180)
# end_date=Label(root,text="End_date",font=('Open Sans',10),bg="#ffe6ff")
# end_date.place(x=20,y=210)
# typem=Label(root,text="Type",font=('Open Sans',10),bg="#ffe6ff")
# typem.place(x=20,y=240)

# e_m_id=Entry()
# e_m_id.place(x=120,y=60)
# e_b_tkm=Entry()
# e_b_tkm.place(x=120,y=90)
# # e_status=Entry()
# # e_status.place(x=120,y=120)
# e_id=Entry()
# e_id.place(x=120,y=150)
# e_start_date=Entry()
# e_start_date.place(x=120,y=180)
# e_end_date=Entry()
# e_end_date.place(x=120,y=210)
# e_typem=Entry()
# e_typem.place(x=120,y=240)

# insert = Button(root,text="Insert",font=("Vina Sans",10) , bg="#ccb3ff",command=insert)
# insert.place(x=50,y=290)
# updatestartdt = Button(root,text="Update start_date",font=("Vina Sans",10) , bg="#ccb3ff",command=update_start_dt)
# updatestartdt.place(x=135,y=290)
# updateenddt = Button(root,text="Update end_date",font=("Vina Sans",10) , bg="#ccb3ff",command=update_end_dt)
# updateenddt.place(x=300,y=290)
# delete = Button(root,text="Delete",font=("Vina Sans",10) , bg="#ccb3ff",command=delete)
# delete.place(x=450,y=290)
# get = Button(root,text="Get",font=("Vina Sans",10) , bg="#ccb3ff",command=get)
# get.place(x=550,y=290)

# exitwin = Button(root,text="Exit",font=("Vina Sans",10) , bg="#ccb3ff",command=exitwin)
# exitwin.place(x=300,y=330)
# searchID = Button(root,text="Search by ID",font=("Vina Sans",10) , bg="#ccb3ff",command=searchbyname)
# searchID.place(x=300,y=250)

# list=Listbox(root,width=120,bg="#ffe6cc",fg="black")
# list.place(x=50,y=60)
# show()

# root.mainloop()

from tkinter import *
from tkinter import messagebox
from subprocess import call
import mysql.connector as mysql

def searchID():
    call(["python", "searchbyID.py"])

def searchname():
    call(["python", "searchbyname.py"])

def showall():
    call(["python","showall.py"])


root=Tk()
root.title("MEMBERSHIP DETAILS")
root.geometry("500x500+380+100")
root.maxsize(500,500)
root.minsize(500,500)
root['background']='#ffe6ff'

options=Label(root,text="Membership Operations",font=("Century Gothic",30),bg="yellow",fg="black")
options.pack()

membersb=Button(root,text="Search By ID",pady=20,width=15,border=2,font=("Century Gothic",10),bg="black",fg="white",command=searchID)
membersb.place(x=190,y=120)

membershipb=Button(root,text="Search By Name",pady=20,width=15,border=2,font=("Century Gothic",10),bg="black",fg="white",command=searchname)
membershipb.place(x=190,y=220)

staffb=Button(root,text="Show all ",pady=20,width=15,border=2,font=("Century Gothic",10),bg="black",fg="white",command=showall)
staffb.place(x=190,y=320)


root.mainloop()



# CREATE TRIGGER update_membership after insert on memberregister
# for each row
# BEGIN
#     IF NEW.status = 'active' THEN
#         insert into membership (m_id, name,gender phone_num,email_addr,status_val)
#         values (NEW.id, NEW.name,NEW.dob, NEW.email, NEW.phone_no, 'active');
#     END IF;
# END;