from time import *
from Main import *
from tkinter import *
#bot = AlarmRinger(list1)
root = Tk()
root.geometry("500x100")
a = Label(root, text = ctime(), fg = "black", bg = "red")
a.pack()
enterTime = Entry(root)
enterTime.place(relx=0,y=0)
enterDate = Entry(root)
enterDate.place(relx=0.75,rely=0)
enterText = Entry(root)
enterText.place(relx=0.373,rely=0.5)
b = Label(root, text="boom")
b.pack()

root.mainloop()
#>>>>>>> f13e6dca88ba0e3999959b4ccf16828144c39d0a
