from cProfile import label
from cmd import PROMPT
from time import *
from Main import *
from tkinter import *
root = Tk()
root.geometry("500x150")
b = ctime()
a = Label(root, text = ctime(), fg = "black", bg = "red")
a.pack()
enterTime = Entry()
enterTime.place(x=0,y=0)
enterDate = Entry()
enterDate.place(x=375,y=0)
enterText = Entry()
enterText.place(x=186,y=43)
b = Label(text="boom")
b.pack()

root.mainloop()