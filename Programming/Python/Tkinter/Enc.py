from tkinter import *
import random

win = Tk()
win.geometry("300x100")
win.title("Encryptor")

class Encrypt:
	def __init__(self):
		self.outputpass = ""
		win.geometry("300x100")
		self.clrwnd()
		Wel = Label(win,text="Welcome to Encryptor v1")
		BtnO = Button(win,text="Strengthen your existing password",width=20,height=2,wraplength=100,command=self.Recreate)
		BtnN = Button(win,text="Create new password",width=20,height=2,wraplength=100,command=self.NewPass)
		Wel.pack()
		BtnO.pack()
		BtnN.pack(side=BOTTOM)
	def clrwnd(self):
		for x in win.winfo_children():
			x.destroy()
	def updateBox(self):
		self.Newp.delete(first=0,last=len(self.outputpass))
		self.Newp.insert("end",self.outputpass)
	def Recreate(self):
		print("Strengthen")
		self.clrwnd()
		win.geometry("600x300")
		BtM = Button(win,text="Main Menu", height=1, command=self.__init__ ,width=20)
		BtM.grid(row=0,column=0)

		Oldt = Label(win, text="Input:",width=10).grid(row=0,column=1,padx=10)
		self.Oldp = Entry(win,width=45)
		self.Oldp.grid(row=0,column=2)
		Newt = Label(win,text="Output:",width=10).grid(row=1,column=1,padx=10)
		self.Newp = Entry(win,width=45)
		self.Newp.grid(row=1,column=2)
		
		#Rearrange existing password
		Reabtn = Button(win,text="Jumble Letters",command=self.randompos ,width=20)
		Reabtn.grid(row=1,column=0)

		#Add Custom strings
		cusbtn = Button(win,text="Add Custom Strings",width=20,command=self.cusstring)
		cusbtn.grid(row=2,column=0)
		custxt = Label(win,text="String:",width=10).grid(row=2,column=1)
		self.cusent = Entry(win,width=45)
		self.cusent.grid(row=2,column=2)

		#Add Random Strings
		ranbtn = Button(win,text="Add Random Strings",width=20,command=self.ranstring)
		ranbtn.grid(row=3,column=0)

		#Reset All
		resbtn = Button(win,text="Reset",width=20,command=self.clroutput)
		resbtn.grid(row=4,column=0)

	def clroutput(self):
		print("Clear")
		self.Newp.delete(first=0,last=len(self.outputpass))
		self.outputpass = ""
	def checkoutput(self):
		if self.outputpass == "":
			print("Old password used")
			self.oldpass = self.Oldp.get()
		if self.outputpass != "":
			print("New Password used")
			self.oldpass = self.Newp.get()
	def randompos(self):
		tmpli = []
		self.checkoutput()
		print("Old Password:" + self.oldpass)
		for x in self.oldpass:
			tmpli.append(x)
		print(tmpli)
		n = 0
		self.outputpass = ""
		while len(self.outputpass) < len(self.oldpass):
			n = random.randint(0,(len(tmpli)-1))
			self.outputpass += tmpli[n]
			tmpli.pop(n)

		print("New Password:" + self.outputpass)
		self.updateBox()
	def cusstring(self):
		self.checkoutput()
		customstring = self.cusent.get()
		tmpli = []
		
		if customstring in self.oldpass:
			print("string found")
			new = self.oldpass.split(customstring)
			print(new)
			self.oldpass = ""
			for x in new:
				self.oldpass += x
			print(self.oldpass)
		
		for x in self.oldpass:
			tmpli.append(x)
		print(tmpli)
		n = random.randint(0,len(tmpli)-1)
		tmpli[n] = tmpli[n] + customstring
		self.outputpass = ""
		for x in tmpli:
			self.outputpass += x

		print("Output:" + self.outputpass)
		self.updateBox()
	def ranstring(self):
		u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		l = u.lower()
		n = "0123456789"
		nlu = n+l+u

		self.checkoutput()
		tmpli = []
		for x in self.oldpass:
			tmpli.append(x)
		n = random.randint(0,len(tmpli)-1)
		m = random.randint(0,len(self.oldpass)-1)
		new = ""
		while len(new) < m:
			z = random.randint(0,len(nlu)-1)
			new += nlu[z]
		print(new)
		tmpli[n] += new
		self.outputpass	= ""
		for x in tmpli:
			self.outputpass += x
		self.updateBox()
enc = Encrypt()
win.mainloop()