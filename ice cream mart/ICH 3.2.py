from tkinter import *
import sys
import mysql.connector
from easygui import *
import datetime
from tkinter import messagebox
from PIL import Image,ImageTk
import tkinter as tk

swindow =Tk()
swindow.title("Start Menu")
swindow.iconbitmap("icon.ico")

load =Image.open('a.png')
render= ImageTk.PhotoImage(load)
img= Label(swindow, image=render)
img.image = render
img.grid(row= 0,column =1 ,sticky = W+E,padx=10,pady=0)

load =Image.open('b.png')
render= ImageTk.PhotoImage(load)
img= Label(swindow, image=render)
img.image = render
img.grid(row= 1,column =1 ,sticky = W+E,padx=10,pady=5)

def mainclick():
    #Using easygui for making username password box
    msg="Enter Login Details"
    title="Login"
    values=["Username","Password"]

    global usepass
    usepass=multpasswordbox(msg,title,values)                   #Creating the login box 

    if usepass == ['','']:
        sys.exit()
    elif usepass == ['mart owner','ip2021']:                                               #creating the id password information

        print("""Logged in successfully as merchant mart owner """)
        swindow.destroy()
        pass

    elif usepass == ['nachiket','testing123']:

        print("Logged in successfully as Nachiket ")
        swindow.destroy()
        pass

    elif usepass == ['','']:

        print("Logged in successfully as Nachiket ")
        swindow.destroy()
        pass
    
    elif usepass == ['mart owner','ip2021']:                                               #creating the id password information

        print("""Logged in successfully as merchant mart owner """)
        swindow.destroy()
        pass

    elif usepass == ['Nachiket','testing123']:

        print("Logged in successfully as Nachiket ")
        swindow.destroy()
        pass

    else:
        sys.exit()

    #Using tkinter making the frames and window

    bwindow=Tk()                                                             #creating the window
    bwindow.title("ICE CREAM MART")
    bwindow.iconbitmap('spyder.ico')
    bwindow.configure(background="white")

    
    load =Image.open('d.png')
    render= ImageTk.PhotoImage(load)
    img= Label(bwindow, image=render)
    img.image = render
    img.grid(row= 0,column =1 ,sticky = W+E,padx=10,pady=5)

    window=Tk()                                                             #creating the window
    window.title("ICE CREAM MART")
    window.iconbitmap('spyder.ico')
    window.configure(background="black")


                                                                            #creating the frames for the widgets
    frame2=Frame(window,bg="black")

    frame2.grid(row=0,column=1 )

    frame1=Frame(window,bg="black")

    frame1.grid(row = 1,column = 1, sticky =E)
                                                                            
    frame3=Frame(window,bg="black")

    frame3.grid(row=1, column = 0, sticky=W)





    #functions for the buttons

                                                                        
    global Cname                                                            #defining the variables used throughout the functions and the whole syntax
    Cname=""

    global counter1
    counter1= 0

    global counter2
    counter2 =0

    global n
    n = 0

    global name
    name= ""
    global phone
    phone=''
    global now
    now=datetime.datetime.now()
    global dtm
    dtm=str(now)
    
    def click1():                                                                                       #defining what each Button does 
        text1.insert(END,"Chocolate Rs.20  ")
        items.delete(0.0,END)
        global counter1
        counter1 += 1
        items.insert(END, counter1)
        bill.delete(0.0,END)
        global counter2
        counter2 += 20
        bill.insert(END, counter2)
        

    def click2():
        text1.insert(END,"Vanilla Rs.15   ")
        items.delete(0.0,END)
        global counter1
        counter1 += 1
        items.insert(END, counter1)
        bill.delete(0.0,END)
        global counter2
        counter2 += 15
        bill.insert(END, counter2)
        
    def click3():
        text1.insert(END,"Cookie cream Rs.30        ")
        items.delete(0.0,END)
        global counter1
        counter1 += 1
        bill.delete(0.0,END)
        global counter2
        counter2 += 30
        bill.insert(END, counter2)
        items.insert(END, counter1)
        
    def click4():
        text1.insert(END,"Dark mist Rs.30 ")
        items.delete(0.0,END)
        global counter1
        counter1 += 1
        items.insert(END, counter1)
        bill.delete(0.0,END)
        global counter2
        counter2 += 30
        bill.insert(END, counter2)
        
    def click5():
        text1.insert(END,"Hazelnut Rs.25 ")
        items.delete(0.0,END)
        global counter1
        counter1 += 1
        items.insert(END, counter1)
        bill.delete(0.0,END)
        global counter2
        counter2 += 25
        bill.insert(END, counter2)
        
    def click6():
        text1.insert(END,"American blue Rs.35          ")
        items.delete(0.0,END)
        global counter1
        counter1 += 1
        items.insert(END, counter1)
        bill.delete(0.0,END)
        global counter2
        counter2 += 35
        bill.insert(END, counter2)
        
    def click7():
        text1.insert(END,"Choco fudge Rs.40    ")
        items.delete(0.0,END)
        global counter1
        counter1 += 1
        items.insert(END, counter1)
        bill.delete(0.0,END)
        global counter2
        counter2 += 40
        bill.insert(END, counter2)
        
    def click8():
        text1.insert(END,"  Kulfi Rs.35    ")
        items.delete(0.0,END)
        global counter1
        counter1 += 1
        items.insert(END, counter1)
        bill.delete(0.0,END)
        global counter2
        counter2 += 35
        bill.insert(END, counter2)
        
    def click9():
        text1.insert(END,"   Mango Rs.50       ")
        items.delete(0.0,END)
        global counter1
        counter1 += 1
        items.insert(END, counter1)
        bill.delete(0.0,END)
        global counter2
        counter2 += 50
        bill.insert(END, counter2)

    def click10():
        text1.delete(0.0, END)
        items.delete(0.0,END)
        bill.delete(0.0,END)
        global counter1
        counter1 = 0
        global counter2
        counter2 = 0

    def blckcur():
        text1.insert(END,"   BlackCurrent Rs.50       ")
        items.delete(0.0,END)
        global counter1
        counter1 += 1
        items.insert(END, counter1)
        bill.delete(0.0,END)
        global counter2
        counter2 += 50
        bill.insert(END, counter2)

    def rdvel():
        text1.insert(END,"   Red velvet Rs.50       ")
        items.delete(0.0,END)
        global counter1
        counter1 += 1
        items.insert(END, counter1)
        bill.delete(0.0,END)
        global counter2
        counter2 += 50
        bill.insert(END, counter2)

    def blb():
        text1.insert(END,"   Blueberry Rs.50       ")
        items.delete(0.0,END)
        global counter1
        counter1 += 1
        items.insert(END, counter1)
        bill.delete(0.0,END)
        global counter2
        counter2 += 50
        bill.insert(END, counter2)    
        
        
    def click11():
        nwindow=Tk()
        nwindow.title("Invoice")
        global counter1
        global counter2
        global name
        global Cname

        def nclick():
            global Cname
            global name
            global counter1
            global counter2
            global dtm
            global phone
            phone=phno.get()
            
            Cname=name.get()

            print('-'*65)
            print("\t\t\tInvoice")
            print('-'*65)
            print("Date : {0:>55s}".format(dtm))
            print('-'*65)
            print("Name\t\tNo.of Items\tBill\tTotal Bill(with tax)")                                           #These lines are for the invoice
            print('-'*65)
            
            print("{0:<25s}".format(Cname),end = " ")
            print("{0:<10d}".format(counter1),end=" ")
            print("{0:>7.2f}".format(counter2),end=" ")
            print("{0:>14.2f}".format(counter2+(counter2*18/100)),end=" ")

            print()
            

            print('-'*65)
        
            nwindow.destroy()
        
        Label(nwindow,text="Your total bill is :",fg ="black").grid(row=2,column=0,sticky=W+E,padx=5,pady=5)

        bill=Label(nwindow,text=counter2,fg="black").grid(row=2,column=1,sticky=W+E,padx=5,pady=5)

        Label(nwindow,text="Total no. of items :",fg ="black").grid(row=3,column=0,sticky=W+E,padx=5,pady=5)

        items=Label(nwindow,text=counter1,fg="black").grid(row=3,column=1,sticky=W+E,padx=5,pady=5)

        Label(nwindow,text="Customer Name",fg = "black").grid(row=0,column=0,sticky=W+E,padx=5,pady=5)
        
        Label(nwindow,text="Phone number",fg = "black").grid(row=1,column=0,sticky=W+E,padx=5,pady=5)
        
        name=Entry(nwindow,fg="black")
        
        name.grid(row=0,column=1,sticky=W+E,padx=5,pady=5)
        
        phno=Entry(nwindow,fg="black")
        
        phno.grid(row=1,column=1,sticky=W+E,padx=5,pady=5)
        
        Button(nwindow, text="Print",bg="light green" ,width=5, command = nclick).grid(row=4,column=1,padx=5,pady=5)
    
        nwindow.resizable(0,0)
        nwindow.mainloop()

        return 

    def click13():
        global n
        n=n+1
        global counter1

        global counter2

        global Cname

        global phone
        
        global dtm

        date = datetime.date.today()
        
        tax_bill = counter2 +counter2*18/100
        
        conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='tiger',
        db='project'
        )


        cursor = conn.cursor()
        if conn.is_connected:
            print("connected to database ")

        sql = """INSERT INTO CUSTOMER
        VALUES (%s,%s,%s,%s,%s)"""
        val = (Cname,phone,counter1,tax_bill,date)
        cursor.execute(sql, val)
        
        conn.commit()

        conn.close()

        print("""
    Data Stored To DataBase
    """)
    
    
    def click14():
        import numpy as np
        import pandas as pd
        conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='tiger',
        db='project'
        )
        
        cursor=conn.cursor()
        
        query1="""SELECT * FROM CUSTOMER"""
        
        cursor.execute(query1)
        
        data=cursor.fetchall()
        
        dtfr1=pd.DataFrame(data)
        
        dtfr1.rename(columns={0:'name',1:'ph_no',2:'no.of items',3:'total bill amount',4:'date  of purchase'},inplace=True)
        
        print(dtfr1)
        
        conn.commit()
        
    def delete():

        def remove():
            global dname
            customername = dname.get()
            conn=mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = 'root',
                db='project')
            cur=conn.cursor()
            query = "DELETE FROM CUSTOMER WHERE NAME = %s "
            data = (customername,)
            cur.execute(query, data)
            conn.commit()
            print('deleted record for name :',customername)
            conn.close()
        
        top=Tk()                                                             #creating the window
        top.title("ICE CREAM MART")
        Label(top,text="Delete records",fg = "black",font="font 12" ).grid(row=0,column=0,sticky=W+E,padx=5,pady=5)
        Label(top,text="Customer Name",fg = "black").grid(row=1,column=0,sticky=W+E,padx=5,pady=5)

        global dname

        dname=Entry(top,fg="black")
        dname.grid(row=1,column=1,sticky=W+E,padx=5,pady=5)
        Button(top, text="Delete record", width = 10, command = remove ,bg="light blue",font="font 11").grid(padx=10,pady=2)
        
    #widgets and heading
    welcome='Welcome'

    username =welcome,usepass[0]




    Label(frame2, text="Ice",bg="black",fg = "orange",font="font 30 bold underline").pack(side = LEFT)
    Label(frame2, text=" Cream ",bg="black",fg = "cyan",font="font 30 bold underline").pack(side = LEFT)
    Label(frame2, text="Mart",bg="black",fg = "magenta",font="font 30 bold underline").pack(side = LEFT)

    Label(window, text=username,bg="black",fg = "White", font = "times 14 ").grid(row =0,column =0)

    text1=Text(frame3, width = 18, height = 24.5, wrap = WORD,bg= "light blue")       #The big box with the name of item and price

    text1.grid(row= 0, column = 0, sticky = W, padx= 10, pady = 0)

    items=Text(frame1, width = 10, height = 1, wrap = WORD, background = "slate grey")      #These boxes are not displayed instead are used to store values    

    bill=Text(frame1, width = 10, height = 1, wrap = WORD, background = "slate grey")

    #tkinter buttons


    Button(frame1, text="Chocolate", width=20, command = click1,height=4,font="font 11",bg= 'brown').grid(row=4, column =1, padx=10,pady=10 )

    Button(frame1, text="Vanilla", width=20, command = click2,height=4,font="font 11",bg= 'white',fg = 'black').grid(row=3, column =1, padx=10,pady=10)

    Button(frame1, text="Cookie Cream", width=20, command = click3,height=4,font="font 11",bg= 'orange').grid(row=3, column =2, padx=10,pady=10)

    Button(frame1, text="Dark Mist", width=20, command = click4,height=4,font="font 11",bg= 'brown').grid(row=2, column =2, padx=10,pady=10)

    Button(frame1, text="Hazelnut", width=20, command = click5,height=4,font="font 11",bg= 'salmon').grid(row=2, column =1, padx=10,pady=10)

    Button(frame1, text="American blue", width=20, command = click6,height=4,font="font 11",bg= 'cyan').grid(row=4, column =2, padx=10,pady=10)

    Button(frame1, text="Choco fudge", width=20, command = click7,height=4,font="font 11",bg= 'brown').grid(row=4, column =3, padx=10,pady=10)

    Button(frame1, text="Kulfi", width=20, command = click8,height=4,font="font 11",bg= 'light pink').grid(row=3, column =3, padx=10,pady=10)

    Button(frame1, text="Mango", width=20, command = click9,height=4,font="font 11",bg= 'yellow').grid(row=2, column =3, padx=10,pady=10)

    Button(frame1, text="Blueberry", width=20, command = blb,height=4,font="font 11",bg= 'cyan').grid(row=2, column =4, padx=10,pady=10)

    Button(frame1, text="Black Current", width=20, command = blckcur,height=4,font="font 11",bg= 'cadetblue').grid(row=3, column =4, padx=10,pady=10)

    Button(frame1, text="Red velvet", width=20, command = rdvel,height=4,font="font 11",bg= 'red').grid(row=4, column =4, padx=10,pady=10)

    Button(frame1, text="Delete records", width=20, command = delete,height=4,font="font 11",bg= 'brown').grid(row=5, column =3, padx=10,pady=10)

    Button(frame3, text="Clear", width = 15, command = click10,bg="light blue",font="font 11").grid(padx=10,pady=2)

    Button(frame1, text="Invoice", width = 20, command = click11,height=4,bg="light blue",font="font 11").grid(row = 5, column = 2, sticky = W,padx=10,pady = 10)

    Button(frame1, text="Save", width = 20 , command = click13, height= 4, bg="light green",font="font 11").grid(row = 5, column = 1, sticky = W,padx = 10, pady= 10)
    
    Button(frame1, text="Show Records", width = 20 , command = click14, height= 4, bg="light green",font="font 11").grid(row = 5, column = 4, sticky = W,padx = 10, pady= 10)
    
    #Some more window functions
                               #To set the size of window to not be changable
    window.mainloop()                               #To display the window constantly

