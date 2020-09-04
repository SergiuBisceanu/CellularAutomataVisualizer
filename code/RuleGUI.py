# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 17:08:07 2020

@author: spiku
"""

from tkinter import *

root = Tk()
root.geometry("300x300") 
root.title("Rule Form")

rules = []

requests = ["Provide the input for the following in order, as a string: ", "1. For all blocks of state 1: ", "2. For block one and two of state 1: ", 
            "3. For block one and three of state 1: " ,"4. For block one of state 1: ", "5. For blocks two and three of state 1: ", 
            "6. For block 2 of state 1: ", "7. For block three of state 1: ", "8. For no block of state 1: "]

def Click():
    rules.append(e.get())
    root.destroy()

for i in range(9):
    label = Label(root, text=requests[i])
    label.pack()
    
e = Entry(root, width=50, borderwidth=5)
e.pack()
    
button = Button(root, text="Press to provide input", command=Click)
button.pack()




    