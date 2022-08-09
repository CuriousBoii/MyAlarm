from time import *
from Main import *
from tkinter import *
root = Tk()
root.geometry("500x500")
b = ctime()
a = Label(root, text = ctime(), fg = "black", bg = "red")
a.pack()

root.mainloop()