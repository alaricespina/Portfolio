from random import *

class Slot:
	def __init__(self):
		self.choices = [" | | "," |X| "]
		self.state = 0
		self.show = self.choices[self.state]
	def changestate(self):
		self.state = randint(0,1)
		self.show = self.choices[self.state]
	def goback(self):
		self.state = 0



while True:
	a = Slot()
	b = Slot()
	c = Slot()
	d = Slot()
	e = Slot()
	f = Slot()
	g = Slot()
	h = Slot()
	i = Slot()
	lofa = [a,b,c,d,e,f,g,h,i]

	print("---------------")
	print(a.show + b.show + c.show)
	print("---------------")
	print(d.show + e.show + f.show)
	print("---------------")
	print(g.show + h.show + i.show)
	print("---------------")
	play = input("Where?:")
	if int(play) > len(lofa):
		print("Cannot pick more than number of assigned")
	if int(play) <= 0:
		print("Only from 1 to 9 please")

	ai = randint(0,8)
	t = lofa[ai]
	t.changestate()
	if ai == int(play) - 1:
		print("You guessed right!") 
		print("---------------")
		print(a.show + b.show + c.show)
		print("---------------")
		print(d.show + e.show + f.show)
		print("---------------")
		print(g.show + h.show + i.show)
		print("---------------")
	elif ai != int(play) - 1:
		print("You were incorrect! it was at " + str(ai+1))
		print("---------------")
		print(a.show + b.show + c.show)
		print("---------------")
		print(d.show + e.show + f.show)
		print("---------------")
		print(g.show + h.show + i.show)
		print("---------------")

	w = input("Press Enter")	
	a.goback()
	b.goback()
	c.goback()
	d.goback()
	e.goback()
	f.goback()
	g.goback()
	h.goback()
	i.goback()
	print("Done")
	






