from os import name
from time import sleep  
from tkinter import *
from tkinter import ttk

from pytube import streams
small_font = ('Verdana',10)

window=Tk()
window.title("MP3 MP4 Downloader")
label = Label(window,text="", font=('arial',97,'bold'),bg="light cyan",fg="white")
label.pack(side=TOP,fill=X)
label = Label(window,text="Downladed to location of EXE",font=('arial',13,'bold'),bg="black",fg="white")
label.pack(side=BOTTOM,fill=X)

name_entry=StringVar()
name_entry=ttk.Entry(window, textvariable=name_entry,font=small_font)
name_entry.place(x=7,y=64)
name_entry.focus()

def videodownload():
    from pytube import YouTube 
    video = YouTube(name_entry.get())
    stream = video.streams.filter(resolution='720p').first() 
    stream.download()

def songdownload():
    from pytube import YouTube 
    import os 
    video = YouTube(name_entry.get())
    stream = video.streams.filter(only_audio=True).first() 
    out_file = stream.download() 
    base, ext = os.path.splitext(out_file) 
    new_file = base + '.mp3'
    os.rename(out_file, new_file) 


btn= ttk.Button(window,text='Video (MP4)', command=videodownload)
btn.place(x=180,y=60, width=120,height=30)
btn= ttk.Button(window,text='Song(MP3)', command=songdownload)
btn.place(x=180,y=94, width=120,height=30)

window.geometry('325x180')
window.resizable(True,True)
window.mainloop()