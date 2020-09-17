from tkinter import *
import time
x = 10
y = 10
dim = 100
win = Tk()
win.geometry("600x500")
C = Canvas(win, width=500, height=500, bg="White")
C.create_line(x,y,x+dim,y)
while True:
	x += 10
	
C.pack()
win.mainloop()