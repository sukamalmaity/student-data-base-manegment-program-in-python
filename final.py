                                    ##STUDENT DATABASE MANAGEMENT SYSTEM USING PYTHON##

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import random
import sqlite3

link="C:/Users/dipte/Desktop/final project/"
db=sqlite3.connect(link+'studentdatabaseinfo1.db')

uname=[]
pssd=[]
sid=""
spss=""

def uidpasschk():
    windows = Tk()
    windows.title("HOME")
    windows.geometry('1350x720')
    windows.configure(background='lightsteelblue')
    lb2=Label(windows,text="UID",font=("Times New Roman Bold",15),background="lightsteelblue")
    lb2.grid(column=0,row=1)
    uid=Entry(windows,width=20)
    uid.grid(column=1,row=1)
    lb3=Label(windows,text="Password",font=("Times New Roman Bold",15),background="lightsteelblue")
    lb3.grid(column=0,row=2)
    pss=Entry(windows,width=20, show="*")
    pss.grid(column=1,row=2)
    lb4=Label(windows,text="STUDENT ID",font=("Times New Roman Bold",15),background="lightsteelblue")
    lb4.grid(column=7,row=1)
    sid=Entry(windows,width=20)
    sid.grid(column=8,row=1)
    lb5=Label(windows,text="Password",font=("Times New Roman Bold",15),background="lightsteelblue")
    lb5.grid(column=7,row=2)
    spss=Entry(windows,width=20, show="*")
    spss.grid(column=8,row=2)

