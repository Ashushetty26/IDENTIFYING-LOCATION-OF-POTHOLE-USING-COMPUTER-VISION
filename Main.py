import tkinter as tk
from tkinter import Message ,Text
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.font as font
from tkinter import filedialog
import tkinter.messagebox as tm
import train as TR
import predictonimage as pre
import realtimePredictor as detectes
from tkinter import ttk
import mapdemo as gmap
import webbrowser




fontScale=1
fontColor=(0,0,0)
cond=0

bgcolor="#FF5733"
fgcolor="white"

window = tk.Tk()
window.title("Identifying the location of pothole using computer vision")

 
window.geometry('1280x720')
window.configure(background=bgcolor)
#window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)


message1 = tk.Label(window, text="Identifying the location of pothole using computer vision" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
message1.place(x=100, y=10)




lbl1 = tk.Label(window, text="Select Image",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl1.place(x=10, y=200)

txt1 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt1.place(x=300, y=215)



def clear():
        #txt.delete(0, 'end') 
        txt1.delete(0, 'end')

def browse():
        path=filedialog.askdirectory()
        print(path)
        txt.delete(0, 'end') 
        txt.insert('end',path)
        if path !="":
                print(path)
        else:
                tm.showinfo("Input error", "Select Dataset Folder")     

def browse1():
        path=filedialog.askopenfilename()
        print(path)
        txt1.delete(0, 'end') 

        txt1.insert('end',path)
        if path !="":
                print(path)
        else:
                tm.showinfo("Input error", "Select image")      




        
def trainprocess():
        TR.process()
        tm.showinfo("Output", "Training Successfully Finished")


def predict():
        sym1=txt1.get()
        if sym1 != "":
                pre.process(sym1)
                #tm.showinfo("Output", "Predicted as: " )
        else:
                tm.showinfo("Input error", "Select Image")
def predict1():
        detectes.process()
def mapprocess():
        gmap.process()
        file_path = 'map15.html'
        new = 2
        webbrowser.open(file_path,new=new)
                
                
clearButton = tk.Button(window, text="Clear", command=clear  ,fg=fgcolor  ,bg=bgcolor  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton.place(x=830, y=200)

browse = tk.Button(window, text="Browse", command=browse  ,fg=fgcolor  ,bg=bgcolor  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
browse.place(x=530, y=205)

browse1 = tk.Button(window, text="Browse", command=browse1  ,fg=fgcolor  ,bg=bgcolor  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
browse1.place(x=530, y=205)



pre1 = tk.Button(window, text="Train", command=trainprocess  ,fg=fgcolor  ,bg=bgcolor  ,width=10  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
pre1.place(x=30, y=500)


qr = tk.Button(window, text="Predict", command=predict  ,fg=fgcolor ,bg=bgcolor  ,width=10  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
qr.place(x=230, y=500)
qr1 = tk.Button(window, text="Real Time Prediction", command=predict1  ,fg=fgcolor ,bg=bgcolor  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
qr1.place(x=430, y=500)
qr2 = tk.Button(window, text="Map Plotting", command=mapprocess  ,fg=fgcolor ,bg=bgcolor  ,width=10  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
qr2.place(x=630, y=500)


quitWindow = tk.Button(window, text="QUIT", command=window.destroy  ,fg=fgcolor ,bg=bgcolor  ,width=10  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=830, y=500)

 
window.mainloop()
