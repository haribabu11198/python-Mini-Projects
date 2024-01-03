from tkinter import *

parent_window = Tk()# base command for creating a window
parent_window.geometry('300x100')

def createnewwindow():
    new_win = Toplevel(parent_window)# parent_window is the base window
    new_win.geometry('350x250') # setting size for output window
    new_win.config(bg='cyan')
    l=Label(new_win,text='hari created a new window',bg='yellow').place(x=30,y=30)


b = Button(parent_window, text="press to create new window",command=createnewwindow)
b.pack()

parent_window.mainloop()























