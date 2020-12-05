# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 15:23:00 2020

@author: John Kao
"""

from pytube import YouTube
import tkinter as tk

def onClick():
    global var
    var.set(entry.get())
    try:    
    yt = YouTube(var.get(), on_progress_callback=progress)
    stream = yt.streams.filter(res="1080p").first()
    stream.download("C:\\Users\\John Kao\\OneDrive\\Desktop\\New Folder","Mimikyu AND Mightyena Sync Move")
    except:
        print("Download Failed")
    
    
    
def progress(stream,chunk,bytes_remaining):
    size = stream.filesize
    global progress
    preprogress = progress
    currentprogress = int((size-bytes_remaining)*100/size)
    progress = currentprogress
    if preprogress != progress:
        print("Downloaded:" + str(currentprogress)+ "%")
        return
    if progress == 100:
        scale.set(progress)
        window.update()
        print("Download Complete")



var = tk.StingVar()
window = tk.Tk()
window.title("scale")
label = tk.Label(window, bg='#f00', text = 'Insert your video URL')
label.pack()
entry = tk.Entry(window, width = 50)
entry.pack()
scale = tk.Scale(window,label="scale", orient = tk.HORIZONTAL, length = 200)
scale.pack()
button1 = tk.Button(window, text = "Download!" )
button1.pack()
window.mainloop()
#find the video + download