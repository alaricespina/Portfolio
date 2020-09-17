from tkinter import * 
main = Tk()

Resultbox = Text(main, height=1)
Evaluatebox = Entry(main)
class Calculator:
	process = 0

	def input1(self):
		b = str(1)
		Evaluatebox.insert(END,b)
	def input2(self):
		b = str(2)
		Evaluatebox.insert(END,b)
	def input3(self):
		b = str(3)
		Evaluatebox.insert(END,b)
	def input4(self):
		b = str(4)
		Evaluatebox.insert(END,b)
	def input5(self):
		b = str(5)
		Evaluatebox.insert(END,b)
	def input6(self):
		b = str(6)
		Evaluatebox.insert(END,b)
	def input7(self):
		b = str(7)
		Evaluatebox.insert(END,b)
	def input8(self):
		b = str(8)
		Evaluatebox.insert(END,b)
	def input9(self):
		b = str(9)
		Evaluatebox.insert(END,b)
	def input0(self):
		b = str(0)
		Evaluatebox.insert(END,b)	
	def backspace(self):
		Evaluatebox.delete("end-2c", "end")
	def backall(self):
		Evaluatebox.delete("1.0", "end")
	def add(self):
		Resultbox.delete("1.0","end")
		b = int(Evaluatebox.get())
		Calculator.process += b
		Evaluatebox.delete(first=0,last=100)
		Resultbox.insert(END,Calculator.process)
		print(Calculator.process)
	def subtract(self):
		Resultbox.delete("1.0","end")
		b = int(Evaluatebox.get())
		Calculator.process -= b
		Evaluatebox.delete(first=0,last=100)
		Resultbox.insert(END,Calculator.process)
		print(Calculator.process)		
	def multiply(self):
		Resultbox.delete("1.0","end")
		b = int(Evaluatebox.get())
		Calculator.process *= b
		Evaluatebox.delete(first=0,last=100)
		Resultbox.insert(END,Calculator.process)
		print(Calculator.process)
	def divide(self):
		Resultbox.delete("1.0","end")
		b = int(Evaluatebox.get())
		Calculator.process /= b
		Evaluatebox.delete(first=0,last=100)
		Resultbox.insert(END,Calculator.process)
		print(Calculator.process)


tor = Calculator()


btn1 = Button(main,text="1", command=tor.input1)
btn2 = Button(main,text="2", command=tor.input2)
btn3 = Button(main,text="3", command=tor.input3)
btn4 = Button(main,text="4", command=tor.input4)
btn5 = Button(main,text="5", command=tor.input5)
btn6 = Button(main,text="6", command=tor.input6)
btn7 = Button(main,text="7", command=tor.input7)
btn8 = Button(main,text="8", command=tor.input8)
btn9 = Button(main,text="9", command=tor.input9)
btn0 = Button(main,text="0", command=tor.input0)
add = Button(main,text="+", command=tor.add)
subtract = Button(main,text="-", command=tor.subtract)
divide = Button(main,text="/", command=tor.divide)
multiply = Button(main,text="x", command=tor.multiply)
clearall = Button(main, text="Del", command=tor.backall)
clear = Button(main,text="<-", command=tor.backspace)

#Top
Resultbox.grid(columnspan=4)

#First Row
Evaluatebox.grid(row=1,columnspan=4)

#Second Row
btn1.grid(row=2,column=0)
btn2.grid(row=2,column=1)
btn3.grid(row=2,column=2)
add.grid(row=2,column=3)

#Third Row
btn4.grid(row=3,column=0)
btn5.grid(row=3,column=1)
btn6.grid(row=3,column=2)
subtract.grid(row=3,column=3)

#Fourth Row
btn7.grid(row=4,column=0)
btn8.grid(row=4,column=1)
btn9.grid(row=4,column=2)
divide.grid(row=4,column=3)

#Fifth Row
btn0.grid(row=5,column=0)
clearall.grid(row=5,column=1)
clear.grid(row=5,column=2)
multiply.grid(row=5,column=3)



main.mainloop()