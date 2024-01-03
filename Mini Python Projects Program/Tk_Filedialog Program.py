import tkinter # first type of module importation
import tkinter.filedialog

win = tkinter.Tk()

def print_path():
    f = tkinter.filedialog.askopenfilename(
        parent=win, initialdir='D:',
        title='choose file from D drive',
        filetypes=[('png images', '.png'),
                   ('gif images', '.gif')]
        )

    print(f)

b1 = tkinter.Button(win, text='Print file path',bg='yellow', command=print_path)
b1.pack(fill='x')

win.mainloop()