def dbclick():
    dbwindow = Tk()
    dbwindow.title("Database creator")
    dbwindow.iconbitmap('icon.ico')

    dbwindow.configure(background  = "black")

    Label(dbwindow,text="Database Creator",bg="Black",fg= "Magenta",font="forte 20 bold").grid(row = 0,column = 0,sticky=W+E)

    mframe1 = Frame(dbwindow,bg="Black")
    mframe1.grid(row = 1, column = 0)

    def click1():
        messagebox.showinfo("Readme","Note that a database with name project will be created and a table named customer will be created in the database\
        so be sure to check that these don't exist already so no error will show up\
        \
        \
        \
        The table customer created will have five column namely: 'Name, Ph_no, No_items, Total_bill, Date'\
        \
        \
        \
        Thank You for using the ICH program and the database creator")

    def click2():
        conn1 = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'tiger',
        db = 'mysql'
        )

        query1 = "CREATE DATABASE PROJECT;"
        cursor1 = conn1.cursor()
        if conn1.is_connected():
            print("connected to database 1")

        cursor1.execute(query1)

        conn2 = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'tiger',
            db = 'project'
        )
        if conn2.is_connected():
            print("connected to database 2")

        cursor2= conn2.cursor()

        query2 = """CREATE TABLE CUSTOMER
        (Name CHAR(50) ,
        Ph_no VARCHAR(30) ,
        No_items INT(20) ,
        Total_bill INT(20) ,
        Date DATE 
        );"""

        cursor2.execute(query2)

        conn2.commit()
        
        conn2.close()
            
        conn1.commit()

        conn1.close()
        print("Database and table created you may exit now")


    Button(mframe1,text="Create Database and table ",width = 20, command = click2,font = "times 14 bold", bg = "Black", fg = "red").grid(row = 4, column = 0, sticky = W+E, padx = 5, pady = 5)

    Button(mframe1,text="Important readme",width = 15, command = click1,font = "times 14 bold", bg = "Black", fg = "red").grid(row = 4, column = 1, sticky = W+E,padx = 5, pady = 5)
    
    dbwindow.resizable(0,0)
    dbwindow.mainloop()

Iframe = Frame(swindow)
Iframe.configure(background="darkslategrey")
Iframe.grid(row = 10,column = 1)

 # Creating a photoimage object to use image 
photo = PhotoImage(file = "k.png")
photob = PhotoImage(file = "l.png")
  
# here, image option is used to 
# set image on button 
Button(Iframe, image = photo,command = mainclick,font = "ariel 12 bold",bg = "black", fg = "white").grid(row = 3, column = 0, sticky = W,padx=15,pady=15)
Button(Iframe, image = photob,command = dbclick,font= "ariel 12 bold",bg = "black", fg = "white").grid(row = 3, column = 1, sticky = W,padx=15,pady=15)

swindow.resizable(10,0)
swindow.mainloop()
