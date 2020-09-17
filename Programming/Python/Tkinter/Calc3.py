from tkinter import *

win = Tk()
outputtxt = ""
refreshit = 0
class calclgc:	
	def __init__(self):
		global outputtxt
		#Main Value Buttons
		n = 1
		for x in range(1,4,1):
			for y in range(0,3,1):
				new = self.calcbtn(n,x,y)
				n += 1

		self.output = Entry(win,width=20)
		self.output.grid(row=0,column=0,columnspan=5,pady=10)
		print("Loaded output")
		self.otherbtns()
	

	def calcbtn(self,value,row,column,*args):
		def concat():
				global outputtxt
				outputtxt += str(value)
				print("Refresh")
				self.output.insert("end",str(value))
				print(outputtxt)		
		self.args = []
		for x in args:
			self.args.append(x)
		self.value = value
		if len(self.args) == 0:
			self.btn = Button(win,text=str(value),command=concat,width=5,height=1)
			self.btn.grid(row=row,column=column)
		elif len(self.args) == 1:
			self.btn = Button(win,text=str(value),command=concat,width=5,height=self.args[0]*1)
			self.btn.grid(row=row,column=column,rowspan=self.args[0])
		elif len(self.args) == 2:
			self.btn = Button(win,text=str(value),command=concat,width=self.args[1]*5,height=self.args[0]*1)
			self.btn.grid(row=row,column=column,rowspan=self.args[0],columnspan=self.args[1])

		
	
	def otherbtns(self):			
		add = self.calcbtn("+",1,4)
		subtract = self.calcbtn("-",2,4)
		divide = self.calcbtn("/",3,4)
		multiply = self.calcbtn("*",4,4)
		zero = self.calcbtn(0,4,0)
		clr = Button(win,text="<-",command=self.clrall,width=5)
		equal = Button(win,text="=",command=self.getem,width=5)
		clr.grid(row=4,column=1)
		equal.grid(row=4,column=2)

	def clrall(self):
		global outputtxt
		outputtxt = ""
		self.output.delete(first=0,last=len(self.output.get()))

	def getem(self):
		global outputtxt		
		rawthing = self.output.get()
		result = eval(rawthing)
		self.output.delete(first=0,last=len(self.output.get()))
		self.output.insert("end",str(result))
		print(result)
		print("gotem")
		outputtxt = ""


maincom = calclgc()


win.mainloop()