#Gui Version of Practice 2.py, simplified version
from tkinter import messagebox
from tkinter import *
win = Tk()
win.geometry("300x200")
win.title("_Hub Login")

class blankhub:
	def __init__(self):
		for x in range(4): Grid.rowconfigure(win, x, weight=1)
		for y in range(2): Grid.columnconfigure(win, y, weight=1)
		self.mainmenu()
		self.userlist, self.passlist, self.thelist = ["123"], ["123"], [12]
	def clearall(self):
		for x in win.winfo_children(): x.destroy()
	def mainmenu(self):
		self.clearall()
		welcome, usertxt, passtxt, self.userent, self.passent, loginbtn, regbtn = Label(win,text="Welcome to _HubCommunity!"), Label(win,text="Username:"), Label(win,text="Password:"), Entry(win,width=25), Entry(win,width=25), Button(win,text="Login",width=10,command=self.login), Button(win,text="Register",width=10,command=self.register)

		a = [welcome.grid(row=0,columnspan=2),usertxt.grid(row=1,column=0),passtxt.grid(row=2,column=0),self.userent.grid(row=1,column=1,sticky=W),self.passent.grid(row=2,column=1,sticky=W),regbtn.grid(row=3,column=0),loginbtn.grid(row=3,column=1)]
	def login(self):
		user, pasw = self.userent.get(), self.passent.get()
		for x in range(2): Grid.rowconfigure(win, x, weight=1)
		for y in range(1): Grid.columnconfigure(win, y, weight=1)
		welcomeback = StringVar()
		if user not in self.userlist: messagebox.showwarning("Warning","Username not found, please register")
		else:
			self.clearall()
			a = self.userlist.index(user)
			self.accindex = a
			if self.passlist[a] != pasw: messagebox.showwarning("Warning","Incorrect Password")
			else:
				welcomeback.set('Welcome back '+ user + '\nCurrent Size: ' + str(self.thelist[a]))
				welcometxt, btmbtn, delbtn = Label(win,textvariable=welcomeback), Button(win,text="Back to Menu",width=15,command=self.mainmenu), Button(win,text="Delete this account",width=15,command=self.delacc)
				z = [welcometxt.grid(row=0,columnspan=2),btmbtn.grid(row=1,column=0,columnspan=2),delbtn.grid(row=2,column=0,columnspan=2)]
	def register(self):
		for x in range(5):Grid.rowconfigure(win, x, weight=1)
		for y in range(2):Grid.columnconfigure(win, y, weight=1)
		self.clearall()
		welcome, usertxt, passtxt, sizetxt, self.userent, self.passent, self.sizeent, btmbtn, regbtn = Label(win,text="Register to _HubCommunity!"), Label(win,text="Username:"), Label(win,text="Password:"), Label(win,text="____ size:"), Entry(win,width=25), Entry(win,width=25), Entry(win,width=25), Button(win,text="Back to Menu",width=10,command=self.mainmenu), Button(win,text="Register",width=10,command=self.regedit)
		aa = [welcome.grid(row=0,columnspan=2),usertxt.grid(row=1,column=0),passtxt.grid(row=2,column=0),sizetxt.grid(row=3,column=0),self.userent.grid(row=1,column=1,sticky=W),self.passent.grid(row=2,column=1,sticky=W),self.sizeent.grid(row=3,column=1,sticky=W),btmbtn.grid(row=4,column=0),regbtn.grid(row=4,column=1)]
	def regedit(self):
		if self.userent.get() not in self.userlist: 
			try:
				a = int(self.sizeent.get())
				self.thelist.append(self.sizeent.get())
				self.userlist.append(self.userent.get())
				self.passlist.append(self.passent.get())
				messagebox.showinfo("Success","You have succesfully registered")
			except ValueError: messagebox.showwarning("WARNING","Invalid size")
		else: messagebox.showwarning("User Found","Username already exists in database")
		for x in [self.userlist,self.passlist,self.thelist]: print(x)	
	def delacc(self):
		for x in [self.userlist,self.passlist,self.thelist]: del x[self.accindex]
		messagebox.showinfo("Deleted","Account has been deleted")
		self.mainmenu()
login = blankhub()
win.mainloop()