from translate import Translator
from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry('350x200')
window.title('Translator')
#window.config(background='')
choice = {'Tamil','English','Telugu','Hawaiian','Malayalam','Kannada','Gujarati','German','French'}
def clear():
    entry.delete(first=0,last=100000)
    output.delete(first=0,last=100000)
    lan2.set(None)
def cancel():
    window.destroy()
def trans():
    lang1 = lan1.get()
    lang2 = lan2.get()
    #text = entry.get()
    #result = output.get()
    translator = Translator(from_lang=lang1,to_lang=lang2)
    translation = translator.translate(entry.get())
    output.insert(0,translation)
#GUI
#Labels
label = Label(window,text='Text')
label.grid(row=0,column=0)
'''#Background
C = Canvas(window, bg="blue", height=250, width=300)
filename = PhotoImage(file = "C:\\Users\\Ram\\Downloads\\pp.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()'''
#Entry
entry = Entry(window)
entry.grid(row=0,column=1,padx=10)
output = Entry(window)
output.grid(row=4,column=1)
#For dropdown menu
lan1 = StringVar(window)
lan2 = StringVar(window)
lan1.set('English')
lan2.set(None)
lan1menu = OptionMenu(window,lan1,*choice)
label = Label(window,text='From').grid(row=1,column=0)
lan1menu.grid(row=2,column=0)
lan2menu = OptionMenu(window,lan2,*choice)
label = Label(window,text='To').grid(row=1,column=1)
lan2menu.grid(row=2,column=1)
#Buttons
b1 = Button(window,text='Convert',command=trans)
b1.grid(row=2,column=3)
b2 = Button(window,text='Clear',command=clear)
b2.grid(row=5,column=1)
b3 = Button(window,text='Quit',command=cancel)
b3.grid(row=5,column=2)
window.mainloop()
