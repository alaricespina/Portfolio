from tkinter import *

class Calculator:
	c = 0
	def Add(self):
		Line.delete("1.0","end")
		a = EntryBox.get()
		b = int(a)
		Calculator.c += b
		Line.insert(END,Calculator.c)
		EntryBox.delete(first=0,last=len(a))
	def Subtract(self):
		Line.delete("1.0","end")
		a = EntryBox.get()
		b = int(a)
		Calculator.c -= b
		Line.insert(END,Calculator.c)
		EntryBox.delete(first=0,last=len(a))
	def Multiply(self):
		Line.delete("1.0","end")
		a = EntryBox.get()
		b = int(a)
		Calculator.c *= b
		Line.insert(END,Calculator.c)
		EntryBox.delete(first=0,last=len(a))
	def Divide(self):
		Line.delete("1.0","end")
		a = EntryBox.get()
		b = int(a)
		Calculator.c /= b
		Line.insert(END,Calculator.c)
		EntryBox.delete(first=0,last=len(a))

tor = Calculator()

main = Tk()
Line = Text(main)
EntryBox = Entry(main, width=20)
Addition = Button(text="+",command=tor.Add)
Subtraction = Button(text="-", command=tor.Subtract)
Multiplication = Button(text="x", command=tor.Multiply)
Division = Button(text="/", command=tor.Divide)
Equate = Button(text="=")

Line.grid(row=0,columnspan=5)
EntryBox.grid(row=1,columnspan=5)
Addition.grid(row=2,column=0)
Subtraction.grid(row=2,column=1)
Multiplication.grid(row=2,column=2)
Division.grid(row=2,column=3)
Equate.grid(row=2,column=4)

main.mainloop()