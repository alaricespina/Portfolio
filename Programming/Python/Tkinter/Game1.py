import tkinter as a

#functions
class switch():
	def __init__():
		back.pack_forget()
		back = a.Button(w, text="Back to Main Menu")
		back.pack()
	def single():
		main.pack_forget()
	def multi():
		main.pack_forget()
	def instruct():
		main.pack_forget()

swap = switch()
#main windows
w = a.Tk()
main = a.Frame(w)
main.pack()
singleplayer = a.Frame(w)
multiplayer = a.Frame(w)
insFrame = a.Frame(w)

#Buttons
H = a.Label(main,text="Welcome", justify="center")
single = a.Button(main,text="Singleplayer",command=swap.single)
multi = a.Button(main,text="Multiplayer", command=swap.multi)
instruc = a.Button(main,text="Instructions", command=swap.instruct)



#Layouting
H.grid()
single.grid(row=1)
multi.grid(row=2)
w.mainloop()