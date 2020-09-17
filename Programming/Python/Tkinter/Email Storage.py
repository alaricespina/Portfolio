from tkinter import *



win = Tk()
win.title('Email Storage using Py')

aet = Label(win,text="Email:").grid(row=0,column=0,sticky=W)
apt = Label(win,text="Password:").grid(row=1,column=0,sticky=W)
att = Label(win,text="Tag:").grid(row=2,column=0,sticky=W)

addemail = Entry(win,width=30,bd=5)
addpass = Entry(win,width=30,bd=5)
addtag = Entry(win,width=30,bd=5)

btnaddemail = Button(win, text="Add to List")


addemail.grid(row=0,column=1,padx=10)
addpass.grid(row=1,column=1,padx=10)
addtag.grid(row=2,column=1,padx=10)
btnaddemail.grid(row=0,column=2,padx=10,rowspan=3)

mainlist = Frame(win)

n = 4
class makestuff():
	global n
	def __init__(self):
		self.btn = Button(mainlist,text=n,command=self.clearthis)
		self.btn.pack(side=LEFT)
	def clearthis(self):
		self.btn.pack_forget()

while n > 0:
	b1 = makestuff()
	n -= 1


mainlist.grid(row=3,columnspan=3)
win.mainloop()