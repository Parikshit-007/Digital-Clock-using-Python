from tkinter import Tk
from tkinter import Label
import time
import sys

root = Tk()
root.title = ("Digital Clock")

def get_time():
    timeVar = time.strftime ('%H:%M:%S %p')
    clock.config(text=timeVar)
    clock.after(200, get_time)

clock = Label(root, font = ("Calibri",90), background = "black", foreground = "white" )
clock.pack()

get_time()
root.mainloop()
