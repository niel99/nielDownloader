#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 12:00:28 2018

@author: niel99
"""

import tqdm
import requests
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("niel File Downloader")
        self.minsize(640,480)
        self.buttonframe = Label(self)
        self.buttonframe.grid(column=0,row=0,padx=150,pady=100 )
        self.Add_text()
        self.Add_button()
        self.Add_progress()
        
    def Add_text(self):
        self.inp=StringVar()
        self.textbox=ttk.Entry(self.buttonframe,textvariable=self.inp)
        self.textbox.grid(column=4, row =2,padx=100, pady=4)
        self.button2=ttk.Button(self.buttonframe,text="Browse",command=self.filename)
        self.button2.grid(column=4, row=3,pady=10)
    
    def Add_button(self):
        self.button1=ttk.Button(self.buttonframe,text="Download",command=self.download)
        self.button1.grid(column=4, row=4,padx=95,pady=10)
    
    def Add_progress(self):
        self.progress_bar=ttk.Progressbar(self.buttonframe,orient="horizontal",length=360,mode="determinate",maximum=100)
        self.progress_bar.grid(column=4, row=5, pady=10)
    
    def filename(self):
        self.file=filedialog.asksaveasfilename(initialdir="./",title="Select File",filetypes=(("PDF Files","*.pdf"),("All Files", "*.*")))    
        self.path=Label(self.buttonframe,text=self.file)
        self.path.grid(column=4,row=3,pady=10)
        self.button2.grid(column=5,row=3,pady=10)
        
    def download(self):
        self.r=requests.get(self.inp.get(),stream=True)
        self.f=open(self.file,"wb")
        size=int(self.r.headers["Content-Length"])
        chunk=1
        downloaded=0
        chunkSize=1024
        bars=int(size/chunkSize)
        with open(self.file, "wb") as fp:
            for chunk in tqdm.tqdm(self.r.iter_content(chunk_size=chunkSize), total=bars, unit="KB",desc=self.file, leave=True):
                fp.write(chunk)
                downloaded += chunkSize # increment the downloaded
                self.progress_bar["value"] = (downloaded*100/size)
                self.progress_bar.update()
        return
        
        
window=Root()
window.mainloop()