#import tkinter
#import tkinter.colorchooser

import tkinter
import tkinter.colorchooser

win = tkinter.Tk()

def color_button():
    color = tkinter.colorchooser.askcolor(parent=win)
    
    print(color)
    b1.configure(bg=color[1])

b1 = tkinter.Button(win, text='Chosen Color by rk', command=color_button)
b1.pack(fill='x')

win.mainloop()
