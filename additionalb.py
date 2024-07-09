from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql
from subprocess import call

def exitwin():
    root.destroy()
def insert():
    id=e_id.get()
    p_id=e_p_id.get()
    nutriname=e_nutriname.get()
    gender=e_saustatus.get()
    pstartdate=e_pstartdate.get()
    penddate=e_penddate.get()


    if(id==""):
        Messagebox.showinfo("Insert Status","ID is compulsory for insertion!!")
    else:
        db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym1")
        cursor=db.cursor()
        cursor.execute("insert into additionalbenefits (id,p_id,nutritionist_name,sauna,p_start_date,p_end_date)values ('"+ id +"','"+ p_id +"','"+ nutriname +"','"+ gender +"','"+ pstartdate +"','"+ penddate +"')")
        cursor.execute("commit")
        
        e_id.delete(0,'end')
        e_p_id.delete(0,'end')
        e_nutriname.delete(0,'end')
        e_saustatus.delete(0,'end')
        e_pstartdate.delete(0,'end')
        e_penddate.delete(0,'end')

        # show()
        Messagebox.showinfo("Insert Status", "Insert Successfull!!")
        db.close()

def delete():
    id=e_id.get()
    p_id=e_p_id.get()

    if(id==""):
        Messagebox.showinfo("Delete Status","ID is Compulsory for deletion!!")
    else:
        db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym1")
        cursor=db.cursor()
        cursor.execute("delete from additionalbenefits where id='"+ e_id.get() +"'")
        cursor.execute("commit")
        
        e_id.delete(0,'end')
        e_p_id.delete(0,'end')
        e_nutriname.delete(0,'end')
        e_saustatus.delete(0,'end')
        e_pstartdate.delete(0,'end')
        e_penddate.delete(0,'end')

        # show()
        Messagebox.showinfo("Delete Status", "Delete Successfull!!")
        db.close()

def showdetails():
    call(["python","showaddb.py"])

# def update_phn():

#     id=e_id.get()
#     pstartdate=e_pstartdate.get()
#     if(id==""):
#         Messagebox.showinfo("Update Status","ID is Compulsory for updation")
#     else:
#         db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym")
#         cursor=db.cursor()
#         cursor.execute("update members set phone_num='"+ pstartdate +"' where id='"+ id +"'")
#         cursor.execute("commit")
        
#         e_id.delete(0,'end')
#         e_p_id.delete(0,'end')
#         e_nutriname.delete(0,'end')
#         e_saustatus.delete(0,'end')
#         e_pstartdate.delete(0,'end')
#         e_penddate.delete(0,'end')

#         # show()
#         Messagebox.showinfo("Update Status", "Update Successfull!!")
#         db.close()

# def update_penddate():

#     id=e_id.get()
#     penddate=e_penddate.get()
#     if(id==""):
#         Messagebox.showinfo("Update Status","ID is Compulsory for updation")
#     else:
#         db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym")
#         cursor=db.cursor()
#         cursor.execute("update members set penddate_addr='"+ penddate +"' where id='"+ id +"'")
#         cursor.execute("commit")

#         e_id.delete(0,'end')
#         e_p_id.delete(0,'end')
#         e_nutriname.delete(0,'end')
#         e_saustatus.delete(0,'end')
#         e_pstartdate.delete(0,'end')
#         e_penddate.delete(0,'end')
#         # show()
#         Messagebox.showinfo("Update Status", "Update Successfull!!")
#         db.close()

def get():
    e_p_id.delete(0,'end')
    e_nutriname.delete(0,'end')
    e_saustatus.delete(0,'end')
    e_pstartdate.delete(0,'end')
    e_penddate.delete(0,'end')
    id=e_id.get()

    if(id==""):
        Messagebox.showinfo("Fetch Status","ID is Compulsory for fetching!!")
    else:
        db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym1")
        cursor=db.cursor()
        cursor.execute("select * from additionalbenefits where id='"+ id +"'")
        rows=cursor.fetchall()
        
        for row in rows:
                e_p_id.insert(0,row[1])
                e_nutriname.insert(0,row[2])
                e_saustatus.insert(0,row[3])
                e_pstartdate.insert(0,row[4])
                e_penddate.insert(0,row[5])

        db.close()


