from tkinter import *
import random

win = Tk()
win.title("Random Card")
win.geometry("150x100")
b = 0
def Roll():
	global b
	result.delete("1.0","end")
	streak.delete("1.0","end")
	a = random.randint(1,1)
	print(a)
	result.insert("end", a)
	if res.get() == a:
		b += 1
	else:
		b = 0
	streak.insert("end", b)



res = IntVar()
rtxt = Label(win,text="Result:").grid(row=0,columnspan=2)
result = Text(win, width=5, height=1)
stxt = Label(win,text="Streak:").grid(row=0,column=2,columnspan=2)
streak = Text(win, width=5, height=1)
chc1 = Radiobutton(win, variable=res, value=1, text=1).grid(row=2)
chc2 = Radiobutton(win, variable=res, value=2, text=2).grid(row=2,column=1)
chc3 = Radiobutton(win, variable=res, value=3, text=3).grid(row=2,column=2)
chc4 = Radiobutton(win, variable=res, value=4, text=4).grid(row=2,column=3)
go = Button(win, text="ROLL!", command=Roll).grid(row=3,columnspan=4)

result.grid(row=1,columnspan=2)
streak.grid(row=1,column=2,columnspan=2)

win.mainloop()