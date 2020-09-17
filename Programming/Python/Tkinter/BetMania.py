from tkinter import *


class gameClass:
	roundn = 1

	def __init__(self):
		print("Initialization")

		self.clearAll()
		root.resizable(False,False)
		root.title("BETMANIA")
		root.geometry("100x100")
		titletxt = Label(win,text="BETMANIA")
		Playbtn = Button(win,text="PLAY",command=self.playState)
		Helpbtn = Button(win,text="HELP")
		titletxt.grid(row=0,pady=10,padx=20)
		Playbtn.grid(row=1)
		Helpbtn.grid(row=2)
		
	def playState(self):
		print("Play state")
		self.clearAll()
		root.geometry("300x200")
		newtxt = Label(win,text="Choose a difficulty").grid(row=0,pady=10,padx=100)
		easy = Button(win,text="Easy",command=self.easy).grid(row=1)
		medium = Button(win,text="Medium",command=self.medium).grid(row=2)
		hard = Button(win,text="Hard",command=self.hard).grid(row=3)
		btm = Button(win,text="Main Menu",command=self.__init__).grid(row=4)

	def clearAll(self):
		global win
		win.destroy()
		win = Frame(root)
		win.place(relheight=1.0,relwidth=1.0)

	def easy(self):
		self.difficulty = "easy"
		self.play()

	def medium(self):
		self.difficulty = "medium"
		self.play()

	def hard(self):
		self.difficulty = "hard"
		self.play()

	def play(self):
		print(self.difficulty)

print("start")

root = Tk()
win = Frame(root)
win.place(relheight=1.0,relwidth=1.0)
theWholeThing = gameClass()
print("end")
win.mainloop()