# importing everything from tkinter module 
from tkinter import *

# root object of class tk()
root=Tk()
# defining the dimensions of the gui window
root.geometry("655x354")
# adding title to the window
root.title("FIRST Great GUI PROGRAM")

l1=Label(root,text="WELCOME TO THE CODING WORLD")
l1.pack()

# for display until the window is closed
root.mainloop()