#new registration===========================================================================
    def clicked3():
            windows=Tk()
            windows.title("INFORMATION")
            windows.geometry('1300x720')
            windows.configure(background='lightsteelblue')
            windows.resizable(0, 0)
            lbl=Label(windows,text="NAME",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl.grid(column=0,row=0,padx=10,pady=10)
            ent=Entry(windows,width=30)
            ent.grid(column=2,row=0,padx=10,pady=10)
            lbl2=Label(windows,text="FATHER'S NAME",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl2.grid(column=0,row=1,padx=10,pady=10)
            ent2=Entry(windows,width=30)
            ent2.grid(column=2,row=1,padx=10,pady=10)
            lbl3=Label(windows,text="MOTHER'S NAME",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl3.grid(column=0,row=2,padx=10,pady=10)
            ent3=Entry(windows,width=30)
            ent3.grid(column=2,row=2,padx=10,pady=10)
            lbl4=Label(windows,text="DATE OF BIRTH",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl4.grid(column=0,row=3,padx=10,pady=10)
            combo1 = Combobox(windows)
            combo1['values']= ("DATE",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,1,19,20,21,22,23,24,25,26,27,28,29,30,31)
            combo1.grid(column=1, row=3,padx=10,pady=10)
            combo2 = Combobox(windows)
            combo2['values']= ("MONTH","JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER")
            combo2.grid(column=2, row=3,padx=10,pady=10)
            combo3 = Combobox(windows)
            combo3['values']= ("YEAR",1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005)
            combo3.grid(column=3, row=3,padx=10,pady=10)
            lbl11=Label(windows,text="ADDRESS",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl11.grid(column=0,row=4,padx=10,pady=10)
            ent11=Entry(windows,width=30)
            ent11.grid(column=2,row=4,padx=10,pady=10)
            lbl5=Label(windows,text="GENDER",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl5.grid(column=0,row=5,padx=10,pady=10)
            gn=Entry(windows,width=30)
            gn.grid(column=2,row=5,padx=10,pady=10)
            lbl6=Label(windows,text="EMAIL ID",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl6.grid(column=0,row=6,padx=10,pady=10)
            ent6=Entry(windows,width=30)
            ent6.grid(column=2,row=6,padx=10,pady=10)
            lbl7=Label(windows,text="MOBILE NUMBER",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl7.grid(column=3,row=6,padx=10,pady=10)
            ent7=Entry(windows,width=30)
            ent7.grid(column=5,row=6,padx=10,pady=10)
            lbl8=Label(windows,text="10TH STD. BOARD NAME",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl8.grid(column=0,row=7,padx=10,pady=10)
            combo4 = Combobox(windows)
            combo4['values']= ("Select","WBBSE","CBSE","ICSE")
            combo4.grid(column=2, row=7,padx=10,pady=10)
            lbl9=Label(windows,text="10TH STD. PERCENTAGE",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl9.grid(column=3,row=7,padx=10,pady=10)
            ent9=Entry(windows,width=30)
            ent9.grid(column=5,row=7,padx=10,pady=10)
            lbl10=Label(windows,text="12TH STD. BOARD NAME",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl10.grid(column=0,row=8,padx=10,pady=10)
            combo5 = Combobox(windows)
            combo5['values']= ("Select","WBBSE","CBSE","ICSE")
            combo5.grid(column=2, row=8,padx=10,pady=10)
            lbl11=Label(windows,text="12TH STD. PERCENTAGE",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl11.grid(column=3,row=8,padx=10,pady=10)
            ent11=Entry(windows,width=30)
            ent11.grid(column=5,row=8,padx=10,pady=10)
            lbl12=Label(windows,text="INSTITUTE NAME",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl12.grid(column=0,row=9,padx=10,pady=10)
            ent12=Entry(windows,width=30)
            ent12.grid(column=2,row=9,padx=10,pady=10)
          
            lbl21=Label(windows,text="DEPARTMENT",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl21.grid(column=3,row=9,padx=10,pady=10)
            ent21=Entry(windows,width=30)
            ent21.grid(column=5,row=9,padx=10,pady=10)
            lbl22=Label(windows,text="ROLL NO",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl22.grid(column=3,row=10,padx=10,pady=10)
            ent22=Entry(windows,width=30)
            ent22.grid(column=5,row=10,padx=10,pady=10)
            
            lbl14=Label(windows,text="COUNTRY",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl14.grid(column=0,row=10,padx=10,pady=10)
            ent14=Entry(windows,width=30)
            ent14.grid(column=2,row=10,padx=10,pady=10)
          
            lbl16=Label(windows,text="AGE",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl16.grid(column=0,row=11,padx=10,pady=10)
            ent16=Entry(windows,width=30)
            ent16.grid(column=2,row=11,padx=10,pady=10)
            lbl17=Label(windows,text="YEAR OF PASSING",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl17.grid(column=0,row=12,padx=10,pady=10)
            ent17=Entry(windows,width=30)
            ent17.grid(column=2,row=12,padx=10,pady=10)
            lbl18=Label(windows,text="LAST YEAR YGPA",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl18.grid(column=0,row=13,padx=10,pady=10)
            ent18=Entry(windows,width=30)
            ent18.grid(column=2,row=13,padx=10,pady=10)
            
            def addnew():
                uidd=""
                def ud():

                    finpass=""
                    num='1234567890'
                    alp="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    
                    for i in range(3):
                    
                        n=random.randint(0,len(num)-1)
                        al=random.randint(0,len(alp)-1)
                        finpass+=num[n]+alp[al]
                    print(finpass)
                    return finpass
                uidd=ud()
                password=""
                def id():
                    pword=""
                    num='1234567890'
                    alp="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    finpass1=""
                    finpass2=""
                    for i in range(6):
                        n=random.randint(0,len(num)-1)
                        al=random.randint(0,len(alp)-1)
                        finpass1+=num[n]
                        finpass2+=alp[al]
                    pword=finpass1+finpass2
                    print(pword)
                    return pword
                password=id()
#DATABASE================================================================================================
                
                link="C:/Users/dipte/Desktop/final project/"
                db=sqlite3.connect(link+'studentdatabaseinfo1.db')
                cursor=db.cursor()
                e1=ent.get()
                e2=ent2.get()
                e3=ent3.get()
                e4=ent11.get()
                e5=gn.get()
                e6=ent6.get()
                e7=ent7.get()
                e9=ent9.get()
                e11=ent11.get()
                e12=ent12.get()
                e21=ent21.get()
                e22=ent22.get()
                e14=ent14.get()
                e16=ent16.get()
                e17=ent17.get()
                e18=ent18.get()
                if(len(ent7.get())==10):
                    e7=ent7.get()
                else:
                        messagebox.showinfo('ERROR.....','ENTER PROPER NUMBER')
                     
                try:
                    TABLE="INFO"
                    db.execute('''CREATE TABLE '''+TABLE+'''(NAME TEXT NOT NULL, FATHER TEXT NOT NULL, MOTHER TEXT NOT NULL,DOB DATE NOT NULL,USERID STRING NOT NULL,PASSWORD STRING NOT NULL,ADDRESS TEXT NOT NULL,GENDER TEXT NOT NULL,MAIL_ID STRING NOT NULL,MOB_NO STRING NOT NULL,ROLL_NO STRING NOT NULL,TEN STRING NOT NULL,TWELVE STRING NOT NULL,INST TEXT NOT NULL,DEPT TEXT NOT NULL,COUNTRY TEXT NOT NULL,AGE STRING NOT NULL,YOP TEXT NOT NULL,YGPA FLOAT NOT NULL);''')
                except:
                    pass
                cursor.execute('''INSERT INTO INFO(NAME,FATHER,MOTHER,DOB,USERID,PASSWORD,ADDRESS,GENDER,MAIL_ID,MOB_NO,ROLL_NO,TEN,TWELVE,INST,DEPT,COUNTRY,AGE,YOP,YGPA)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (e1,e2,e3,combo1.get()+"-"+combo2.get()+"-"+combo3.get(),password,uidd,e4,e5,e6,e7,e22,e9,e11,e12,e21,e14,e16,e17,e18))
                db.commit()
                def mbx():
                    messagebox.showinfo('User id',password)
                    messagebox.showinfo('PASSWORD',uidd)
                    print("Records created sucessfully")
                mbx()
            btn1=Button(windows,text="ADD NEW",command=addnew)
            btn1.grid(column=0,row=19)
            windows.mainloop()
    def clicked2():

        link="C:/Users/dipte/Desktop/final project/"
        db=sqlite3.connect(link+'studentdatabaseinfo1.db')
        cursor=db.cursor()
        cursor=db.execute("Select USERID,PASSWORD from INFO")
        for row in cursor:
            uname.append(row[0])
            pssd.append(row[1])
        if (sid.get() in uname):
          indx=uname.index(sid.get())
        if (spss.get()==pssd[indx]):
            
            print("success")
        windows=Tk()
        windows.title("INFORMATION")
        windows.geometry('1300x720')
        windows.configure(background='lightsteelblue')
        windows.resizable(0, 0)
        lbl=Label(windows,text="NAME",font=("Times New Roman Bold",10),background='lightsteelblue')
        lbl.grid(column=0,row=0,padx=10,pady=10)
        ent=Entry(windows,width=30)
        ent.grid(column=2,row=0,padx=10,pady=10)
        lbl2=Label(windows,text="FATHER'S NAME",font=("Times New Roman Bold",10),background='lightsteelblue')
        lbl2.grid(column=0,row=1,padx=10,pady=10)
        ent2=Entry(windows,width=30)
        ent2.grid(column=2,row=1,padx=10,pady=10)
        lbl3=Label(windows,text="MOTHER'S NAME",font=("Times New Roman Bold",10),background='lightsteelblue')
        lbl3.grid(column=0,row=2,padx=10,pady=10)
        ent3=Entry(windows,width=30)
        ent3.grid(column=2,row=2,padx=10,pady=10)
        lbl4=Label(windows,text="DATE OF BIRTH",font=("Times New Roman Bold",10),background='lightsteelblue')
        lbl4.grid(column=0,row=3,padx=10,pady=10)
        combo1 = Combobox(windows)
        combo1['values']= ("DATE",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,1,19,20,21,22,23,24,25,26,27,28,29,30,31)
        combo1.grid(column=1, row=3,padx=10,pady=10)
        combo2 = Combobox(windows)
        combo2['values']= ("MONTH","JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER")
        combo2.grid(column=2, row=3,padx=10,pady=10)
        combo3 = Combobox(windows)
        combo3['values']= ("YEAR",1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005)
        combo3.grid(column=3, row=3,padx=10,pady=10)
        lbl11=Label(windows,text="ADDRESS",font=("Times New Roman Bold",10),background='lightsteelblue')
        lbl11.grid(column=0,row=4,padx=10,pady=10)
        ent11=Entry(windows,width=30)
        ent11.grid(column=2,row=4,padx=10,pady=10)
        lbl5=Label(windows,text="GENDER",font=("Times New Roman Bold",10),background='lightsteelblue')
        lbl5.grid(column=0,row=5,padx=10,pady=10)
        gn=Entry(windows,width=30)
        gn.grid(column=2,row=5,padx=10,pady=10)
        lbl6=Label(windows,text="EMAIL ID",font=("Times New Roman Bold",10),background='lightsteelblue')
        lbl6.grid(column=0,row=6,padx=10,pady=10)
        ent6=Entry(windows,width=30)
        ent6.grid(column=2,row=6,padx=10,pady=10)
        lbl7=Label(windows,text="MOBILE NUMBER",font=("Times New Roman Bold",10),background='lightsteelblue')
        lbl7.grid(column=3,row=6,padx=10,pady=10)
        ent7=Entry(windows,width=30)
        ent7.grid(column=5,row=6,padx=10,pady=10)
        lbl8=Label(windows,text="10TH STD. BOARD NAME",font=("Times New Roman Bold",10),background='lightsteelblue')
        lbl8.grid(column=0,row=7,padx=10,pady=10)
        combo4 = Combobox(windows)
        combo4['values']= ("Select","WBBSE","CBSE","ICSE")
        combo4.grid(column=2, row=7,padx=10,pady=10)
        lbl9=Label(windows,text="10TH STD. PERCENTAGE",font=("Times New Roman Bold",10),background='lightsteelblue')
        lbl9.grid(column=3,row=7,padx=10,pady=10)
        ent9=Entry(windows,width=30)
        ent9.grid(column=5,row=7,padx=10,pady=10)
        lbl10=Label(windows,text="12TH STD. BOARD NAME",font=("Times New Roman Bold",10),background='lightsteelblue')
        lbl10.grid(column=0,row=8,padx=10,pady=10)
        combo5 = Combobox(windows)
        combo5['values']= ("Select","WBBSE","CBSE","ICSE")
        combo5.grid(column=2, row=8,padx=10,pady=10)
        lbl11=Label(windows,text="12TH STD. PERCENTAGE",font=("Times New Roman Bold",10),background='lightsteelblue')
        lbl11.grid(column=3,row=8,padx=10,pady=10)
        ent11=Entry(windows,width=30)
        ent11.grid(column=5,row=8,padx=10,pady=10)
        lbl12=Label(windows,text="INSTITUTE NAME",font=("Times New Roman Bold",10),background='lightsteelblue')
        lbl12.grid(column=0,row=9,padx=10,pady=10)
        ent12=Entry(windows,width=30)
        ent12.grid(column=2,row=9,padx=10,pady=10)
          
        lbl21=Label(windows,text="DEPARTMENT",font=("Times New Roman Bold",10),background='lightsteelblue')
        lbl21.grid(column=3,row=9,padx=10,pady=10)
        ent21=Entry(windows,width=30)
        ent21.grid(column=5,row=9,padx=10,pady=10)
        lbl22=Label(windows,text="ROLL NO",font=("Times New Roman Bold",10),background='lightsteelblue')
        lbl22.grid(column=3,row=10,padx=10,pady=10)
        ent22=Entry(windows,width=30)
        ent22.grid(column=5,row=10,padx=10,pady=10)
            
        lbl14=Label(windows,text="COUNTRY",font=("Times New Roman Bold",10),background='lightsteelblue')
        lbl14.grid(column=0,row=10,padx=10,pady=10)
        ent14=Entry(windows,width=30)
        ent14.grid(column=2,row=10,padx=10,pady=10)
          
        lbl16=Label(windows,text="AGE",font=("Times New Roman Bold",10),background='lightsteelblue')
        lbl16.grid(column=0,row=11,padx=10,pady=10)
        ent16=Entry(windows,width=30)
        ent16.grid(column=2,row=11,padx=10,pady=10)
        lbl17=Label(windows,text="YEAR OF PASSING",font=("Times New Roman Bold",10),background='lightsteelblue')
        lbl17.grid(column=0,row=12,padx=10,pady=10)
        ent17=Entry(windows,width=30)
        ent17.grid(column=2,row=12,padx=10,pady=10)
        lbl18=Label(windows,text="LAST YEAR YGPA",font=("Times New Roman Bold",10),background='lightsteelblue')
        lbl18.grid(column=0,row=13,padx=10,pady=10)
        ent18=Entry(windows,width=30)
        ent18.grid(column=2,row=13,padx=10,pady=10)

        password=""
        uidd=""
        link="C:/Users/dipte/Desktop/final project/"
        db=sqlite3.connect(link+'studentdatabaseinfo1.db')
        cursor=db.cursor()
        e1=ent.get()
        e2=ent2.get()
        e3=ent3.get()
        e4=ent11.get()
        e5=gn.get()
        e6=ent6.get()
        e7=ent7.get()
        e9=ent9.get()
        e11=ent11.get()
        e12=ent12.get()
        e21=ent21.get()
        e22=ent22.get()
        e14=ent14.get()
        e16=ent16.get()
        e17=ent17.get()
        e18=ent18.get()
        e7=ent7.get()
                  
        try:
            TABLE="INFO"
            db.execute('''CREATE TABLE '''+TABLE+'''(NAME TEXT NOT NULL, FATHER TEXT NOT NULL, MOTHER TEXT NOT NULL,DOB DATE NOT NULL,USERID STRING NOT NULL,PASSWORD STRING NOT NULL,ADDRESS TEXT NOT NULL,GENDER TEXT NOT NULL,MAIL_ID STRING NOT NULL,MOB_NO STRING NOT NULL,ROLL_NO STRING NOT NULL,TEN STRING NOT NULL,TWELVE STRING NOT NULL,INST TEXT NOT NULL,DEPT TEXT NOT NULL,COUNTRY TEXT NOT NULL,AGE STRING NOT NULL,YOP TEXT NOT NULL,YGPA FLOAT NOT NULL);''')
        except:
           pass
        cursor.execute('''INSERT INTO INFO(NAME,FATHER,MOTHER,DOB,USERID,PASSWORD,ADDRESS,GENDER,MAIL_ID,MOB_NO,ROLL_NO,TEN,TWELVE,INST,DEPT,COUNTRY,AGE,YOP,YGPA)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (e1,e2,e3,combo1.get()+"-"+combo2.get()+"-"+combo3.get(),password,uidd,e4,e5,e6,e7,e22,e9,e11,e12,e21,e14,e16,e17,e18))
                
        db.commit()


        btn2=Button(windows,text="UPDATE",command=clicked1)
        btn2.grid(column=0,row=20)
    def clicked1():
      
        if uid.get()=="a" and pss.get()=="1":
            windows=Tk()
            windows.title("INFORMATION")
            windows.geometry('1300x720')
            windows.configure(background='lightsteelblue')

        


            windows.resizable(0, 0)
            lbl=Label(windows,text="NAME",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl.grid(column=0,row=0,padx=10,pady=10)
            ent=Entry(windows,width=30)
            ent.grid(column=2,row=0,padx=10,pady=10)
            lbl2=Label(windows,text="FATHER'S NAME",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl2.grid(column=0,row=1,padx=10,pady=10)
            ent2=Entry(windows,width=30)
            ent2.grid(column=2,row=1,padx=10,pady=10)
            lbl3=Label(windows,text="MOTHER'S NAME",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl3.grid(column=0,row=2,padx=10,pady=10)
            ent3=Entry(windows,width=30)
            ent3.grid(column=2,row=2,padx=10,pady=10)
            lbl4=Label(windows,text="DATE OF BIRTH",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl4.grid(column=0,row=3,padx=10,pady=10)
            combo1 = Combobox(windows)
            combo1['values']= ("DATE",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,1,19,20,21,22,23,24,25,26,27,28,29,30,31)
            combo1.grid(column=1, row=3,padx=10,pady=10)
            combo2= Combobox(windows)
            combo2['values']= ("MONTH","JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER")
            combo2.grid(column=2, row=3,padx=10,pady=10)
            combo3 = Combobox(windows)
            combo3['values']= ("YEAR",1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005)
            combo3.grid(column=3, row=3,padx=10,pady=10)
            lbl11=Label(windows,text="ADDRESS",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl11.grid(column=0,row=4,padx=10,pady=10)
            ent11=Entry(windows,width=30)
            ent11.grid(column=2,row=4,padx=10,pady=10)
            lbl5=Label(windows,text="GENDER",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl5.grid(column=0,row=5,padx=10,pady=10)
            gn=Entry(windows,width=30)
            gn.grid(column=2,row=5,padx=10,pady=10)
            lbl6=Label(windows,text="EMAIL ID",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl6.grid(column=0,row=6,padx=10,pady=10)
            ent6=Entry(windows,width=30)
            ent6.grid(column=2,row=6,padx=10,pady=10)
            lbl7=Label(windows,text="MOBILE NUMBER",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl7.grid(column=3,row=6,padx=10,pady=10)
            ent7=Entry(windows,width=30)
            ent7.grid(column=5,row=6,padx=10,pady=10)
            lbl8=Label(windows,text="10TH STD. BOARD NAME",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl8.grid(column=0,row=7,padx=10,pady=10)
            combo4 = Combobox(windows)
            combo4['values']= ("Select","WBBSE","CBSE","ICSE")
            combo4.grid(column=2, row=7,padx=10,pady=10)
            lbl9=Label(windows,text="10TH STD. PERCENTAGE",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl9.grid(column=3,row=7,padx=10,pady=10)
            ent9=Entry(windows,width=30)
            ent9.grid(column=5,row=7,padx=10,pady=10)
            lbl10=Label(windows,text="12TH STD. BOARD NAME",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl10.grid(column=0,row=8,padx=10,pady=10)
            combo5 = Combobox(windows)
            combo5['values']= ("Select","WBBSE","CBSE","ICSE")
            combo5.grid(column=2, row=8,padx=10,pady=10)
            lbl11=Label(windows,text="12TH STD. PERCENTAGE",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl11.grid(column=3,row=8,padx=10,pady=10)
            ent11=Entry(windows,width=30)
            ent11.grid(column=5,row=8,padx=10,pady=10)
            lbl12=Label(windows,text="INSTITUTE NAME",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl12.grid(column=0,row=9,padx=10,pady=10)
            ent12=Entry(windows,width=30)
            ent12.grid(column=2,row=9,padx=10,pady=10)
            lbl21=Label(windows,text="DEPARTMENT",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl21.grid(column=3,row=9,padx=10,pady=10)
            ent21=Entry(windows,width=30)
            ent21.grid(column=5,row=9,padx=10,pady=10)
            lbl22=Label(windows,text="ROLL NO",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl22.grid(column=3,row=10,padx=10,pady=10)
            ent22=Entry(windows,width=30)
            ent22.grid(column=5,row=10,padx=10,pady=10)
            lbl14=Label(windows,text="COUNTRY",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl14.grid(column=0,row=10,padx=10,pady=10)
            ent14=Entry(windows,width=30)
            ent14.grid(column=2,row=10,padx=10,pady=10)
            lbl16=Label(windows,text="AGE",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl16.grid(column=0,row=11,padx=10,pady=10)
            ent16=Entry(windows,width=30)
            ent16.grid(column=2,row=11,padx=10,pady=10)
            lbl17=Label(windows,text="YEAR OF PASSING",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl17.grid(column=0,row=12,padx=10,pady=10)
            ent17=Entry(windows,width=30)
            ent17.grid(column=2,row=12,padx=10,pady=10)
            lbl18=Label(windows,text="LAST YEAR YGPA",font=("Times New Roman Bold",10),background='lightsteelblue')
            lbl18.grid(column=0,row=13,padx=10,pady=10)
            ent18=Entry(windows,width=30)
            ent18.grid(column=2,row=13,padx=10,pady=10)

            def addnew():
                uidd=""
                def ud():

                    finpass=""
                    num='1234567890'
                    alp="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    for i in range(3):
                        n=random.randint(0,len(num)-1)
                        al=random.randint(0,len(alp)-1)
                        finpass+=num[n]+alp[al]
                    print(finpass)
                    return finpass
                uidd=ud()
                password=""
                def id():
                    pword=""
                    num='1234567890'
                    alp="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    finpass1=""
                    finpass2=""
                    for i in range(6):
                        n=random.randint(0,len(num)-1)
                        al=random.randint(0,len(alp)-1)
                        finpass1+=num[n]
                        finpass2+=alp[al]
                    pword=finpass1+finpass2
                    print(pword)
                    return pword
                password=id()

                link="C:/Users/dipte/Desktop/final project/"
                db=sqlite3.connect(link+'studentdatabaseinfo1.db')
                cursor=db.cursor()
                e1=ent.get()
                e2=ent2.get()
                e3=ent3.get()
                e4=ent11.get()
                e5=gn.get()
                e6=ent6.get()
                e7=ent7.get()
                e9=ent9.get()
                e11=ent11.get()
                e12=ent12.get()
                e21=ent21.get()
                e22=ent22.get()
                e14=ent14.get()
                e16=ent16.get()
                e17=ent17.get()
                e18=ent18.get()
                if(len(ent7.get())==10):
                    e7=ent7.get()
                else:
                        messagebox.showinfo('ERROR.....','ENTER PROPER NUMBER')
                     
                try:
                    TABLE="INFO"
                    db.execute('''CREATE TABLE '''+TABLE+'''(NAME TEXT NOT NULL, FATHER TEXT NOT NULL, MOTHER TEXT NOT NULL,DOB DATE NOT NULL,USERID STRING NOT NULL,PASSWORD STRING NOT NULL,ADDRESS TEXT NOT NULL,GENDER TEXT NOT NULL,MAIL_ID STRING NOT NULL,MOB_NO STRING NOT NULL,ROLL_NO STRING NOT NULL,TEN STRING NOT NULL,TWELVE STRING NOT NULL,INST TEXT NOT NULL,DEPT TEXT NOT NULL,COUNTRY TEXT NOT NULL,AGE STRING NOT NULL,YOP TEXT NOT NULL,YGPA FLOAT NOT NULL);''')
                except:
                    pass
                cursor.execute('''INSERT INTO INFO(NAME,FATHER,MOTHER,DOB,USERID,PASSWORD,ADDRESS,GENDER,MAIL_ID,MOB_NO,ROLL_NO,TEN,TWELVE,INST,DEPT,COUNTRY,AGE,YOP,YGPA)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (e1,e2,e3,combo1.get()+"-"+combo2.get()+"-"+combo3.get(),password,uidd,e4,e5,e6,e7,e22,e9,e11,e12,e21,e14,e16,e17,e18))
                
                db.commit()
                
                def mbx():
 
                    messagebox.showinfo('User id',password)
                    messagebox.showinfo('PASSWORD',uidd)
                    print("Records created sucessfully")
                mbx()
            btn1=Button(windows,text="ADD NEW",command=addnew)
            btn1.grid(column=0,row=19)
            btn2=Button(windows,text="UPDATE",command=clicked1)
            btn2.grid(column=0,row=20)
            btn3=Button(windows,text="DELETE",command=clicked1)
            btn3.grid(column=0,row=21)
            btn5=Button(windows,text="DISPLAY",command=clicked1)
            btn5.grid(column=0,row=22)
            btn7=Button(windows,text="EXIT",command=uidpasschk)
            btn7.grid(column=0,row=23)
            windows.mainloop()
    btn1=Button(windows,text="Click",command=clicked1)
    btn1.grid(column=1,row=10)
    btn2=Button(windows,text="Click",command=clicked2)
    btn2.grid(column=8,row=10)
    btn3=Button(windows,text="NEW ENTRY",command=clicked3)
    btn3.grid(column=12,row=10)
    windows.mainloop()
uidpasschk()

