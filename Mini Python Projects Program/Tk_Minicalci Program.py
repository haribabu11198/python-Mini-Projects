from tkinter import *
class MyWindow:
    def __init__(self, win):
        # label intro
        self.lbl1=Label(win, text='First number')
        self.lbl2=Label(win, text='Second number')
        self.lbl3=Label(win, text='Result')
        self.lbl1.place(x=100, y=50)
        self.lbl2.place(x=100, y=100)
        self.lbl3.place(x=100, y=200)
        # entry intro
        self.e1=Entry()
        self.e2=Entry()
        self.e3=Entry()
        self.e1.place(x=200, y=50)
        self.e2.place(x=200, y=100)
        self.e3.place(x=200, y=200)
        # button intro
        self.b1=Button(win, text='Add', command=self.addition,bg='yellow')
        self.b2=Button(win, text='Subtract',bg='yellow')
        self.b2.bind('<Button-1>', self.subtraction)
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)        
    # add fn creation    
    def addition(self):
        self.e3.delete(0, 'end')
        num1=int(self.e1.get())
        num2=int(self.e2.get())
        result=num1+num2
        self.e3.insert(END, str(result))
    # sub fn creation   
    def subtraction(self, event):
        self.e3.delete(0, 'end')
        num1=int(self.e1.get())
        num2=int(self.e2.get())
        result=num1-num2
        self.e3.insert(END, str(result))
# object cration
win=Tk()
mywin=MyWindow(win) # mywin - obj, MyWindow - 
win.title('Hello Python')
win.config(bg='cyan')
win.geometry("400x300")
win.mainloop()
