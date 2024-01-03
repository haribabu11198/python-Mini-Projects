# pip install mysql.connector
# create database rk;
# use rk;
# create table book(book_code varchar(20),book_name varchar(20),book_price varchar(5));

from tkinter import *
import mysql.connector as mc
import tkinter.messagebox as tm

def putdataintomysql(*args):
    e_code = i_code.get()
    e_name = i_name.get()
    e_price = i_price.get()
    # database connection
    conn = mc.connect(host="localhost",user="root", password="", database="rk")
    cur = conn.cursor()
    cur.execute("insert into book(book_code, book_name, book_price) values('"+e_code+"', '"+e_name+"', '"+e_price+"')")
    print('data transfered to mysql successfully ')
    conn.close()

# window creation
root = Tk()
root.geometry('400x100')
root.title("GET DATA")
root.config(bg='cyan')
# frame creation inside window
mainframe = Frame(root)
mainframe.pack()
# value assignment
i_code = StringVar()
i_name = StringVar()
i_price = StringVar()

# entry details
codeEntry = Entry(mainframe, width=20, textvariable=i_code).grid(row=0, column=1)
nameEntry = Entry(mainframe, width=20, textvariable=i_name).grid(row=1, column=1)
priceEntry = Entry(mainframe, width=20,textvariable=i_price).grid(row=2, column=1)
# label details
Label(mainframe, text='Book Code',bg='yellow',fg='green').grid(row=0, column=0)
Label(mainframe, text='Book Name',bg='yellow',fg='green').grid(row=1, column=0)
Label(mainframe, text='Book Price',bg='yellow',fg='green').grid(row=2, column=0)
# button inclusion in window frame
Button(mainframe, text="click to transfer data to mysql", bg='blue',fg='white',command=putdataintomysql).grid(row=3, column=1)

root.mainloop()


