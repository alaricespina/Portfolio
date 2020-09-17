#Profitability Calculator
from tkinter import *



win = Tk()
win.title("Profit Calc")
win.resizable(False,False)
class Hatdog:
	hi, di, wi, mi, sai, yi = 0, 0, 0, 0, 0, 0
	dfvlh, dfvld, dfvlw, dfvlm, dfvlsa, dfvly = "0", "0", "0", "0", "0", "0"
	def __init__(self):
		self.ttext = Label(win,text="Income Calculator").grid(row=0,column=0,columnspan=2,pady=10,padx=10)
		self.htext = Label(win,text="Hourly").grid(row=2,column=0,padx=10)
		self.dtext = Label(win,text="Daily").grid(row=2,column=1)
		self.wtext = Label(win,text="Weekly").grid(row=4,column=0)
		self.mtext = Label(win,text="Monthly").grid(row=4,column=1)
		self.satext = Label(win,text="Semi - Annually").grid(row=6,column=0)
		self.ytext = Label(win,text="Yearly").grid(row=6,column=1)

		self.hety = Entry(win)
		self.dety = Entry(win)
		self.wety = Entry(win)
		self.mety = Entry(win)
		self.saety = Entry(win)
		self.yety = Entry(win)
		self.hety.insert('end',self.hi) 
		self.dety.insert('end',self.di) 
		self.wety.insert('end',self.wi) 
		self.mety.insert('end',self.mi) 
		self.saety.insert('end',self.sai)  
		self.yety.insert('end',self.yi)
		self.refbtn = Button(win,text="REFRESH",command=self.Refresh).grid(row=8,columnspan=2,pady=10)
		self.reftxt = Label(win,text="Everytime you add or change values, press refresh",wraplength=200).grid(row=9,columnspan=2,pady=10)
		self.hety.grid(row=3,column=0)
		self.dety.grid(row=3,column=1)
		self.wety.grid(row=5,column=0)
		self.mety.grid(row=5,column=1)
		self.saety.grid(row=7,column=0)
		self.yety.grid(row=7,column=1)


	def Refresh(self):		
		hourly = self.hety.get()
		daily = self.dety.get()
		weekly = self.wety.get()
		monthly = self.mety.get()
		semiannually = self.saety.get()
		yearly = self.yety.get()

		self.hety.delete(first=0,last=len(hourly))
		self.dety.delete(first=0,last=len(daily))
		self.wety.delete(first=0,last=len(weekly))
		self.mety.delete(first=0,last=len(monthly))
		self.saety.delete(first=0,last=len(semiannually))
		self.yety.delete(first=0,last=len(yearly))

		check = True

		if hourly != self.dfvlh and check: 
			print("Not Equal at hourly")
			self.hi = float(hourly)
			self.di = self.hi*24
			self.wi = 7*self.di
			self.mi = 4*self.wi
			self.sai = 6*self.mi
			self.yi = 2*self.sai 
			check = False
			self.dfvlh, self.dfvld, self.dfvlw, self.dfvlm, self.dfvlsa, self.dfvly = str(self.hi), str(self.di), str(self.wi), str(self.mi), str(self.sai), str(self.yi)
		elif daily != self.dfvld and check:
			print("Not Equal at daily")
			self.di = float(daily)
			self.hi = self.di/24
			self.wi = 7*self.di
			self.mi = 4*self.wi
			self.sai = 6*self.mi
			self.yi = 2*self.sai 
			check = False
			self.dfvlh, self.dfvld, self.dfvlw, self.dfvlm, self.dfvlsa, self.dfvly = str(self.hi), str(self.di), str(self.wi), str(self.mi), str(self.sai), str(self.yi)
		elif weekly != self.dfvlw and check:
			print("Not Equal at weekly")
			self.wi = float(weekly)
			self.di = self.wi/7
			self.hi = self.di/24	
			self.mi = 4*self.wi
			self.sai = 6*self.mi
			self.yi = 2*self.sai 
			check = False
			self.dfvlh, self.dfvld, self.dfvlw, self.dfvlm, self.dfvlsa, self.dfvly = str(self.hi), str(self.di), str(self.wi), str(self.mi), str(self.sai), str(self.yi)
		elif monthly != self.dfvlm and check:
			print("Not Equal at monthly")
			self.mi = float(monthly)
			self.wi = self.mi/4
			self.di = self.wi/7
			self.hi = self.di/24
			self.sai = 6*self.mi
			self.yi = 2*self.sai 
			check = False
			self.dfvlh, self.dfvld, self.dfvlw, self.dfvlm, self.dfvlsa, self.dfvly = str(self.hi), str(self.di), str(self.wi), str(self.mi), str(self.sai), str(self.yi)
		elif semiannually != self.dfvlsa and check:
			print("Not Equal at semiannually")
			self.sai = float(semiannually)
			self.mi = self.sai/6
			self.wi = self.mi/4
			self.di = self.wi/7
			self.hi = self.di/24	
			self.yi = 2*self.sai 
			check = False
			self.dfvlh, self.dfvld, self.dfvlw, self.dfvlm, self.dfvlsa, self.dfvly = str(self.hi), str(self.di), str(self.wi), str(self.mi), str(self.sai), str(self.yi)
		elif yearly != self.dfvly and check:
			print("Not Equal at yearly")
			self.yi = float(yearly)
			self.sai = self.yi/2
			self.mi = self.sai/2
			self.wi = self.mi/4
			self.di = self.wi/7
			self.hi = self.di/24
			check = False
			self.dfvlh, self.dfvld, self.dfvlw, self.dfvlm, self.dfvlsa, self.dfvly = str(self.hi), str(self.di), str(self.wi), str(self.mi), str(self.sai), str(self.yi)
		else:
			print("Hatdog")
		
		print([self.dfvlh, self.dfvld, self.dfvlw, self.dfvlm, self.dfvlsa, self.dfvly])

		check = True
		
		self.hety.insert('end',self.hi) 
		self.dety.insert('end',self.di) 
		self.wety.insert('end',self.wi) 
		self.mety.insert('end',self.mi) 
		self.saety.insert('end',self.sai)  
		self.yety.insert('end',self.yi)


ProfitCalculator = Hatdog()

win.mainloop()