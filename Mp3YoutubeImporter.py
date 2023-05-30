from pytube import YouTube
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

chosenDir = os.getcwd

def download_from_yt():
    links = linkField.get("1.0", END).splitlines()
    for line in links:
        ytManager = YouTube(line)
        sound = ytManager.streams.filter(only_audio=True).first()
        global chosenDir
        file = sound.download(output_path=chosenDir)
        base, ext = os.path.splitext(file)
        name = base + '.mp3'
        os.rename(file, name)
    messagebox.showinfo(message="Finished Download(s)")
        

def browse_dir():
    global chosenDir
    chosenDir = filedialog.askdirectory()
    global dirField
    dirField.delete("1.0", END)
    dirField.insert("end",chosenDir)
    
wd = Tk()
wd.title("Mp3 Youtube Importer by Luiguie")
wd.geometry("600x300")
wd.resizable(0,0)

title = Label(text="MP3 Youtube Importer")
title.place(x=240, y= 20)
linkField = Text(wd, height=10, width=70)
linkField.place(x=20,y=50)
downloadButton = Button(wd,height=1,width=30, command=download_from_yt, text="Download")
downloadButton.place(x=30, y=230)
dirButton = Button(wd,height=1,width=3, command=browse_dir, text="🗀")
dirButton.place(x=300, y=230)
dirField = Text(wd, height=1, width=30)
dirField.place(x=335, y=230)

tk.mainloop()