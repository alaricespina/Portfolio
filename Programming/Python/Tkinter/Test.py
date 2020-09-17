from tkinter import *

#Test Tkinter shits

win = Tk()

def hatdog():
	output.insert("end","hatdog")

output = Entry(win,width=20)
output.grid(row=0,column=0,columnspan=5,pady=10)
btn = Button(win,text="hatdog",command=hatdog)
btn.grid(row=1)

win.mainloop()