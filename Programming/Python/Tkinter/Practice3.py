#Gui Version of Practice 2.py

from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry("300x200")
win.title("_Hub Login")

class blankhub:
	def __init__(self):
		for x in range(4):
			Grid.rowconfigure(win, x, weight=1)
		for y in range(2):
			Grid.columnconfigure(win, y, weight=1)
		self.mainmenu()
		self.userlist = ["123"]
		self.passlist = ["123"]
		self.thelist = [12]
	def clearall(self):
		print("Cleared")
		for x in win.winfo_children():
			x.destroy()
	def mainmenu(self):
		self.clearall()
		welcome = Label(win,text="Welcome to _HubCommunity!")
		usertxt = Label(win,text="Username:")
		passtxt = Label(win,text="Password:")
		self.userent = Entry(win,width=25)
		self.passent = Entry(win,width=25)
		loginbtn = Button(win,text="Login",width=10,command=self.login)
		regbtn = Button(win,text="Register",width=10,command=self.register)

		welcome.grid(row=0,columnspan=2)
		usertxt.grid(row=1,column=0)
		passtxt.grid(row=2,column=0)
		self.userent.grid(row=1,column=1,sticky=W)
		self.passent.grid(row=2,column=1,sticky=W)
		regbtn.grid(row=3,column=0)
		loginbtn.grid(row=3,column=1)

	def login(self):
		user = self.userent.get()
		pasw = self.passent.get()
		
		for x in range(2):
			Grid.rowconfigure(win, x, weight=1)
		for y in range(1):
			Grid.columnconfigure(win, y, weight=1)

		welcomeback = StringVar()
		if user not in self.userlist:
			messagebox.showwarning("Warning","Username not found, please register")
		else:
			self.clearall()
			a = self.userlist.index(user)
			self.accindex = a
			if self.passlist[a] != pasw:
				messagebox.showwarning("Warning","Incorrect Password")
			else:
				welcomeback.set('Welcome back '+ user + '\nCurrent Size: ' + str(self.thelist[a]))
				welcometxt = Label(win,textvariable=welcomeback).grid(row=0,columnspan=2)
				btmbtn = Button(win,text="Back to Menu",width=15,command=self.mainmenu)
				btmbtn.grid(row=1,column=0,columnspan=2)
				delbtn = Button(win,text="Delete this account",width=15,command=self.delacc)
				delbtn.grid(row=2,column=0,columnspan=2)
				print(f"Welcome back {user}\nCurrently: {self.thelist[a]}")


	
	def register(self):

		for x in range(5):
			Grid.rowconfigure(win, x, weight=1)
		for y in range(2):
			Grid.columnconfigure(win, y, weight=1)
		self.clearall()
		welcome = Label(win,text="Register to _HubCommunity!")
		usertxt = Label(win,text="Username:")
		passtxt = Label(win,text="Password:")
		sizetxt = Label(win,text="____ size:")
		self.userent = Entry(win,width=25)
		self.passent = Entry(win,width=25)
		self.sizeent = Entry(win,width=25)
		btmbtn = Button(win,text="Back to Menu",width=10,command=self.mainmenu)
		regbtn = Button(win,text="Register",width=10,command=self.regedit)

		welcome.grid(row=0,columnspan=2)
		usertxt.grid(row=1,column=0)
		passtxt.grid(row=2,column=0)
		sizetxt.grid(row=3,column=0)
		self.userent.grid(row=1,column=1,sticky=W)
		self.passent.grid(row=2,column=1,sticky=W)
		self.sizeent.grid(row=3,column=1,sticky=W)
		btmbtn.grid(row=4,column=0)
		regbtn.grid(row=4,column=1)


	def regedit(self):
		if self.userent.get() not in self.userlist: 
			try:
				a = int(self.sizeent.get())
				self.thelist.append(self.sizeent.get())
				self.userlist.append(self.userent.get())
				self.passlist.append(self.passent.get())
				messagebox.showinfo("Success","You have succesfully registered")
			except ValueError:
				messagebox.showwarning("WARNING","Invalid size")
		else:
			messagebox.showwarning("User Found","Username already exists in database")
			
		print(self.userlist)
		print(self.passlist)
		print(self.thelist)
	
	def delacc(self):
		del self.userlist[self.accindex]
		del self.passlist[self.accindex]
		del self.thelist[self.accindex]
		messagebox.showinfo("Deleted","Account has been deleted")
		self.mainmenu()

login = blankhub()

win.mainloop()