# def show():
#     db= mysql.connect(host="localhost", user="root", password="5hubh@mysql#r00t",database="gym")
#     cursor=db.cursor()
#     cursor.execute("select * from members")
#     rows=cursor.fetchall()
#     list.delete(0,list.size())
#     headtuple=str("ID") + '      ' + str("Name") + '        ' + str("DOB") + '          ' + str("Gender") + '           ' + str("pstartdate") + '             ' + str("penddate") 
#     list.insert(0,headtuple)

#     for row in rows:
#         insertData=str(row[0]) + '          ' + str(row[1]) + '         ' + str(row[2]) + '         ' + str(row[3]) + '               ' + str(row[4]) + '         ' + str(row[5])
#         list.insert(list.size()+1 , insertData)


root=Tk()
root.geometry("950x400+220+50")
root.maxsize(950,400)
root.minsize(950,400)
root.title("ADDITIONAL BENEFITS")
root['background']='#ffe6ff'



# bg=PhotoImage(file="C:/Users/Shubhankar/Pictures/Saved Pictures/gym1.png")
# img_lbl=Label(root,image=bg)
# img_lbl.place(x=0,y=0,relwidth=1,relheight=1)


title=Label(root,text="Additional Benefits",font=('Josefin Sans',20),fg="black",bg="yellow")
title.pack()
id=Label(root,text="Enter ID",font=('Open Sans',15),bg="#ffe6ff")
id.place(x=20, y=60)
p_id=Label(root,text="Enter p_id",font=('Open Sans',15),bg="#ffe6ff")
p_id.place(x=20,y=120)
nutriname=Label(root,text="Enter nutr_name",font=('Open Sans',15),bg="#ffe6ff")
nutriname.place(x=20, y=180)
saustatus=Label(root,text="Sauna status ",font=('Open Sans',15),bg="#ffe6ff")
saustatus.place(x=20,y=240)
pstartdate=Label(root,text="Enter p_start_date",font=('Open Sans',15),bg="#ffe6ff")
pstartdate.place(x=450, y=60)
penddate=Label(root,text="Enter p_end date",font=('Open Sans',15),bg="#ffe6ff")
penddate.place(x=450, y=120)



e_id=Entry(root,font=('Arial',15))
e_id.place(x=170,y=60)
e_p_id=Entry(root,font=('Arial',15))
e_p_id.place(x=170,y=120)
e_nutriname=Entry(root,font=('Arial',15))
e_nutriname.place(x=170,y=180)
e_saustatus=Entry(root,font=('Arial',15))
e_saustatus.place(x=170,y=240)
e_pstartdate=Entry(root,font=('Arial',15))
e_pstartdate.place(x=620,y=60)
e_penddate=Entry(root,font=('Arial',15))
e_penddate.place(x=620,y=120)

insert = Button(root,text="Insert",font=("Vina Sans",10) , bg="#ccb3ff",command=insert)
insert.place(x=330,y=320)
showdet = Button(root,text="Show All Details",font=("Vina Sans",10) , bg="#ccb3ff",command=showdetails)
showdet.place(x=390,y=320)
# updateeml = Button(root,text="Update penddate",font=("Vina Sans",10) , bg="#ccb3ff",command=update_penddate)
# updateeml.place(x=430,y=320)
delete = Button(root,text="Delete",font=("Vina Sans",10) , bg="#ccb3ff",command=delete)
delete.place(x=520,y=320)
get = Button(root,text="Get",font=("Vina Sans",10) , bg="#ccb3ff",command=get)
get.place(x=590,y=320)
exitwin = Button(root,text="Exit",font=("Vina Sans",10) , bg="#ccb3ff",command=exitwin)
exitwin.place(x=470,y=360)


# list=Listbox(root,width=70,bg="#ffe6cc",fg="black")
# list.place(x=300,y=60)
# show()

root.mainloop()

#ecb3ff