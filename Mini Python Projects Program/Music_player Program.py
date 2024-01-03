import pygame
from tkinter.ttk import *
from tkinter import ttk
from PIL import ImageTk,Image
from pygame import mixer
from tkinter import *
import os

def playing():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set('playing')
    mixer.music.play()

def pausing():
    songstatus.set('paused')
    mixer.music.pause()

def resume():
    songstatus.set('resume')
    mixer.music.unpause()

kavish=Tk()
kavish.title('Music Player')
kavish.geometry('900x900')

#bg = PhotoImage(file="C:/Users/ELCOT/Desktop/pro music.png")
mixer.init()
songstatus=StringVar()
songstatus.set('choosing')

lbl=Label(kavish,text='MY MUSIC PLAYER',font=('times',20),bg='blue')
lbl.grid(column=10,row=0)

lbl=Label(kavish,text='SELECT YOUR FAVOURITE SONGS',font=('times',15))
lbl.grid(column=10,row=1)

playlist=Listbox(kavish,selectmode=SINGLE,fg='black',font=('times,15'),width=75,height=15)
playlist.grid(column=10,row=20)

os.chdir("F:\muzc")
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)


playbtn=Button(kavish,text='Play',command=playing)
playbtn.config(font=('times',15),bg='green',fg='white',padx=7,pady=7)
playbtn.grid(column=0,row=21)

pausebtn=Button(kavish,text='Pause',command=pausing)
pausebtn.config(font=('times',15),bg='red',fg='white',padx=7,pady=7)
pausebtn.grid(column=1,row=21)

resumebtn=Button(kavish,text='Resume',command=resume)
resumebtn.config(font=('times',15),bg='yellow',fg='white',padx=7,pady=7)
resumebtn.grid(column= 2,row=21)

kavish.mainloop()
